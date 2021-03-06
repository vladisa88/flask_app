"""new fields in user db

Revision ID: 836e8ec825c8
Revises: ab66a391f516
Create Date: 2020-02-14 19:47:44.082908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '836e8ec825c8'
down_revision = 'ab66a391f516'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
