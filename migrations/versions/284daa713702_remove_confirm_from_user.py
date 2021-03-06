"""Remove confirm from User

Revision ID: 284daa713702
Revises: 405961c4e23a
Create Date: 2021-06-24 17:55:45.618562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '284daa713702'
down_revision = '405961c4e23a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('confirmed')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('confirmed', sa.BOOLEAN(), nullable=False))

    # ### end Alembic commands ###
