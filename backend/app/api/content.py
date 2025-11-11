from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from ..database import get_db
from ..schemas import Project, Experience, Achievement
from ..models import Project as ProjectModel, Experience as ExperienceModel, Achievement as AchievementModel

router = APIRouter()


@router.get("/projects", response_model=List[Project])
async def get_projects(db: AsyncSession = Depends(get_db)):
    """Get all projects"""
    result = await db.execute(select(ProjectModel))
    projects = result.scalars().all()
    return projects


@router.get("/projects/{project_id}", response_model=Project)
async def get_project(project_id: int, db: AsyncSession = Depends(get_db)):
    """Get a specific project by ID"""
    result = await db.execute(select(ProjectModel).where(ProjectModel.id == project_id))
    project = result.scalar_one_or_none()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.get("/experiences", response_model=List[Experience])
async def get_experiences(db: AsyncSession = Depends(get_db)):
    """Get all work experiences"""
    result = await db.execute(select(ExperienceModel).order_by(ExperienceModel.start_date.desc()))
    experiences = result.scalars().all()
    return experiences


@router.get("/achievements", response_model=List[Achievement])
async def get_achievements(db: AsyncSession = Depends(get_db)):
    """Get all achievements"""
    result = await db.execute(select(AchievementModel).order_by(AchievementModel.date.desc()))
    achievements = result.scalars().all()
    return achievements
