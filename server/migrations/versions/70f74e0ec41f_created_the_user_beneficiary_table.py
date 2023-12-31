"""created  the USER_beneficiary table

Revision ID: 70f74e0ec41f
Revises: 1e269b8c6291
Create Date: 2023-11-01 13:09:03.565247

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70f74e0ec41f'
down_revision = '1e269b8c6291'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_beneficiaries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_beneficiaries')
    # ### end Alembic commands ###
