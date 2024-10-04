from fastapi import APIRouter, Request, Depends, status, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy.orm import Session
from config.database import get_db
from models.models import Notice
from datetime import datetime

router = APIRouter(tags=["공지"])

templates = Jinja2Templates(directory="templates/main")

class NoticePost(BaseModel):
    category: str
    title: str
    content: str

@router.post("/notice", status_code=status.HTTP_201_CREATED)
async def postNotice(postNoticeSchema : NoticePost, db : Session=Depends(get_db)):
    if (not postNoticeSchema.title and not postNoticeSchema.category and not postNoticeSchema.content):
        raise HTTPException(status_code=400, detail="입력 필드를 채워주세요.")
    
    try:
        newNotice = Notice(
            category = postNoticeSchema.category,
            title = postNoticeSchema.title,
            content = postNoticeSchema.content
        )
        db.add(newNotice)
        db.commit()
        db.refresh(newNotice)
    except:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
