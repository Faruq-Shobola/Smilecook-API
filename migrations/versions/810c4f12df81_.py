"""empty message

Revision ID: 810c4f12df81
Revises: e46f15c9d812
Create Date: 2023-04-30 19:36:21.200010

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '810c4f12df81'
down_revision = 'e46f15c9d812'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ingredients', sa.String(length=1000), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.drop_column('ingredients')

    # ### end Alembic commands ###