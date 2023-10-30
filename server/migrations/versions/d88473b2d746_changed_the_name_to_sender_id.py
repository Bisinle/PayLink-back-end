"""changed the name to sender_id

Revision ID: d88473b2d746
Revises: 2f5d57bcccc3
Create Date: 2023-10-27 18:48:00.758982

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd88473b2d746'
down_revision = '2f5d57bcccc3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_beneficiaries', schema=None) as batch_op:
        batch_op.drop_constraint('fk_user_beneficiaries_user_profile_id_users_profile', type_='foreignkey')
        batch_op.drop_column('user_profile_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_beneficiaries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_profile_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_user_beneficiaries_user_profile_id_users_profile', 'users_profile', ['user_profile_id'], ['id'])

    # ### end Alembic commands ###