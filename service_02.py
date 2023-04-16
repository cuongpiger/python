import fastapi
import requests
from fastapi import Body
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from tracing import register_to_jaeger
from pydantic import BaseModel

RequestsInstrumentor().instrument()
app = fastapi.FastAPI()
tracer = trace.get_tracer(__name__)
SERVICE_01_URL = "http://localhost:8001"


class UserInfo(BaseModel):
    name: str


@app.post("/foobar")
async def foobar(userinfo: str = Body(...), name: str = Body(..., )):
    with tracer.start_as_current_span("foo"):
        with tracer.start_as_current_span("bar"):
            with tracer.start_as_current_span("baz"):
                print("Hello world from OpenTelemetry Python!")

    return {
        "message": f"Hello {userinfo}, {name}"
    }


@app.post("/foobar2")
async def foobar2(userinfo: str = Body(...), name: str = Body(..., )):
    return {
        "message": f"Hello {userinfo}, {name}"
    }


@app.post("/client")
def client(userinfo: str = Body(...), name: str = Body(..., )):
    res = requests.post(f"{SERVICE_01_URL}/server",
                        json={
                            "userinfo": userinfo,
                            "name": name
                        })

    return res.json()


FastAPIInstrumentor.instrument_app(app)
if __name__ == "__main__":
    register_to_jaeger("fastapi-jaeger", "localhost")
    import uvicorn

    uvicorn.run(app)
