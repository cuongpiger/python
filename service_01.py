import fastapi
from fastapi import Body
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from pydantic import BaseModel
from tracing import register_to_jaeger

app = fastapi.FastAPI()
tracer = trace.get_tracer(__name__)


class UserInfo(BaseModel):
    name: str


@app.post("/server")
async def server(userinfo: str = Body(...), name: str = Body(..., )):
    return {
        "message": f"hello {userinfo}, {name}"
    }


FastAPIInstrumentor.instrument_app(app)
if __name__ == "__main__":
    register_to_jaeger("fastapi-jaeger-server", "localhost")
    import uvicorn

    uvicorn.run(app, port=8001)
