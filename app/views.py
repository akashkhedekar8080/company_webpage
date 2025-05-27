# from django.http import HttpResponse

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils import timezone

from .models import (
    Blog,
    ContactForm,
    FrequentlyAskedQuestions,
    GeneralInfo,
    Services,
    Testimonial,
)

# from .forms import ContactForm


# Create your views here.
def index(request):
    records = GeneralInfo.objects.last()
    services = Services.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = FrequentlyAskedQuestions.objects.all()
    blogs = Blog.objects.all().order_by("-created_at")[:3]
    print(blogs)
    context = {
        "company_name": getattr(records, "company_name", ""),
        "location": getattr(records, "location", ""),
        "phone": getattr(records, "phone", ""),
        "email": getattr(records, "email", ""),
        "open_hours": getattr(records, "open_hours", ""),
        "twitter_url": getattr(records, "twitter_url", ""),
        "facebook_url": getattr(records, "facebook_url", ""),
        "linkedin_url": getattr(records, "linkedin_url", ""),
        "instagram_url": getattr(records, "instagram_url", ""),
        "video_url": getattr(records, "video_url", ""),
        "services": services,
        "testimonials": testimonials,
        "faqs": faqs,
        "blogs": blogs,
    }
    return render(request, "index.html", context)


def aboutus(request):
    return render(request, "aboutus.html")


def contactform(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        context = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message,
        }
        html_content = render_to_string("email.html", context)
        is_success, is_error, error_message = False, False, ""
        try:
            send_mail(
                subject=subject,
                message=None,
                html_message=html_content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
        except Exception as e:
            error_message = str(e)
            messages.error(
                request,
                "An error occurred while sending the email. Please try again later.",
            )
            is_error = True
        else:
            is_success = True
            messages.success(request, "Thank you! Your email was sent successfully.")
        ContactForm.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            action_time=timezone.now(),
            is_success=is_success,
            is_error=is_error,
            error_message=error_message,
        )
    return redirect("home")


def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    recent_posts = Blog.objects.all().exclude(id=blog_id).order_by("-created_at")[:2]
    context = {"blog": blog, "recent_posts": recent_posts}
    return render(request, "blog-details.html", context)


def blogs(request):
    blogs = Blog.objects.all().order_by("-created_at")
    paginator = Paginator(blogs, 3)
    page_num = request.GET.get("page", 1)
    blog_page_obj = paginator.get_page(int(page_num))

    return render(request, "blog.html", {"blog_page_obj": blog_page_obj})
