
from server.database.mongo import expert_collection

# helpers
def expert_helper(expert_data) -> dict:
    return {
        "_id": str(expert_data["_id"]),
        "id": expert_data["id"],
        "name": expert_data["name"],
        "title": expert_data["title"],
        "dob": expert_data["dob"],
        "email": expert_data["email"],
        "citizen": expert_data["citizen"],
        "organization": expert_data["organization"],
        "profile_url": expert_data["profile_url"],
        "citations": expert_data["citations"],
        "h_index": expert_data["h_index"],
        "i10_index": expert_data["i10_index"],
        "expertise": expert_data["expertise"],
        "co_authors": expert_data["co_authors"]
    }

async def get_expert_by_id(id: str) -> dict:
    expert_data = await expert_collection.find_one({"id": id})
    return expert_helper(expert_data)
    
async def get_top_experts(top_k: int):
    experts_data = []
    async for expert in expert_collection.find().sort([("citations", -1), ("h_index", -1)]).limit(top_k):
        experts_data.append(expert_helper(expert))
    return experts_data

async def get_all_locations():
    organizations = []
    async for org in expert_collection.find():
        # if isinstance(org["organization"], str):
        organizations.extend([org["organization"]])
        # else:
        #     organizations.append(org["organization"])
    return set(organizations)