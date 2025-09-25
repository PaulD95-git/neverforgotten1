from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib import messages

from .models import Subscriber



@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    """Admin interface configuration for Subscriber model."""

    list_display = ('email', 'first_name', 'subscribed', 'created_at')
    list_filter = ('subscribed', 'created_at')
    search_fields = ('email', 'first_name', 'last_name')
    actions = ['resubscribe_selected']

    def resubscribe_selected(self, request, queryset):
        """
        Admin action to resubscribe selected subscribers.

        Args:
            request: HttpRequest object
            queryset: QuerySet of selected Subscriber objects
        """
        updated = queryset.update(subscribed=True)
        self.message_user(
            request,
            f'{updated} subscribers were resubscribed.',
            messages.SUCCESS
        )

    resubscribe_selected.short_description = "Resubscribe selected subscribers"
