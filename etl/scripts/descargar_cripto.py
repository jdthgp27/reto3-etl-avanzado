"""
Descarga datos de CoinGecko API y los guarda como JSON.
"""
import requests
import json
from pathlib import Path
from datetime import datetime

URL_BASE = "https://api.coingecko.com/api/v3"
SALIDA = Path(__file__).parent.parent.parent / "data" / "raw" / "api"

def descargar(endpoint, params=None, nombre=None):
    url = f"{URL_BASE}/{endpoint}"
    print(f"🌐 Descargando: {url}")
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    data = r.json()

    archivo = SALIDA / (nombre or f"{endpoint.replace('/', '_')}.json")
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✅ Guardado: {archivo}")
    return data

# 1. Precio actual
descargar("simple/price",
          {"ids": "bitcoin,ethereum,cardano,solana", "vs_currencies": "usd,eur"},
          "cripto_precios_actuales.json")

# 2. Serie temporal de los últimos 90 días
descargar("coins/bitcoin/market_chart",
          {"vs_currency": "usd", "days": 90, "interval": "daily"},
          "bitcoin_historico_90d.json")

# 3. Datos globales del mercado cripto
descargar("global", None, "cripto_global.json")

print("\n🎉 Descargas completadas")