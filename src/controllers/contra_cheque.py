from server.instace import server
from utils.general import format_to_br_real, real_br_money_mask
from utils.utilsContraCheque import *

from controllers.funcionario import Funcionario
from controllers.lancamento import Lancamento
from flask import Flask

app = server.app

class Contra_Cheque:
    def __init__(self, lancamentos, salario_bruto, salario_liquido):
        self.mes_referencia = None
        self.lancamentos = lancamentos
        self.salario_bruto = salario_bruto
        self.salario_liquido = salario_liquido
        self.total_descontos = (salario_liquido - salario_bruto)
    
    def get_Lista_Lancamentos(self):
        
        lista_lancamentos = []
        for lan in self.lancamentos:
            total = "R$" + real_br_money_mask(lan.valor)
            lista = {
                'Tipo': lan.tipo,
                'Valor': total,
                'Descricao': lan.descricao,
            }

            lista_lancamentos.append(lista)

        return lista_lancamentos

@app.route('/contracheque/<id>')
def get_contra_cheque(id):
    funci = Funcionario.query.get_or_404(id)

    cc = criar_contra_cheque(funci)
    lista_lancamentos = cc.get_Lista_Lancamentos()
    return {
    'Mes Referencia': cc.mes_referencia,
        'Lista Lancamentos': lista_lancamentos,
        'Salario bruto': format_to_br_real(cc.salario_bruto),
        'Total de descontos': format_to_br_real(cc.total_descontos),
        'Salario liquido': format_to_br_real(cc.salario_liquido),

    }

def criar_contra_cheque(funcionario):

    salario_bruto = funcionario.salario_bruto
    salario_liquido = salario_bruto  
    lancamentos = []

    lanc_inss  = gerar_lanc_inss(salario_bruto)
    salario_liquido -= lanc_inss.valor
    lancamentos.append(lanc_inss)
    
    lanc_imposto_renda  = gerar_lanc_imposto_renda(salario_bruto)
    if(lanc_imposto_renda):
        salario_liquido -= lanc_imposto_renda.valor
        lancamentos.append(lanc_imposto_renda)
    
    if(funcionario.desconto_plano_saude == True):
        salario_liquido -= 10
        lancamento_pl_saude = Lancamento("Desconto", 10, "Desconto plano de saude") 
        lancamentos.append(lancamento_pl_saude)

    if(funcionario.desconto_plano_dental == True):
        salario_liquido -= 10
        lancamento_pl_dental = Lancamento("Desconto", 10, "Desconto plano dental") 
        lancamentos.append(lancamento_pl_dental)

    if(funcionario.desconto_plano_transporte == True):
        if(salario_bruto > 1500.00):
            desconto = ( salario_bruto * (6 / 100) )
            salario_liquido -= desconto
            lancamento_vale_transporte = Lancamento("Desconto", desconto, "Desconto vale transporte") 
            lancamentos.append(lancamento_vale_transporte)

    lanc_fgts  = gerar_lanc_fgts(salario_bruto)
    salario_liquido -= lanc_fgts.valor
    lancamentos.append(lanc_fgts) 

    contra_cheque = Contra_Cheque(lancamentos, salario_bruto, salario_liquido)

    return contra_cheque
