from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.expenses import router as expenses_router
from app.middleware.timer import timing_middleware

# 1. create the main app (the building)
app = FastAPI()

# 2. add the stopwatch middleware
app.middleware("http")(timing_middleware)

# 3. add the CORS security guard
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. connect the expenses router
app.include_router(expenses_router)