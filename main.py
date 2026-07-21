import tkinter as tk
from tkinter import filedialog, messagebox

arquivos = []


def selecionar_arquivos():
    global arquivos

    arquivos = filedialog.askopenfilenames(
        title="Selecione um ou mais arquivos VCF",
        filetypes=[("Arquivos VCF", "*.vcf")]
    )

    lista.delete(0, tk.END)

    for arquivo in arquivos:
        lista.insert(tk.END, arquivo)


def processar():
    if len(arquivos) == 0:
        messagebox.showwarning("Aviso", "Selecione pelo menos um arquivo.")
        return

    messagebox.showinfo(
        "Em desenvolvimento",
        f"{len(arquivos)} arquivo(s) selecionado(s).\n\nNa próxima etapa começaremos o processamento."
    )


janela = tk.Tk()
janela.title("VCF Colorizador")
janela.geometry("700x500")

titulo = tk.Label(
    janela,
    text="VCF COLORIZADOR",
    font=("Arial", 18, "bold")
)

titulo.pack(pady=10)

btn = tk.Button(
    janela,
    text="Selecionar Arquivos VCF",
    command=selecionar_arquivos,
    width=30,
    height=2
)

btn.pack()

lista = tk.Listbox(
    janela,
    width=90,
    height=15
)

lista.pack(pady=15)

btn2 = tk.Button(
    janela,
    text="Processar",
    command=processar,
    width=20,
    height=2,
    bg="green",
    fg="white"
)

btn2.pack()

janela.mainloop()
