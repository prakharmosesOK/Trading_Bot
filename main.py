from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from trade.routers import user, authentication, trading
import market_connection as mc1
import market_connection2 as mc2
import yfinance as yf
from datetime import date, timedelta
import datetime
import schedule
import time
from sqlalchemy.orm import Session
from trade import schemas, mongodb
import pytz

# Define the origins that are allowed to access the backend

app = FastAPI()

# Allowing frontend to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,  # Set to True if allowing cookies
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers from the frontend
)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(trading.router)