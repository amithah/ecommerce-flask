"""empty message

Revision ID: 356c6e4f3f47
Revises: 
Create Date: 2020-06-08 11:13:42.042063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '356c6e4f3f47'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brand',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('slug', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('slug', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('slug', sa.String(length=64), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('addproduct',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('discount', sa.Integer(), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('colors', sa.Text(), nullable=False),
    sa.Column('desc', sa.Text(), nullable=False),
    sa.Column('pub_date', sa.DateTime(), nullable=False),
    sa.Column('slug', sa.String(length=64), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('brand_id', sa.Integer(), nullable=False),
    sa.Column('image_1', sa.String(length=150), nullable=False),
    sa.Column('filename_1', sa.String(length=80), nullable=True),
    sa.Column('image_2', sa.String(length=150), nullable=False),
    sa.Column('filename_2', sa.String(length=80), nullable=True),
    sa.Column('image_3', sa.String(length=150), nullable=False),
    sa.Column('filename_3', sa.String(length=80), nullable=True),
    sa.ForeignKeyConstraint(['brand_id'], ['brand.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('addproduct')
    op.drop_table('user')
    op.drop_table('category')
    op.drop_table('brand')
    # ### end Alembic commands ###
