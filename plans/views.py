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


@login_required
def create_checkout_session(request, plan_id, memorial_id):
    """Create Stripe checkout session for selected plan."""
    plan = get_object_or_404(Plan, id=plan_id)
    memorial = get_object_or_404(
        Memorial, id=memorial_id, user=request.user
    )

    if plan.price == 0:
        memorial.plan = plan
        memorial.save()
        return redirect(reverse(
            'memorials:memorial_edit',
            kwargs={'pk': memorial_id}
        ))

    mode = 'payment' if plan.billing_cycle == 'lifetime' else 'subscription'

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': plan.stripe_price_id,
                'quantity': 1,
            }],
            mode=mode,
            success_url=settings.DOMAIN + reverse('plans:payment_success'),
            cancel_url=settings.DOMAIN + reverse('plans:payment_cancel'),
            customer_email=request.user.email,
            metadata={
                'user_id': request.user.id,
                'plan_id': plan.id,
                'memorial_id': memorial.id,
            }
        )
        return redirect(checkout_session.url)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_public_id_from_url(url):
    """Extract public ID from Cloudinary URL."""
    parsed = urlparse(url)
    path = parsed.path
    match = re.search(r'/upload/(?:v\d+/)?(?P<public_id>.+)', path)
    return match.group('public_id') if match else None