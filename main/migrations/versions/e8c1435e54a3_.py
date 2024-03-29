"""empty message

Revision ID: e8c1435e54a3
Revises: 479f085838c1
Create Date: 2024-02-08 06:46:58.469348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8c1435e54a3'
down_revision = '479f085838c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'product_user', ['user_id', 'product_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product_user', type_='unique')
    # ### end Alembic commands ###
