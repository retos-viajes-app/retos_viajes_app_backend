"""trip category with delete cascade

Revision ID: c76c16119cd3
Revises: a1fd5762f8f1
Create Date: 2025-03-30 11:13:01.886348

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c76c16119cd3'
down_revision: Union[str, None] = 'a1fd5762f8f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('trip_category_ibfk_1', 'trip_category', type_='foreignkey')
    op.drop_constraint('trip_category_ibfk_2', 'trip_category', type_='foreignkey')
    op.create_foreign_key(None, 'trip_category', 'category', ['category_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'trip_category', 'trip', ['trip_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'trip_category', type_='foreignkey')
    op.drop_constraint(None, 'trip_category', type_='foreignkey')
    op.create_foreign_key('trip_category_ibfk_2', 'trip_category', 'trip', ['trip_id'], ['id'])
    op.create_foreign_key('trip_category_ibfk_1', 'trip_category', 'category', ['category_id'], ['id'])
    # ### end Alembic commands ###
