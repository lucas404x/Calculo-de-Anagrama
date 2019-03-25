import anagrama

def main():

    """
    Função principal da aplicação
    """

    while True:
        
        print()
        print("[1] - Calcular anagrama")
        print("[2] - Sair")
        print()
        
        opcao = int(input("Opção: "))

        if opcao == 2:
            break
        
        else:
            
            valor = int(input("Digite um número para o calculo: "))
            print()
            print('[1] - Exibir todos os valores')
            print('[2] - Exibir o menor anagrama')
            print('[3] - Exibir o maior anagrama')
            print()
            exibir = int(input("Opção: "))

            if exibir is 1:
                exibir = ''
            if exibir is 2:
                exibir = 'min'
            if exibir is 3:
                exibir = 'max'

            print()
            
        print(anagrama.anagrama(valor, exibir))

if __name__ == '__main__':

    main()
