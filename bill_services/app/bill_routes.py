from typing import List

from fastapi import APIRouter, Depends, status, Header
from sqlalchemy.ext.asyncio import AsyncSession

from bill_services.app.bill_database import get_db
from bill_services.app.bill_schema import CheckoutRequest, BillResponse
from bill_services.app.service.bill_service import BillsService
from bill_services.app.service.user_client import UserClient
bill_router = APIRouter(prefix="/bill",tags=["bills"])


@bill_router.post("/checkout", response_model=BillResponse, status_code=status.HTTP_201_CREATED)
async def checkout_books(
    checkout_data: CheckoutRequest,
    authorization: str = Header(...),
    db: AsyncSession = Depends(get_db)
):
    """
    User checkout route:
    - validate stock
    - create bill
    - reduce inventory
    """
    return await BillsService.checkout_books(db, checkout_data, authorization)


@bill_router.get("/my")
async def get_my_bills(
    authorization: str = Header(...),
    db: AsyncSession = Depends(get_db)
):
    """
    Current logged-in user's bills
    """
    return await BillsService.get_user_bills(db,authorization)


@bill_router.get("/order/{order_group}", response_model=BillResponse)
async def get_order_summary(
    order_group: str,
    db: AsyncSession = Depends(get_db)
):
    """
    Get one order-group summary
    """
    return await BillsService.get_bill_order_summary(db, order_group)


@bill_router.get("/")
async def get_all_bills(
    db: AsyncSession = Depends(get_db)
):
    """
    Admin-only: get all bills/orders
    """
    return await BillsService.get_all_bills(db)