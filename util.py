from fpdf import FPDF

def exportar_txt(cartoes):
    nome_arquivo = "cartoes_lotofacil.txt"
    with open(nome_arquivo, "w") as f:
        for i, c in enumerate(cartoes, 1):
            f.write(f"Cartão {i}: {' - '.join(f'{n:02}' for n in c)}\n")
    return nome_arquivo

def exportar_pdf(cartoes):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for i, c in enumerate(cartoes, 1):
        pdf.cell(200, 10, txt=f"Cartão {i}: {' - '.join(f'{n:02}' for n in c)}", ln=True)
    nome_arquivo = "cartoes_lotofacil.pdf"
    pdf.output(nome_arquivo)
    return nome_arquivo
