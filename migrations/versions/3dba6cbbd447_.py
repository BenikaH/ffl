"""empty message

Revision ID: 3dba6cbbd447
Revises: 729a6131b19f
Create Date: 2018-10-30 18:28:31.148084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3dba6cbbd447'
down_revision = '729a6131b19f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('field_team', sa.Column('shark_code', sa.String(length=8), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('field_team', 'shark_code')
    # ### end Alembic commands ###
