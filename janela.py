from tkinter import*
from tkinter import filedialog
from functools import partial
from anagrama import anagrama

class Janela:

        def __init__(self, janela):

                self.windowResult = None
                self.janelaPrincipal = janela
                self.janelaPrincipal.title("Calcula Permutações")
                self.janelaPrincipal.geometry("370x150")
                self.janelaPrincipal.resizable(False, False)
                
                self.info_inserir = Label(self.janelaPrincipal, text = "Insira um número ou nome", font = ("Arial", 10))
                self.inserir_dado = Entry(self.janelaPrincipal, justify = 'center', font = ('Arial', 12), bd = 3.5)
                self.info_comparar = Label(self.janelaPrincipal, text = "Insira algo para verificar se tem nas permutações (opcional)", font = ("Arial", 10))
                self.comparacao = Entry(self.janelaPrincipal, justify = 'center', font = ('Arial', 12), bd = 3.5)
                self.confirmar = Button(self.janelaPrincipal, text = "Calcular", foreground = 'black', command = self.calcularPermutacao)

                self.info_inserir.pack()
                self.inserir_dado.pack()
                self.info_comparar.pack()
                self.comparacao.pack()
                self.confirmar.pack()

        def calcularPermutacao(self):
                
                calc = anagrama(self.inserir_dado.get())
                self.exibirPermutacao(calc)

        def exibirPermutacao(self, calc):

                self.windowResult = Tk()
                self.windowResult.title("Resultado")
                frame_result = Frame(self.windowResult)
                frame_result.pack()
                
                text = ""
                const = len(list(self.inserir_dado.get()))
                
                for valor in range(len(calc)):

                        if valor % const == 0:
                                subframe = Frame(frame_result)
                                subframe.pack()

                        lb = Label(subframe, text = calc[valor] + " |")
                        
                        if calc[valor] == self.comparacao.get():
                                lb['foreground'] = 'green'
                                lb['bg'] = 'white'
                                
                        lb.pack(side = 'left')

                self.inserir_dado.delete(0, END)
                self.comparacao.delete(0, END)
                
                save = Button(self.windowResult, text = "Salvar Anagramas", command = partial(self.save, text))
                sair = Button(self.windowResult, text = "Fechar", command = lambda:self.windowResult.destroy())
                
                save.pack(side = 'right')
                sair.pack(side = 'left')
        
        def save(self, text):

                opcoes = {'defaultextension':'.txt', 'title':"Escolha um diretorio para salvar o Anagrama"}

                try:
                        arquivo = filedialog.asksaveasfile(mode = 'w', **opcoes)
                        arquivo.write(text)
                        arquivo.close()
                except:
                        pass
