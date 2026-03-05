from fpdf import FPDF
from datetime import datetime

class FreightReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.set_text_color(30, 58, 138)
        self.cell(0, 10, 'FREIGHTMETRICS - REPORTE DE COTIZACIÓN', 0, 1, 'C')
        self.set_font('Arial', 'I', 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 5, 'Inteligencia Predictiva para Logística Transfronteriza', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()} | Generado por Freightmetrics Oracle AI', 0, 0, 'C')

def generate_pdf_report(data):
    pdf = FreightReport()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(0, 10, f"ID de Consulta: {datetime.now().strftime('%Y%m%d%H%M')}", 1, 1, 'L', 1)
    pdf.ln(5)
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 10, "DETALLES DEL VIAJE", 0, 1)
    pdf.set_font('Arial', '', 11)
    pdf.cell(95, 8, f"Origen: {data['origin']}", 0, 0)
    pdf.cell(95, 8, f"Destino: {data['destination']}", 0, 1)
    pdf.cell(95, 8, f"Distancia: {data['distance']} km", 0, 0)
    pdf.cell(95, 8, f"Tipo de Equipo: {data['equipment']}", 0, 1)
    pdf.ln(5)
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 10, "DESGLOSE ESTIMADO DE TARIFA (USD)", 0, 1)
    pdf.set_font('Arial', '', 11)
    for concepto, valor in data['breakdown'].items():
        nombre = concepto.replace('_', ' ').capitalize()
        pdf.cell(140, 8, f"{nombre}:", 1, 0)
        pdf.cell(50, 8, f"${valor:,.2f}", 1, 1, 'R')
    pdf.set_font('Arial', 'B', 13)
    pdf.set_text_color(30, 58, 138)
    pdf.cell(140, 12, "TARIFA TOTAL SUGERIDA:", 1, 0)
    pdf.cell(50, 12, f"${data['total_rate']:,.2f} USD", 1, 1, 'R')
    pdf.ln(10)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 10, "ANÁLISIS ESTRATÉGICO DEL ORÁCULO", 0, 1)
    pdf.set_font('Arial', 'I', 10)
    pdf.multi_cell(0, 6, data['ai_analysis'])
    pdf.ln(15)
    pdf.set_font('Arial', 'I', 8)
    pdf.set_text_color(150, 150, 150)
    disclaimer = ("Aviso: Este reporte es una estimación basada en modelos de IA y datos de mercado históricos. "
                  "Los precios finales pueden variar según la disponibilidad, condiciones climáticas y seguridad.")
    pdf.multi_cell(0, 5, disclaimer)
    return pdf.output(dest='S').encode('latin-1')
