"""empty message

Revision ID: 4003bbed2df5
Revises: 2bc6209d8d2b
Create Date: 2020-02-19 19:13:04.735142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4003bbed2df5'
down_revision = '2bc6209d8d2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('cid', sa.Integer(), nullable=False),
    sa.Column('c_first_name', sa.String(), nullable=True),
    sa.Column('c_last_name', sa.String(), nullable=True),
    sa.Column('c_gender', sa.String(), nullable=True),
    sa.Column('c_email', sa.String(), nullable=True),
    sa.Column('c_age', sa.Integer(), nullable=True),
    sa.Column('c_address', sa.String(), nullable=True),
    sa.Column('c_state', sa.String(), nullable=True),
    sa.Column('c_zipcode', sa.Integer(), nullable=True),
    sa.Column('c_phonenumber', sa.String(), nullable=True),
    sa.Column('c_registrationdate', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('cid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customer')
    # ### end Alembic commands ###