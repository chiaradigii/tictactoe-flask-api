"""Create Game table

Revision ID: 5b8c83a65ffe
Revises: 
Create Date: 2024-08-09 09:59:23.828858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b8c83a65ffe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('board_state', sa.String(), nullable=False),
    sa.Column('current_player', sa.String(length=1), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('game')
    # ### end Alembic commands ###
