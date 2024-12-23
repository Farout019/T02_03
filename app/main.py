from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.controllers import user_controller, product_controller, sale_controller
app = FastAPI(
    title="Mini Market API",
    description="API para la gestión de usuarios, productos y ventas en Mini Market.",
    version="1.0.0",
    contact={
        "name": "Soporte Mini Market",
        "email": "soporte@minimarket.com",
        "url": "https://minimarket.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)


# Registrar controladores (routers)
app.include_router(user_controller.router, prefix="/users", tags=["Users"])
app.include_router(product_controller.router, prefix="/products", tags=["Products"])
app.include_router(sale_controller.router, prefix="/sales", tags=["Sales"])


@app.get("/")
def read_root():
    return {"message": "Welcome to Mini Market API"}


# Personalizar el esquema OpenAPI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Mini Market API",
        version="1.0.0",
        description="Documentación de la API de Mini Market, incluyendo la gestión de usuarios, productos y ventas.",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://your-logo-url.com/logo.png"  # Cambia esta URL por la de tu logo
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
