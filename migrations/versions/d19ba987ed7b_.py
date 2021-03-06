"""empty message

Revision ID: d19ba987ed7b
Revises: 4a2103e8312a
Create Date: 2020-02-19 19:21:20.322361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd19ba987ed7b'
down_revision = '4a2103e8312a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('pid', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(), nullable=True),
    sa.Column('product_brand', sa.String(), nullable=True),
    sa.Column('product_description', sa.String(), nullable=True),
    sa.Column('product_color', sa.String(), nullable=True),
    sa.Column('product_unitprice', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('pid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###
