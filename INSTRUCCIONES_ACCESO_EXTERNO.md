# CONFIGURACIÓN DE NGROK PARA FREIGHTMETRICS

## ✅ CONFIGURACIÓN COMPLETADA
- Token configurado: 3AXJ***Y1v5D4oKn (zvicente90@gmail.com)
- URL Actual: https://crew-jural-tellingly.ngrok-free.dev
- Panel Web: http://127.0.0.1:4040

## 🚀 ACCESO RÁPIDO
Usar el script automatizado:
```bash
start_public_access.bat
```

## 🔧 COMANDOS MANUALES

### Iniciar túnel público:
```bash
ngrok http 8501
```

### URLs disponibles:
- **Internet**: https://crew-jural-tellingly.ngrok-free.dev (cambia al reiniciar)
- **Red local**: http://192.168.1.23:8501
- **Localhost**: http://localhost:8501

## 📊 MONITOREO
Panel de control ngrok: http://127.0.0.1:4040
- Ver conexiones en tiempo real
- Obtener nueva URL si cambió
- Estadísticas de uso

## ⚠️ NOTAS IMPORTANTES:
- URL pública cambia cada vez que reinicias ngrok
- Plan gratuito: límite de conexiones simultáneas
- Para URL fija: necesitas plan de pago
- El túnel funciona mientras ngrok esté ejecutándose

## ALTERNATIVA: Usar localtunnel
Si ngrok da problemas:
```bash
npm install -g localtunnel
lt --port 8501 --subdomain freightmetrics
```
URL: https://freightmetrics.loca.lt