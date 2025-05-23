from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import db
from routes.fermentations import fermentation_bp

app = Flask(__name__)

# Configuración de la base de datos (ajustá esto a tu conexión)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:contraseña@localhost/nombre_basedatos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar base de datos
db.init_app(app)

# Registrar blueprint de fermentation
app.register_blueprint(fermentation_bp)

# Crear las tablas
with app.app_context():
    db.create_all()

# Iniciar la app
if __name__ == '__main__':
    app.run(debug=True)
