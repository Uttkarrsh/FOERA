"""Add cost field to products model

Revision ID: cce9d856205f
Revises: a63e8ba7186c
Create Date: 2024-07-07 17:05:04.161415

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cce9d856205f'
down_revision: Union[str, None] = 'a63e8ba7186c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('cost', sa.Float(), nullable=False, server_default='0.0'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'cost')
    # ### end Alembic commands ###
