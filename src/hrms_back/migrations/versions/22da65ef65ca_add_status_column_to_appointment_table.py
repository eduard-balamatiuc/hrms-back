"""Add status column to appointment table

Revision ID: 22da65ef65ca
Revises: e4f1a07ed6c7
Create Date: 2024-10-03 12:50:23.236874

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "22da65ef65ca"
down_revision = "e4f1a07ed6c7"
branch_labels = None
depends_on = None


def upgrade():
    """Add the 'status' column to the 'appointment' table"""
    op.add_column("appointment", sa.Column("status", sa.String(), nullable=False))


def downgrade():
    """Remove the 'status' column if the migration is downgraded"""
    op.drop_column("appointment", "status")
