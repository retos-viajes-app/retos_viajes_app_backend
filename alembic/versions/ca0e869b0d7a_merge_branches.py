"""Merge branches

Revision ID: ca0e869b0d7a
Revises: 045197714b87, f4c320bb01d9
Create Date: 2025-03-15 16:54:16.962947

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca0e869b0d7a'
down_revision: Union[str, None] = ('045197714b87', 'f4c320bb01d9')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
