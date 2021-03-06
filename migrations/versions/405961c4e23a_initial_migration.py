"""Initial migration

Revision ID: 405961c4e23a
Revises: 
Create Date: 2021-06-19 19:00:10.036097

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
import citywok_ms


# revision identifiers, used by Alembic.
revision = "405961c4e23a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "employee",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("zh_name", sa.String(), nullable=True),
        sa.Column("sex", sqlalchemy_utils.types.choice.ChoiceType(), nullable=False),
        sa.Column("birthday", sa.Date(), nullable=True),
        sa.Column("contact", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column(
            "id_type",
            sqlalchemy_utils.types.choice.ChoiceType(length=255),
            nullable=False,
        ),
        sa.Column("id_number", sa.String(), nullable=False),
        sa.Column("id_validity", sa.Date(), nullable=False),
        sa.Column(
            "nationality",
            sqlalchemy_utils.types.country.CountryType(length=2),
            nullable=False,
        ),
        sa.Column("nif", sa.Integer(), nullable=True),
        sa.Column("niss", sa.Integer(), nullable=True),
        sa.Column("employment_date", sa.Date(), nullable=True),
        sa.Column(
            "total_salary", citywok_ms.utils.models.SqliteDecimal(), nullable=True
        ),
        sa.Column(
            "taxed_salary", citywok_ms.utils.models.SqliteDecimal(), nullable=True
        ),
        sa.Column("remark", sa.Text(), nullable=True),
        sa.Column("active", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("nif"),
        sa.UniqueConstraint("niss"),
    )
    op.create_table(
        "supplier",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("abbreviation", sa.String(), nullable=True),
        sa.Column("principal", sa.String(), nullable=True),
        sa.Column("contact", sa.Integer(), nullable=True),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("nif", sa.Integer(), nullable=True),
        sa.Column("iban", sa.String(), nullable=True),
        sa.Column("address", sa.String(), nullable=True),
        sa.Column("postcode", sa.String(), nullable=True),
        sa.Column("city", sa.String(), nullable=True),
        sa.Column("remark", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("iban"),
        sa.UniqueConstraint("nif"),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "role", sqlalchemy_utils.types.choice.ChoiceType(length=255), nullable=False
        ),
        sa.Column("confirmed", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "file",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("full_name", sa.String(), nullable=False),
        sa.Column("upload_date", sa.DateTime(), nullable=False),
        sa.Column("delete_date", sa.DateTime(), nullable=True),
        sa.Column("size", sa.Integer(), nullable=True),
        sa.Column("remark", sa.Text(), nullable=True),
        sa.Column("type", sa.String(), nullable=True),
        sa.Column("employee_id", sa.Integer(), nullable=True),
        sa.Column("supplier_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["employee_id"],
            ["employee.id"],
        ),
        sa.ForeignKeyConstraint(
            ["supplier_id"],
            ["supplier.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("file")
    op.drop_table("user")
    op.drop_table("supplier")
    op.drop_table("employee")
    # ### end Alembic commands ###
