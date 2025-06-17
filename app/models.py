from sqlalchemy import Column, Integer, String, Date, Boolean, Time, ForeignKey, Text, Table
from sqlalchemy.orm import relationship

from  .db import Base

class Asociacion(Base):
    __tablename__ = "asociacion"

    id = Column(Integer, primary_key=True)
    nombre = Column(Text, nullable=False)
    pais_aso = Column(Text, nullable=False)
    ciudad_aso = Column(Text, nullable=False)

    jugadores = relationship("Jugador", back_populates="asociacion_rel")


class Equipo(Base):
    __tablename__ = "equipo"

    id = Column(Integer, primary_key=True)

    inscripciones = relationship("Inscripcion", back_populates="equipo_rel")
    jugadores = relationship("Jugador", back_populates="equipo_rel")


class Inscripcion(Base):
    __tablename__ = "inscripcion"

    id = Column(Integer, primary_key=True)
    equipo = Column(Integer, ForeignKey("equipo.id"), nullable=False)

    equipo_rel = relationship("Equipo", back_populates="inscripciones")
    jugadores = relationship("Jugador", back_populates="inscripcion_rel")
    categorias = relationship("Categoria", back_populates="inscripcion_rel")
    torneos = relationship("Torneo", back_populates="inscripcion_rel")


class Categoria(Base):
    __tablename__ = "categoria"

    id = Column(Integer, primary_key=True)
    edad_min = Column(Integer)
    edad_max = Column(Integer)
    genero_categoria = Column(Text, nullable=False)
    sets_partido = Column(Integer)
    puntos_sets = Column(Integer)
    equipo = Column(Boolean)
    inscripcion = Column(Integer, ForeignKey("inscripcion.id"), nullable=False)

    inscripcion_rel = relationship("Inscripcion", back_populates="categorias")
    categoria_torneos = relationship("CategoriaTorneo", back_populates="categoria_rel")
    fases = relationship("Fase", back_populates="categoria_rel")
    categoria_partidos = relationship("CategoriaPartido", back_populates="categoria_rel")


class Jugador(Base):
    __tablename__ = "jugador"

    id = Column(Integer, primary_key=True)
    nombre = Column(Text, nullable=False)
    fecha_nacimiento = Column(Date)
    genero_jugador = Column(Text, nullable=False)
    pais_jugador = Column(Text, nullable=False)
    ciudad_jugador = Column(Text, nullable=False)
    asociacion = Column(Integer, ForeignKey("asociacion.id"))
    equipo = Column(Integer, ForeignKey("equipo.id"), nullable=False)
    inscripcion = Column(Integer, ForeignKey("inscripcion.id"), nullable=False)

    asociacion_rel = relationship("Asociacion", back_populates="jugadores")
    equipo_rel = relationship("Equipo", back_populates="jugadores")
    inscripcion_rel = relationship("Inscripcion", back_populates="jugadores")
    fases = relationship("FaseJugador", back_populates="jugador_rel")
    partidos_1 = relationship("JugadorPartido", back_populates="jugador_rel")
    partidos_2 = relationship("JugadorPartido2", back_populates="jugador_rel")


class Torneo(Base):
    __tablename__ = "torneo"

    id = Column(Integer, primary_key=True)
    nombre = Column(Text, nullable=False)
    fecha_inscrip = Column(Date)
    mesas_disp = Column(Integer)
    competencia = Column(Text, nullable=False)
    inscripcion = Column(Integer, ForeignKey("inscripcion.id"), nullable=False)

    inscripcion_rel = relationship("Inscripcion", back_populates="torneos")
    categoria_torneos = relationship("CategoriaTorneo", back_populates="torneo_rel")
    fases = relationship("Fase", back_populates="torneo_rel")
    mesas = relationship("Mesas", back_populates="torneo_rel")


