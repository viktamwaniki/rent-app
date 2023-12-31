"""add_new_table

Revision ID: 41407aea2cca
Revises: 
Create Date: 2023-09-10 20:37:58.774236

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '41407aea2cca'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'new_table',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('new_table')