"""empty message

Revision ID: 059ba63d4cb5
Revises: 158115263cb5
Create Date: 2018-10-01 22:25:47.589951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '059ba63d4cb5'
down_revision = '158115263cb5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('nfl_boxscore_receiving', sa.Column('lg_td', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('nfl_boxscore_receiving', 'lg_td')
    # ### end Alembic commands ###
