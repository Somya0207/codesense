# storage/database.py — sets up database connection and tables

from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, Session

engine = create_engine("sqlite:///codesense.db")

class Base(DeclarativeBase):
    pass

class AnalysisRun(Base):
    __tablename__ = "analysis_runs"
    id        = Column(Integer, primary_key=True)
    file_path = Column(String)
    run_date  = Column(DateTime, default=datetime.utcnow)
    total     = Column(Integer)
    warnings  = Column(Integer)

def init_db():
    Base.metadata.create_all(engine)

def save_run(file_path: str, total: int, warnings: int):
    with Session(engine) as db:
        run = AnalysisRun(
            file_path=file_path,
            total=total,
            warnings=warnings
        )
        db.add(run)
        db.commit()

def get_history() -> list:
    with Session(engine) as db:
        return db.query(AnalysisRun).order_by(AnalysisRun.id.desc()).all()