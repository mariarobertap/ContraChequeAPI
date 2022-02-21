
from flask import Flask, request
from datetime import datetime
from server.instace import server
from utils.general import  cpf_validate, verify_required_fields, format_to_br_real
from db.database import db

app = server.app

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    sobrenome = db.Column(db.String(80),  nullable=False)
    documento = db.Column(db.String(20),  nullable=False)
    setor = db.Column(db.String(80),  nullable=False)
    salario_bruto = db.Column(db.Float, nullable=False)
    data_admissao = db.Column(db.DateTime,  nullable=False)
    desconto_plano_saude = db.Column(db.Boolean,  nullable=False)
    desconto_plano_dental = db.Column(db.Boolean,  nullable=False)
    desconto_plano_transporte = db.Column(db.Boolean,  nullable=False)



    def __repr__(self):
        return f"{self.id} - {self.nome}"


@app.route('/funcionario')
def get_funcionarios():

    funcionarios = Funcionario.query.all()

    output = []
    print(float("45.000.00".replace(".", "").replace(".", ",")))
    for funcionario in funcionarios:
        salario = format_to_br_real(funcionario.salario_bruto)

        funcionario_data = {
            'id': funcionario.id, 
            'nome': funcionario.nome,
            'sobrenome': funcionario.sobrenome,
            'documento': funcionario.documento,
            'setor': funcionario.setor,
            'salario_bruto': salario,
            'data_admissao': funcionario.data_admissao,
            'desconto_plano_saude': funcionario.desconto_plano_saude,
            'desconto_plano_dental': funcionario.desconto_plano_dental,
            'desconto_plano_transporte': funcionario.desconto_plano_transporte
        }

        output.append(funcionario_data)
    return {
        "Funcionários": output
    }

@app.route('/funcionario/<id>')
def get_funcionario(id):

    funcionario = Funcionario.query.get_or_404(id)
    salario = format_to_br_real(funcionario.salario_bruto)


    return {

            'id': funcionario.id, 
            'nome': funcionario.nome,
            'sobrenome': funcionario.sobrenome,
            'documento': funcionario.documento,
            'setor': funcionario.setor,
            'salario_bruto': salario,
            'data_admissao': funcionario.data_admissao,
            'desconto_plano_saude': funcionario.desconto_plano_saude,
            'desconto_plano_dental': funcionario.desconto_plano_dental,
            'desconto_plano_transporte': funcionario.desconto_plano_transporte
    }

@app.route('/funcionario', methods=['POST'])
def create_funcionario():

    requiredFields = ["nome", "sobrenome", "documento", "setor", "salario_bruto", "data_admissao", "desconto_plano_saude", "desconto_plano_dental", "desconto_plano_transporte"]
    data = request.json

    if(verify_required_fields(requiredFields, data) == False):
        return {
            "status": False,
            "description": "Campos obrigatórios estão faltando"
        }

    if(cpf_validate(data['documento']) == False):
        return {
            "status": False,
            "description": "Insira um CPF valido"
            }

    try:
        date = datetime.fromisoformat(data['data_admissao'])
        func = Funcionario(nome = data['nome'],
                        sobrenome = data['sobrenome'],
                        documento = data['documento'],
                        setor = data['setor'],
                        salario_bruto = data['salario_bruto'],
                        data_admissao = date,
                        desconto_plano_saude = data['desconto_plano_saude'],
                        desconto_plano_dental = data['desconto_plano_dental'],
                        desconto_plano_transporte = data['desconto_plano_transporte']
                        )

        db.session.add(func)
        db.session.commit()
        db.session.flush()
    except Exception as e:
            return {
            "status": False,
            "description": str(e)
            }

    return {
        "status": True,
        "description": "Funcionario criado!",
        "ID Funcionario": func.id
    }

