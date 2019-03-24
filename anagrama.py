def fatorial(numero):

        calc = 1

        for i in range(numero):

                calc *= numero
                numero -= 1

        return calc

def gerarAnagrama(qnt_numeros, numero):

        import random as r
        
        verificar, permutacao, numeroLista = [], '', list(str(numero))
        
        for k in range(qnt_numeros):

                number = r.randint(0, len(numeroLista) - 1)

                while True:

                        number = r.randint(0, len(numeroLista) - 1)

                        if not number in verificar or len(verificar) == qnt_numeros: break

                verificar.append(number)
                permutacao += numeroLista[number]

        return permutacao

def anagrama(numero, df = ''):

        """
        df - parametro que define o que você quer visualizar

        df == 'min': menor anagrama
        df == 'max': maior anagrama
        df == (vazio): todos os anagramas
        """

        numero = str(numero)
        
        qnt_numeros, permutacoes = len(numero), []

        for i in range(fatorial(qnt_numeros)):

                permutacao = gerarAnagrama(qnt_numeros, numero)

                while permutacoes.count(permutacao) > 0:

                        permutacao = gerarAnagrama(qnt_numeros, numero)

                        permutacao = str(permutacao)

                        if not permutacao in permutacoes: break
                   
                permutacoes.append(permutacao)
                
        if df is 'max': return int(max(permutacoes))
        if df is 'min': return int(min(permutacoes))

        return permutacoes
