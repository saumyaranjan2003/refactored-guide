# api.py
from fastapi import FastAPI, HTTPException, Depends, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from game_chatbot import GameChatbot
import logging
import time

# --------------------------
# Logging Configuration
# --------------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# --------------------------
# API Key Configuration
# --------------------------
API_KEY = "mysecretapikey123"  # Change to a secure value

def get_api_key(x_api_key: str = Header(...)):
    """Validate API key."""
    if x_api_key != API_KEY:
        logger.warning("Unauthorized access attempt with API key: %s", x_api_key)
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return x_api_key

# --------------------------
# Initialize FastAPI and Chatbot
# --------------------------
app = FastAPI(
    title="Game Chatbot REST API",
    description="An API to interact with the Game Chatbot",
    version="1.0.0"
)
chatbot = GameChatbot()

# --------------------------
# Enable CORS (Optional)
# --------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------
# Request/Response Models
# --------------------------
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

# --------------------------
# Middleware for Logging Request Time
# --------------------------
@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info("%s %s completed in %.3f sec", request.method, request.url.path, process_time)
    return response

# --------------------------
# API Endpoints
# --------------------------
@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to the Game Chatbot API! Visit /docs for API documentation."}

@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse, dependencies=[Depends(get_api_key)])
async def chat(request: ChatRequest):
    """Send message to Game Chatbot and get response."""
    user_input = request.message
    bot_response = await chatbot.generate_response_async(user_input) if hasattr(chatbot, "generate_response_async") else chatbot.generate_response(user_input)
    return ChatResponse(response=bot_response)
