
def calculo_inss(salario):

    if salario <= 1045.00:
        desconto_inss = ( salario * (7.5 / 100) )
        print("O desconto é de 7.5% em cima de "+str(salario))
    elif salario >= 1045.01 and salario <= 2089.60:
        desconto_inss = ( salario * (9 / 100) )
        print("O desconto é de 9% em cima de "+str(salario))

    elif salario >= 2089.61 and salario <= 3134.40:
        desconto_inss =  ( salario * (12 / 100) )
        print("O desconto é de 12% em cima de "+str(salario))

    elif salario >= 3134.41 and salario <= 6101.06:
        desconto_inss = ( salario * (14 / 100) )
        print("O desconto é de 14% em cima de "+str(salario))

    elif salario > 6101.07:
        desconto_inss = (salario * (14 / 100))
        print("O desconto é de 14% em cima de "+str(salario))
        
    
    return desconto_inss

def calculo_imposto_renda(salario):

    if salario <= 1903.98:
        desconto_imposto_renda = None
    elif salario >= 1903.99 and salario <= 2826.65:
        desconto_imposto_renda = (salario * (7.5 / 100))

        if(desconto_imposto_renda > 142.80):
            desconto_imposto_renda = 142.80

        print("O desconto é de 7.5% em cima de "+str(salario))

    elif salario >= 2826.66 and salario <= 3751.05:
        desconto_imposto_renda =  (salario * (15 / 100))
        if(desconto_imposto_renda > 354.80):
            desconto_imposto_renda = 354.80
        
        print("O desconto é de 12% em cima de "+str(salario))

    elif salario >= 3751.06 and salario <= 4664.68:
        desconto_imposto_renda = (salario * (22.5 / 100))
        if(desconto_imposto_renda > 636.13):
            desconto_imposto_renda = 636.13
        print("O desconto é de 14% em cima de "+str(salario))

    elif salario > 4664.68:
        desconto_imposto_renda = (salario * (27.5 / 100))
        if(desconto_imposto_renda > 869.36):
            desconto_imposto_renda = 869.36
    
    return desconto_imposto_renda

def calculo_fgts(salario):
    desconto = ( salario * (8 / 100) )
    return desconto
