# app/cruds/mesas.py
from sqlalchemy.orm import Session
from ..models import Mesas

# crea las mesas en base a la cantidad que se solicite
def create_mesas(session: Session, cantidad: int, torneo_id: int):
    mesas_creadas = []
    for _ in range(cantidad):
        mesa = Mesas(asignado=False, torneo=torneo_id)
        session.add(mesa)
        mesas_creadas.append(mesa)
    session.commit()
    return mesas_creadas

def get_mesas(session: Session):
    return session.query(Mesas).all()

def get_mesas_por_torneo(session: Session, torneo_id: int):
    return session.query(Mesas).filter(Mesas.torneo == torneo_id).all()

def delete_mesa(session: Session, mesa_id: int):
    mesa = session.get(Mesas, mesa_id)
    if mesa:
        session.delete(mesa)
        session.commit()
        return mesa
    return None
