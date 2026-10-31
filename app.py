import mysql.connector
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def check_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",               # Tu usuario
            password="",               # Tu contraseña
            database="control_escolar" # Tu base de datos
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 1;")
        
        # Leemos el resultado para limpiar el buffer del cursor
        cursor.fetchall()
        
        cursor.close()
        conn.close()
        return True, "¡Conexión exitosa a la base de datos 'control_escolar'!"
    except Exception as e:
        return False, f"Error al conectar con la base de datos: {str(e)}"
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/check-db")
def api_check_db():
    success, message = check_db_connection()
    return jsonify({"success": success, "message": message})

if __name__ == "__main__":
    app.run(debug=True)