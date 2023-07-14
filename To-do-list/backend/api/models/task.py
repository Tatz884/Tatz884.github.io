from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from backend.api.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    user_key = Column(String(16), unique=True, index=True) # set the password of your favorite length later in frontend
    is_active = Column(Boolean, default=True)
    tasks = relationship("Task", back_populates="user", cascade="delete")

    # def __repr__(self) -> str:
    #     return f"User(id={self.id!r}, user_key={self.user_key!r}, is_active={self.is_active!r}, tasks={self.tasks!r})"

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(1024))
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    done = relationship("Done", back_populates="task", cascade="delete")
    user = relationship("User", back_populates="tasks")

    # def __repr__(self) -> str:
    #     return f"Task(id={self.id!r}, title={self.title!r}, user_id={self.user_id!r}, done={self.done!r}, user={self.user!r})"
    


class Done(Base):
    __tablename__ = "dones"
    id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)
    task = relationship("Task", back_populates="done")

    def __repr__(self) -> str:
        return f"Done(id={self.id!r}, task={self.task!r})"

