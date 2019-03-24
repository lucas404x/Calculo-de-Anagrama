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

        if type(numero) is int and numero >= 0:

                numero = str(numero)
                
                qnt_numeros, permutacoes = len(numero), set()

                for i in range(fatorial(qnt_numeros)):

                        permutacao = gerarAnagrama(qnt_numeros, numero)

                        permutacao = gerarAnagrama(qnt_numeros, numero)
                           
                        permutacoes.add(permutacao)
                        
                if df is 'max': return int(max(permutacoes))
                if df is 'min': return int(min(permutacoes))
                if df is '': return permutacoes

        return None
