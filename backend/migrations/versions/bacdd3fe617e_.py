"""empty message

Revision ID: bacdd3fe617e
Revises: d0e1c48ca415
Create Date: 2022-07-08 17:21:51.590929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bacdd3fe617e'
down_revision = 'd0e1c48ca415'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_pw', sa.String(), nullable=True),
    sa.Column('user_name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('events', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'events', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'events', type_='foreignkey')
    op.drop_column('events', 'user_id')
    op.drop_table('users')
    # ### end Alembic commands ###
