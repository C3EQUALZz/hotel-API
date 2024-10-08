import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("kot@pes.com", "kotopes", 201),
        ("kot@pes.com", "kot0pes", 409),
        ("pes@kot.com", "pesokot", 201),
        ("abcde", "pesokot", 422),
    ],
)
async def test_register_user(
    email: str, password: str, status_code: int, async_client: AsyncClient
):
    response = await async_client.post(
        "/auth/register",
        json={
            "email": email,
            "password": password,
        },
    )

    assert response.status_code == status_code


@pytest.mark.parametrize(
    "email,password,status_code",
    [
        ("test@test.com", "test", 200),
        ("artem@example.com", "artem", 200),
    ],
)
async def test_login_user(
    email: str, password: str, status_code: int, async_client: AsyncClient
):
    response = await async_client.post(
        "/auth/login",
        json={
            "email": email,
            "password": password,
        },
    )

    assert response.status_code == status_code
