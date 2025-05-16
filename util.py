from fpdf import FPDF

def exportar_txt(cartoes):
    caminho = "/mnt/data/cartoes_lotofacil.txt"
    with open(caminho, "w") as f:
        for i, c in enumerate(cartoes, 1):
            linha = f"Cartão {i}: {' - '.join(f'{d:02}' for d in c)}\n"
            f.write(linha)
    return caminho

def exportar_pdf(cartoes):
    caminho = "/mnt/data/cartoes_lotofacil.pdf"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for i, c in enumerate(cartoes, 1):
        linha = f"Cartão {i}: {' - '.join(f'{d:02}' for d in c)}"
        pdf.cell(200, 10, txt=linha, ln=True)
    pdf.output(caminho)
    return caminho