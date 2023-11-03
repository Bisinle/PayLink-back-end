"""added  the balance col and changed it's data type to float in wallet

Revision ID: 7b4f0a960edd
Revises: 1c221f941303
Create Date: 2023-11-01 20:32:11.098230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b4f0a960edd'
down_revision = '1c221f941303'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wallets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('balance', sa.Numeric(precision=10, scale=2), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('wallets', schema=None) as batch_op:
        batch_op.drop_column('balance')

    # ### end Alembic commands ###