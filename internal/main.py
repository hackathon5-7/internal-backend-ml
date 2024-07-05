from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from internal.config import config
from internal.routers import internal

app = FastAPI()

origins = config['cors']['allow_origins']
allow_credentials = config['cors']['allow_credentials']
allow_methods = config['cors']['allow_methods']
allow_headers = config['cors']['allow_headers']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=allow_credentials,
    allow_methods=allow_methods,
    allow_headers=allow_headers,
)

app.include_router(internal.router, prefix="/api/internal")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
