from tkinter import*
from functools import partial
from anagrama import anagrama

class Janela:

        def __init__(self, janela):
                
                self.janela = janela
                self.janela.title("Calcula Permutações")
                self.janela.geometry("250x85")
                self.janela.resizable(False, False)
                
                self.info_inserir = Label(self.janela, text = "Insira um número ou nome")
                self.inserir_dado = Entry(self.janela)
                self.confirmar = Button(self.janela, text = "Calcular", foreground = 'black', command = self.calcularPermutacao)

                self.info_inserir.pack()
                self.inserir_dado.pack()
                self.confirmar.pack()

        def calcularPermutacao(self):

                calc = anagrama(self.inserir_dado.get())
                text = ""
                const = len(list(self.inserir_dado.get()))
                VALUE_CONST = const
                
                for valor in range(len(calc)):

                        if valor + 1 == const:
                                text += calc[valor] + "\n"
                                const += VALUE_CONST
                        else:
                                text += calc[valor] + " |"

                self.exibirPermutacao(text)

        def exibirPermutacao(self, text_result):

                windowResult = Tk()
                windowResult.title("Resultado")
                self.janela.resizable(False, False)
                
                lb = Label(windowResult, text = text_result)
                save = Button(windowResult, text = "Salvar Anagramas", command = partial(self.save, text_result))
                sair = Button(windowResult, text = "Fechar", command = lambda:exit)

                lb.pack()
                save.pack(side = 'right')
                sair.pack(side = 'left')
        
        def save(self, text):
                pass
