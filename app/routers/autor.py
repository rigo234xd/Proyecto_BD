from fastapi import APIRouter, HTTPException, Depends

from ..db import get_db
from ..cruds.autor import (
    create_autor,
    get_autor,
    get_autores,
    update_autor,
    delete_autor,
)


router = APIRouter()


@router.get("/")
def get_autores_endpoint(session=Depends(get_db)):
    autores = get_autores(session)
    return [
        {
            "id": autor.id,
            "nombre": autor.nombre,
            "pais": autor.pais_aso,
            "ciudad": autor.ciudad_aso,
            "jugadores": [
                {
                    "id": jugador.id,
                    "nombre": jugador.nombre,
                    "fecha_nacimiento": jugador.fecha_nacimiento,
                    "genero": jugador.genero_jugador,
                    "pais": jugador.pais_jugador,
                    "ciudad": jugador.ciudad_jugador
                }
                for jugador in autor.jugadores
            ] if autor.jugadores else []
        }
        for autor in autores
    ]


@router.get("/{autor_id}")
def get_autor_endpoint(autor_id: int, session=Depends(get_db)):
    autor = get_autor(session, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Asociacion not found")
    return {"id": autor.id, "nombre": autor.nombre}


@router.post("/")
def create_autor_endpoint(nombre: str, pais_aso: str, ciudad_aso: str,session=Depends(get_db)):
    autor = create_autor(session, nombre, pais_aso, ciudad_aso)
    return {"id": autor.id, "nombre": autor.nombre, "pais": autor.pais_aso, "ciudad": autor.ciudad_aso}


@router.put("/{autor_id}")
def update_autor_endpoint(autor_id: int, nombre: str, pais_aso: str, ciudad_aso: str, session=Depends(get_db)):
    autor = update_autor(session, autor_id, nombre, pais_aso, ciudad_aso)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor not found")
    return {"id": autor.id, "nombre": autor.nombre, "pais": autor.pais_aso, "ciudad": autor.ciudad_aso}


@router.delete("/{autor_id}")
def delete_autor_endpoint(autor_id: int, session=Depends(get_db)):
    autor = delete_autor(session, autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor not found")
    return {"detail": "Autor deleted successfully"}