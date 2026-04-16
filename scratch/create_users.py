import os
import sys
import django
from django.utils import timezone

# Add current directory to path
sys.path.append(os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workshop_portal.settings')
django.setup()

from django.contrib.auth.models import User, Group
from workshop_app.models import Profile

def create_user(username, position, is_instructor=False):
    user, created = User.objects.get_or_create(username=username)
    user.email = f"{username}@example.com"
    user.set_password("fossee123")
    user.first_name = username.capitalize()
    user.save()
    
    profile, created = Profile.objects.get_or_create(user=user)
    profile.position = position
    profile.is_email_verified = True
    profile.institute = "FOSSEE IITB"
    profile.phone_number = "9999999999"
    profile.save()
    
    if is_instructor:
        group, _ = Group.objects.get_or_create(name='instructor')
        user.groups.add(group)
    
    print(f"User {username} ({position}) created/updated.")

if __name__ == "__main__":
    create_user("instructor", "instructor", is_instructor=True)
    create_user("coordinator", "coordinator")
    print("\nLogin Credentials:")
    print("Instructor:  instructor / fossee123")
    print("Coordinator: coordinator / fossee123")
