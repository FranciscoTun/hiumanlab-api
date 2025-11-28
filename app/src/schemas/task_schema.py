from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class TaskStatus(str, Enum):
    PENDING = "PENDIENTE"
    IN_PROGRESS = "EN PROGRESO"
    COMPLETED = "COMPLETADA"

class TaskSchema(BaseModel):
    # id: str = Field(..., description="User-defined unique ID")
    title: str = Field(..., description="The title of the task.")
    description: Optional[str] = Field(None, description="Detailed description of the task.")
    status: TaskStatus = Field(
        TaskStatus.PENDING, 
        description="Current status of the task."
    )

    class Config:
        from_attributes = True


class UpdateTaskSchema(BaseModel):
    title: Optional[str] = Field(None, description="The title of the task.")
    description: Optional[str] = Field(None, description="Detailed description of the task.")
    status: Optional[TaskStatus] = Field(None, description="New status of the task.")

    class Config:
        from_attributes = True
