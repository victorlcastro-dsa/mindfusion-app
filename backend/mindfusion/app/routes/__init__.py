from fastapi import APIRouter
from .auth_routes import router as auth_router
from .payment_routes import router as payment_router
from .review_routes import router as review_router
from .session_routes import router as session_router
from .tutor_routes import router as tutor_router
from .user_routes import router as user_router
from app.schemas import UserCreate, UserUpdate, UserOut, TutorCreate, TutorUpdate, TutorOut, SessionCreate, SessionUpdate, SessionOut, ReviewCreate, ReviewUpdate, ReviewOut

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(payment_router, prefix="/payment", tags=["payment"])
router.include_router(review_router, prefix="/reviews", tags=["reviews"])
router.include_router(session_router, prefix="/sessions", tags=["sessions"])
router.include_router(tutor_router, prefix="/tutors", tags=["tutors"])
router.include_router(user_router, prefix="/users", tags=["users"])