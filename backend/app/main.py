from fastapi import FastAPI
from app.api.routes import router
app = FastAPI(title='UTS PEMWEB API')
app.include_router(router, prefix='')
