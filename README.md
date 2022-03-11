# Take 5 - Teste para Analista de Testes Python

O objetivo desse teste é avaliar as competências do candidato como um analista de testes Python com conhecimentos no framework **Django**.

## Geral
Execute um fork desse repositório para iniciar o seu trabalho. O repositório deve conter um README com os passos para rodar o seu projeto.

O link com o repositório contendo o resultado final do seu trabalho deve ser enviado por email para alex.vieira@take5.com.br em até 2 dias úteis após o recebimento da tarefa.

## Preparação do ambiente

Para realizar a preparação do ambiente e iniciar os seus trabalhos você deverá ter [Python 3](https://www.python.org/downloads/ "Python 3") instalado em sua máquina. Após a instalação você deve executar os comandos abaixo em uma janela do terminal de sua escolha:

```
pip install virtualenv
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt --upgrade
python manage.py migrate
```

## Teste

Esse projeto contém uma API REST feita com o [Django Rest Framework](https://www.django-rest-framework.org/ "Django Rest Framework") e possui um [CRUD](https://developer.mozilla.org/pt-BR/docs/Glossary/CRUD "CRUD") para manipulação de participantes.

O modelo desse participante é o que segue abaixo:

```
class Participant(models.Model):
    name = models.CharField(_('Nome'), max_length=256, blank=False, null=False)
    age = models.IntegerField(_('Idade'), blank=False, null=False)
```

Todos os testes devem ser executados dentro do arquivo ```participant/tests.py```. A estrutura do arquivo não deve ser alterada. Dentro dele já existem indicativos do que deve ser testado. Nenhum outro arquivo deve ser alterado.

Os testes devem ser realizados considerando todos os [corner cases](https://en.wikipedia.org/wiki/Corner_case#:~:text=In%20engineering%2C%20a%20corner%20case,parameter%20is%20within%20the%20specified "Corner cases") que você conseguir imaginar para o que é pedido.

Após finalizar a criação dos testes você pode executar os mesmos utilizando o comando abaixo:

```
python manage.py test
```