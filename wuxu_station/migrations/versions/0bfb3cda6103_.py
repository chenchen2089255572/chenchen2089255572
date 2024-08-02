"""empty message

Revision ID: 0bfb3cda6103
Revises: b3c9820ec342
Create Date: 2024-05-25 22:43:09.829182

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0bfb3cda6103'
down_revision = 'b3c9820ec342'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test_score', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_name', sa.String(length=20), nullable=True))
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test_score', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_column('user_name')

    # ### end Alembic commands ###