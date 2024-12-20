from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_tutor():
    return {"message": "Tutor route is working"}