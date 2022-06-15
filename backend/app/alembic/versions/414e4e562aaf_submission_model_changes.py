"""Submission model changes

Revision ID: 414e4e562aaf
Revises: acfa549599ba
Create Date: 2022-06-15 01:09:27.796276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '414e4e562aaf'
down_revision = 'acfa549599ba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submission', sa.Column('evaluated', sa.Boolean(), nullable=True))
    op.add_column('submission', sa.Column('evaluation_begin', sa.DateTime(), nullable=True))
    op.add_column('submission', sa.Column('evaluation_end', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('submission', 'evaluation_end')
    op.drop_column('submission', 'evaluation_begin')
    op.drop_column('submission', 'evaluated')
    # ### end Alembic commands ###
