from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field


class FileModel(BaseModel):
    id: str = Field(
        default_factory=lambda: str(ObjectId()),
        description="File ID",
        alias="_id",
    )
    file_name: str = Field(..., description="File name")
    file_path: str = Field(..., description="File path")
    file_size: int = Field(..., description="File size")
    file_ext: str = Field(..., description="File extension")
    file_duration: float = Field(default=0, description="File duration")
    created_at: datetime = Field(
        default_factory=lambda:datetime.utcnow(), description="Created at"
    )

    class Config:
        schema_extra = {
            "example": {
                "file_name": "file_name",
                "file_path": "file_path",
                "file_size": 0,
                "file_ext": "mp4",
                "file_duration": 0,
                "created_at": "2022-01-01T00:00:00.000Z",
            },
            "allow_population_by_field_name": True,
        }
