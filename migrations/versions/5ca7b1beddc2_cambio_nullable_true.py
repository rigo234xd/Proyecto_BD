"""cambio nullable true

Revision ID: 5ca7b1beddc2
Revises: b59706ac9665
Create Date: 2025-06-26 17:23:18.154978

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ca7b1beddc2'
down_revision: Union[str, None] = 'b59706ac9665'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('jugador', 'equipo',
               existing_type=sa.INTEGER(),
               nullable=True,
               schema='testpublic')
    op.alter_column('jugador', 'inscripcion',
               existing_type=sa.INTEGER(),
               nullable=True,
               schema='testpublic')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('jugador', 'inscripcion',
               existing_type=sa.INTEGER(),
               nullable=False,
               schema='testpublic')
    op.alter_column('jugador', 'equipo',
               existing_type=sa.INTEGER(),
               nullable=False,
               schema='testpublic')
    # ### end Alembic commands ###
