from django.shortcuts import render
from app.models import *


def frequenciaView(request):
    consulta = {
        'frequencias': Frequencia.objects.all(),
    }

    return render(request, 'pessoa/frequencia.html', consulta)


def matriculaView(request):
    consulta = {
        'matriculas': Matricula.objects.all(),
    }

    return render(request, 'pessoa/matricula.html', consulta)


def instituicaoView(request):
    consulta = {
        'instituicoes': Instituicao.objects.all(),
    }

    return render(request, 'instituicao/instituicao.html', consulta)


def ocorrenciaView(request):
    consulta = {
        'ocorrencias': Ocorrencia.objects.all(),
    }

    return render(request, 'turma/ocorrencia.html', consulta)


def turmaView(request):
    consulta = {
        'turmas': Turma.objects.all(),
    }

    return render(request, 'turma/turma.html', consulta)


def cursoView(request):
    consulta = {
        'cursos': Curso.objects.all(),
    }

    return render(request, 'curso/curso.html', consulta)


def disciplinaporcursoView(request):
    consulta = {
        'dpcs': DisciplinaPorCurso.objects.all(),
    }

    return render(request, 'curso/disciplina_por_curso.html', consulta)


def disciplinaView(request):
    consulta = {
        'disciplinas': Disciplina.objects.all(),
    }

    return render(request, 'curso/disciplina.html', consulta)


def avaliacaoView(request):
    consulta = {
        'avaliacoes': Avaliacao.objects.all(),
    }

    return render(request, 'avaliacao/avaliacao.html', consulta)


def tipoavaliacaoView(request):
    consulta = {
        'tas': TipoAvaliacao.objects.all(),
    }

    return render(request, 'avaliacao/tipo_avaliacao.html', consulta)


def areaView(request):
    consulta = {
        'areas': Area.objects.all(),
    }

    return render(request, 'curso/area.html', consulta)


def ocupacaoView(request):
    consulta = {
        'ocupacoes': Ocupacao.objects.all(),
    }

    return render(request, 'pessoa/ocupacao.html', consulta)


def semestreView(request):
    consulta = {
        'semestres': Semestre.objects.all(),
    }

    return render(request, 'semestre/semestre.html', consulta)


def periodoView(request):
    consulta = {
        'periodos': Periodo.objects.all(),
    }

    return render(request, 'semestre/periodo.html', consulta)


def pessoaView(request):
    if request.POST:
        nova_pessoa = Pessoa()
        nova_pessoa.nome = request.POST.get('nome')
        nova_pessoa.pai = request.POST.get('pai')
        nova_pessoa.mae = request.POST.get('mae')
        nova_pessoa.cpf = request.POST.get('cpf')
        nova_pessoa.email = request.POST.get('email')
        nova_pessoa.data_nasc = request.POST.get('data_nasc')
        try:
            nova_pessoa.cidade = Cidade.objects.get(request.POST.get('cidade'))
            nova_pessoa.ocupacao = Ocupacao.objects.get(request.POST.get('ocupacao'))
            nova_pessoa.save()
        except Cidade.DoesNotExist:
            print("Cidade não encontrada!")
        except Ocupacao.DoesNotExist:
            print("Ocupacao não encontrada!")
        except Exception as e:
            print("Erro: ", e)

    consulta = {
        'pessoas': Pessoa.objects.all(),
        'cidades': Cidade.objects.all(),
        'ocupacoes': Ocupacao.objects.all(),
    }

    return render(request, 'pessoa/pessoa.html', consulta)


def cidadeView(request):
    if request.POST:
        nova_cidade = Cidade()
        nova_cidade.nome = request.POST.get('nome')
        nova_cidade.uf = request.POST.get('uf')
        nova_cidade.save()

    consulta = {
        'cidades': Cidade.objects.all(),
    }

    return render(request, 'instituicao/cidade.html', consulta)
