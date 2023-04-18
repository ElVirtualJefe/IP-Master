"""Added description to subnets

Revision ID: fb310a6087d9
Revises: 6380e945d6be
Create Date: 2023-04-12 16:09:48.624791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb310a6087d9'
down_revision = '6380e945d6be'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vlans', 'vlanNumber',
               existing_type=sa.SMALLINT(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vlans', 'vlanNumber',
               existing_type=sa.SMALLINT(),
               nullable=True)
    # ### end Alembic commands ###
