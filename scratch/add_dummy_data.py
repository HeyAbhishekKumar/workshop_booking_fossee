import os
import sys
import django
from django.utils import timezone
import datetime

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workshop_portal.settings')
django.setup()

from django.contrib.auth.models import User
from workshop_app.models import WorkshopType, Workshop

def add_dummy_data():
    coordinator = User.objects.filter(username='coordinator').first()
    instructor = User.objects.filter(username='instructor').first()

    if not coordinator or not instructor:
        print("Please ensure 'coordinator' and 'instructor' users exist first.")
        return

    # Create Workshop Types
    wt1, _ = WorkshopType.objects.get_or_create(
        name='Python for Beginners',
        defaults={
            'description': 'Introduction to Python programming.',
            'duration': 2,
            'terms_and_conditions': 'Must attend all sessions.'
        }
    )
    
    wt2, _ = WorkshopType.objects.get_or_create(
        name='Advanced Django',
        defaults={
            'description': 'Deep dive into Django framework.',
            'duration': 5,
            'terms_and_conditions': 'Requires basic Python knowledge.'
        }
    )

    # Create some proposed workshops (Pending status=0)
    w1, created1 = Workshop.objects.get_or_create(
        coordinator=coordinator,
        workshop_type=wt1,
        date=timezone.now().date() + datetime.timedelta(days=10),
        defaults={
            'status': 0,
            'tnc_accepted': True
        }
    )
    
    # Create some accepted workshops (Accepted status=1) with instructor assigned
    w2, created2 = Workshop.objects.get_or_create(
        coordinator=coordinator,
        workshop_type=wt2,
        date=timezone.now().date() + datetime.timedelta(days=20),
        defaults={
            'status': 1,
            'instructor': instructor,
            'tnc_accepted': True
        }
    )

    print("Dummy data added successfully!")
    print(f"- WorkshopType 1: {wt1.name}")
    print(f"- WorkshopType 2: {wt2.name}")
    print(f"- Workshop 1 (Pending): {w1.workshop_type.name} on {w1.date}")
    print(f"- Workshop 2 (Accepted): {w2.workshop_type.name} on {w2.date} by {instructor.username}")

if __name__ == '__main__':
    add_dummy_data()
