from fastapi import APIRouter, Depends, HTTPException
from ..db import get_db
from ..cruds.resultado_set import (
    create_resultado_set,
    get_resultado,
    get_resultados,
    update_resultado,
    delete_resultado,
)

router = APIRouter()

@router.get("/")
def get_resultados_endpoint(session=Depends(get_db)):
    resultados = get_resultados(session)
    return [
        {
            "id": r.id,
            "partido_id": r.partido,
            "num_set": r.num_set,
            "jugador_1": r.jugador_1,
            "jugador_2": r.jugador_2
        }
        for r in resultados
    ]

@router.get("/{resultado_id}")
def get_resultado_endpoint(resultado_id: int, session=Depends(get_db)):
    resultado = get_resultado(session, resultado_id)
    if not resultado:
        raise HTTPException(status_code=404, detail="Resultado no encontrado")
    return {
        "id": resultado.id,
        "partido_id": resultado.partido,
        "num_set": resultado.num_set,
        "jugador_1": resultado.jugador_1,
        "jugador_2": resultado.jugador_2
    }

@router.post("/")
def create_resultado_endpoint(partido: int, num_set: str, jugador_1: str, jugador_2: str, session=Depends(get_db)):
    resultado = create_resultado_set(session, partido, num_set, jugador_1, jugador_2)
    return {"id": resultado.id}

@router.put("/{resultado_id}")
def update_resultado_endpoint(resultado_id: int, num_set: str, jugador_1: str, jugador_2: str, session=Depends(get_db)):
    resultado = update_resultado(session, resultado_id, num_set, jugador_1, jugador_2)
    if not resultado:
        raise HTTPException(status_code=404, detail="Resultado no encontrado")
    return {"id": resultado.id}

@router.delete("/{resultado_id}")
def delete_resultado_endpoint(resultado_id: int, session=Depends(get_db)):
    resultado = delete_resultado(session, resultado_id)
    if not resultado:
        raise HTTPException(status_code=404, detail="Resultado no encontrado")
    return {"detail": "Resultado eliminado correctamente"}
