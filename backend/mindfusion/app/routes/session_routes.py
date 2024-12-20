from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_session():
    return {"message": "Session route is working"}