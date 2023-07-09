import csv
import time
from datetime import datetime
from django.core.management.base import BaseCommand
from trading.models import Trading

class Command(BaseCommand):
    help = 'Inserts CSV data into the database'

    def handle(self, *args, **options):
        file_path = 'static\csv\coin_Bitcoin.csv'  # Replace with the actual path to your CSV file
        start_row = 100
        end_row = 500

        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)

            # Skip to the starting row
            for _ in range(start_row - 1):
                next(reader)

            # Insert data row by row
            for row_number, row in enumerate(reader, start=start_row):
                # Break if we exceed the end row
                if row_number > end_row:
                    break

                # Convert date format
                csv_date = row[3]  # Assuming 'Date' is at index 3 in the CSV
                date_object = datetime.strptime(csv_date, '%Y-%m-%d %H:%M:%S')
                formatted_date = date_object.strftime('%Y-%m-%d')

                # Assuming the CSV columns match the model fields, create a new instance of the model
                data = {
                    'Date': formatted_date,  # Convert date format
                    'High':float(row[4]),
                    'Low':float(row[5]),
                    'Open': float(row[6]),  # Assuming 'Open' is at index 6 in the CSV
                    'Close': float(row[7]),  # Assuming 'Close' is at index 7 in the CSV
                    'Volume': float(row[8]),  # Assuming 'Volume' is at index 8 in the CSV
                    'Marketcap': float(row[9]),  # Assuming 'Marketcap' is at index 9 in the CSV
                    
                }
                instance = Trading(**data)

                # Save the instance to the database
                instance.save()

                time.sleep(1)

                # Optionally, print the inserted row for debugging
                print(f"Inserted row {row_number}: {data}")
            self.stdout.write(self.style.SUCCESS('All data inserted successfully.'))
