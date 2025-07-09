from sqlalchemy.orm import Session

from ..models import Asociacion


def create_autor(session: Session, nombre: str, pais_aso: str, ciudad_aso: str):
    autor = Asociacion(nombre=nombre, pais_aso=pais_aso, ciudad_aso=ciudad_aso)
    session.add(autor)
    session.commit()
    return autor


def get_autores(session: Session):
    return session.query(Asociacion).all()


def get_autor(session: Session, autor_id: int, pais_aso: str, ciudad_aso: str):
    return session.get(Asociacion, autor_id, pais_aso, ciudad_aso)


def update_autor(session: Session, autor_id: int, nombre: str):
    autor = session.get(Asociacion, autor_id)
    if autor:
        autor.nombre = nombre
        session.commit()
    return autor


def delete_autor(session: Session, autor_id: int):
    autor = session.get(Asociacion, autor_id)
    if autor:
        session.delete(autor)
        session.commit()
        return autor
    return None