class CategoriaTorneo(Base):
    __tablename__ = "categoria_torneo"

    categoria = Column(Integer, ForeignKey("categoria.id"), primary_key=True)
    torneo = Column(Integer, ForeignKey("torneo.id"), primary_key=True)

    categoria_rel = relationship("Categoria", back_populates="categoria_torneos")
    torneo_rel = relationship("Torneo", back_populates="categoria_torneos")


class Fase(Base):
    __tablename__ = "fase"

    id = Column(Integer, primary_key=True)
    tipo_fase = Column(Text, nullable=False)
    nombre_fase = Column(Text, nullable=False)
    torneo = Column(Integer, ForeignKey("torneo.id"), nullable=False)
    categoria = Column(Integer, ForeignKey("categoria.id"), nullable=False)

    torneo_rel = relationship("Torneo", back_populates="fases")
    categoria_rel = relationship("Categoria", back_populates="fases")
    jugadores = relationship("FaseJugador", back_populates="fase_rel")


class FaseJugador(Base):
    __tablename__ = "fase_jugador"

    fase = Column(Integer, ForeignKey("fase.id"), primary_key=True)
    jugador = Column(Integer, ForeignKey("jugador.id"), primary_key=True)

    fase_rel = relationship("Fase", back_populates="jugadores")
    jugador_rel = relationship("Jugador", back_populates="fases")


class Mesas(Base):
    __tablename__ = "mesas"

    id = Column(Integer, primary_key=True)
    asignado = Column(Boolean)
    torneo = Column(Integer, ForeignKey("torneo.id"), nullable=False)

    torneo_rel = relationship("Torneo", back_populates="mesas")
    partidos = relationship("Partido", back_populates="mesas_rel")


class Partido(Base):
    __tablename__ = "partido"

    id = Column(Integer, primary_key=True)
    tipo_partido = Column(Text, nullable=False)
    horario = Column(Time)
    mesas = Column(Integer, ForeignKey("mesas.id"), nullable=False)

    mesas_rel = relationship("Mesas", back_populates="partidos")
    categoria_partidos = relationship("CategoriaPartido", back_populates="partido_rel")
    jugador_partidos_1 = relationship("JugadorPartido", back_populates="partido_rel")
    jugador_partidos_2 = relationship("JugadorPartido2", back_populates="partido_rel")
    resultados = relationship("ResultadoSet", back_populates="partido_rel")


class CategoriaPartido(Base):
    __tablename__ = "categoria_partido"

    categoria = Column(Integer, ForeignKey("categoria.id"), primary_key=True)
    partido = Column(Integer, ForeignKey("partido.id"), primary_key=True)

    categoria_rel = relationship("Categoria", back_populates="categoria_partidos")
    partido_rel = relationship("Partido", back_populates="categoria_partidos")


class JugadorPartido(Base):
    __tablename__ = "jugador_partido"

    jugador = Column(Integer, ForeignKey("jugador.id"), primary_key=True)
    partido = Column(Integer, ForeignKey("partido.id"), primary_key=True)

    jugador_rel = relationship("Jugador", back_populates="partidos_1")
    partido_rel = relationship("Partido", back_populates="jugador_partidos_1")


class JugadorPartido2(Base):
    __tablename__ = "jugador_partido_2"

    jugador = Column(Integer, ForeignKey("jugador.id"), primary_key=True)
    partido = Column(Integer, ForeignKey("partido.id"), primary_key=True)

    jugador_rel = relationship("Jugador", back_populates="partidos_2")
    partido_rel = relationship("Partido", back_populates="jugador_partidos_2")


class ResultadoSet(Base):
    __tablename__ = "resultado_set"

    id = Column(Integer, primary_key=True)
    partido = Column(Integer, ForeignKey("partido.id"), nullable=False)
    num_set = Column(Text, nullable=False)
    jugador_1 = Column(Text, nullable=False)
    jugador_2 = Column(Text, nullable=False)

    partido_rel = relationship("Partido", back_populates="resultados")

