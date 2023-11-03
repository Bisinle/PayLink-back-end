"""deropped the balance col in wallet

Revision ID: 895075832bb7
Revises: 9acc0de97545
Create Date: 2023-11-01 20:11:30.229691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '895075832bb7'
down_revision = '9acc0de97545'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wallets', schema=None) as batch_op:
        batch_op.drop_column('balance')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wallets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('balance', sa.FLOAT(), nullable=True))

    # ### end Alembic commands ###