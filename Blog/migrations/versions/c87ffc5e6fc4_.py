"""empty message

Revision ID: c87ffc5e6fc4
Revises: 08e39a7c0528
Create Date: 2021-09-17 21:11:23.611487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c87ffc5e6fc4'
down_revision = '08e39a7c0528'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_icon', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'user_icon')
    # ### end Alembic commands ###