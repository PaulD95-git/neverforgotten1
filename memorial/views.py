"""
Views for NeverForgotten application.
Handles memorial creation, management, and all related functionality.
"""

# Django Core
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, reverse
from django.views.generic import CreateView


# Local Apps
from .forms import MemorialForm
from .models import Memorial

# ---------------------------
# Memorial CRUD Views
# ---------------------------


class MemorialCreateView(LoginRequiredMixin, CreateView):
    """View for creating new memorials"""
    model = Memorial
    form_class = MemorialForm
    template_name = 'memorials/memorial_form.html'

    def form_valid(self, form):
        """Assign user and default free plan before saving"""
        form.instance.user = self.request.user

        try:
            free_plan = Plan.objects.get(name='free')
            form.instance.plan = free_plan
        except Plan.DoesNotExist:
            pass

        memorial = form.save()
        return redirect(reverse(
            'plans:choose_plan',
            kwargs={'memorial_id': memorial.pk}
        ))
