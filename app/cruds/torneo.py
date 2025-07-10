# cruds/torneo.py
from sqlalchemy.orm import Session
from ..models import Torneo

def get_torneos(session: Session):
    return session.query(Torneo).all()

def get_torneo(session: Session, torneo_id: int):
    return session.get(Torneo, torneo_id)

def create_torneo(session: Session, nombre: str, fecha_inscrip, mesas_disp: int, competencia: str, inscripcion: int):
    torneo = Torneo(
        nombre=nombre,
        fecha_inscrip=fecha_inscrip,
        mesas_disp=mesas_disp,
        competencia=competencia,
        inscripcion=inscripcion
    )
    session.add(torneo)
    session.commit()
    session.refresh(torneo)
    return torneo

def update_torneo(session: Session, torneo_id: int, nombre: str, fecha_inscrip, mesas_disp: int, competencia: str, inscripcion: int):
    torneo = session.get(Torneo, torneo_id)
    if torneo:
        torneo.nombre = nombre
        torneo.fecha_inscrip = fecha_inscrip
        torneo.mesas_disp = mesas_disp
        torneo.competencia = competencia
        torneo.inscripcion = inscripcion
        session.commit()
    return torneo

def delete_torneo(session: Session, torneo_id: int):
    torneo = session.get(Torneo, torneo_id)
    if torneo:
        session.delete(torneo)
        session.commit()
        return torneo
    return None
