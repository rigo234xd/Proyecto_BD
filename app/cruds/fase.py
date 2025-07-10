from sqlalchemy.orm import Session
from ..models import Fase

def create_fase(session: Session, tipo_fase: str, nombre_fase: str, torneo_id: int, categoria_id: int):
    fase = Fase(tipo_fase=tipo_fase, nombre_fase=nombre_fase, torneo=torneo_id, categoria=categoria_id)
    session.add(fase)
    session.commit()
    session.refresh(fase)
    return fase

def get_fases(session: Session):
    return session.query(Fase).all()

def get_fase(session: Session, fase_id: int):
    return session.get(Fase, fase_id)

def update_fase(session: Session, fase_id: int, tipo_fase: str, nombre_fase: str):
    fase = session.get(Fase, fase_id)
    if fase:
        fase.tipo_fase = tipo_fase
        fase.nombre_fase = nombre_fase
        session.commit()
        session.refresh(fase)
    return fase

def delete_fase(session: Session, fase_id: int):
    fase = session.get(Fase, fase_id)
    if fase:
        session.delete(fase)
        session.commit()
    return fase
