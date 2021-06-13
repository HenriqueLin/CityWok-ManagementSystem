from citywok_ms.auth.models import User
import os
from datetime import date

import click
from flask import Blueprint, current_app
from flask.cli import AppGroup

from citywok_ms import db
from citywok_ms.employee.models import Employee
from citywok_ms.file.models import EmployeeFile
from citywok_ms.supplier.models import Supplier
from sqlalchemy.exc import IntegrityError, OperationalError
from werkzeug.security import generate_password_hash

command = Blueprint("command", __name__, cli_group=None)


db_cli = AppGroup("db")


@db_cli.command("create")
def create():
    "Create the database"
    db.create_all()
    click.echo("Created all tables.")

    admin = User(
        username=current_app.config["ADMIN_NAME"],
        email=current_app.config["ADMIN_EMAIL"],
        password=generate_password_hash(current_app.config["ADMIN_PASSWORD"]),
        role="admin",
    )
    db.session.add(admin)
    db.session.commit()
    click.echo("Created admin user.")


@db_cli.command("drop")
@click.confirmation_option(prompt="Are you sure you want to drop the db?")
def drop():
    "Drop the database and remove all user files"
    db.drop_all()
    click.echo("Dropped all tables.")

    path = current_app.config["UPLOAD_FOLDER"]
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        click.echo(f"Deleted {filename}.")
    click.echo("Deleted all files.")


@db_cli.command("load_example")
def load_example():
    """Load example entities to the database"""
    try:
        # first employee
        employee_1 = Employee(
            first_name="Marques",
            last_name="Terrell",
            sex="M",
            id_type="passport",
            id_number="123",
            id_validity=date(2100, 1, 1),
            nationality="US",
            total_salary=1000,
            taxed_salary=635.00,
        )
        db.session.add(employee_1)
        # second employee
        db.session.add(
            Employee(
                first_name="Lia",
                last_name="Daniels",
                zh_name="小红",
                sex="F",
                birthday=date(1999, 1, 1),
                contact="123123123",
                email="123@mail.com",
                id_type="passport",
                id_number="123",
                id_validity=date(2100, 1, 1),
                nationality="US",
                nif=123123,
                niss=321321,
                employment_date=date(2020, 1, 1),
                total_salary="1500",
                taxed_salary="635.00",
                remark="REMARK",
                active=False,
            )
        )
        # supplier
        db.session.add(
            Supplier(
                name="Pingo Doce",
                principal="Peter",
            )
        )
        # employee's file
        file_1 = EmployeeFile(full_name="abc.txt")
        employee_1.files.append(file_1)
        db.session.flush()
        with open(
            os.path.join(current_app.config["UPLOAD_FOLDER"], str(file_1.id) + ".txt"),
            "x",
        ) as file:
            file.write("test_file")
        file_1.size = os.path.getsize(file_1.path)
        db.session.commit()
        click.echo("Loaded example entities.")
    except IntegrityError:
        click.echo("Database already loaded.")
    except OperationalError:
        click.echo("Please create database first.")


command.cli.add_command(db_cli)
