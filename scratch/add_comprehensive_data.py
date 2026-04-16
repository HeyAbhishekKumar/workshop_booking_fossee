import os
import sys
import django
import random
from datetime import timedelta
from django.utils import timezone

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workshop_portal.settings')
django.setup()

from django.contrib.auth.models import User, Group
from workshop_app.models import Workshop, WorkshopType, Profile

def add_comprehensive_dummy_data():
    print("Populating comprehensive dummy data for statistics...")
    
    # Ensure types exist
    types = [
        ("Python for Beginners", 2),
        ("Advanced Django", 5),
        ("Scilab Scientific Computing", 3),
        ("Latex Typesetting", 1),
        ("Linux Administration", 4),
        ("Data Science with R", 6),
    ]
    
    workshop_types = []
    for name, duration in types:
        wt, created = WorkshopType.objects.get_or_create(name=name, defaults={'duration': duration, 'description': f"Course on {name}", 'terms_and_conditions': "Standard T&C"})
        workshop_types.append(wt)
        if created:
            print(f"Created WorkshopType: {name}")

    # Ensure users and profiles exist
    instructors = User.objects.filter(groups__name='instructor')
    coordinators = User.objects.filter(groups__name='coordinator')
    
    if not instructors.exists() or not coordinators.exists():
        print("Creating default users...")
        # Create groups if they don't exist
        instructor_group, _ = Group.objects.get_or_create(name='instructor')
        coordinator_group, _ = Group.objects.get_or_create(name='coordinator')
        
        # Create Instructor
        i_user, _ = User.objects.get_or_create(username='instructor', defaults={'first_name': 'Ina', 'last_name': 'Instructor'})
        i_user.set_password('fossee123')
        i_user.save()
        i_user.groups.add(instructor_group)
        Profile.objects.get_or_create(user=i_user, defaults={'position': 'instructor', 'institute': 'IIT Bombay', 'phone_number': '9999999999', 'location': 'Mumbai'})

        # Create Coordinator
        c_user, _ = User.objects.get_or_create(username='coordinator', defaults={'first_name': 'Cory', 'last_name': 'Coordinator'})
        c_user.set_password('fossee123')
        c_user.save()
        c_user.groups.add(coordinator_group)
        Profile.objects.get_or_create(user=c_user, defaults={'position': 'coordinator', 'institute': 'VJTI Mumbai', 'phone_number': '8888888888', 'location': 'Mumbai'})

        instructors = User.objects.filter(groups__name='instructor')
        coordinators = User.objects.filter(groups__name='coordinator')

    # States for distribution
    states = ["Maharashtra", "Karnataka", "Tamil Nadu", "Gujarat", "Delhi", "Kerala", "West Bengal", "Punjab", "Rajasthan", "Telangana"]
    
    # Create 40 random workshops spread across time and states
    count = 0
    now = timezone.now()
    
    for i in range(40):
        # Random date in last 3 months to next 3 months
        random_days = random.randint(-90, 90)
        workshop_date = (now + timedelta(days=random_days)).date()
        
        # Random state/location
        state = random.choice(states)
        
        # Select random users
        coordinator = random.choice(coordinators)
        instructor = random.choice(instructors)
        w_type = random.choice(workshop_types)
        
        # We need a way to track the state. 
        # In this app, it seems 'location' or the coordinator's state is used.
        # Let's update the coordinator's profile state to the random state chosen for this record simulation
        # Note: In a real app, many coordinators would be from different states.
        # To show a good map, we'll create several coordinators or update existing one's profile location temporarily?
        # Better: create a few dummy coordinators from different states.
        
        temp_c_username = f"coord_{state.lower().replace(' ', '_')}"
        temp_c, _ = User.objects.get_or_create(username=temp_c_username, defaults={'first_name': 'Coord', 'last_name': state})
        temp_c.groups.add(Group.objects.get(name='coordinator'))
        profile, _ = Profile.objects.get_or_create(user=temp_c)
        profile.institute = f"Institute in {state}"
        profile.location = state
        profile.state = state
        profile.save()

        Workshop.objects.create(
            workshop_type=w_type,
            date=workshop_date,
            instructor=instructor,
            coordinator=temp_c,
            status=True,
            tnc_accepted=True
        )
        count += 1

    print(f"Successfully added {count} workshops spanning across {len(states)} states.")

if __name__ == "__main__":
    add_comprehensive_dummy_data()
