from sqlalchemy.orm import Session
from ..models import JugadorPartido2

def create_jugador_partido2(session: Session, jugador: int, partido: int):
    jp = JugadorPartido2(jugador=jugador, partido=partido)
    session.add(jp)
    session.commit()
    return jp

def get_jugadores_partido2(session: Session):
    return session.query(JugadorPartido2).all()

def get_jugador_partido2(session: Session, jugador_id: int, partido_id: int):
    return session.query(JugadorPartido2).filter_by(jugador=jugador_id, partido=partido_id).first()

def delete_jugador_partido2(session: Session, jugador_id: int, partido_id: int):
    jp = session.query(JugadorPartido2).filter_by(jugador=jugador_id, partido=partido_id).first()
    if jp:
        session.delete(jp)
        session.commit()
    return jp
