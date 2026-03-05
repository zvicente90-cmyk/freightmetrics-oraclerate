import pandas as pd
from fpdf import FPDF
import tempfile

# Función para generar PDF desde un DataFrame

def dataframe_to_pdf(df: pd.DataFrame, title: str = "Reporte FreightMetrics") -> bytes:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=title, ln=True, align='C')
    pdf.ln(10)
    # Encabezados
    for col in df.columns:
        pdf.cell(40, 10, col, border=1)
    pdf.ln()
    # Filas
    for i in range(len(df)):
        for col in df.columns:
            pdf.cell(40, 10, str(df.iloc[i][col]), border=1)
        pdf.ln()
    # Guardar en archivo temporal y devolver bytes
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        pdf.output(tmp.name)
        tmp.seek(0)
        pdf_bytes = tmp.read()
    return pdf_bytes
