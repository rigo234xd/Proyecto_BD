from fastapi import APIRouter, HTTPException, Depends
from datetime import date
from ..db import get_db
from ..cruds.jugador import (
    create_jugador,
    get_jugador,
    get_jugadores,
    update_jugador,
    delete_jugador,
)

router = APIRouter()

@router.get("/")
def get_jugadores_endpoint(Session=Depends(get_db)):
    jugadores = get_jugadores(Session)
    return[
        {"id": j.id,
        "nombre": j.nombre,
        "fecha_nacimiento": j.fecha_nacimiento,
        "genero": j.genero_jugador,
        "pais": j.pais,
        "ciudad": j.ciudad,
        "asociacion": {
        "id": j.asociacion_rel.id,
        "nombre":j.asociacion_rel.nombre
    } if j.asociacion_rel else None,
    "equipo": {
        "id": j.equipo_rel.id,
    } if j.equipo_rel else None,
    "inscripcion": {
        "id": j.inscripcion_rel.id,
    } if j.inscripcion_rel else None,
        }
        for j in jugadores
    ]


@router.get("/{jugador_id}")
def get_jugador_endpoint(jugador_id:int, Session=Depends(get_db)):
    jugador = get_jugador(Session, jugador_id)
    if not jugador:
        raise HTTPException(status_code=404, detail="jugador no encontrado")
    return{
        "id": jugador.id,
        "nombre": jugador.nombre,
        "fecha_nacimiento": jugador.fecha_nacimiento,
        "genero": jugador.genero_jugador,
        "pais": jugador.pais_jugador,
        "ciudad": jugador.ciudad_jugador,
        "asociacion": {
        "id": jugador.asociacion_rel.id,
        "nombre": jugador.asociacion_rel.nombre
    } if jugador.asociacion_rel else None,
    "equipo": {
        "id": jugador.equipo_rel.id,
    } if jugador.equipo_rel else None,
    "inscripcion": {
        "id": jugador.inscripcion_rel.id,
    } if jugador.inscripcion_rel else None,
    }


@router.post("/")
def create_jugador_endpoint(nombre:str, fecha_nacimiento:date, genero_jugador:str, pais_jugador:str, ciudad_jugador:str, session=Depends(get_db)):
    jugador = create_jugador(session, nombre, fecha_nacimiento, genero_jugador, pais_jugador, ciudad_jugador)
    return{
        "nombre": jugador.nombre,
        "fecha_nacimiento": jugador.fecha_nacimiento,
        "genero": jugador.genero_jugador,
        "pais": jugador.pais_jugador,
        "ciudad": jugador.ciudad_jugador,
        "asociacion": {
        "id": jugador.asociacion_rel.id,
        "nombre": jugador.asociacion_rel.nombre
    } if jugador.asociacion_rel else None,
    "equipo": {
        "id": jugador.equipo_rel.id,
    } if jugador.equipo_rel else None,
    "inscripcion": {
        "id": jugador.inscripcion_rel.id,
    } if jugador.inscripcion_rel else None,
    }

@router.put("/{jugador_id}")
def update_jugador_endpoint(jugador_id:int, nombre:str, fecha_nacimiento:date, genero_jugador:str, pais_jugador:str, ciudad_jugador:str, session=Depends(get_db)):
    jugador = update_jugador(session, jugador_id, nombre, fecha_nacimiento, genero_jugador, pais_jugador, ciudad_jugador)
    return{
        "id": jugador.id,
        "nombre": jugador.nombre,
        "fecha_nacimiento": jugador.fecha_nacimiento,
        "genero": jugador.genero_jugador,
        "pais": jugador.pais_jugador,
        "ciudad":jugador.ciudad_jugador,
        "asociacion": {
        "id": jugador.asociacion_rel.id,
        "nombre": jugador.asociacion_rel.nombre
    } if jugador.asociacion_rel else None,
    "equipo": {
        "id": jugador.equipo_rel.id,
    } if jugador.equipo_rel else None,
    "inscripcion": {
        "id": jugador.inscripcion_rel.id,
    } if jugador.inscripcion_rel else None,
    }

@router.delete("/{jugador_id}")
def delete_jugador_endpoint(jugador_id:int, session=Depends(get_db)):
    jugador = delete_jugador(session, jugador_id)
    if not jugador:
        raise HTTPException(status_code=404, detail="jugador not found")
    return{
        "detail": "jugador deleted successfully"
    }