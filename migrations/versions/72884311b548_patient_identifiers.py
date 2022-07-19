"""patient_identifiers

Revision ID: 72884311b548
Revises: 00c28d2ab1f9
Create Date: 2020-06-30 14:40:57.436755

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "72884311b548"
down_revision = "00c28d2ab1f9"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        "ix_failed_request_queue_hard_fail", table_name="failed_request_queue"
    )
    op.drop_index(
        "ix_failed_request_queue_last_fail_time_", table_name="failed_request_queue"
    )
    op.drop_table("failed_request_queue")
    op.add_column(
        "hl7_message", sa.Column("patient_identifiers", sa.JSON(), nullable=True)
    )
    op.drop_column("hl7_message", "content_parsed")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "hl7_message",
        sa.Column("content_parsed", sa.VARCHAR(), autoincrement=False, nullable=True),
    )
    op.drop_column("hl7_message", "patient_identifiers")
    op.create_table(
        "failed_request_queue",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            "created_", postgresql.TIMESTAMP(), autoincrement=False, nullable=False
        ),
        sa.Column("api_name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("path_to_module", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column(
            "call_args",
            postgresql.JSON(astext_type=sa.Text()),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column("fail_count", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column(
            "last_fail_time_",
            postgresql.TIMESTAMP(),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "last_fail_reason", sa.VARCHAR(), autoincrement=False, nullable=False
        ),
        sa.Column("hard_fail", sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.Column("succeeded", sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.Column("type", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("identifier", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="failed_request_queue_pkey"),
        sa.UniqueConstraint(
            "type", "identifier", name="failed_request_queue_type_identifier_key"
        ),
    )
    op.create_index(
        "ix_failed_request_queue_last_fail_time_",
        "failed_request_queue",
        ["last_fail_time_"],
        unique=False,
    )
    op.create_index(
        "ix_failed_request_queue_hard_fail",
        "failed_request_queue",
        ["hard_fail"],
        unique=False,
    )
    # ### end Alembic commands ###