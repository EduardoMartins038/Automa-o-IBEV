#Banco de dados

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Inicialize o SDK do Firebase com as credenciais do arquivo serviceAccountKey.json
cred = credentials.Certificate("app-cards-23f24-firebase-adminsdk-ap3rq-e56adc2e19.json")
firebase_admin.initialize_app(cred)

# Inicialize o Firestore
db = firestore.client()

# Defina os dados que você deseja adicionar ao documento
dados_documento = {
    u'campo1': u'valor1',
    u'campo2': u'valor2',
    # Adicione outros campos conforme necessário
}

# Adicione os dados ao Firestore criando uma coleção e um documento
# A coleção pode ser criada automaticamente quando você adiciona um documento
doc_ref = db.collection(u'suaColecao').document()

# Insira os dados no documento recém-criado
doc_ref.set(dados_documento)

print("Coleção e documento criados com sucesso!")



#Automação Cadastro
print('Olá, Seja bem-vindo á IBEV! Para realizar o seu cadastro é necessário preencher os seguintes dados:')
nomec=input('Informe por favor seu nome completo:')
cpf=input('Digite seu CPF:')
datanascimento=input('Informe por favor sua data de nascimento:')
endereco=input('Informe por favor seu endereço completo, Exemplo: *Av. Crisantino de Almeida, 590 - Vargem Grande II, Montes Claros - MG, 39403-452* ')
contato=input('Qual o telefone para contato?')
nome=input('Como gostaria de ser chamado?')
confirm=input('Maravilha {}, Agora me confime os dados informados: Seu nome completo é: {}, Seu Cpf: {}, Sua data de nascimento: {}, Seu endereco: {}, Sua naturalidade: {}, Seu telefone para contato: {}'
.format(nome, nomec, cpf, datanascimento, endereco, contato))
print('Glorias a Deus, {}! Seu cadastro foi feito com sucesso.'.format(nome))