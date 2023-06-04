import logging
from http import HTTPStatus
from typing import Dict
from fastapi import FastAPI
from .routers import order

logging.basicConfig(
    encoding="utf-8",
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__file__)

app = FastAPI(
    title="Fruit Service",
    version="1.0.0",
    description="Fruit Service - Order your favorite fruit",
    root_path=""
)
app.include_router(order.router)


@app.get("/", status_code=HTTPStatus.OK)
async def root() -> Dict[str, str]:
    """
    Endpoint for basic connectivity test
    """

    logger.info("root called")
    return {
        "message": "I am alive"
    }
