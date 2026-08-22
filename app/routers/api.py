from fastapi import APIRouter

from app.routers.auth import router as auth_router
from app.routers.users import router as users_router
from app.routers.doctors import router as doctors_router
from app.routers.students import router as students_router
from app.routers.categories import router as categories_router
from app.routers.documents import router as documents_router
from app.routers.plans import router as plans_router
from app.routers.subscriptions import router as subscriptions_router
from app.routers.payments import router as payments_router
from app.routers.chat import router as chat_router
from app.routers.notifications import router as notifications_router
from app.routers.audit_logs import router as audit_logs_router

api_router = APIRouter()

api_router.include_router(auth_router)
api_router.include_router(users_router)
api_router.include_router(doctors_router)
api_router.include_router(students_router)
api_router.include_router(categories_router)
api_router.include_router(documents_router)
api_router.include_router(plans_router)
api_router.include_router(subscriptions_router)
api_router.include_router(payments_router)
api_router.include_router(chat_router)
api_router.include_router(notifications_router)
api_router.include_router(audit_logs_router)
