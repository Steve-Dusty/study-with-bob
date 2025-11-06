from fastapi import APIRouter
from .routes import student, teacher, auth, realtime

router = APIRouter()

router.include_router(student.router, prefix="/student", tags=["student"])
router.include_router(teacher.router, prefix="/teacher", tags=["teacher"])
router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(realtime.router, prefix="/realtime", tags=["realtime"])

