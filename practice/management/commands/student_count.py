from django.core.management.base import BaseCommand, CommandParser

from ...models import Student


class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("-c", "--name", type=str)

    def handle(self, *args, **options):
        count = Student.objects.count()
        print(f"total students: {count}")
        particular_name = options["name"]
        particular_name_count = Student.objects.filter(name=particular_name).count()
        print(f"partulcar name students: {particular_name_count}")
