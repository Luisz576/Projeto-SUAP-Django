"""
URL configuration for suap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    path('pessoa/', pessoaView, name='pessoa'),
    path('ocupacao/', ocupacaoView, name='ocupacao'),
    path('matricula/', matriculaView, name='matricula'),
    path('frequencia/', frequenciaView, name='frequencia'),

    path('instituicao/', instituicaoView, name='instituicao'),
    path('cidade/', cidadeView, name='cidade'),

    path('semestre/', semestreView, name='semestre'),
    path('periodo/', periodoView, name='periodo'),

    path('curso/', cursoView, name = 'curso'),
    path('disciplinaporcurso/', disciplinaporcursoView, name = 'disciplinaporcurso'),
    path('disciplina/', disciplinaView, name = 'disciplina'),
    path('area/', areaView, name = 'area'),

    path('turma/', turmaView, name = 'turma'),
    path('ocorrencias/', ocorrenciaView, name = 'ocorrencia'),

    path('avaliacao/', avaliacaoView, name = 'avaliacao'),
    path('tipoavaliacao/', tipoavaliacaoView, name = 'tipoavaliacao'),

    path('admin/', admin.site.urls),
]
