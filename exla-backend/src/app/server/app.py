from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routes.expert import router as ExpertRouter
from server.routes.search import router as SearchRouter
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ExpertRouter, tags=["expert"], prefix="/expert")
app.include_router(SearchRouter, tags=["search"], prefix="/search")

# @app.on_event("startup") 
# async def startup_event():
#     # load all model checkpoints to RAM 

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Expert Landscape!"}
