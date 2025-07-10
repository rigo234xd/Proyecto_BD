# routers/categoria.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..db import get_db
from ..cruds.categoria import (
    get_categorias,
    get_categoria,
    create_categoria,
    update_categoria,
    delete_categoria,
)

router = APIRouter()

@router.get("/")
def get_categorias(session: Session = Depends(get_db)):
    return get_categorias(session)

@router.get("/{categoria_id}")
def get_categoria(categoria_id: int, session: Session = Depends(get_db)):
    categoria = get_categoria(session, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

@router.post("/")
def create_categoria(edad_min: int, edad_max: int, genero_categoria: str, sets_partido: int, puntos_sets: int, equipo: bool, inscripcion: int, session: Session = Depends(get_db)):
    return create_categoria(session, edad_min, edad_max, genero_categoria, sets_partido, puntos_sets, equipo, inscripcion)

@router.put("/{categoria_id}")
def update_categoria(categoria_id: int, edad_min: int, edad_max: int, genero_categoria: str, sets_partido: int, puntos_sets: int, equipo: bool, inscripcion: int, session: Session = Depends(get_db)):
    categoria = update_categoria(
        session, categoria_id,
        edad_min=edad_min, edad_max=edad_max,
        genero_categoria=genero_categoria,
        sets_partido=sets_partido,
        puntos_sets=puntos_sets,
        equipo=equipo,
        inscripcion=inscripcion
    )
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

@router.delete("/{categoria_id}")
def remove_categoria(categoria_id: int, session: Session = Depends(get_db)):
    categoria = delete_categoria(session, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return {"detail": "Categoría eliminada correctamente"}
