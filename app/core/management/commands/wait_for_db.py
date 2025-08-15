"""
Command to wait for the database to be available before starting the server.
"""
import time

from psycopg2 import OperationalError as psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait fotr database."""

    def handle(self, *args, **options):
        """Entry point for command"""
        self.stdout.write("Waiting for database...")
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (psycopg2OpError, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
