
def real_br_money_mask(my_value):
    a = '{:,.2f}'.format(my_value)
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')

def cpf_validate(numbers):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    #if cpf == cpf[::-1]:
        #return False

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

def format_to_br_real(number):
        
     return "R$" + real_br_money_mask(number)

def verify_required_fields(requiredFields, data):
    if data == None:
        return False

    if(data):
        for i in requiredFields:
            if i not in data:
                return False

