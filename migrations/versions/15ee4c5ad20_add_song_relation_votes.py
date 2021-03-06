"""add song_relation_votes

Revision ID: 15ee4c5ad20
Revises: 47591e8eb26
Create Date: 2016-12-09 18:51:36.246568

"""

# revision identifiers, used by Alembic.
revision = '15ee4c5ad20'
down_revision = '47591e8eb26'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('song_relation_votes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('song_relation_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['song_relation_id'], ['song_relations.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('song_relations', sa.Column('created', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('created', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'created')
    op.drop_column('song_relations', 'created')
    op.drop_table('song_relation_votes')
    ### end Alembic commands ###
