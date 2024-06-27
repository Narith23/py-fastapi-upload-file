from datetime import datetime
import os
import uuid
from fastapi import UploadFile
from fastapi.responses import FileResponse

from app.model.File import FileModel
from config.config import IMAGE_FOLDER
from config.response import CreateResponseModel, NotFoundResponseModel, SuccessfulResponseModel
from config.database import files
from tinytag import TinyTag


class FileController:
    @staticmethod
    async def upload_file(file: UploadFile):
        duration = 0
        extension = file.filename.rsplit(".", 1)[-1]
        # new name file
        new_name_file = (
            str(round(datetime.now().timestamp()))
            + "_"
            + str(datetime.now().microsecond)
            + "_"
            + uuid.uuid4().hex[:9].upper()
            + "."
            + extension
        )
        # Check file extension image
        if extension in ["jpg", "jpeg", "png"]:
            file_path = os.path.join(f"{IMAGE_FOLDER}/images", new_name_file)
        # Check file extension video
        elif extension in ["mp4"]:
            file_path = os.path.join(f"{IMAGE_FOLDER}/videos", new_name_file)
        # Check file extension audio
        elif extension in ["mp3", "m4a"]:
            file_path = os.path.join(f"{IMAGE_FOLDER}/audios", new_name_file)
        # Check file extension other
        else:
            file_path = os.path.join(f"{IMAGE_FOLDER}/others", new_name_file)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as f:
            content = file.file.read()
            f.write(content)

        if extension in ["mp4", "mp3"]:
            tag = TinyTag.get(file_path)
            duration = float(f"{tag.duration:.2f}")

        data = FileModel(
            file_name=file.filename,
            file_path=file_path,
            file_size=file.size,
            file_ext=extension,
            file_duration=duration,
        )
        await files.insert_one(data.dict(by_alias=True))
        return CreateResponseModel(message="Upload file successfully")

    @staticmethod
    async def get_file(file_id: str):
        file = await files.find_one({"_id": file_id})
        if file is None:
            return NotFoundResponseModel(message="File not found")
        elif file["file_ext"] in ["mp4"]:
            return FileResponse(path=file["file_path"], filename=file["file_name"], media_type="video/mp4")
        elif file["file_ext"] in ["mp3", "m4a"]:
            return FileResponse(path=file["file_path"], filename=file["file_name"], media_type="audio/mp3")
        elif file["file_ext"] in ["jpg", "jpeg", "png"]:
            return FileResponse(path=file["file_path"], filename=file["file_name"], media_type="image/jpeg")
        elif file["file_ext"] in ["pdf"]:
            return FileResponse(path=file["file_path"], filename=file["file_name"], media_type="application/pdf")
        else:
            return FileResponse(path=file["file_path"], filename=file["file_name"])

    @staticmethod
    async def delete_file(file_id: str):
        file = await files.find_one({"_id": file_id})
        if file is None:
            return NotFoundResponseModel(message="File not found")
        os.remove(file["file_path"])
        await files.delete_one({"_id": file_id})
        return SuccessfulResponseModel(message="Delete file successfully")
