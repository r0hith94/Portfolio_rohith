from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Skill

def home(request):
    skills = Skill.objects.all()
    featured_projects = Project.objects.filter(featured=True)[:3]
    context = {
        'skills': skills,
        'featured_projects': featured_projects
    }
    return render(request, 'portfolio_app/home.html', context)

def projects(request):
    all_projects = Project.objects.all()
    context = {
        'projects': all_projects
    }
    return render(request, 'portfolio_app/projects.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        'project': project
    }
    return render(request, 'portfolio_app/project_detail.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Compose email
        full_message = f"From: {name} <{email}>\n\n{message}"
        
        try:
            # Send email (configure in settings)
            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ['your-email@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        except:
            messages.error(request, 'Something went wrong. Please try again.')
    
    return render(request, 'portfolio_app/contact.html')