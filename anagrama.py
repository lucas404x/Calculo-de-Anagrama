from random import sample

def repeticoes(numero):

        repeticoes = 1

        valor = []

        numero = list(str(numero))

        for k in numero:

                if numero.count(k) > 1 and k not in valor:

                        number = numero.count(k)

                        repeticoes *= fatorial(number)

                valor.append(k)

        print(repeticoes)
        return repeticoes

def fatorial(numero):

        calc = 1

        for i in range(numero):

                calc *= numero
                numero -= 1

        return calc

def anagrama(numero, df = ''):

        """
        df - parametro que define o que você quer visualizar

        df == 'min': menor anagrama
        df == 'max': maior anagrama
        df == (vazio): todos os anagramas
        """
        
        qnt_numeros, permutacoes, listaNumero = len(str(numero)), [], list(str(numero))

        totalPermutacoes = fatorial(qnt_numeros) / fatorial(repeticoes(numero))
        
        if totalPermutacoes < 1: totalPermutacoes = 1
        
        while len(permutacoes) != round(totalPermutacoes):

                permutacao = ''
                
                gerarAnagrama = sample(str(numero), qnt_numeros)

                for k in gerarAnagrama:

                        permutacao += k

                if permutacao not in permutacoes:
                        
                        permutacoes.append(permutacao)
                
        if df is 'max': return int(max(permutacoes))
        if df is 'min': return int(min(permutacoes))
        if df is '': return permutacoes
