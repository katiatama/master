<<<<<<< HEAD
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
=======
import pytest
import httpx
from app.main import app


@pytest.mark.asyncio
async def test_health():
    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(
        transport=transport,
        base_url="http://test"
    ) as client:

        response = await client.get("/health")

        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
>>>>>>> ef687b8 (feat: create FastAPI application with tests)
