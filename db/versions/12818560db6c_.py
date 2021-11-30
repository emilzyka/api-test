"""empty message

Revision ID: 12818560db6c
Revises: c5a1a2bdabcc
Create Date: 2021-11-30 18:35:29.603417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12818560db6c'
down_revision = 'c5a1a2bdabcc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
        'is_published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text
        ('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
