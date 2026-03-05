# Arquitectura para cálculo de tarifa Index Spot FreightMetrics
# Tarifa spot = [(CF + CV) * Mn] + Casetas

class FreightMetricsEngine:
    def __init__(self, costo_fijo, costo_variable, multiplicador_mercado, costo_casetas):
        self.costo_fijo = costo_fijo
        self.costo_variable = costo_variable
        self.multiplicador_mercado = multiplicador_mercado
        self.costo_casetas = costo_casetas

    def calcular_tarifa(self):
        tarifa_base = (self.costo_fijo + self.costo_variable) * self.multiplicador_mercado
        tarifa_final = tarifa_base + self.costo_casetas
        return tarifa_final

# Ejemplo de uso:
# engine = FreightMetricsEngine(
#     costo_fijo=10000,
#     costo_variable=15000,
#     multiplicador_mercado=1.08,
#     costo_casetas=2500
# )
# print(engine.calcular_tarifa())

# Nuevo modelo de cálculo de tarifa spot por componentes
class FreightMetricsCalculator:
    def __init__(self, diesel, casetas, sueldo, mantenimiento, riesgo, administracion, utilidad_pct=0.18):
        self.diesel = diesel
        self.casetas = casetas
        self.sueldo = sueldo
        self.mantenimiento = mantenimiento
        self.riesgo = riesgo
        self.administracion = administracion
        self.utilidad_pct = utilidad_pct

    def costo_operativo(self):
        return (
            self.diesel +
            self.casetas +
            self.sueldo +
            self.mantenimiento +
            self.riesgo +
            self.administracion
        )

    def tarifa_spot_final(self):
        cpk = self.costo_operativo()
        utilidad = cpk * self.utilidad_pct
        return round(cpk + utilidad, 2)

# Ejemplo de uso:
# calc = FreightMetricsCalculator(
#     diesel=11.40,
#     casetas=5.40,
#     sueldo=4.50,
#     mantenimiento=3.00,
#     riesgo=1.60,
#     administracion=1.20,
#     utilidad_pct=0.18
# )
# print(calc.tarifa_spot_final())
