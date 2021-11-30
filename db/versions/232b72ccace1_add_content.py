"""add content

Revision ID: 232b72ccace1
Revises: 8d54ee6e0eb6
Create Date: 2021-11-30 17:14:59.874645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = ' '
down_revision = '8d54ee6e0eb6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
