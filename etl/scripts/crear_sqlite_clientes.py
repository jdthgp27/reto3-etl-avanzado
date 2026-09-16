"""
Crea una base de datos SQLite con datos de clientes para el Reto 3.
"""
import sqlite3
import random
import numpy as np
from pathlib import Path

RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)

DB_PATH = Path(__file__).parent.parent.parent / "data" / "raw" / "sql" / "clientes.db"

# Conectar (lo crea si no existe)
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    cliente_id TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL,
    edad INTEGER,
    genero TEXT,
    pais TEXT,
    ciudad TEXT,
    fecha_registro TEXT,
    tipo_cliente TEXT,
    ingresos_anuales INTEGER
)
""")

# Limpiar por si ya existe
cursor.execute("DELETE FROM clientes")

# Generar datos
NOMBRES = ["Ana", "Luis", "María", "Carlos", "Lucía", "Javier", "Sofía", "Pablo",
           "Elena", "David", "Carmen", "Miguel", "Laura", "Sergio", "Marta"]
APELLIDOS = ["García", "López", "Martín", "Sánchez", "Rodríguez", "Fernández",
             "Gómez", "Ruiz", "Díaz", "Moreno", "Álvarez", "Romero"]
CIUDADES = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao",
            "Málaga", "Zaragoza", "Murcia", "Palma", "Alicante"]
PAISES = ["España", "Portugal", "Francia", "Italia", "Alemania"]
TIPOS = ["Nuevo", "Recurrente", "VIP", "Inactivo"]

filas = []
for i in range(1, 2001):  # 2000 clientes
    nombre = f"{random.choice(NOMBRES)} {random.choice(APELLIDOS)}"
    ciudad = random.choice(CIUDADES)
    filas.append((
        f"CLI-{i:05d}",
        nombre,
        f"cliente{i}@email.com",
        int(np.random.randint(18, 75)),
        random.choice(["M", "F", "Otro"]),
        random.choice(PAISES),
        ciudad,
        f"202{random.randint(0, 3)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
        random.choices(TIPOS, weights=[30, 45, 10, 15])[0],
        int(np.random.choice([20000, 30000, 45000, 60000, 80000, 120000])),
    ))

cursor.executemany("INSERT INTO clientes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", filas)
conn.commit()

# Verificar
cursor.execute("SELECT COUNT(*) FROM clientes")
total = cursor.fetchone()[0]
print(f"✅ Base de datos creada: {DB_PATH}")
print(f"   {total} clientes insertados")

cursor.execute("SELECT * FROM clientes LIMIT 3")
for row in cursor.fetchall():
    print(f"   {row}")

conn.close()