# Proyecto con SQLAlchemy + Alembic + PostgreSQL

Este proyecto usa **SQLAlchemy** como ORM y **Alembic** para las migraciones, conectando a una base de datos **PostgreSQL**.

---

# participantes:
-Benjamin uribe\
-Max Coñoman\
-Rigoberto Alvarado\
-Angelo Reyes

---

# Enunciado

Se necesita modelar e implementar una base de datos para la gestión de torneos de tenis de mesa, que permita registrar la información de los jugadores, sus asociaciones y su participación en los torneos.
Los jugadores pueden estar afiliados a una asociación, pero también pueden tener una ciudad y país distintos a los de su asociación, de lo contrario son jugadores independientes.
Los torneos se organizan en fases de grupos (clasificación) y/o eliminación directa (llaves), con partidos que pueden ser individuales o dobles. Cada torneo cuenta con mesas 
disponibles para la distribución de partidos, y estos se programan con horarios de inicio específicos.
Los jugadores se inscriben en categorías que corresponden a su edad y sexo. Las categorías son datos maestros del sistema (por ejemplo: "Todo competidor Varón") y pueden ser 
utilizadas en múltiples torneos. Una vez cerradas las inscripciones, el torneo inicia el proceso de asignar partidos a las mesas, comenzando por la fase de grupos o, si no hay 
fase de grupos, por la eliminación directa.
Las llaves de eliminación directa pueden incluir Bye, permitiendo que algunos participantes avancen automáticamente sin jugar si no se pueden emparejar todos.
Cada partido debe registrar su resultado, lo que implica anotar los sets ganados por cada jugador o equipo. Para esto, cada categoría define cuántos sets se juegan por 
partido y cuántos puntos se requieren para ganar un set, ya que estas reglas pueden variar según la categoría.

El sistema debe gestionar:

Información de jugadores: nombre, fecha de nacimiento, género, ciudad, país, asociación (si corresponde).
Información de asociaciones: nombre, ciudad, país.
Información de torneos: nombre, fechas de inscripción y competencia, mesas disponibles.
Información de categorías como entidades maestras (edad mínima, edad máxima, género, sets por partido, puntos por set).
Participación de jugadores individuales y equipos de dobles en categorías específicas dentro de un torneo.
Partidos: tipo (individual o dobles), participantes, horario, mesa asignada y resultados.
Gestión de la fase de grupos, con asignación de participantes a grupos y partidos dentro de cada grupo.
Gestión de la eliminación directa, incluyendo rondas, posiciones en la llave, y manejo de Byes.
Registro de resultados por set en cada partido, tanto en individuales como dobles.


---

## 🔧 Configuración rápida

1. **Copia y edita la configuración**

```bash
cp sample.env .env
````

Edita `.env` y cambia `DATABASE_URI` con tu conexión PostgreSQL:

```
DATABASE_URI=postgresql://usuario:password@localhost:5432/mi_base
```

---

2. **(Opcional recomendado)** Crea entorno virtual

```bash
python -m venv env
source env/bin/activate  # en Windows: .\env\Scripts\activate
```

---

3. **Instala dependencias**

```bash
pip install -r requirements.txt
```

---

4. **Crea y aplica migraciones**

```bash
alembic revision --autogenerate -m "primer modelo"
alembic upgrade head
```

---

5. **Listo para usar**

Ahora puedes importar modelos y usar SQLAlchemy normalmente con la base de datos migrada.

---

## 📁 Archivos importantes

* `.env`: configuración local (no lo subas)
* `sample.env`: plantilla para `.env`
* `app/models.py`: define tus modelos aquí
* `app/db.py`: define `Base` y conexión

---

## 📝 Notas

* Las migraciones quedan en `alembic/versions/`.
* Usa `alembic downgrade -1` si necesitas deshacer una migración.
