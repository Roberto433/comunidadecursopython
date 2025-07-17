from comunidadeimpressionadora import app, database
from comunidadeimpressionadora .models import Usuario

# Comandos para deletar e recriar o Banco de Dados
# with app.app_context():
#     database.drop_all()
#     database.create_all()

# Comando para verificar os usuarios no Banco de Dados
# with app.app_context():
#     usuario = Usuario.query.all()
#     print(usuario)
#     usuario = Usuario.query.first()
#     print(usuario.email)
#     print(usuario.senha)
#     print(usuario.username)
#     print(usuario.cursos)
#     usuario2 = Usuario.query.filter_by(username="Roberto Ferreira").first()
#     print(usuario2.email)
#     print(usuario2.senha)
#     print(usuario2.username)
#     print(usuario2.cursos)