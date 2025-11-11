from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from datetime import datetime
from .database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    long_description = Column(Text)
    technologies = Column(Text)  # JSON string
    video_url = Column(String)
    demo_url = Column(String)
    github_url = Column(String)
    image_url = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    featured = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Experience(Base):
    __tablename__ = "experiences"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, nullable=False)
    position = Column(String, nullable=False)
    description = Column(Text)
    location = Column(String)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime)
    current = Column(Boolean, default=False)
    technologies = Column(Text)  # JSON string
    achievements = Column(Text)  # JSON string
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Achievement(Base):
    __tablename__ = "achievements"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    category = Column(String)
    date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
