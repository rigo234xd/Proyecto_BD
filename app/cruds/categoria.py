# cruds/categoria.py
from sqlalchemy.orm import Session
from ..models import Categoria

def get_categorias(session: Session):
    return session.query(Categoria).all()

def get_categoria(session: Session, categoria_id: int):
    return session.get(Categoria, categoria_id)

def create_categoria(session: Session, edad_min: int, edad_max: int, genero_categoria: str, sets_partido: int, puntos_sets: int, equipo: bool, inscripcion: int):
    categoria = Categoria(
        edad_min=edad_min,
        edad_max=edad_max,
        genero_categoria=genero_categoria,
        sets_partido=sets_partido,
        puntos_sets=puntos_sets,
        equipo=equipo,
        inscripcion=inscripcion
    )
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria

def update_categoria(session: Session, categoria_id: int, **kwargs):
    categoria = session.get(Categoria, categoria_id)
    if categoria:
        for key, value in kwargs.items():
            setattr(categoria, key, value)
        session.commit()
        session.refresh(categoria)
    return categoria

def delete_categoria(session: Session, categoria_id: int):
    categoria = session.get(Categoria, categoria_id)
    if categoria:
        session.delete(categoria)
        session.commit()
        return categoria
    return None
