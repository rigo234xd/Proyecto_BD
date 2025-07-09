from fastapi import APIRouter, HTTPException, Depends
from ..db import get_db
from ..cruds.jugador_partido import (
    create_jugador_partido,
    get_jugador_partido,
    get_jugadores_partido,
    delete_jugador_partido
)

router = APIRouter()

@router.get("/")
def get_jugadores_partido_endpoint(session=Depends(get_db)):
    return [
        {
            "jugador": jp.jugador,
            "partido": jp.partido
        } for jp in get_jugadores_partido(session)
    ]

@router.get("/{jugador_id}/{partido_id}")
def get_jugador_partido_endpoint(jugador_id: int, partido_id: int, session=Depends(get_db)):
    jp = get_jugador_partido(session, jugador_id, partido_id)
    if not jp:
        raise HTTPException(status_code=404, detail="Jugador-Partido not found")
    return {
        "jugador": jp.jugador,
        "partido": jp.partido
    }

@router.post("/")
def create_jugador_partido_endpoint(jugador: int, partido: int, session=Depends(get_db)):
    jp = create_jugador_partido(session, jugador, partido)
    return {
        "jugador": jp.jugador,
        "partido": jp.partido
    }

@router.delete("/{jugador_id}/{partido_id}")
def delete_jugador_partido_endpoint(jugador_id: int, partido_id: int, session=Depends(get_db)):
    deleted = delete_jugador_partido(session, jugador_id, partido_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Jugador-Partido not found")
    return {"detail": "Jugador-Partido deleted successfully"}
