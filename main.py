import logging

from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

from .app.routers import autor
from .app.routers import jugador
from .app.routers import inscripcion
from .app.routers import equipo
from .app.routers import categoria
from .app.routers import mesas
from .app.routers import torneo
from .app.routers import fase
from .app.routers import jugador_partiddo
from .app.routers import jugador_partido2
from .app.routers import partido
from .app.routers import categoria_partido
from .app.routers import resultado_set


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Inicio de la aplicación
    logging.info("Aplicación iniciada")

    yield

    # Cierre de la aplicación
    logging.info("Aplicación cerrada")
    pass


FASTAPI_CONFIG = {
    "title": "Aplicación FastAPI",
    "description": "Una aplicación de ejemplo utilizando FastAPI",
    "openapi_url": "/openapi.json",
    "version": "0.1.0",
    "swagger_ui_parameters": {"defaultModelsExpandDepth": -1},
}

MIDDLEWARE_CONFIG = {
    "allow_origins": ["*"],
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}  # Permite solicitudes desde cualquier origen

app = FastAPI(**FASTAPI_CONFIG, lifespan=lifespan)
app.add_middleware(CORSMiddleware, **MIDDLEWARE_CONFIG)

# Routers
app.include_router(autor.router, prefix="/asociacion", tags=["Asociacion"])
app.include_router(jugador.router, prefix="/jugador", tags=["jugador"])
app.include_router(inscripcion.router, prefix="/inscripcion", tags=["inscripcion"])
app.include_router(equipo.router, prefix="/equipo", tags=["equipo"])
app.include_router(categoria.router, prefix="/categoria", tags=["categoria"])
app.include_router(mesas.router, prefix="/mesas", tags=["mesas"])
app.include_router(torneo.router, prefix="/torneo", tags=["torneo"])
app.include_router(fase.router, prefix="/fase", tags=["fase"])
app.include_router(jugador_partiddo.router, prefix="/jugador_partido", tags=["jugador_partido"])
app.include_router(jugador_partido2.router, prefix="/jugador_partido2", tags=["jugador_partido2"])
app.include_router(partido.router, prefix="/partido", tags=["partido"])
app.include_router(categoria_partido.router, prefix="/categoria_partido", tags=["categoria_partido"])
app.include_router(resultado_set.router, prefix="/resultado_Set", tags=["resultado_Set"])