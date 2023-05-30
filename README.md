# sistema_de_impressao

Como instalar:
**Inicie o processo com:**
    python3 -m venv env (Para criar ambiente virtual)
    python3 manage.py createsuperuser (Para criar um superusuário)
    source env/bin/activate (Para ativar ambiente)
**Em seguida:**
    python manage.py shell (Para iniciar o shell) <br>
    from diagnosticos.models import ResponsavelTecnico, ProdutorRural, Propriedade, Diagnostico (Para importar as classes)
    **Adicione como nos exemplos abaixo:**
    responsavel = ResponsavelTecnico.objects.create(nome='Nome do Responsável', cnpj='12345678901234', numero_registro='123456')
    produtor = ProdutorRural.objects.create(nome='Nome do Produtor', propriedade='Nome da Propriedade')
    propriedade = Propriedade.objects.create(descricao='Descrição da Propriedade', cnpj='12345678901234', local='Local da Propriedade', latitude=12.345678, longitude=98.765432)
    diagnostico = Diagnostico.objects.create(cultura='Nome da Cultura', produto_comercial='Nome do Produto', alvo='Nome do Alvo', area_a_tratar=100.00, volume_da_calda=10.00, intervalo_de_seguranca=7, modalidade_aplicacao='Nome da Modalidade', equipamento_aplicacao='Nome do Equipamento', quantidade_a_adquirir=5, n_aplicacoes=3, epoca_aplicacao='Época de Aplicação')
**Para finalizar:**
    http://127.0.0.1:8000/exibir-diagnostico/ (Acesse para ver os dados inseridos no arquivo e imprima)
