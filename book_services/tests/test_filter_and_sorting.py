import pytest

from book_services.tests.get_token import get_token


@pytest.mark.asyncio
async def test_filter_category(client):
    token = await get_token()

    response = await client.get(
        "/book/filter?category=Programming",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200

    books = response.json()

    for book in books:
        assert "Programming" in book["category"]


@pytest.mark.asyncio
async def test_filter_available_books(client):
    token = await get_token()

    response = await client.get(
        "/book/filter?available=true",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200

    books = response.json()

    for book in books:
        assert book["quantity"] > 0

@pytest.mark.asyncio
async def test_filter_book_type(client):
    token = await get_token()
    response = await client.get(
        "/book/filter?book_type=hardcopy",
        headers = {"Authorization": f"bearer {token}"})
    
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_sort_price_ascending(client):
    token = await get_token()

    response = await client.get(
        "/book/filter?sort_by=price",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200

    books = response.json()
    prices = [book["price"] for book in books]

    assert prices == sorted(prices)


@pytest.mark.asyncio
async def test_sort_price_descending(client):
    token = await get_token()

    response = await client.get(
        "/book/filter?sort_by=price&order=desc",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200

    books = response.json()
    prices = [book["price"] for book in books]

    assert prices == sorted(prices, reverse=True)

@pytest.mark.asyncio
async def test_filter_non_existing_category(client):
    token = await get_token()

    response = await client.get(
        "/book/filter?category=UnknownCategory",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.asyncio
async def test_filter_non_existing_author(client):
    token = await get_token()

    response = await client.get(
        "/book/filter?author=UnknownAuthor",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.asyncio
async def test_filter_price_range_only(client):
    token = await get_token()

    response = await client.get(
        "/book/filter?min_price=200&max_price=800",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200

    books = response.json()

    for book in books:
        assert 200 <= book["price"] <= 800


@pytest.mark.asyncio
async def test_invalid_sort_by(client):
    token = await get_token()

    response = await client.get(
        "/book/filter?sort_by=invalid_column",
        headers={"Authorization": f"Bearer {token}"},
    )

    # Change if your API returns a different status
    assert response.status_code in (400, 422)


@pytest.mark.asyncio
async def test_invalid_order(client):
    token = await get_token()

    response = await client.get(
        "/book/filter?sort_by=price&order=random",
        headers={"Authorization": f"Bearer {token}"},
    )
    # Change if your API returns a different status
    assert response.status_code in (400, 422)


@pytest.mark.asyncio
async def test_invalid_price_range(client):
    token = await get_token()

    response = await client.get(
        "/book/filter?min_price=1000&max_price=100",
        headers={"Authorization": f"Bearer {token}"},
    )

    # Change if your API returns a different status
    assert response.status_code in (400, 422)

@pytest.mark.asyncio
async def test_invalid_price_min_range(client):
    token = await get_token()

    response = await client.get(
        "/book/filter?min_price=-1",
        headers={"Authorization": f"Bearer {token}"},
    )

    # Change if your API returns a different status
    assert response.status_code in (400, 422)

@pytest.mark.asyncio
async def test_invalid_price_max_range(client):
    token = await get_token()

    response = await client.get(
        "/book/filter?max_price=-1",
        headers={"Authorization": f"Bearer {token}"},
    )

    # Change if your API returns a different status
    assert response.status_code in (400, 422)

@pytest.mark.asyncio
async def test_filter_without_parameters(client):
    token = await get_token()

    response = await client.get(
        "/book/filter",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200

    books = response.json()

    assert isinstance(books, list)