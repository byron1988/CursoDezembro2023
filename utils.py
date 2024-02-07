def numero_perfeito(num):
    '''
    num: um número inteiro
    
    Essa função retorna True se num for um número perfeito e False caso contrário.
    '''

    soma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            soma_divisores += i
    return soma_divisores == num



def obter_mais_longa_substring(s):
    '''
    s: string que será passada
    
    Essa função retorna a mais longa substring de texto em ordem alfabética.
    '''
    maior_substring = ''
    caract = s[0]
    substring = ''
    for x in s[1::]:
        if caract <= x:
            if substring == '':
                substring += caract + x
            else:
                substring += x
        else:
            if len(substring) > len(maior_substring):
                maior_substring = substring
            substring = ''
            
        caract = x
    
    return maior_substring


def tupla_par(tupla):
    return tuple(tupla[i] for i in range(0, len(tupla), 2))
