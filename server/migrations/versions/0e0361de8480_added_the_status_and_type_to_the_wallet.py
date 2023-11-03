"""added the status and type to the wallet

Revision ID: 0e0361de8480
Revises: bef15edefe3e
Create Date: 2023-11-01 02:12:44.650291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e0361de8480'
down_revision = 'bef15edefe3e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wallets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('type', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('status', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wallets', schema=None) as batch_op:
        batch_op.drop_column('status')
        batch_op.drop_column('type')

    # ### end Alembic commands ###