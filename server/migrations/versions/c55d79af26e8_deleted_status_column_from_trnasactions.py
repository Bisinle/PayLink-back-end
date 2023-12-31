"""deleted status column from trnasactions

Revision ID: c55d79af26e8
Revises: 40fd49c047cd
Create Date: 2023-10-30 13:55:07.515158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c55d79af26e8'
down_revision = '40fd49c047cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions', schema=None) as batch_op:
        batch_op.drop_column('status')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###
