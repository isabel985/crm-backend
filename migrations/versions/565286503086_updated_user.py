"""updated user

Revision ID: 565286503086
Revises: 26169d106cc0
Create Date: 2020-07-29 00:34:20.115130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '565286503086'
down_revision = '26169d106cc0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'user', ['user_email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    # ### end Alembic commands ###
