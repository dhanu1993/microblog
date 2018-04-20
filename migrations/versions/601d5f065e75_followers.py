"""followers

Revision ID: 601d5f065e75
Revises: d2ff4f91f93f
Create Date: 2018-04-13 14:36:29.070732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '601d5f065e75'
down_revision = 'd2ff4f91f93f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
