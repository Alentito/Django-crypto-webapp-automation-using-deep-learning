from django.core.management.base import BaseCommand
from trading.models import Trading

class Command(BaseCommand):
    help = 'Deletes all data from the database table'

    def handle(self, *args, **options):
        Trading.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All data deleted successfully.'))
