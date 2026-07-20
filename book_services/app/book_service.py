from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from book_services.app.book_repo import BookRepository
from book_services.app.book_schema import BookCreate, BookUpdate
from book_services.app.utils.book_service_utils import valid_sort_by, valid_order, valid_min_price, valid_max_price, valid_max_min_price

class BookService:
    """
    Handles business logic related to books / inventory.
    """

    @staticmethod
    async def create_book(db: AsyncSession, book_data: BookCreate):
        return await BookRepository.create_book(db, book_data)

    @staticmethod
    async def get_all_books(db: AsyncSession):
        return await BookRepository.get_all_books(db)

    @staticmethod
    async def get_available_books(db: AsyncSession):
        return await BookRepository.get_available_books(db)

    @staticmethod
    async def get_book_by_id(db: AsyncSession, book_id: int):
        book = await BookRepository.get_book_by_id(db, book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Book with id {book_id} not found"
            )
        return book

    @staticmethod
    async def search_books(db: AsyncSession, keyword: str):
        return await BookRepository.search_books(db, keyword)

    @staticmethod
    async def update_book(db: AsyncSession, book_id: int, update_data: BookUpdate):
        book = await BookRepository.get_book_by_id(db, book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Book with id {book_id} not found"
            )

        return await BookRepository.update_book(db, book, update_data)

    @staticmethod
    async def delete_book(db: AsyncSession, book_id: int):
        book = await BookRepository.get_book_by_id(db, book_id)
        if not book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Book with id {book_id} not found"
            )

        await BookRepository.delete_book(db, book)
        return {"message": f"Book with id {book_id} deleted successfully"}
    
    @staticmethod
    async def filter_and_sort_books(
        db: AsyncSession,
        category: str | None = None,
        author: str | None = None,
        book_type: str | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        available: bool | None = None,
        sort_by: str = "id",
        order: str = "asc"        
        ):
        
        if sort_by:
            if not valid_sort_by(sort_by):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid sort_by request.")
        
        if order:
            if not valid_order(order):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid order request.")
        
        if min_price and max_price:
            if not valid_max_min_price(min_price, max_price):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid order request.")
        if min_price:
            if not valid_min_price(min_price):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid order request.")
        if max_price:
            if not valid_max_price(max_price):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid order request.")
                    
        return await BookRepository.filter_and_sort_books(
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
    
    @staticmethod
    async def get_book_id(db: AsyncSession):
        return await BookRepository.get_book_id(db)
        
    @staticmethod
    async def reduce_book_stock(db: AsyncSession, id: int, quantity: int):
        book = await BookRepository.get_book_by_id(db, id)
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        if quantity <= 0 :
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail="Invalid Quantity.")
        result = await BookRepository.reduce_book_stock(db, id, quantity)
        return result