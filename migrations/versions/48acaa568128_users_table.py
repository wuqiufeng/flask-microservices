"""users table

Revision ID: 48acaa568128
Revises: 
Create Date: 2019-02-26 14:12:03.947785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48acaa568128'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'user_auths', 'users', ['user_id'], ['id'])
    op.add_column('users', sa.Column('avatar_url', sa.String(length=128), nullable=True))
    op.add_column('users', sa.Column('name', sa.String(length=32), nullable=True))
    op.add_column('users', sa.Column('phone', sa.String(length=11), nullable=True))
    op.add_column('users', sa.Column('uuid', sa.String(length=255), nullable=True))
    op.create_unique_constraint(None, 'users', ['uuid'])
    op.create_unique_constraint(None, 'users', ['phone'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'uuid')
    op.drop_column('users', 'phone')
    op.drop_column('users', 'name')
    op.drop_column('users', 'avatar_url')
    op.drop_constraint(None, 'user_auths', type_='foreignkey')
    # ### end Alembic commands ###