from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, ConfigDict


class ChatMessageBase(BaseModel):
    role: str  # 'user', 'assistant', 'system'
    message: str


class ChatMessageCreate(ChatMessageBase):
    pass


class ChatMessageRead(ChatMessageBase):
    id: int
    session_id: int
    tokens: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ChatSessionCreate(BaseModel):
    pass


class ChatSessionRead(BaseModel):
    id: int
    student_id: int
    started_at: datetime
    ended_at: Optional[datetime] = None
    messages: Optional[List[ChatMessageRead]] = []

    model_config = ConfigDict(from_attributes=True)


class ChatQueryRequest(BaseModel):
    message: str
    session_id: Optional[int] = None


class ChatQueryResponse(BaseModel):
    session_id: int
    user_message: ChatMessageRead
    bot_message: ChatMessageRead
