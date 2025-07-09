from fastapi import APIRouter, Depends, HTTPException
from ..db import get_db
from ..cruds.partido import (
    create_partido,
    get_partido,
    get_partidos,
    update_partido,
    delete_partido
)

router = APIRouter()

@router.get("/")
def get_partidos_endpoint(session=Depends(get_db)):
    partidos = get_partidos(session)
    return [
        {
            "id": p.id,
            "tipo": p.tipo_partido,
            "horario": p.horario,
            "mesa": {
                "id": p.mesas_rel.id,
                "asignado": p.mesas_rel.asignado
            } if p.mesas_rel else None
        }
        for p in partidos
    ]

@router.get("/{partido_id}")
def get_partido_endpoint(partido_id: int, session=Depends(get_db)):
    partido = get_partido(session, partido_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido not found")
    return {
        "id": partido.id,
        "tipo": partido.tipo_partido,
        "horario": partido.horario
    }

@router.post("/")
def create_partido_endpoint(tipo_partido: str, horario, mesas_id: int, session=Depends(get_db)):
    partido = create_partido(session, tipo_partido, horario, mesas_id)
    return {
        "id": partido.id,
        "tipo": partido.tipo_partido,
        "horario": partido.horario,
        "mesa_id": partido.mesas
    }

@router.put("/{partido_id}")
def update_partido_endpoint(partido_id: int, tipo_partido: str, horario, mesas_id: int, session=Depends(get_db)):
    partido = update_partido(session, partido_id, tipo_partido, horario, mesas_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido not found")
    return {
        "id": partido.id,
        "tipo": partido.tipo_partido,
        "horario": partido.horario,
        "mesa_id": partido.mesas
    }

@router.delete("/{partido_id}")
def delete_partido_endpoint(partido_id: int, session=Depends(get_db)):
    partido = delete_partido(session, partido_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido not found")
    return {"detail": "Partido deleted successfully"}
