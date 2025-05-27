from django.contrib import admin

from .models import (
    Author,
    Blog,
    ContactForm,
    FrequentlyAskedQuestions,
    GeneralInfo,
    Services,
    Testimonial,
)


# Register your models here.
@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ["company_name", "location", "email", "phone", "open_hours"]
    list_filter = ["company_name", "location"]
    search_fields = ["company_name", "location", "email", "phone"]
    readonly_fields = ["email"]

    class meta:
        ordering = ["company_name"]


class ServiceAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]
    list_filter = ["title"]
    search_fields = ["title"]
    # list_editable = ["icon"]


admin.site.register(Services, ServiceAdmin)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["username", "user_job_title", "display_rating_count"]

    def display_rating_count(self, obj):
        return "*" * obj.rating_count  # Unicode for ★

    display_rating_count.short_description = "Rating"


@admin.register(FrequentlyAskedQuestions)
class FrequentlyAskedQuestionsAdmin(admin.ModelAdmin):
    list_display = ["question", "answer"]


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ["email", "is_success", "is_error", "action_time"]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=...):
        return False

    def has_delete_permission(self, request, obj=...):
        return False


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "country", "joined_at"]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "blog_image", "created_at"]
