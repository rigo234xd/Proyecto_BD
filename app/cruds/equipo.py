from sqlalchemy.orm import Session
from ..models import Equipo

def create_equipo(session: Session):
    equipo = Equipo()
    session.add(equipo)
    session.commit()
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
