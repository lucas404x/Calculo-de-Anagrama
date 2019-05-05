from tkinter import*
from tkinter import messagebox, filedialog
from functools import partial
from anagrama import anagrama

class Janela:

        def __init__(self, janela):

                self.janelaPrincipal = janela
                self.janelaPrincipal.title("Calcula Permutações")
                self.janelaPrincipal.geometry("250x85")
                self.janelaPrincipal.resizable(False, False)
                self.windowResult = None
                
                self.info_inserir = Label(self.janelaPrincipal, text = "Insira um número ou nome", font = (14))
                self.inserir_dado = Entry(self.janelaPrincipal)
                self.confirmar = Button(self.janelaPrincipal, text = "Calcular", foreground = 'black', command = self.calcularPermutacao)

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

                self.inserir_dado.delete(0, END)
                self.exibirPermutacao(text)

        def exibirPermutacao(self, text_result):

                self.windowResult = Tk()
                self.windowResult.title("Resultado")
                
                lb = Label(self.windowResult, text = text_result)
                save = Button(self.windowResult, text = "Salvar Anagramas", command = partial(self.save, text_result))
                sair = Button(self.windowResult, text = "Fechar", command = lambda:self.windowResult.destroy())

                lb.pack()
                save.pack(side = 'right')
                sair.pack(side = 'left')
        
        def save(self, text):

                opcoes = {'defaultextension':'.txt', 'title':"Escolha um diretorio para salvar o Anagrama"}

                try:
                        arquivo = filedialog.asksaveasfile(mode = 'w', **opcoes)
                        arquivo.write(text)
                        arquivo.close()
                except:
                        print("Arquivo não foi salvo")
