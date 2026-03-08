from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import Optional
from datetime import date, datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

user_child = db.Table('user_child',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('child_id', db.Integer, db.ForeignKey('child.id'), primary_key=True)
)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(db.String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(db.String(50), nullable=False)
    email: Mapped[str] = mapped_column(db.String(120), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(db.String(256), nullable=False)
    children: Mapped[list["Child"]] = relationship(secondary=user_child, back_populates="parents")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Child(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(db.String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(db.String(50), nullable=False)
    dob: Mapped[date] = mapped_column(db.Date, nullable=False)
    gender: Mapped[str] = mapped_column(db.CHAR(1), nullable=False)
    eye_color: Mapped[Optional[str]] = mapped_column(db.String(20))
    parents: Mapped[list["User"]] = relationship( secondary=user_child, back_populates="children")

class FeedingEvent(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    child_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('child.id'), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(db.DateTime, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(db.String(512))
