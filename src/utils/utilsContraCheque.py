from controllers.lancamento import Lancamento
from utils.utilsCalculos import *

def gerar_lanc_inss(salario_bruto):
    desconto = calculo_inss(salario_bruto)
    lancamento = Lancamento("Desconto", desconto, "Desconto INSS") 
    return lancamento

def gerar_lanc_imposto_renda(salario_bruto):
    desconto = calculo_imposto_renda(salario_bruto)
    lancamento = Lancamento("Desconto", desconto, "Desconto imposto de renda") 
    return lancamento

def gerar_lanc_fgts(salario_bruto):
    desconto = calculo_fgts(salario_bruto)
    lancamento = Lancamento("Desconto", desconto, "Desconto FGTS") 
    return lancamento
