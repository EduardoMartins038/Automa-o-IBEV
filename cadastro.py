#Banco de dados :)

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Inicialize o SDK do Firebase com as credenciais do arquivo serviceAccountKey.json
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Inicialize o Firestore
db = firestore.client()
def salvar_cliente(nomec, cpf, datanascimento, endereco, contato, nome):
    # Crie um documento no banco de dados com o CPF como ID
    doc_ref = db.collection('clientes').document(nome)

    # Adicione os dados do cliente ao documento
    doc_ref.set({
        'nomec': nomec,
        'cpf': cpf,
        'datanascimento': datanascimento,
        'endereco': endereco,
        'contato': contato,
        'nome': nome
    })

# Solicite os dados do cliente ao usuário
nomec=input('Informe por favor seu nome completo:')
cpf=input('Digite seu CPF:')
datanascimento=input('Informe por favor sua data de nascimento:')
endereco=input('Informe por favor seu endereço completo, Exemplo: *Av. Crisantino de Almeida, 590 - Vargem Grande II, Montes Claros - MG, 39403-452* ')
contato=input('Qual o telefone para contato?')
nome=input('Como gostaria de ser chamado?')

# Salve os dados do cliente no banco de dados firebase
salvar_cliente(nomec, cpf, datanascimento, endereco, contato, nome)