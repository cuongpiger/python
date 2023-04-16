import json
from random import randint
import traceback
import click
from flask import Flask, request
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.grpc import GrpcInstrumentorClient
from opentelemetry.instrumentation.pymongo import PymongoInstrumentor
from opentelemetry.instrumentation.redis import RedisInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.propagators.jaeger import JaegerPropagator
from opentelemetry.trace import Span
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.resources import Resource, SERVICE_NAME, SERVICE_NAMESPACE
from opentelemetry.propagate import set_global_textmap

set_global_textmap(JaegerPropagator())
resource = Resource(attributes={
    SERVICE_NAME: "flask-app",
    SERVICE_NAMESPACE: "flask-app-namespace",
})
jaeger_exporter = JaegerExporter(
    agent_host_name='localhost',
    agent_port=6831,
)
provider = TracerProvider(resource=resource)
processor = SimpleSpanProcessor(jaeger_exporter)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

RequestsInstrumentor().instrument()
GrpcInstrumentorClient().instrument()
SQLAlchemyInstrumentor().instrument()
PymongoInstrumentor().instrument()
RedisInstrumentor().instrument()

app = Flask(__name__)
tracer = trace.get_tracer(__name__)


def request_hook(span: Span, _):
    def request_params():
        request_params = {}
        request_params.update(request.args.to_dict())
        request_params.update(request.form.to_dict())

        json_params = None
        try:
            json_params = getattr(request, 'json', None)
        except Exception:
            pass

        if isinstance(json_params, dict):
            request_params.update(json_params)
        if len(str(request_params)) > 1000:
            return "Truncate request-params: " + str(request_params)[-1000:]
        return request_params

    span.set_attributes({
        "request.params": json.dumps(request_params()) or "",
        "request.uid": request.headers.get("Access-User") or "",
    })


FlaskInstrumentor().instrument_app(app=app, request_hook=request_hook)


@app.route('/roll', methods=['GET'])
def roll_dice():
    with tracer.start_as_current_span("do_roll") as rollspan:
        res = randint(1, 6)
        rollspan.set_attribute("roll.value", res)
        rollspan.set_attributes({
            "error": "true",
            "stacktrace": traceback.format_exc()})

    return {
        "roll": res
    }


@click.command()
@click.option('--port', "-p", default=8000, help='Port to listen on.')
@click.option('--host', "-h", default="0.0.0.0", help='Server run host.')
def start(host: str, port: int):
    app.run(host=host, port=int(port))


if __name__ == '__main__':
    start()
