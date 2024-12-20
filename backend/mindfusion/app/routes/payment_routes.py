from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_payment():
    return {"message": "Payment route is working"}