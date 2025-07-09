from fastapi import APIRouter, Depends, HTTPException
from ..db import get_db
from ..cruds.jugador_partido2 import (
    create_jugador_partido2,
    get_jugadores_partido2,
    get_jugador_partido2,
    delete_jugador_partido2,
)

router = APIRouter()

@router.get("/")
def get_jugadores_partido2_endpoint(session=Depends(get_db)):
    relaciones = get_jugadores_partido2(session)
    return [{"jugador": r.jugador, "partido": r.partido} for r in relaciones]

@router.get("/{jugador_id}/{partido_id}")
def get_jugador_partido2_endpoint(jugador_id: int, partido_id: int, session=Depends(get_db)):
    relacion = get_jugador_partido2(session, jugador_id, partido_id)
    if not relacion:
        raise HTTPException(status_code=404, detail="Relación no encontrada")
    return {"jugador": relacion.jugador, "partido": relacion.partido}

@router.post("/")
def create_jugador_partido2_endpoint(jugador_id: int, partido_id: int, session=Depends(get_db)):
    relacion = create_jugador_partido2(session, jugador_id, partido_id)
    return {"jugador": relacion.jugador, "partido": relacion.partido}

@router.delete("/{jugador_id}/{partido_id}")
def delete_jugador_partido2_endpoint(jugador_id: int, partido_id: int, session=Depends(get_db)):
    relacion = delete_jugador_partido2(session, jugador_id, partido_id)
    if not relacion:
        raise HTTPException(status_code=404, detail="Relación no encontrada")
    return {"detail": "Relación eliminada correctamente"}
