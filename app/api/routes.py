from fastapi import APIRouter
from pydantic import BaseModel
from app.ml.model import load_model, predict_from_features

router = APIRouter()

class SessionIn(BaseModel):
    user_id: str
    duration_minutes: int
    breaks: int
    focus_score: float
    sleep_hours: float
    mood: int

model = load_model()

@router.post('/predict')
def predict_route(payload: SessionIn):
    features = payload.dict()
    label, prob = predict_from_features(model, features)
    return {"label": label, "probability": float(prob)}

@router.get('/health')
def health():
    return {"status": "ok"}
