from fastapi import APIRouter, HTTPException, Depends
from ..db import get_db
from ..cruds.equipo import create_equipo, get_equipo, get_equipos, delete_equipo

router = APIRouter()

@router.get("/")
def get_equipos_endpoint(session=Depends(get_db)):
    equipos = get_equipos(session)
    return [{"id": equipo.id} for equipo in equipos]

@router.get("/{equipo_id}")
def get_equipo_endpoint(equipo_id: int, session=Depends(get_db)):
    equipo = get_equipo(session, equipo_id)
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo not found")
    return {"id": equipo.id}

@router.post("/")
def create_equipo_endpoint(session=Depends(get_db)):
    equipo = create_equipo(session)
    return {"id": equipo.id}

@router.delete("/{equipo_id}")
def delete_equipo_endpoint(equipo_id: int, session=Depends(get_db)):
    equipo = delete_equipo(session, equipo_id)
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo not found")
    return {"detail": "Equipo deleted successfully"}
