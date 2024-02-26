# Bibliotecas
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
# Criação do documento e salvar informações
def create_id():
    return firestore.client().collection(u'collection_name').document().id
def salvar_cliente(nomec, cpf, datanascimento, endereco, contato, nome, email):
    # Verificações no BD
    if not validate_email.validate_email(email):
        raise ValueError('Email inválido')
    
    doc_ref = db.collection('clientes').document(cpf)
    doc = doc_ref.get()
    if doc.exists:
        raise ValueError('CPF já existe no banco de dados')
    
    doc_ref = db.collection('clientes').document(nomec)
    doc = doc_ref.get()
    if doc.exists:
        raise ValueError('Nome completo já existe no banco de dados')
    # Converção de tipo das variaveis
    data_nascimento_obj = datetime.strptime(datanascimento, '%d/%m/%Y')
    data_nascimento_str = data_nascimento_obj.strftime('%d/%m/%Y')
    contato_int = int(contato.replace('-', ''))
    cpf_int=int(cpf.replace('-',''))
    # Crie um documento no banco de dados com o NOME como ID
    doc_id = create_id()
    doc_ref = db.collection('clientes').document(str(doc_id))
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
# Solicite os dados ao usuário
nomec=input('Informe por favor seu nome completo:')
cpf=input('Digite seu CPF:')
datanascimento=input('Informe por favor sua data de nascimento:')
endereco=input('Informe por favor seu endereço completo, Exemplo: *Av. Crisantino de Almeida, 590 - Vargem Grande II, Montes Claros - MG, 39403-452* ')
contato=input('Qual o telefone para contato?')
nome=input('Como gostaria de ser chamado?')
email=input('Por favor insira seu e-mail:')
# Salve os dados dos clientes no banco de dados
salvar_cliente(nomec, cpf, datanascimento, endereco, contato, nome, email)