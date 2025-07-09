from sqlalchemy.orm import Session
from datetime import date
from ..models import Jugador


def create_jugador(session: Session, nombre:str, fecha_nacimiento: date, genero_jugador:str, pais_jugador:str, ciudad_jugador:str):
    jugador = Jugador(nombre=nombre, fecha_nacimiento = fecha_nacimiento, genero_jugador = genero_jugador, pais_jugador = pais_jugador, ciudad_jugador = ciudad_jugador)
    session.add(jugador)
    session.commit()
    return jugador


def get_jugadores(session: Session):
    return session.query(Jugador).all()

def get_jugador(session: Session, Jugador_id: int):
    return session.get(Jugador, Jugador_id)

def update_jugador(session: Session, jugador_id: int, nombre: str, fecha_nacimiento:date, genero_jugador:str, pais_jugador: str, ciudad_jugador:str):
    jugador = session.get(Jugador, jugador_id)
    if jugador:
        jugador.nombre = nombre
        jugador.fecha_nacimiento = fecha_nacimiento
        jugador.genero_jugador = genero_jugador
        jugador.pais_jugador = pais_jugador
        jugador.ciudad_jugador = ciudad_jugador
        session.commit()
    return jugador

def delete_jugador(session: Session, jugador_id: int):
    jugador = session.get(Jugador, jugador_id)
    if jugador:
        session.delete(jugador)
        session.commit()
        return jugador
    return None

