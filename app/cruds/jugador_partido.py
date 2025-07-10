from sqlalchemy.orm import Session
from ..models import JugadorPartido

def create_jugador_partido(session: Session, jugador: int, partido: int):
    jp = JugadorPartido(jugador=jugador, partido=partido)
    session.add(jp)
    session.commit()
    return jp

def get_jugadores_partido(session: Session):
    return session.query(JugadorPartido).all()

def get_jugador_partido(session: Session, jugador_id: int, partido_id: int):
    return session.query(JugadorPartido).filter_by(jugador=jugador_id, partido=partido_id).first()

def delete_jugador_partido(session: Session, jugador_id: int, partido_id: int):
    jp = session.query(JugadorPartido).filter_by(jugador=jugador_id, partido=partido_id).first()
    if jp:
        session.delete(jp)
        session.commit()
    return jp
