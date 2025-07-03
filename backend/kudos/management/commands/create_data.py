from django.core.management.base import BaseCommand
from kudos.models import User, Organization, Kudos
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        org = Organization.objects.create(name="TestOrg")
        users = [User.objects.create(name=f"User{i}", organization=org) for i in range(5)]

        for _ in range(5):
            from_user = random.choice(users)
            to_user = random.choice([u for u in users if u != from_user])
            msg = random.choice(["Great job!", "Well done!", "Thanks for your help"])
            Kudos.objects.create(from_user=from_user, to_user=to_user, message=msg)
