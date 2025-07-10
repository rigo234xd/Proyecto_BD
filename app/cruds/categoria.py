from sqlalchemy.orm import Session
from ..models import Categoria

def create_categoria(session: Session, edad_min: int, edad_max: int, genero_categoria: str, sets_partido: int, puntos_sets: int, equipo: bool, inscripcion_id: int):
    categoria = Categoria(
        edad_min=edad_min,
        edad_max=edad_max,
        genero_categoria=genero_categoria,
        sets_partido=sets_partido,
        puntos_sets=puntos_sets,
        equipo=equipo,
        inscripcion=inscripcion_id
    )
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria

def get_categorias(session: Session):
    return session.query(Categoria).all()

def get_categoria(session: Session, categoria_id: int):
    return session.get(Categoria, categoria_id)

def update_categoria(session: Session, categoria_id: int, edad_min: int, edad_max: int, genero_categoria: str, sets_partido: int, puntos_sets: int, equipo: bool):
    categoria = session.get(Categoria, categoria_id)
    if categoria:
        categoria.edad_min = edad_min
        categoria.edad_max = edad_max
        categoria.genero_categoria = genero_categoria
        categoria.sets_partido = sets_partido
        categoria.puntos_sets = puntos_sets
        categoria.equipo = equipo
        session.commit()
        session.refresh(categoria)
    return categoria

def delete_categoria(session: Session, categoria_id: int):
    categoria = session.get(Categoria, categoria_id)
    if categoria:
        session.delete(categoria)
        session.commit()
    return categoria