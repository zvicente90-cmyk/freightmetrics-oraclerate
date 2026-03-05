class MockLLM:
    def generate_content(self, prompt):
        # Simulación de respuesta de IA
        return type('obj', (object,), {'text': 'Análisis de auditoría simulado por IA para la ruta y tarifa proporcionadas.'})()
