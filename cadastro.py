#Banco de dados

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime
import validate_email
# Inicialize o SDK do Firebase com as credenciais do arquivo serviceAccountKey.json
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Inicialize o Firestore
db = firestore.client()
def salvar_cliente(nomec, cpf, datanascimento, endereco, contato, nome, email):
    # Verifique se o email é válido
    if not validate_email.validate_email(email):
        raise ValueError('Email inválido')
    
    # Converta a data de nascimento para um objeto do tipo datetime
    data_nascimento_obj = datetime.strptime(datanascimento, '%d/%m/%Y')
    data_nascimento_str = data_nascimento_obj.strftime('%d/%m/%Y')

     # Verifique se o nome completo já existe no banco de dados
 #   doc_ref = db.collection('clientes').document(nomec)
 #   doc = doc_ref.get()
 #   if doc.exists:
 #       raise ValueError('Nome completo já existe no banco de dados')
    

    # Converta o telefone para um número inteiro
    contato_int = int(contato.replace('-', ''))
    cpf_int=int(cpf.replace('-',''))
    # Crie um documento no banco de dados com o CPF como ID
    doc_ref = db.collection('clientes').document(nome)

    # Adicione os dados do cliente ao documento
    doc_ref.set({
        'nomec': nomec,
        'cpf': cpf_int,
        'datanascimento': data_nascimento_obj,
        'endereco': endereco,
        'contato': contato_int,
        'nome': nome,
        'email': email
    })

# Solicite os dados do cliente ao usuário
nomec=input('Informe por favor seu nome completo:')
cpf=input('Digite seu CPF:')
datanascimento=input('Informe por favor sua data de nascimento:')
endereco=input('Informe por favor seu endereço completo, Exemplo: *Av. Crisantino de Almeida, 590 - Vargem Grande II, Montes Claros - MG, 39403-452* ')
contato=input('Qual o telefone para contato?')
nome=input('Como gostaria de ser chamado?')
email=input('Por favor insira seu e-mail:')

# Salve os dados do cliente no banco de dados firebase
salvar_cliente(nomec, cpf, datanascimento, endereco, contato, nome, email)