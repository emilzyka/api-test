"""add user table

Revision ID: 797643f54726
Revises:  
Create Date: 2021-11-30 17:20:09.479193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '797643f54726'
down_revision = ' '
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )


def downgrade():
    op.drop_table('users')
    pass
