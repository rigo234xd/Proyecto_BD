from sqlalchemy.orm import Session

from ..models import ResultadoSet

def create_resultado(session: Session, partido:int):
    resultado = ResultadoSet(partido = partido)
    session.add(resultado)
    session.commit()
    return resultado
    
def get_resultados(session: Session):
    return session.query(ResultadoSet).all()

def get_resultado(session: Session, ResultadoSet_id: int):
    return session.get(ResultadoSet, ResultadoSet_id)

def update_resultado(session: Session, ResultadoSet_id: int, partido: str):
    resultado = session.get(ResultadoSet, ResultadoSet_id)
    if resultado:
        resultado.partido = partido
        session.commit()
    return resultado


def delete_resultado(session: Session, Resultado_id: int):
    resultado = session.get(ResultadoSet, Resultado_id)
    if resultado:
        session.delete(resultado)
        session.commit
        return resultado
    return None