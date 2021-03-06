"""empty message

Revision ID: 1159a970b737
Revises: 2a8ecdf28f51
Create Date: 2018-10-01 21:22:18.936033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1159a970b737'
down_revision = '2a8ecdf28f51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('nfl_boxscore_defense_game_id_fkey', 'nfl_boxscore_defense', type_='foreignkey')
    op.create_foreign_key(None, 'nfl_boxscore_defense', 'nfl_boxscore_game', ['game_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('nfl_boxscore_fumbles_game_id_fkey', 'nfl_boxscore_fumbles', type_='foreignkey')
    op.create_foreign_key(None, 'nfl_boxscore_fumbles', 'nfl_boxscore_game', ['game_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('nfl_boxscore_kicking_game_id_fkey', 'nfl_boxscore_kicking', type_='foreignkey')
    op.create_foreign_key(None, 'nfl_boxscore_kicking', 'nfl_boxscore_game', ['game_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('nfl_boxscore_kickoff_returns_game_id_fkey', 'nfl_boxscore_kickoff_returns', type_='foreignkey')
    op.create_foreign_key(None, 'nfl_boxscore_kickoff_returns', 'nfl_boxscore_game', ['game_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('nfl_boxscore_passing_game_id_fkey', 'nfl_boxscore_passing', type_='foreignkey')
    op.create_foreign_key(None, 'nfl_boxscore_passing', 'nfl_boxscore_game', ['game_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('nfl_boxscore_punting_game_id_fkey', 'nfl_boxscore_punting', type_='foreignkey')
    op.create_foreign_key(None, 'nfl_boxscore_punting', 'nfl_boxscore_game', ['game_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('nfl_boxscore_receiving_game_id_fkey', 'nfl_boxscore_receiving', type_='foreignkey')
    op.create_foreign_key(None, 'nfl_boxscore_receiving', 'nfl_boxscore_game', ['game_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('nfl_boxscore_rushing_game_id_fkey', 'nfl_boxscore_rushing', type_='foreignkey')
    op.create_foreign_key(None, 'nfl_boxscore_rushing', 'nfl_boxscore_game', ['game_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('nfl_punt_returns_game_id_fkey', 'nfl_punt_returns', type_='foreignkey')
    op.create_foreign_key(None, 'nfl_punt_returns', 'nfl_boxscore_game', ['game_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'nfl_punt_returns', type_='foreignkey')
    op.create_foreign_key('nfl_punt_returns_game_id_fkey', 'nfl_punt_returns', 'nfl_boxscore_game', ['game_id'], ['id'])
    op.drop_constraint(None, 'nfl_boxscore_rushing', type_='foreignkey')
    op.create_foreign_key('nfl_boxscore_rushing_game_id_fkey', 'nfl_boxscore_rushing', 'nfl_boxscore_game', ['game_id'], ['id'])
    op.drop_constraint(None, 'nfl_boxscore_receiving', type_='foreignkey')
    op.create_foreign_key('nfl_boxscore_receiving_game_id_fkey', 'nfl_boxscore_receiving', 'nfl_boxscore_game', ['game_id'], ['id'])
    op.drop_constraint(None, 'nfl_boxscore_punting', type_='foreignkey')
    op.create_foreign_key('nfl_boxscore_punting_game_id_fkey', 'nfl_boxscore_punting', 'nfl_boxscore_game', ['game_id'], ['id'])
    op.drop_constraint(None, 'nfl_boxscore_passing', type_='foreignkey')
    op.create_foreign_key('nfl_boxscore_passing_game_id_fkey', 'nfl_boxscore_passing', 'nfl_boxscore_game', ['game_id'], ['id'])
    op.drop_constraint(None, 'nfl_boxscore_kickoff_returns', type_='foreignkey')
    op.create_foreign_key('nfl_boxscore_kickoff_returns_game_id_fkey', 'nfl_boxscore_kickoff_returns', 'nfl_boxscore_game', ['game_id'], ['id'])
    op.drop_constraint(None, 'nfl_boxscore_kicking', type_='foreignkey')
    op.create_foreign_key('nfl_boxscore_kicking_game_id_fkey', 'nfl_boxscore_kicking', 'nfl_boxscore_game', ['game_id'], ['id'])
    op.drop_constraint(None, 'nfl_boxscore_fumbles', type_='foreignkey')
    op.create_foreign_key('nfl_boxscore_fumbles_game_id_fkey', 'nfl_boxscore_fumbles', 'nfl_boxscore_game', ['game_id'], ['id'])
    op.drop_constraint(None, 'nfl_boxscore_defense', type_='foreignkey')
    op.create_foreign_key('nfl_boxscore_defense_game_id_fkey', 'nfl_boxscore_defense', 'nfl_boxscore_game', ['game_id'], ['id'])
    # ### end Alembic commands ###
