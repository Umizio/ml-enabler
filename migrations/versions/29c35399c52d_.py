"""empty message

Revision ID: 29c35399c52d
Revises: f4a2a808cf0a
Create Date: 2019-05-21 16:53:18.383888

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2

# revision identifiers, used by Alembic.
revision = '29c35399c52d'
down_revision = 'f4a2a808cf0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('predictions', sa.Column('bbox', geoalchemy2.types.Geometry(geometry_type='POLYGON', srid=4326), nullable=True))
    op.add_column('predictions', sa.Column('version', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('predictions', 'version')
    op.drop_column('predictions', 'bbox')
    # ### end Alembic commands ###
