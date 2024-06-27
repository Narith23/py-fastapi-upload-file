from fastapi import status
from typing import Generic, List, TypeVar, Union

from fastapi.responses import JSONResponse
from pydantic import BaseModel


T = TypeVar("T")


class ResponseModel(BaseModel, Generic[T]):
    status_code: Union[int] = status.HTTP_200_OK
    message: Union[str] = "OK"
    result: Union[T, List[T], None]


class ListResponseModel(BaseModel, Generic[T]):
    status_code: Union[int] = status.HTTP_200_OK
    message: Union[str] = "OK"
    result: Union[List[T], None]


def SuccessfulResponseModel(
    message: Union[str] = "OK", result: Union[T | List[T]] = None
):
    if isinstance(result, list):
        return ListResponseModel(message=message, result=result)
    else:
        return ResponseModel(message=message, result=result)


def CreateResponseModel(
    message: Union[str] = "Created successfully.", result: Union[T | List[T]] = None
):
    return ResponseModel(
        status_code=status.HTTP_201_CREATED, message=message, result=result
    )


def UpdateResponseModel(
    message: Union[str] = "Updated successfully.", result: Union[T | List[T]] = None
):
    return ResponseModel(status_code=status.HTTP_200_OK, message=message, result=result)


def DeleteResponseModel(
    message: Union[str] = "Deleted successfully.", result: Union[T | List[T]] = None
):
    return ResponseModel(status_code=status.HTTP_200_OK, message=message, result=result)


def ErrorResponseModel(
    message: Union[str] = "Internal Server Error", result: Union[T | List[T]] = None
):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            "message": message,
            "result": result,
        },
    )


def NotFoundResponseModel(
    message: Union[str] = "Not Found", result: Union[T | List[T]] = None
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "status_code": status.HTTP_404_NOT_FOUND,
            "message": message,
            "result": result,
        },
    )


def BadRequestResponseModel(
    message: Union[str] = "Bad Request", result: Union[T | List[T]] = None
):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "status_code": status.HTTP_400_BAD_REQUEST,
            "message": message,
            "result": result,
        },
    )


def UnauthorizedResponseModel(
    message: Union[str] = "Unauthorized", result: Union[T | List[T]] = None
):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={
            "status_code": status.HTTP_401_UNAUTHORIZED,
            "message": message,
            "result": result,
        },
    )
