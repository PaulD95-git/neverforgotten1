"""
Views for NeverForgotten application.
Handles memorial creation, management, and all related functionality.
"""

# Django Core
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, reverse
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse


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


class MemorialEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """View for editing existing memorials"""
    model = Memorial
    form_class = MemorialForm
    template_name = 'memorials/memorial_edit.html'

    def get_success_url(self):
        """Redirect to memorial detail after edit"""
        return reverse_lazy(
            'memorials:memorial_detail',
            kwargs={'pk': self.object.pk}
        )

    def test_func(self):
        """Ensure only memorial owner can edit"""
        return self.request.user == self.get_object().user

    def get_context_data(self, **kwargs):
        """Add update URLs to context"""
        context = super().get_context_data(**kwargs)
        context['update_name_url'] = reverse_lazy(
            'memorials:update_name',
            kwargs={'pk': self.object.pk}
        )
        context['update_dates_url'] = reverse_lazy(
            'memorials:update_dates',
            kwargs={'pk': self.object.pk}
        )
        return context


# ---------------------------
# Memorial Content Views
# ---------------------------

@csrf_protect
def memorial_detail(request, pk):
    """Detailed view of a memorial with tributes and stories"""
    memorial = get_object_or_404(Memorial, pk=pk)
    memorial.refresh_from_db()

    tributes = memorial.tributes.all().order_by('-created_at')[:6]
    stories = memorial.stories.all().order_by('-created_at')[:3]

    plan_name = memorial.plan.name.lower() if memorial.plan else ""
    is_premium_plan = plan_name in ['premium', 'lifetime']
    is_premium = (
        request.user.is_authenticated and
        request.user == memorial.user and
        is_premium_plan
    )

    if (request.method == 'POST' and
            request.headers.get('x-requested-with') == 'XMLHttpRequest'):
        if 'story_content' in request.POST:
            return create_story(request, pk)
        return create_tribute(request, pk)

    return render(
        request,
        'memorials/memorial_detail.html',
        {
            'memorial': memorial,
            'tributes': tributes,
            'stories': stories,
            'is_premium': is_premium,
            'request': request,
        }
    )


# ---------------------------
# AJAX Update Views
# ---------------------------

@require_POST
def update_name(request, pk):
    """AJAX endpoint for updating memorial name"""
    try:
        memorial = Memorial.objects.get(pk=pk)
        memorial.first_name = request.POST.get('first_name', '')
        memorial.middle_name = request.POST.get('middle_name', '')
        memorial.last_name = request.POST.get('last_name', '')
        memorial.save()

        full_name = (
            f"{memorial.first_name} "
            f"{memorial.middle_name + ' ' if memorial.middle_name else ''}"
            f"{memorial.last_name}"
        )

        return JsonResponse({
            'status': 'success',
            'new_name': full_name.strip()
        })
    except Memorial.DoesNotExist:
        return JsonResponse(
            {'status': 'error', 'message': 'Memorial not found'},
            status=404
        )
    except Exception as e:
        return JsonResponse(
            {'status': 'error', 'message': str(e)},
            status=400
        )


@require_POST
def update_dates(request, pk):
    """AJAX endpoint for updating memorial dates"""
    try:
        memorial = Memorial.objects.get(pk=pk)

        date_of_birth_str = request.POST.get('date_of_birth')
        date_of_death_str = request.POST.get('date_of_death')

        try:
            date_of_birth = datetime.strptime(
                date_of_birth_str,
                '%Y-%m-%d'
            ).date()
            date_of_death = datetime.strptime(
                date_of_death_str,
                '%Y-%m-%d'
            ).date()
        except (ValueError, TypeError):
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid date format. Use YYYY-MM-DD.'
            }, status=400)

        memorial.date_of_birth = date_of_birth
        memorial.date_of_death = date_of_death
        memorial.save()

        return JsonResponse({
            'status': 'success',
            'new_dates': (
                f"{date_of_birth.strftime('%B %d, %Y')} - "
                f"{date_of_death.strftime('%B %d, %Y')}"
            )
        })
    except Memorial.DoesNotExist:
        return JsonResponse(
            {'status': 'error', 'message': 'Memorial not found'},
            status=404
        )
    except Exception as e:
        return JsonResponse(
            {'status': 'error', 'message': str(e)},
            status=400
        )


@require_POST
@login_required
def update_quote(request, pk):
    """AJAX endpoint for updating memorial quote"""
    memorial = get_object_or_404(Memorial, pk=pk, user=request.user)

    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            quote = data.get('quote', '').strip()
        else:
            quote = request.POST.get('quote', '').strip()

        memorial.quote = quote
        memorial.save()

        return JsonResponse({
            'status': 'success',
            'quote': memorial.quote,
            'message': 'Quote updated successfully'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)


@require_POST
@login_required
def update_banner(request, pk):
    """AJAX endpoint for updating memorial banner"""
    try:
        memorial = Memorial.objects.get(pk=pk, user=request.user)

        banner_type = request.POST.get('banner_type')
        banner_value = request.POST.get('banner_value')

        if not banner_type or not banner_value:
            return JsonResponse({
                'status': 'error',
                'message': 'Missing required fields'
            }, status=400)

        if banner_type not in ['image', 'color']:
            return JsonResponse({
                'status': 'error',
                'message': 'Invalid banner type'
            }, status=400)

        if banner_type == 'image' and banner_value.startswith('/static/'):
            banner_value = banner_value.replace('/static/', '')

        memorial.banner_type = banner_type
        memorial.banner_value = banner_value
        memorial.save()

        return JsonResponse({
            'status': 'success',
            'banner_type': banner_type,
            'banner_value': banner_value
        })

    except Memorial.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Memorial not found'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)


@require_POST
@login_required
def update_biography(request, pk):
    """AJAX endpoint for updating memorial biography"""
    try:
        memorial = get_object_or_404(Memorial, pk=pk, user=request.user)
        biography = request.POST.get('biography', '')
        memorial.biography = biography
        memorial.save()
        return JsonResponse({
            'success': True,
            'biography': biography.replace('\n', '<br>')
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)