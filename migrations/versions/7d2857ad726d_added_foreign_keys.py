"""added foreign keys

Revision ID: 7d2857ad726d
Revises: 7e9c0b02c377
Create Date: 2020-07-30 22:24:22.747234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d2857ad726d'
down_revision = '7e9c0b02c377'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('company', sa.Column('name_id', sa.Integer(), nullable=True))
    op.add_column('company', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'company', 'user', ['user_id'], ['user_id'])
    op.create_foreign_key(None, 'company', 'name', ['name_id'], ['name_id'])
    op.add_column('name', sa.Column('company_id', sa.Integer(), nullable=True))
    op.add_column('name', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'name', 'company', ['company_id'], ['company_id'])
    op.create_foreign_key(None, 'name', 'user', ['user_id'], ['user_id'])
    op.add_column('user', sa.Column('team_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'team', ['team_id'], ['team_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'team_id')
    op.drop_constraint(None, 'name', type_='foreignkey')
    op.drop_constraint(None, 'name', type_='foreignkey')
    op.drop_column('name', 'user_id')
    op.drop_column('name', 'company_id')
    op.drop_constraint(None, 'company', type_='foreignkey')
    op.drop_constraint(None, 'company', type_='foreignkey')
    op.drop_column('company', 'user_id')
    op.drop_column('company', 'name_id')
    # ### end Alembic commands ###