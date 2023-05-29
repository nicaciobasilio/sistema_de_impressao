from django.db import models

class ResponsavelTecnico(models.Model):
    nome = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14)
    numero_registro = models.CharField(max_length=20)

    class Meta: 
        verbose_name="Responsável técnico"
        verbose_name_plural="Responsáveis técnicos"
        db_table = "responsal_tecnico"

class ProdutorRural(models.Model):
    nome = models.CharField(max_length=50)
    propriedade = models.CharField(max_length=100)

    class Meta: 
        verbose_name="Produtor rural"
        verbose_name_plural="Produtores rurais"
        db_table = "produtor_rural"

class Propriedade(models.Model):
    descricao = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14)
    local = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta: 
        verbose_name="Propriedade"
        verbose_name_plural="Propriedades"
        db_table = "propriedade"

class Diagnostico(models.Model):
    cultura = models.CharField(max_length=100)
    produto_comercial = models.CharField(max_length=100)
    alvo = models.CharField(max_length=100)
    area_a_tratar = models.DecimalField(max_digits=8, decimal_places=2)
    volume_da_calda = models.DecimalField(max_digits=8, decimal_places=2)
    intervalo_de_seguranca = models.IntegerField()
    modalidade_aplicacao = models.CharField(max_length=100)
    equipamento_aplicacao = models.CharField(max_length=100)
    quantidade_a_adquirir = models.IntegerField()
    n_aplicacoes = models.IntegerField()
    epoca_aplicacao = models.CharField(max_length=100)

    class Meta: 
        verbose_name="Diagnóstico"
        verbose_name_plural="Diagnostícos"
        db_table = "diagnostico"

