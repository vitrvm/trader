from django.core.management.base import BaseCommand, CommandError, CommandParser

class Command(BaseCommand):
    help = "Start IG Streamer"

    def add_arguments(self, parser: CommandParser) -> None:
        return super().add_arguments(parser)

    def handle(self, *args, **options):
        print(f"Hello wworld")
        