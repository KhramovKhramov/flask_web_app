"""added email to user

Revision ID: 94696c2ea742
Revises: 42dd3b6257d8
Create Date: 2022-08-20 22:33:38.489433

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94696c2ea742'
down_revision = '42dd3b6257d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    # ### end Alembic commands ###