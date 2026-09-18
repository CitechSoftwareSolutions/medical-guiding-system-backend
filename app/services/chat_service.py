from datetime import datetime, timezone
from typing import List, Optional, Tuple
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from fastapi import HTTPException, status

from app.models.chat import ChatSession, ChatMessage
from app.schemas.chat import ChatQueryRequest


class ChatService:
    @staticmethod
    def create_session(db: Session, student_id: int) -> ChatSession:
        session = ChatSession(student_id=student_id)
        db.add(session)
        db.commit()
        db.refresh(session)
        return session

    @staticmethod
    def get_session(db: Session, session_id: int) -> Optional[ChatSession]:
        return db.scalar(
            select(ChatSession)
            .where(ChatSession.id == session_id)
            .options(selectinload(ChatSession.messages))
        )

    @staticmethod
    def list_student_sessions(db: Session, student_id: int) -> List[ChatSession]:
        return list(
            db.scalars(
                select(ChatSession)
                .where(ChatSession.id == student_id)
                .options(selectinload(ChatSession.messages))
                .order_by(ChatSession.started_at.desc())
            ).all()
        )

    @staticmethod
    def process_chat_query(
        db: Session, student_id: int, query: ChatQueryRequest
    ) -> Tuple[ChatMessage, ChatMessage, int]:
        # Retrieve or create session
        session_id = query.session_id
        if not session_id:
            session = ChatSession(student_id=student_id)
            db.add(session)
            db.flush()
            session_id = session.id
        else:
            session = db.get(ChatSession, session_id)
            if not session or session.student_id != student_id:
                raise HTTPException(status_code=404, detail="Chat session not found")

        # Save user message
        user_tokens = len(query.message.split())
        user_msg = ChatMessage(
            session_id=session_id,
            role="user",
            message=query.message,
            tokens=user_tokens,
        )
        db.add(user_msg)
        db.flush()

        # Simulated AI medical guidance response (ready for OpenAI/Gemini integration)
        prompt_preview = query.message.lower()
        if "anatomy" in prompt_preview:
            bot_text = "In human anatomy, structured revision of systems (cardiovascular, nervous, musculoskeletal) is key. Let me know which anatomical region you are currently studying!"
        elif "pharmacology" in prompt_preview or "drug" in prompt_preview:
            bot_text = "Pharmacology requires understanding mechanisms of action, pharmacokinetics, and clinical indications. Which class of drugs would you like to review?"
        elif "pathology" in prompt_preview or "disease" in prompt_preview:
            bot_text = "When studying pathology, focus on etiology, pathogenesis, morphologic changes, and clinical consequences. What disease condition are you analyzing?"
        else:
            bot_text = f"Hello! As your Medical Guidance AI Assistant, I am here to help you understand complex medical concepts, clarify clinical case studies, and guide your exam preparations regarding: '{query.message}'."

        bot_tokens = len(bot_text.split())
        bot_msg = ChatMessage(
            session_id=session_id,
            role="assistant",
            message=bot_text,
            tokens=bot_tokens,
        )
        db.add(bot_msg)
        db.commit()
        db.refresh(user_msg)
        db.refresh(bot_msg)

        return user_msg, bot_msg, session_id
