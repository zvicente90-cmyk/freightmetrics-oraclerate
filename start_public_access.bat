@echo off
echo ========================================
echo   FREIGHTMETRICS - ACCESO PUBLICO
echo ========================================
echo.
echo Verificando servicios...

cd /d "C:\Users\Vicente Sanchez\Documents\VICENTE DOCKER\freightmetrics_mvp"
call .venv\Scripts\activate.bat

echo.
echo Iniciando FreightMetrics con acceso publico...
echo.
echo URLS DE ACCESO:
echo [LOCAL]     http://localhost:8501
echo [RED LOCAL] http://192.168.1.23:8501  
echo [INTERNET]  https://crew-jural-tellingly.ngrok-free.dev
echo.
echo NOTA: La URL de internet cambia cada vez que reinicias
echo Para obtener la nueva URL, ve al panel: http://127.0.0.1:4040
echo.
echo Presiona Ctrl+C en cualquier momento para detener
echo.

start "" http://127.0.0.1:4040
timeout /t 3 >nul

echo Iniciando Streamlit...
start /b streamlit run app.py --server.address=0.0.0.0 --server.port=8501

timeout /t 5 >nul

echo Iniciando tunel publico ngrok...
ngrok http 8501