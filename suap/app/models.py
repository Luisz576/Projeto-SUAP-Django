from django.db import models


class Ocupacao(models.Model):
    nome = models.CharField(max_length=25)

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=45)
    uf = models.CharField(max_length=5)

    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField(max_length=40)
    pai = models.CharField(max_length=40)
    mae = models.CharField(max_length=40)
    cpf = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    data_nasc = models.DateField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Instituicao(models.Model):
    nome = models.CharField(max_length=45)
    site = models.CharField(max_length=50)
    telefone = models.CharField(max_length=12)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Area(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=30)
    area_saber = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    nome = models.CharField(max_length=30)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

    def __str__(self):
        return f"{self.instituicao} - {self.pessoa} - {self.curso}"


class Periodo(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Semestre(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Turma(models.Model):
    nome = models.CharField(max_length=30)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class DisciplinaPorCurso(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    carga_horaria = models.IntegerField()
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.curso} - {self.disciplina} - {self.carga_horaria}"


class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    numero_faltas = models.IntegerField()

    def __str__(self):
        return f"{self.pessoa} - {self.curso} - {self.disciplina}"


class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=100)
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.data} - {self.curso} - {self.disciplina}"


class TipoAvaliacao(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    tipo_avaliacao = models.ForeignKey(TipoAvaliacao, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.curso} - {self.disciplina} - {self.tipo_avaliacao}"
