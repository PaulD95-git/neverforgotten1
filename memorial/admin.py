from django.contrib import admin
from .models import Memorial, Tribute, GalleryImage, ContactMessage

# --- Admin Registrations ---
admin.site.register(Tribute)  # Basic registration (no custom admin needed)


# --- Inline Admin Classes ---
class GalleryImageInline(admin.TabularInline):
    """Inline editor for memorial gallery images."""
    model = GalleryImage
    extra = 1  # Number of empty image slots shown by default


