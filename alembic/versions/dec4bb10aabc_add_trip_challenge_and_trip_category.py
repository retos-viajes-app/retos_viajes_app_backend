"""add_trip_challenge_and_trip_category

Revision ID: dec4bb10aabc
Revises: a6993f27ca05
Create Date: 2025-03-12 09:40:16.914605

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dec4bb10aabc'
down_revision: Union[str, None] = 'a6993f27ca05'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trip_category',
    sa.Column('trip_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['trip_id'], ['trip.id'], ),
    sa.PrimaryKeyConstraint('trip_id', 'category_id')
    )
    op.create_table('trip_challenge',
    sa.Column('trip_id', sa.Integer(), nullable=False),
    sa.Column('challenge_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['challenge_id'], ['challenge.id'], ),
    sa.ForeignKeyConstraint(['trip_id'], ['trip.id'], ),
    sa.PrimaryKeyConstraint('trip_id', 'challenge_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trip_challenge')
    op.drop_table('trip_category')
    # ### end Alembic commands ###
