from fastapi import APIRouter, HTTPException, Depends
from ..db import get_db
from ..cruds.fase import (
    create_fase, 
    get_fases, 
    get_fase, 
    update_fase, 
    delete_fase,
)

router = APIRouter()

@router.get("/")
def get_fases_endpoint(session=Depends(get_db)):
    fases = get_fases(session)
    return [
        {
            "id": f.id,
            "tipo_fase": f.tipo_fase,
            "nombre_fase": f.nombre_fase,
            "torneo_id": f.torneo,
            "categoria_id": f.categoria
        } for f in fases
    ]

@router.get("/{fase_id}")
def get_fase_endpoint(fase_id: int, session=Depends(get_db)):
    fase = get_fase(session, fase_id)
    if not fase:
        raise HTTPException(status_code=404, detail="Fase not found")
    return {
        "id": fase.id,
        "tipo_fase": fase.tipo_fase,
        "nombre_fase": fase.nombre_fase,
        "torneo_id": fase.torneo,
        "categoria_id": fase.categoria
    }

@router.post("/")
def create_fase_endpoint(
    tipo_fase: str,
    nombre_fase: str,
    torneo_id: int,
    categoria_id: int,
    session=Depends(get_db)
):
    fase = create_fase(session, tipo_fase, nombre_fase, torneo_id, categoria_id)
    return {
        "id": fase.id,
        "tipo_fase": fase.tipo_fase,
        "nombre_fase": fase.nombre_fase,
        "torneo_id": fase.torneo,
        "categoria_id": fase.categoria
    }

@router.put("/{fase_id}")
def update_fase_endpoint(
    fase_id: int,
    tipo_fase: str,
    nombre_fase: str,
    session=Depends(get_db)
):
    fase = update_fase(session, fase_id, tipo_fase, nombre_fase)
    if not fase:
        raise HTTPException(status_code=404, detail="Fase not found")
    return {
        "id": fase.id,
        "tipo_fase": fase.tipo_fase,
        "nombre_fase": fase.nombre_fase,
        "torneo_id": fase.torneo,
        "categoria_id": fase.categoria
    }

@router.delete("/{fase_id}")
def delete_fase_endpoint(fase_id: int, session=Depends(get_db)):
    fase = delete_fase(session, fase_id)
    if not fase:
        raise HTTPException(status_code=404, detail="Fase not found")
    return {"detail": "Fase deleted successfully"}
