import sqlite3
import sys

def search_user(username):
    print("[1] Conectando a la base de datos 'users.db'...")
    input("Presiona Enter para continuar...")
    conn = sqlite3.connect("users.db")
    print("[2] Creando cursor para ejecutar consultas...")
    input("Presiona Enter para continuar...")
    cursor = conn.cursor()
    print("[3] Preparando consulta SQL vulnerable (concatenando el nombre de usuario)...")
    input("Presiona Enter para continuar...")
    query = "SELECT * FROM users WHERE name = '" + username + "';"
    print(f"Consulta generada: {query}")
    input("Presiona Enter para ejecutar la consulta...")
    cursor.execute(query)
    print("[4] Obteniendo resultados de la consulta...")
    input("Presiona Enter para continuar...")
    results = cursor.fetchall()
    print("[5] Resultados:")
    print(results)
    input("Presiona Enter para cerrar la conexión...")
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python vulnerable.py <username>")
    else:
        search_user(sys.argv[1])
