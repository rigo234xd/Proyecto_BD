# CRUD: cruds/inscripcion.py
from sqlalchemy.orm import Session
from ..models import Inscripcion, Jugador

#enlista el id del jugador para despues ser filtrado y ser ingresado el la inscripcion
def create_inscripcion(session: Session, equipo_id: int, jugador_id: int):
    inscripcion = Inscripcion(equipo=equipo_id)
    session.add(inscripcion)
    session.flush()

    jugadores= [jugador_id]

    if jugadores:
        jugadores = session.query(Jugador).filter(Jugador.id.in_(jugadores)).all()
        for jugador in jugadores:
            jugador.inscripcion = jugador.id  # asignamos FK directamente
        session.flush()

    session.commit()
    session.refresh(inscripcion)
    return inscripcion

def get_inscripciones(session: Session):
    return session.query(Inscripcion).all()

def get_inscripcion(session: Session, inscripcion_id: int):
    return session.get(Inscripcion, inscripcion_id)

def update_inscripcion(session: Session, inscripcion_id: int, equipo_id: int):
    inscripcion = session.get(Inscripcion, inscripcion_id)
    if inscripcion:
        inscripcion.equipo = equipo_id
        session.commit()
    return inscripcion

def delete_inscripcion(session: Session, inscripcion_id: int):
    inscripcion = session.get(Inscripcion, inscripcion_id)
    if inscripcion:
        session.delete(inscripcion)
        session.commit()
        return inscripcion
    return None
