"""Extra problem fields

Revision ID: 3fc64185108d
Revises: 84d51d4e2b0e
Create Date: 2022-06-13 21:19:31.565984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fc64185108d'
down_revision = '84d51d4e2b0e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('problem', sa.Column('listed', sa.Boolean(), nullable=True))
    op.add_column('problem', sa.Column('disabled', sa.Boolean(), nullable=True))
    op.add_column('problem', sa.Column('frozen', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('problem', 'frozen')
    op.drop_column('problem', 'disabled')
    op.drop_column('problem', 'listed')
    # ### end Alembic commands ###
