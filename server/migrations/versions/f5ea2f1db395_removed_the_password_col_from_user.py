"""removed the  password col from user

Revision ID: f5ea2f1db395
Revises: 8c79feac9462
Create Date: 2023-11-03 11:31:47.524930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5ea2f1db395'
down_revision = '8c79feac9462'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('_password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('_password', sa.VARCHAR(), nullable=True))

    # ### end Alembic commands ###
