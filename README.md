# Web Data Analyzer
 Este é um projeto de pratica, criado para testar minhas habilidades com Framework Vue e Flask.

[![Python Version][python-image]][python-url]
[![Flask Version][flask-image]][flask-url]
[![Vue Version][vue-image]][vue-url]
[![Vue/Cli Version][vue/cli-image]][vue/cli-url]
[![MongoDB Version][mongodb-image]][mongodb-url]

O intuito do projeto é testar minhas habilidades com uso do framework Vue e Flask, assim como suas integrações e processos.
O projeto como um todo ainda se encontra imcompleto, por conta de falhas operacionais no envio do arquivo pelo Vue e o tratamento do esquema pela API. Observando estes fatos, apenas está disponivel o fluxo por meio do backend, visto que ele foi projetado como uma API Restful.

## Pacotes

Segue a lista de pacotes utilizados no projeto backend.

Package                                      | Version  |
---------------------------------------------| ---------|
[Flask][flask-url]                           | 1.1.1    |
[Flask-Cors][flask_cors-url]                 | 3.0.8    |
[flask-Restful][flask_restful-url]           | 0.3.7    |
[Flask-Mongoengine][flask_mongoengine-url]   | 0.9.5    |
[gunicorn][gunicorn-url]                     | 19.9.0   |
[python-dotenv][python_dotenv-url]           | 0.10.3   |
[pandas][pandas-url]                         | 0.25.3   |

## Instalação:

Para instalação em ambiente de desenvolvimento, segue o contexto abaixo, explicando apenas sobre a parte backend. Caso prefira e tenha conhecimentos avançados, utilizamos como servidor e compilador, nginx e gunicorn, logo disponibilizaremos arquivos de configurações caso sabia como implanta-los e queria testa-los em ambiente de homologação.

Devemos em breve, finalizar o projeto com uma versão dockerizada, para fins de teste pratico.

### Etapas para uso em desenvolvimento:

#### Rotas e recursos
Rotas                                       | Metodos    |
--------------------------------------------|------------|
http://127.0.0.1:5000/data/insert           | POST       |
http://127.0.0.1:5000/data/logs             | GET        |

**Obs**:
 * É necessario realizar o teste pelo primeiro endpoint, repassando o parametrô ```file``` na requisão POST.
 * Quanto a requisção da lista de logs, apenas resgatar o processo de todos os logs.


1. Com a sua ambiente python, instale a lista de pacotes.
```sh
pip install -r requeriments/dev.txt
```
2. Não esqueça de criar suas variaveis de ambiente, usem o editor de preferência e insira dentro da pasta do projeto.
Segue exemplo das variaveis exigidas para funcionamento do projeto:

```
[settings]
SECRET_KEY="1234567"
UPLOAD_FOLDER = "path/to/folder/uploads"
LOG= "path/to/file/,env"
DB_NAME='dbname'
DB_HOST='dns_db'
DB_PORT= 'porta'
DB_USERNAME= 'username'
DB_PASSWORD= 'senha'

[flask_settings]
DEBUG=True
APP_PORT=5000
FLASK_APP="main.py"
FLASK_ENV="development"
```

3. Na pasta do projeto com as variaveis de ambientes definidas, realize a criação da base de dados do projeto, entrando pelo terminal ou GUI, acessar o MongoDB e criar usuarios.
```
```
4. Após a criação da base, apenas agora execute o projeto

```sh
flask run
```

### Customize configuration
Veja [Configuration Reference Vue](https://cli.vuejs.org/config/) e [Configuration Reference Flask](https://flask.palletsprojects.com/en/1.1.x/)

## Contribuate

1. Fork it ((https://github.com/xarpy/web_data_analyze))
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request


<!-- Markdown link & img dfn's -->
[vue-image]: https://img.shields.io/badge/vue-v2.6-green
[vue-url]: https://vuejs.org/
[vue/cli-image]: https://img.shields.io/badge/vue%2Fcli-v4.4.1-green
[vue/cli-url]: https://cli.vuejs.org/
[python-image]: https://img.shields.io/badge/python-v3.7-blue
[flask-image]: https://img.shields.io/badge/flask-v1.1.1-blue
[python-url]: https://www.python.org/downloads/release/python-374/
[flask-url]: https://flask.palletsprojects.com/en/1.1.x/
[flask_cors-url]: https://flask-cors.readthedocs.io/en/latest/
[flask_restful-url]: https://flask-restful.readthedocs.io/en/latest/
[python_dotenv-url]: https://github.com/theskumar/python-dotenv
[flask_mongoengine-url]: http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/
[mongodb-image]: https://img.shields.io/badge/mongodb-v4.2.1-yellowgreen
[mongodb-url]: https://docs.mongodb.com/
[gunicorn-url]: http://docs.gunicorn.org/en/latest/index.html
[pandas-url]: https://pandas.pydata.org/
[marshmallow-url]: https://marshmallow.readthedocs.io/en/stable/index.html