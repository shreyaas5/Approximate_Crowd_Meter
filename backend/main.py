from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict

app = FastAPI()

# Allow frontend to fetch data from backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to frontend origin later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy Data (this will be replaced with YOLO detection later)
crowd_data = {
    "library": {
        "Ground Floor": {"current": 20, "capacity": 50},
        "First Floor": {"current": 32, "capacity": 50},
        "Second Floor": {"current": 10, "capacity": 50},
    },
    "gym": {"current": 18, "capacity": 40},
    "kravings": {"current": 12, "capacity": 30},
    "sports": {
        "Badminton Court": {"current": 6, "capacity": 10},
        "Basketball Court": {"current": 10, "capacity": 20},
    },
}

@app.get("/crowd")
def get_crowd() -> Dict:
    # Later we’ll replace this with YOLO results
    return crowd_data
