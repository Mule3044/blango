from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import timedelta

from django.conf import settings
from django.utils import timezone

from blango_auth.models import User

# User.objects.filter(
#     is_active=False,
#     date_joined__lt=timezone.now() - timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
# ).delete()

# Create your views here.
@login_required
def profile(request):
    return render(request, "blango_auth/profile.html")