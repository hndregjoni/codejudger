"""Submission

Revision ID: acfa549599ba
Revises: 0cbc86275bf6
Create Date: 2022-06-15 01:03:38.031934

"""
from alembic import op
import sqlalchemy as sa

from app.core.config import settings


# revision identifiers, used by Alembic.
revision = 'acfa549599ba'
down_revision = '0cbc86275bf6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('submission', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('submission', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('submission', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('submission', sa.Column('problem_id', sa.Integer(), nullable=True))
    op.add_column('submission', sa.Column('code', sa.String(length=settings.MAX_SOL_LEN), nullable=True))
    op.add_column('submission', sa.Column('judger_id', sa.Integer(), nullable=True))
    op.add_column('submission', sa.Column('language_id', sa.String(), nullable=True))
    op.add_column('submission', sa.Column('passed', sa.Integer(), nullable=True))
    op.add_column('submission', sa.Column('failed', sa.Integer(), nullable=True))
    op.add_column('submission', sa.Column('failed_wrong', sa.Integer(), nullable=True))
    op.add_column('submission', sa.Column('failed_time', sa.Integer(), nullable=True))
    op.add_column('submission', sa.Column('failed_space', sa.Integer(), nullable=True))
    op.add_column('submission', sa.Column('failed_syntax', sa.Integer(), nullable=True))
    op.add_column('submission', sa.Column('failed_other', sa.Integer(), nullable=True))
    op.add_column('submission', sa.Column('weighted_sum', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'submission', 'user', ['user_id'], ['id'])
    op.create_foreign_key(None, 'submission', 'language', ['language_id'], ['id'])
    op.create_foreign_key(None, 'submission', 'problem', ['problem_id'], ['id'])
    op.create_foreign_key(None, 'submission', 'judger', ['judger_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'submission', type_='foreignkey')
    op.drop_constraint(None, 'submission', type_='foreignkey')
    op.drop_constraint(None, 'submission', type_='foreignkey')
    op.drop_constraint(None, 'submission', type_='foreignkey')
    op.drop_column('submission', 'weighted_sum')
    op.drop_column('submission', 'failed_other')
    op.drop_column('submission', 'failed_syntax')
    op.drop_column('submission', 'failed_space')
    op.drop_column('submission', 'failed_time')
    op.drop_column('submission', 'failed_wrong')
    op.drop_column('submission', 'failed')
    op.drop_column('submission', 'passed')
    op.drop_column('submission', 'language_id')
    op.drop_column('submission', 'judger_id')
    op.drop_column('submission', 'code')
    op.drop_column('submission', 'problem_id')
    op.drop_column('submission', 'user_id')
    op.drop_column('submission', 'updated_at')
    op.drop_column('submission', 'created_at')
    # ### end Alembic commands ###
