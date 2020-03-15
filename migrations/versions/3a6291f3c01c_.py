"""empty message

Revision ID: 3a6291f3c01c
Revises: 26792a2cfa51
Create Date: 2020-03-14 20:03:53.153479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a6291f3c01c'
down_revision = '26792a2cfa51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('pro_pic', sa.String(length=300), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'pro_pic')
    # ### end Alembic commands ###