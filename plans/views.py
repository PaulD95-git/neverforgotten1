import stripe
from django.conf import settings
from django.shortcuts import (
    render, get_object_or_404, redirect, reverse
)
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .models import Plan
from memorial.models import Memorial
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import logging
from cloudinary.uploader import destroy
from urllib.parse import urlparse
import re
from decouple import config 

logger = logging.getLogger(__name__)

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def choose_plan(request, memorial_id):
    """View for selecting a plan for a memorial."""
    memorial = get_object_or_404(Memorial, pk=memorial_id)
    plans = Plan.objects.filter(is_active=True).order_by('price')
    context = {
        'plans': plans,
        'memorial': memorial,
        'memorial_id': memorial_id,
    }
    return render(request, 'plans/choose_plan.html', context)
