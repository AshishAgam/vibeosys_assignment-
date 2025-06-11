from fastapi import FastAPI
from app.database import engine, Base


# create all tables
Base.metadata.create_all(bind=engine)

from app.routes import products

app = FastAPI(title="Products API")

# Include Routers
app.include_router(products.router)