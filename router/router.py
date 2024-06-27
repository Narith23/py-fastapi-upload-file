from fastapi import APIRouter, UploadFile, status

from app.controller.FileController import FileController

router = APIRouter(prefix="/upload", tags=["Upload".upper()])


@router.get("/{file_id}", status_code=status.HTTP_200_OK)
async def get_file(file_id: str):
    return await FileController.get_file(file_id=file_id)


@router.post("", status_code=status.HTTP_201_CREATED)
async def upload_file(file: UploadFile):
    return await FileController.upload_file(file=file)


@router.delete("/{file_id}", status_code=status.HTTP_200_OK)
async def delete_file(file_id: str):
    return await FileController.delete_file(file_id=file_id)
