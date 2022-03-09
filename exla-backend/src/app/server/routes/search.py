from typing import List, Any
from fastapi import APIRouter
from server.dms.search import search_expert
from server.utils.response import (
    ErrorResponseModel,
    ResponseModel,
)
from server.schemas.expert import Expert

router = APIRouter()

@router.post('/search_expert',
    response_model=Any,
    response_description="Search expert",
)
async def search(name, expertise_names, organisation_name, sort_by='citation', size=20):
    res = search_expert(name, expertise_names, organisation_name, sort_by, size)
    if res:
        return ResponseModel(res , "Search results retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Result is not existed.")