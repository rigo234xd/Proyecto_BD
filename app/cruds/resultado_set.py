from sqlalchemy.orm import Session

from ..models import ResultadoSet

def create_resultado(session: Session, partido_id: int, num_set: str, jugador_1: str, jugador_2: str):
    resultado = ResultadoSet(
        partido=partido_id,
        num_set=num_set,
        jugador_1=jugador_1,
        jugador_2=jugador_2
    )
    session.add(resultado)
    session.commit()
    return resultado
    
def get_resultados(session: Session):
    return session.query(ResultadoSet).all()

def get_resultado(session: Session, ResultadoSet_id: int):
    return session.get(ResultadoSet, ResultadoSet_id)

def update_resultado(session: Session, resultado_id: int, num_set: str, jugador_1: str, jugador_2: str):
    resultado = session.get(ResultadoSet, resultado_id)
    if resultado:
        resultado.num_set = num_set
        resultado.jugador_1 = jugador_1
        resultado.jugador_2 = jugador_2
        session.commit()
    return resultado

def delete_resultado(session: Session, Resultado_id: int):
    resultado = session.get(ResultadoSet, Resultado_id)
    if resultado:
        session.delete(resultado)
        session.commit()
        return resultado
    return None