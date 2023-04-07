from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


class User(Base):
	__tablename__ = "users"

	idx = Column(Integer, primary_key=True, index=True)
	email = Column(String, unique=True, index=True)
	hashed_password = Column(String)
	created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())