# sistema_de_impressao

Como instalar:<br><br>
**Inicie o processo com:**<br>
    python3 -m venv env (Para criar ambiente virtual)<br>
    python3 manage.py createsuperuser (Para criar um superusuário)<br>
    source env/bin/activate (Para ativar ambiente)<br>
    pip install Django (Para baixar pacote)<br>
    cd sistema_de_impressao/ (Entre na pasta do arquivo) <br>
    pip install django-jazzmin (Instale o tema jazzmin)<br>
    python manage.py runserver (Para iniciar o server, para verificar se está tudo ok)<br><br>
**Em seguida:**<br>
    python manage.py shell (Para iniciar o shell) <br>
    from diagnosticos.models import ResponsavelTecnico, ProdutorRural, Propriedade, Diagnostico (Para importar as classes)<br><br>
    **Adicione como nos exemplos abaixo:**<br>
    responsavel = ResponsavelTecnico.objects.create(nome='Nome do Responsável', cnpj='12345678901234', numero_registro='123456')<br><br>
    minha_propriedade = Propriedade.objects.create(nome="Nome da propriedade", descricao="Descrição da Propriedade", cnpj="12345678901234", local="Local da Propriedade", latitude=12.345678, longitude=98.765432)<br><br>
    
produtor = ProdutorRural.objects.create(nome="Nome do Produtor", propriedade=minha_propriedade)<br><br>
 
diagnostico = Diagnostico.objects.create(cultura='Nome da Cultura', produto_comercial='Nome do Produto', alvo='Nome do Alvo', area_a_tratar=100.00, volume_da_calda=10.00, intervalo_de_seguranca=7, modalidade_aplicacao='Nome da Modalidade', equipamento_aplicacao='Nome do Equipamento', quantidade_a_adquirir=5, n_aplicacoes=3, epoca_aplicacao='Época de Aplicação')<br><br>
**Prosseguindo:**<br>
exit() (Para sair do shell)<br><br>
**Para finalizar:**<br>
    python manage.py runserver (Para iniciar o server)<br>
    http://127.0.0.1:8000/exibir-diagnostico/ (Acesse para ver os dados inseridos no arquivo e imprima)<br>
