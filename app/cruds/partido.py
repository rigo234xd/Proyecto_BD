from sqlalchemy.orm import Session
from ..models import Partido

def create_partido(session: Session, tipo_partido: str, horario, mesas_id: int):
    partido = Partido(tipo_partido=tipo_partido, horario=horario, mesas=mesas_id)
    session.add(partido)
    session.commit()
    session.refresh(partido)
    return partido

def get_partidos(session: Session):
    return session.query(Partido).all()

def get_partido(session: Session, partido_id: int):
    return session.get(Partido, partido_id)

def update_partido(session: Session, partido_id: int, tipo_partido: str, horario, mesas_id: int):
    partido = session.get(Partido, partido_id)
    if partido:
        partido.tipo_partido = tipo_partido
        partido.horario = horario
        partido.mesas = mesas_id
        session.commit()
        session.refresh(partido)
    return partido

def delete_partido(session: Session, partido_id: int):
    partido = session.get(Partido, partido_id)
    if partido:
        session.delete(partido)
        session.commit()
    return partido
