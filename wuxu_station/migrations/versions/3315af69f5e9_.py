"""empty message

Revision ID: 3315af69f5e9
Revises: 0bfb3cda6103
Create Date: 2024-06-01 17:50:12.937980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3315af69f5e9'
down_revision = '0bfb3cda6103'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('forum',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('img', sa.String(length=100), nullable=True),
    sa.Column('url', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['tb_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('img', sa.String(length=100), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('speaker_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['forum.id'], ),
    sa.ForeignKeyConstraint(['speaker_id'], ['tb_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('collect',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('author_create', sa.DateTime(), nullable=True),
    sa.Column('img', sa.String(length=100), nullable=True),
    sa.Column('url', sa.String(length=100), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['forum.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['tb_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('collect')
    op.drop_table('answer')
    op.drop_table('forum')
    # ### end Alembic commands ###