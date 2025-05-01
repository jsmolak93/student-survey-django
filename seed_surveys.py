import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "student_survey_django.settings")
django.setup()

from surveys.models import Survey

# Optional: Clear existing data
Survey.objects.all().delete()

# Sample survey entries
sample_data = [
    {
        "first_name": "Alice",
        "last_name": "Johnson",
        "street": "123 Maple St",
        "city": "Fairfax",
        "state": "VA",
        "zip": "22030",
        "telephone": "123-456-7890",
        "email": "alice@example.com",
        "survey_date": date(2024, 10, 1),
        "liked_most": "Hands-on assignments",
        "interest_source": "Friend",
        "recommend_likelihood": "Very Likely"
    },
    {
        "first_name": "Bob",
        "last_name": "Smith",
        "street": "456 Oak Ave",
        "city": "Arlington",
        "state": "VA",
        "zip": "22201",
        "telephone": "987-654-3210",
        "email": "bob@example.com",
        "survey_date": date(2024, 10, 2),
        "liked_most": "Instructor feedback",
        "interest_source": "Online Ad",
        "recommend_likelihood": "Likely"
    },
    {
        "first_name": "Charlie",
        "last_name": "Lee",
        "street": "789 Pine Rd",
        "city": "Alexandria",
        "state": "VA",
        "zip": "22301",
        "telephone": "555-123-4567",
        "email": "charlie@example.com",
        "survey_date": date(2024, 10, 3),
        "liked_most": "Course structure",
        "interest_source": "Professor",
        "recommend_likelihood": "Extremely Likely"
    },
]

# Insert into DB
for entry in sample_data:
    Survey.objects.create(**entry)

print("Surveys successfully seeded into RDS!")
