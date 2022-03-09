from typing import List, Any
from fastapi import APIRouter
from server.dms.expert import (get_expert_by_id, get_top_experts, get_all_locations)
from server.utils.response import (
    ErrorResponseModel,
    ResponseModel,
)
from server.schemas.expert import Expert

router = APIRouter()

@router.get('/expert_by_id',
    response_model=Any,
    response_description="Get expert by id",
)
async def retrieve_expert_by_id(expert_id: str):
    expert = await get_expert_by_id(expert_id)
    if expert:
        return ResponseModel(expert , "Expert data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Expert is not existed.")

@router.get('/top_experts',
    response_model=Any,
    response_description="Get top experts",
)
async def retrieve_top_experts(top_k: int):
    experts = await get_top_experts(top_k)
    if experts:
        return ResponseModel(experts , "Experts data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Experts are not existed.")

@router.get('/all_locations',
    response_model=Any,
    response_description="Get all locations",
)
async def retrieve_all_locations():
    locations = await get_all_locations()
    if locations:
        return ResponseModel(locations , "Locations data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Locations are not existed.")
