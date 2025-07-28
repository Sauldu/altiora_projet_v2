# app/gateway/main.py
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi_limiter import FastAPILimiter
from redis.asyncio import Redis
import jwt, time, os

redis = Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))
oauth2 = OAuth2PasswordBearer(tokenUrl="login")
app = FastAPI()

@app.on_event("startup")
async def startup() -> None:
    await FastAPILimiter.init(redis)

async def rate_limit() -> None:
    if not await FastAPILimiter.check("global", 100, 60):
        raise HTTPException(status.HTTP_429_TOO_MANY_REQUESTS)

def refresh_jwt(token: str = Depends(oauth2)) -> str:
    now = time.time()
    try:
        payload = jwt.decode(token, os.getenv("SECRET"))
    except jwt.ExpiredSignatureError:
        payload = jwt.decode(token, os.getenv("SECRET"), options={"verify_exp": False})
        if now - payload["exp"] > 60:           # fenêtre refresh 60 s
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)
        payload["exp"] = now + 3600
        return jwt.encode(payload, os.getenv("SECRET"))
    return token

@app.get("/protected", dependencies=[Depends(rate_limit)])
async def protected(_: str = Depends(refresh_jwt)):
    return {"ok": True}