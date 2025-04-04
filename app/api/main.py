from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import confirmation_codes, destinations, user,trips
from app.api.routes import categories
from app.api.routes import trips_categories



app = FastAPI()

### CORS configuration
origins = [
    "http://localhost:8081",
    "http://localhost:19006",  # Expo development server
    "http://localhost:13000",  # Your API server
    "exp://localhost:19000"    # Expo Go app
]

######### !!! CAMBIAR ORIGINS EN PRODUCCION

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

app.include_router(user.router)
app.include_router(confirmation_codes.router)
app.include_router(trips.router)
app.include_router(destinations.router)
app.include_router(categories.router)
app.include_router(trips_categories.router)
#app.mount("/static", StaticFiles(directory="static"), name="static")