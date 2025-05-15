import sys
try:
    intDividendo = int(input('Digite o Dividendo: '))
    intDivisor = int(input('Digite o Dividendo: '))
    flResultado = intDividendo / intDivisor
except ValueError:
    print('Erro Informe um valor    ue possa ser convertido em Inteiro.')
except ZeroDivisionError:
    print(f'ERRO: Não existe divisão por ZERO. ')
        except:
    print(f'ERRO: {sys.exc_info()}')
        else:
    print(flResultado)