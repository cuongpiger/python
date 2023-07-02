from flask import Flask
import demo1
import logging
import time
import asyncio

from jaeger_client import Config

app = Flask(__name__)
tracer = None


@app.route('/')
def hello():
    fn(demo1.construct_span2(tracer))
    return 'Hello, World!'


async def fn(f):
    # call the method f
    f()
    await asyncio.sleep(2)


if __name__ == '__main__':
    log_level = logging.DEBUG
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(asctime)s %(message)s', level=log_level)

    config = Config(
        config={  # usually read from some yaml config
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'local_agent': {
                # Specify the hostname and port number of the Jaeger agent.
                # To ensure data reliability, we recommend that you run the Jaeger client and the Jaeger agent on the same host. Therefore, the reporting_host parameter is set to 127.0.0.1.
                'reporting_host': '127.0.0.1',
                'reporting_port': 6831,
            },
            'logging': True,
        },
        # Specify the application name.
        service_name="mytest3",
        validate=True,
    )

    tracer = config.initialize_tracer()

    app.run(host='0.0.0.0', port=5000)
