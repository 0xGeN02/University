import os
import requests
import zipfile
from datetime import datetime, timedelta

# Configuración
SYMBOL = "BTCUSDT"
INTERVAL = "1h"
START_YEAR = 2019
end_year = datetime.now().year
OUTPUT_DIR = "binance_data"
BASE_URL = "https://data.binance.vision/data/spot/daily/klines/{symbol}/{interval}/{symbol}-{interval}-{date}.zip"

# Crear directorio de salida si no existe
os.makedirs(OUTPUT_DIR, exist_ok=True)

def download_and_extract(url, output_path):
    """Descarga y extrae un archivo ZIP."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        zip_path = os.path.join(output_path, url.split("/")[-1])
        with open(zip_path, "wb") as f:
            f.write(response.content)

        # Extraer el archivo ZIP
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(output_path)

        # Eliminar el archivo ZIP después de extraerlo
        os.remove(zip_path)
        print(f"Descargado y extraído: {url}")
    else:
        print(f"Error al descargar: {url} (Status code: {response.status_code})")

# Generar fechas desde el inicio hasta hoy
def generate_dates(start_year, end_year):
    current_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    while current_date <= end_date:
        yield current_date.strftime("%Y-%m-%d")
        current_date += timedelta(days=1)

# Descargar y extraer todos los archivos
for date in generate_dates(START_YEAR, end_year):
    url = BASE_URL.format(symbol=SYMBOL, interval=INTERVAL, date=date)
    try:
        download_and_extract(url, OUTPUT_DIR)
    except requests.exceptions.RequestException as e:
        print(f"Error de red al procesar {url}: {e}")
    except FileNotFoundError as e:
        print(f"Error de archivo no encontrado al procesar {url}: {e}")
    except Exception as e:
        print(f"Error procesando {url}: {e}")

print("Proceso completado.")
