"""Initial db

Revision ID: b681b702bc92
Revises:
Create Date: 2024-09-18 16:29:17.420940

"""

import sqlalchemy as sa
from alembic import op

revision = "b681b702bc92"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """Create tables user, appointment, general_information"""
    op.create_table(
        "user",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("idnp", sa.String(length=50), nullable=False),
        sa.Column("email", sa.String(length=50), nullable=False),
        sa.Column("hashed_password", sa.String(length=255), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("surname", sa.String(length=50), nullable=False),
        sa.Column("location", sa.String(length=255), nullable=False),
        sa.Column("phone", sa.Integer(), nullable=True),
        sa.Column("image_uri", sa.String(length=255), nullable=True),
        sa.Column("role", sa.String(length=25), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("is_verified", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "appointment",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column("doctor_user_id", sa.UUID(), nullable=True),
        sa.Column("start_time", sa.DateTime(), nullable=True),
        sa.Column("end_time", sa.DateTime(), nullable=True),
        sa.Column("comments", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["doctor_user_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "general_information",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=True),
        sa.Column("height", sa.Integer(), nullable=True),
        sa.Column("weight", sa.Integer(), nullable=True),
        sa.Column("blood_type", sa.String(), nullable=True),
        sa.Column("gender", sa.String(), nullable=True),
        sa.Column("date_of_birth", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    """Drop tables user, appointment, general_information"""
    op.drop_table("general_information")
    op.drop_table("appointment")
    op.drop_table("user")
