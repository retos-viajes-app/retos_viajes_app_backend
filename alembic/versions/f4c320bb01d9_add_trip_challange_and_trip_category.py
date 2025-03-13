"""add_trip_challange_and_trip_category

Revision ID: f4c320bb01d9
Revises: dec4bb10aabc
Create Date: 2025-03-12 17:18:00.977053

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f4c320bb01d9'
down_revision: Union[str, None] = 'dec4bb10aabc'
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
    op.drop_constraint('trip_ibfk_2', 'trip', type_='foreignkey')
    op.create_foreign_key(None, 'trip', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'trip', type_='foreignkey')
    op.create_foreign_key('trip_ibfk_2', 'trip', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_table('trip_challenge')
    op.drop_table('trip_category')
    # ### end Alembic commands ###
