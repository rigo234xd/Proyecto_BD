# app/routers/mesas.py
from fastapi import APIRouter, Depends, HTTPException
from ..db import get_db
from ..cruds.mesas import (
    create_mesas, 
    get_mesas, 
    get_mesas_por_torneo, 
    delete_mesa,
)

router = APIRouter(prefix="/mesas", tags=["mesas"])

@router.post("/")
def create_mesas_endpoint(cantidad: int, torneo_id: int, session=Depends(get_db)):
    mesas = create_mesas(session, cantidad, torneo_id)
    return [{"id": m.id, "asignado": m.asignado, "torneo": m.torneo} for m in mesas]

@router.get("/")
def get_mesas_endpoint(session=Depends(get_db)):
    mesas = get_mesas(session)
    return [{"id": m.id, "asignado": m.asignado, "torneo": m.torneo} for m in mesas]

@router.get("/torneo/{torneo_id}")
def get_mesas_por_torneo_endpoint(torneo_id: int, session=Depends(get_db)):
    mesas = get_mesas_por_torneo(session, torneo_id)
    return [{"id": m.id, "asignado": m.asignado, "torneo": m.torneo} for m in mesas]

@router.delete("/{mesa_id}")
def delete_mesa_endpoint(mesa_id: int, session=Depends(get_db)):
    mesa = delete_mesa(session, mesa_id)
    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")
    return {"detalle": "Mesa eliminada exitosamente"}

