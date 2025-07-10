# routers/torneo.py
from fastapi import APIRouter, HTTPException, Depends
from ..db import get_db
from ..cruds.torneo import (
    get_torneos,
    get_torneo,
    create_torneo,
    update_torneo,
    delete_torneo
)

router = APIRouter()

@router.get("/")
def get_torneos_endpoint(session=Depends(get_db)):
    torneos = get_torneos(session)
    return [
        {
            "id": t.id,
            "nombre": t.nombre,
            "fecha_inscrip": t.fecha_inscrip,
            "mesas_disp": t.mesas_disp,
            "competencia": t.competencia,
            "inscripcion": t.inscripcion
        }
        for t in torneos
    ]

@router.get("/{torneo_id}")
def get_torneo_endpoint(torneo_id: int, session=Depends(get_db)):
    torneo = get_torneo(session, torneo_id)
    if not torneo:
        raise HTTPException(status_code=404, detail="Torneo not found")
    return {
        "id": torneo.id,
        "nombre": torneo.nombre,
        "fecha_inscrip": torneo.fecha_inscrip,
        "mesas_disp": torneo.mesas_disp,
        "competencia": torneo.competencia,
        "inscripcion": torneo.inscripcion
    }

@router.post("/")
def create_torneo_endpoint(nombre: str, fecha_inscrip, mesas_disp: int, competencia: str, inscripcion: int, session=Depends(get_db)):
    torneo = create_torneo(session, nombre, fecha_inscrip, mesas_disp, competencia, inscripcion)
    return {
        "id": torneo.id,
        "nombre": torneo.nombre,
        "fecha_inscrip": torneo.fecha_inscrip,
        "mesas_disp": torneo.mesas_disp,
        "competencia": torneo.competencia,
        "inscripcion": torneo.inscripcion
    }

@router.put("/{torneo_id}")
def update_torneo_endpoint(torneo_id: int, nombre: str, fecha_inscrip, mesas_disp: int, competencia: str, inscripcion: int, session=Depends(get_db)):
    torneo = update_torneo(session, torneo_id, nombre, fecha_inscrip, mesas_disp, competencia, inscripcion)
    if not torneo:
        raise HTTPException(status_code=404, detail="Torneo not found")
    return {
        "id": torneo.id,
        "nombre": torneo.nombre,
        "fecha_inscrip": torneo.fecha_inscrip,
        "mesas_disp": torneo.mesas_disp,
        "competencia": torneo.competencia,
        "inscripcion": torneo.inscripcion
    }

@router.delete("/{torneo_id}")
def delete_torneo_endpoint(torneo_id: int, session=Depends(get_db)):
    torneo = delete_torneo(session, torneo_id)
    if not torneo:
        raise HTTPException(status_code=404, detail="Torneo not found")
    return {"detail": "Torneo deleted successfully"}
