import tkinter as tk

class Main(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = root
        self.pack()
        self.main()
    
    def main(self):
        self.buttonFont = ('arial', '15')
        self.buttonPady = 5
        self.buttonwidth = 20
        self.mainFrame = tk.Frame().pack()


        self.title = tk.Label(self.mainFrame, text = 'Reconhecimento de voz', font = ('arial', '25', 'bold')).pack(pady = 60)

        self.bInit = tk.Button(
            self.mainFrame, text = 'Iniciar', font = self.buttonFont, width = self.buttonwidth
            ).pack(pady = self.buttonPady)
        self.bConf = tk.Button(
            self.mainFrame, text = 'Configurações', font = self.buttonFont, width = self.buttonwidth, command= self.openConfig
            ).pack(pady = self.buttonPady)
    
    def openConfig(self):
        print('Configurações')
        Config(master=root)

class Config(tk.Frame):
    def __init__(self, master=Main):
        super().__init__(master)
        self.master = root
    
        # self.configFrame.wm_transient()
        # self.configFrame.focus_force()
        # self.configFrame.grab_set()
        self.pack()
        self.config()
        
    def config(self):
        print('foi')
        self.buttonFont = ('arial', '15')
        self.buttonPady = 5
        self.buttonwidth = 20
        self.mainFrame = tk.Toplevel(width = width, height = height)
        

        self.title = tk.Label(self.mainFrame, text = 'Configurações do Banco de Dados', font = ('arial', '25', 'bold')).pack(pady = 60)


        self.bRegister = tk.Button(
            self.mainFrame, text = 'Cadastrar comando', font = self.buttonFont, width = self.buttonwidth
            ).pack(pady = self.buttonPady)
        self.bChange = tk.Button(
            self.mainFrame, text = 'Alterar', font = self.buttonFont, width = self.buttonwidth
            ).pack(pady = self.buttonPady)
        self.bRemove = tk.Button(
            self.mainFrame, text = 'Remover', font = self.buttonFont, width = self.buttonwidth
            ).pack(pady = self.buttonPady)
        self.bVisualize = tk.Button(
            self.mainFrame, text = 'Visualizar', font = self.buttonFont, width = self.buttonwidth
            ).pack(pady = self.buttonPady)
        self.bQuit = tk.Button(
            self.mainFrame, text = 'Voltar ao menu', font = self.buttonFont, width = self.buttonwidth, command= self.destroy
            ).pack(pady = self.buttonPady)
    
    

root = tk.Tk()
width = 600
height = 400
root.geometry('{}x{}'.format(width, height))
root.title('Reconhecimento de Voz')
app = Main(master=root)

app.mainloop()
