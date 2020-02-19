"""empty message

Revision ID: 487b3587c001
Revises: c10a886838a5
Create Date: 2020-02-19 18:32:28.025539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '487b3587c001'
down_revision = 'c10a886838a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_product_list',
    sa.Column('user_product_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_product_list')
    # ### end Alembic commands ###
