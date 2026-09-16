"""
Reduce el CSV de Online Retail a las primeras N filas para hacer
el flujo NiFi manejable.
"""
import pandas as pd
from pathlib import Path

# Rutas
BASE = Path(__file__).parent.parent.parent
ORIGEN = BASE / "data" / "raw" / "csv" / "OnlineRetail.csv"
DESTINO = BASE / "data" / "raw" / "csv" / "OnlineRetail_10k.csv"

# Leer solo las primeras 10.000 filas
print(f"📖 Leyendo {ORIGEN}...")
df = pd.read_csv(ORIGEN, nrows=10000, encoding="ISO-8859-1")
print(f"   → {len(df)} filas leídas")

# Guardar
df.to_csv(DESTINO, index=False, encoding="utf-8")
print(f"✅ Guardado: {DESTINO}")
print(f"   Tamaño: {DESTINO.stat().st_size / 1024:.2f} KB")
print(f"\nColumnas: {list(df.columns)}")
print(f"\nPrimeras filas:")
print(df.head(3))