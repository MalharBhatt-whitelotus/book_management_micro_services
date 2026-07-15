from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from book_services.app.book_database import get_db
from book_services.app.book_schema import BookCreate, BookUpdate, BookRead
from book_services.app.book_service import BookService

book_router = APIRouter(prefix="/book", tags=["books"])

@book_router.get("/", response_model=List[BookRead])
async def get_books(
    db: AsyncSession = Depends(get_db),
    keyword: Optional[str] = Query(default=None)
):
    """
    Public / authenticated book listing.
    If keyword is passed, search by title/author/category.
    """
    if keyword:
        return await BookService.search_books(db, keyword)
    return await BookService.get_all_books(db)


@book_router.get("/available", response_model=List[BookRead])
async def get_available_books(db: AsyncSession = Depends(get_db)):
    """
    Books with stock > 0
    """
    return await BookService.get_available_books(db)

@book_router.get("/filter")
async def filter_books(
    category: Optional[str] = None,
    author: Optional[str] = None,
    book_type: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    available: Optional[bool] = None,
    sort_by: str = "id",
    order: str = "asc",
    db: AsyncSession = Depends(get_db)
):
    return await BookService.filter_and_sort_books(
        db=db,
        category=category,
        author=author,
        book_type=book_type,
        min_price=min_price,
        max_price=max_price,
        available=available,
        sort_by=sort_by,
        order=order
        )

@book_router.get("/get_book_by_id", response_model=BookRead)
async def get_book_by_id(book_id: int, db: AsyncSession = Depends(get_db)):
    return await BookService.get_book_by_id(db, book_id)


@book_router.post("/", response_model=BookRead, status_code=status.HTTP_201_CREATED)
async def create_book(
    book_data: BookCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Admin-only: create book
    """
    return await BookService.create_book(db, book_data)


@book_router.put("/{book_id}", response_model=BookRead)
async def update_book(
    book_id: int,
    update_data: BookUpdate,
    db: AsyncSession = Depends(get_db)
):
    """
    Admin-only: update book
    """
    return await BookService.update_book(db, book_id, update_data)


@book_router.delete("/{book_id}")
async def delete_book(
    book_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Admin-only: delete book
    """
    return await BookService.delete_book(db, book_id)

@book_router.patch("/reduce_book_stock")
async def reduce_book_stock(book_id: int, quantity: int, db: AsyncSession = Depends(get_db)):
    return await BookService.reduce_book_stock(db, book_id, quantity)