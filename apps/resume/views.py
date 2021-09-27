from django.forms.models import inlineformset_factory
from apps.resume.forms import ResumeForm, ResumeImageForm
from django.shortcuts import render, redirect
from .models import Resume, ResumeImage
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render
from django.template.loader import get_template
from django.shortcuts import get_object_or_404, render
from reportlab.pdfgen import canvas
from django.http import HttpResponse, request
from django.template.loader import get_template
from xhtml2pdf import pisa
from apps.resume.models import Resume
from apps.users.models import User





def index(request):
    resume = Resume.objects.all()
    if 'key_word' in request.GET:
        key = request.GET.get('words')
        posts = Resume.objects.filter (user = request.user)
    return render(request, 'cv.html')
    


def create_resume(request):
    form = ResumeForm(request.POST, None)
    ResumeImageFormset = inlineformset_factory(Resume, ResumeImage, form=ResumeImageForm, extra=1)
    if form.is_valid():
        resume = form.save()
        formset = ResumeImageFormset(request.POST, request.FILES, instance=resume)
        if formset.is_valid():
            formset.save()
        return redirect('/')
    formset = ResumeImageFormset()
    return render(request, 'resume/create.html', locals())


def watch_resume(request):
    return render(request, 'resume/resume_watch.html', {})


def show_resume(request):
   resume = Resume.objects.all()

   context = {
      'resume': resume
   }

   return render(request, 'pdf/showinfo.html', locals())

def users_pdf_view(request, *args, **kwargs):
#    pk = kwargs.get('pk')
#    resume = get_object_or_404(User, pk=pk)

    resume = Resume.objects.all()
    template_path = 'pdf/pdfreport.html'
    context = {'resume': resume}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/csv')
    response['Content-Disposition'] = 'attachment; filename="resume_report.pdf"'
        # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
   

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
        # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response   



def pdf_report_create(request):
    pdf = request.user.pdf
    template_path = 'pdf/pdfreport.html'
    context = {'pdf': pdf}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/csv')
    response['Content-Disposition'] = 'filename="resume_report.pdf"'
        # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
        # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

