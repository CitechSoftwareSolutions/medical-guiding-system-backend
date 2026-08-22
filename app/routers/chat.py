from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.deps import get_db, get_current_user
from app.models.user import User
from app.schemas.chat import (
    ChatSessionCreate,
    ChatSessionRead,
    ChatMessageRead,
    ChatQueryRequest,
    ChatQueryResponse,
)
from app.services.chat_service import ChatService
from app.services.student_service import StudentService

router = APIRouter(prefix="/chat", tags=["AI Medical Guidance Chatbot"])


@router.post("/query", response_model=ChatQueryResponse)
def query_ai_guidance(
    query: ChatQueryRequest,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    student_profile = StudentService.get_by_user_id(db=db, user_id=current_user.id)
    if not student_profile:
        raise HTTPException(status_code=400, detail="Only students can interact with the guidance chatbot")

    user_msg, bot_msg, session_id = ChatService.process_chat_query(
        db=db, student_id=student_profile.id, query=query
    )
    return ChatQueryResponse(
        session_id=session_id,
        user_message=ChatMessageRead.model_validate(user_msg),
        bot_message=ChatMessageRead.model_validate(bot_msg),
    )


@router.get("/sessions", response_model=List[ChatSessionRead])
def list_my_chat_sessions(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    student_profile = StudentService.get_by_user_id(db=db, user_id=current_user.id)
    if not student_profile:
        raise HTTPException(status_code=400, detail="Current user is not a student")
    return ChatService.list_student_sessions(db=db, student_id=student_profile.id)


@router.get("/sessions/{session_id}", response_model=ChatSessionRead)
def get_chat_session(
    session_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    student_profile = StudentService.get_by_user_id(db=db, user_id=current_user.id)
    if not student_profile:
        raise HTTPException(status_code=400, detail="Current user is not a student")

    session = ChatService.get_session(db=db, session_id=session_id)
    if not session or session.student_id != student_profile.id:
        raise HTTPException(status_code=404, detail="Chat session not found")
    return session
