@echo off
cd /d "C:\Users\Vicente Sanchez\Documents\VICENTE DOCKER\freightmetrics_mvp"
call .venv\Scripts\activate.bat
echo Iniciando FreightMetrics con acceso externo...
echo.
echo URLs de acceso:
echo - Local: http://localhost:8501
echo - Red: http://192.168.1.23:8501
echo.
echo Para usuarios externos, comparte: http://192.168.1.23:8501
echo (Solo funciona si están en tu misma red WiFi)
echo.
streamlit run app.py --server.address=0.0.0.0 --server.port=8501