from sqlalchemy.orm import Session
from ..models import CategoriaPartido

def create_categoria_partido(session: Session, categoria_id: int, partido_id: int):
    relacion = CategoriaPartido(categoria=categoria_id, partido=partido_id)
    session.add(relacion)
    session.commit()
    return relacion

def get_categorias_partido(session: Session):
    return session.query(CategoriaPartido).all()

def get_categoria_partido(session: Session, categoria_id: int, partido_id: int): #filtra la busqueda por los id de categoria y partido
    return session.query(CategoriaPartido).filter_by(categoria=categoria_id, partido=partido_id).first()

def delete_categoria_partido(session: Session, categoria_id: int, partido_id: int):
    relacion = session.query(CategoriaPartido).filter_by(categoria=categoria_id, partido=partido_id).first()
    if relacion:
        session.delete(relacion)
        session.commit()
    return relacion
