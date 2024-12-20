from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_review():
    return {"message": "Review route is working"}