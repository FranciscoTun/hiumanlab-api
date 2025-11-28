from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class ProjectStatus(str, Enum):
    PLANNING = "PLANIFICACIÓN"
    ACTIVE = "ACTIVO"
    ON_HOLD = "EN PAUSA"
    CANCELLED = "CANCELADO"
    COMPLETED = "FINALIZADO"

class ProjectSchema(BaseModel):
    id: str = Field(..., description="Unique project ID")
    name: str = Field(..., description="Project name")
    description: Optional[str] = Field(None, description="Project description")
    status: ProjectStatus = Field(
        ProjectStatus.PLANNING,
        description="Project status: PENDIENTE, EN PROGRESO, COMPLETADO"
    )

    class Config:
        from_attributes = True

class UpdateProjectSchema(BaseModel):
    name: Optional[str] = Field(None, description="Project name")
    description: Optional[str] = Field(None, description="Project description")
    status: Optional[ProjectStatus] = Field(
        None,
        description="Project status: PLANIFICACIÓN, ACTIVO, EN PAUSA, CANCELADO, FINALIZADO"
    )

    class Config:
        from_attributes = True
