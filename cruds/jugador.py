from sqlalchemy.orm import session
from datetime import datetime
from ..models import Jugador


def create_jugador(session: session, nombre:str, fecha_nacimiento: datetime, genero:str, pais:str, ciudad:str):
    Jugador = Jugador(nombre=nombre, , genero = genero, pais = pais, ciudad = ciudad)
    session.add(Jugador)
    session.commit()
    return Jugador


def get_jugadores(session: session):
    return session.query(Jugador).all()

def get_jugador(session: session, Jugador_id: int):
    return session.get(Jugador, Jugador_id)

def update_jugador(args):
 pass