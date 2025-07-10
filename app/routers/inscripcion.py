# routers/inscripcion.py
from fastapi import APIRouter, HTTPException, Depends
from ..db import get_db
from ..cruds.jugador import (get_jugador)
from ..cruds.inscripcion import (
    create_inscripcion,
    get_inscripcion,
    get_inscripciones,
    update_inscripcion,
    delete_inscripcion,
)
router = APIRouter()

@router.get("/")
def get_inscripciones_endpoint(session=Depends(get_db)):
    inscripciones = get_inscripciones(session)
    return [
        {
            "id": i.id,
            "equipo": {
                "id": i.equipo_rel.id,
            } if i.equipo_rel else None,
            "jugadores": [
                {
                    "id": j.id,
                    "nombre": j.nombre,
                } for j in i.jugadores
            ] if i.jugadores else [],
            "categorias": [
                {
                    "id": c.id,
                    "nombre": c.genero_categoria,
                } for c in i.categorias
            ] if i.categorias else [],
            "torneos": [
                {
                    "id": t.id,
                    "nombre": t.nombre,
                } for t in i.torneos
            ] if i.torneos else [],
        }
        for i in inscripciones
    ]

@router.get("/{inscripcion_id}")
def get_inscripcion_endpoint(inscripcion_id: int, session=Depends(get_db)):
    inscripcion = get_inscripcion(session, inscripcion_id)
    if not inscripcion:
        raise HTTPException(status_code=404, detail="Inscripción no encontrada")
    return {
        "id": inscripcion.id,
        "equipo": inscripcion.equipo,
    }

@router.post("/")
def create_inscripcion_endpoint(equipo_id: int, jugador_id:int, session=Depends(get_db)):
    inscripcion = create_inscripcion(session, equipo_id, jugador_id)
    return {
        "id": inscripcion.id,
        "id_jugador":jugador_id,
        "equipo": inscripcion.equipo,
    }

@router.put("/{inscripcion_id}")
def update_inscripcion_endpoint(inscripcion_id: int, equipo_id: int, session=Depends(get_db)):
    inscripcion = update_inscripcion(session, inscripcion_id, equipo_id)
    if not inscripcion:
        raise HTTPException(status_code=404, detail="Inscripción no encontrada")
    return {
        "id": inscripcion.id,
        "equipo": inscripcion.equipo,
    }

@router.delete("/{inscripcion_id}")
def delete_inscripcion_endpoint(inscripcion_id: int, session=Depends(get_db)):
    inscripcion = delete_inscripcion(session, inscripcion_id)
    if not inscripcion:
        raise HTTPException(status_code=404, detail="Inscripción no encontrada")
    return {"detail": "Inscripción eliminada correctamente"}
