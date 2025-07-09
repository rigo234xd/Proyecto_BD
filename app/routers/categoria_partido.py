from fastapi import APIRouter, Depends, HTTPException
from ..db import get_db
from ..cruds.categoria_partido import (
    create_categoria_partido,
    get_categoria_partido,
    get_categorias_partido,
    delete_categoria_partido
)

router = APIRouter()

@router.get("/")
def get_categorias_partido_endpoint(session=Depends(get_db)):
    relaciones = get_categorias_partido(session)
    return [{"categoria": r.categoria, "partido": r.partido} for r in relaciones]

@router.get("/{categoria_id}/{partido_id}")
def get_categoria_partido_endpoint(categoria_id: int, partido_id: int, session=Depends(get_db)):
    relacion = get_categoria_partido(session, categoria_id, partido_id)
    if not relacion:
        raise HTTPException(status_code=404, detail="Relacion no encontrada")
    return {"categoria": relacion.categoria, "partido": relacion.partido}

@router.post("/")
def create_categoria_partido_endpoint(categoria_id: int, partido_id: int, session=Depends(get_db)):
    relacion = create_categoria_partido(session, categoria_id, partido_id)
    return {"categoria": relacion.categoria, "partido": relacion.partido}

@router.delete("/{categoria_id}/{partido_id}")
def delete_categoria_partido_endpoint(categoria_id: int, partido_id: int, session=Depends(get_db)):
    relacion = delete_categoria_partido(session, categoria_id, partido_id)
    if not relacion:
        raise HTTPException(status_code=404, detail="Relacion no encontrada")
    return {"detail": "Relacion eliminada correctamente"}
