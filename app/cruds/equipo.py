from sqlalchemy.orm import Session
from ..models import Equipo, Jugador

def create_equipo(session: Session, jugador_ids: list[int] = None):
    equipo = Equipo()
    session.add(equipo)
    session.flush()  # para que equipo tenga id sin hacer commit aún

    if jugador_ids:
        jugadores = session.query(Jugador).filter(Jugador.id.in_(jugador_ids)).all()
        for jugador in jugadores:
            jugador.equipo = equipo.id  # asignamos FK directamente
        session.flush()

    session.commit()
    session.refresh(equipo)
    return equipo

def get_equipos(session: Session):
    return session.query(Equipo).all()

def get_equipo(session: Session, equipo_id: int):
    return session.get(Equipo, equipo_id)

def delete_equipo(session: Session, equipo_id: int):
    equipo = session.get(Equipo, equipo_id)
    if equipo:
        session.delete(equipo)
        session.commit()
        return equipo
    return None
