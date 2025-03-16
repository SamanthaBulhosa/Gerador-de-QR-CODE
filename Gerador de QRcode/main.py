from tkinter import *
from tkinter import filedialog
import qrcode
from PIL import ImageTk

class GerarQRCode:
    def __init__(self):
        self.root = Tk()
        self.root.title('Gerador de QRCode')
        self.root.geometry('600x400+40+60')
        self.root.resizable(False, False)

        # Definição de cores iniciais
        self.cor01 = '#2c3e50'  # Cinza escuro
        self.cor02 = '#bdc3c7'  # Branco
        self.root.config(bg=self.cor02)  # Define cor de fundo inicial

        self.qr_cor = "black"  # Cor inicial do QR Code
        self.img_qrcode = None  # Variável para armazenar a imagem do QR
        self.qr_image = None  # Variável para salvar a imagem original do QR Code

        self.containers()
        self.root.mainloop()

    def containers(self):
        """Criação dos containers principais"""
        self.fr_container01 = Frame(self.root, height=400, width=300, bg=self.cor01)
        self.fr_container02 = Frame(self.root, height=400, width=300, bg=self.cor02)

        # Impede que os containers se ajustem ao conteúdo
        self.fr_container01.pack_propagate(0)
        self.fr_container02.pack_propagate(0)

        self.fr_container01.pack(side=LEFT)
        self.fr_container02.pack(side=LEFT)

        # Elementos no container 01
        Label(self.fr_container01, text="GERADOR DE QRCODE", font=20, fg='white', bg=self.cor01).pack(pady=50)
        Label(self.fr_container01, text="Digite o texto para gerar o QR Code:", fg='white', bg=self.cor01).pack(pady=10)

        self.entrada_texto = Entry(self.fr_container01, width=30)
        self.entrada_texto.pack(pady=5)

        self.btn_gerar = Button(self.fr_container01, text="Gerar QR Code", command=self.gerar_qr)
        self.btn_gerar.pack(pady=10)

        self.btn_salvar = Button(self.fr_container01, text="Salvar QR Code", command=self.salvar_qr, state=DISABLED)
        self.btn_salvar.pack(pady=10)

        # Label onde o QR Code será exibido
        self.lbl_qrcode = Label(self.fr_container02, bg=self.cor02)
        self.lbl_qrcode.pack(pady=20)

    """Gera e exibe o QR Code"""
    def gerar_qr(self):
        """Gera o QR Code a partir do texto digitado"""
        texto = self.entrada_texto.get().strip()
        if texto:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(texto)
            qr.make(fit=True)

            img = qr.make_image(fill=self.qr_cor, back_color="white")

            # Salva a imagem original para ser baixada depois
            self.qr_image = img

            # Converter para exibição no Tkinter
            img = img.resize((200, 200))
            self.img_qrcode = ImageTk.PhotoImage(img)

            self.lbl_qrcode.config(image=self.img_qrcode, text="")  # Atualiza a imagem e remove o texto de aviso
            self.btn_salvar.config(state=NORMAL)  # Ativa o botão de salvar
        else:
            self.lbl_qrcode.config(image='', text="Digite algo!", fg="red")  # Remove imagem e exibe aviso
            self.btn_salvar.config(state=DISABLED)  # Desativa o botão de salvar
            
    """Salva o QR Code gerado como arquivo PNG"""
    def salvar_qr(self):
        if self.qr_image:
            caminho_arquivo = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("Imagem PNG", "*.png")],
                title="Salvar QR Code"
            )
            if caminho_arquivo:
                self.qr_image.save(caminho_arquivo)  # Salva a imagem original
                print(f"✅ QR Code salvo em: {caminho_arquivo}")

# Executar o programa
GerarQRCode()
