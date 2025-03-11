"""añadir is verified

Revision ID: a6993f27ca05
Revises: 8ff18d90c462
Create Date: 2025-03-11 11:43:54.653874

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a6993f27ca05'
down_revision: Union[str, None] = '8ff18d90c462'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_verified', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_verified')
    # ### end Alembic commands ###
