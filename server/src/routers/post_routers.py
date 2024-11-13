from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.schemas import post_schemas as schemas
from src.db.database import get_db
from src.models import post_models as models

post_router = APIRouter()


@post_router.get("/posts/", response_model=list[schemas.Post])
async def get_posts(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    # return db.query(models.Post).offset(skip).limit(limit).all()
    query = select(models.Post)
    print("omething")
    result = await db.execute(query)
    print("something")
    return result.scalars().all()


@post_router.post("/posts/", response_model=schemas.Post)
async def create_post(post: schemas.PostCreate, db: AsyncSession = Depends(get_db)):
    post = models.Post(title=post.title, content=post.content)
    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post
