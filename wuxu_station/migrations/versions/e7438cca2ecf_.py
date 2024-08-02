"""empty message

Revision ID: e7438cca2ecf
Revises: 507fb05793ab
Create Date: 2024-05-19 13:50:55.138546

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e7438cca2ecf'
down_revision = '507fb05793ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tb_user', schema=None) as batch_op:
        batch_op.drop_index('email')
        batch_op.drop_column('join_time')
        batch_op.drop_column('email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tb_user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', mysql.VARCHAR(length=100), nullable=False))
        batch_op.add_column(sa.Column('join_time', mysql.DATETIME(), nullable=True))
        batch_op.create_index('email', ['email'], unique=True)

    # ### end Alembic commands ###
