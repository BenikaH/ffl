"""empty message

Revision ID: c1162743df1d
Revises: 39af87230883
Create Date: 2018-10-31 18:59:48.965035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1162743df1d'
down_revision = '39af87230883'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('field_player', sa.Column('name', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('field_player', 'name')
    # ### end Alembic commands ###
