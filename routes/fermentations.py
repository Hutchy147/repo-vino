from flask import Blueprint, render_template, request, redirect, url_for
from database import db
from models.fermentation import Fermentation
from datetime import datetime

fermentation_bp = Blueprint('fermentation', __name__, url_prefix='/fermentation')

@fermentation_bp.route('/')
def index():
    fermentations = Fermentation.query.all()
    return render_template('fermentation/index.html', fermentations=fermentations)

@fermentation_bp.route('/new')
def new():
    return render_template('fermentation/new.html')

@fermentation_bp.route('/create', methods=['POST'])
def create():
    try:
        fermentation = Fermentation(
            reception_id=request.form['reception_id'],
            start_date=datetime.strptime(request.form['start_date'], '%Y-%m-%d'),
            end_date=datetime.strptime(request.form['end_date'], '%Y-%m-%d') if request.form['end_date'] else None,
            temperature=float(request.form['temperature']) if request.form['temperature'] else None,
            acidity=float(request.form['acidity']) if request.form['acidity'] else None,
            ph=float(request.form['ph']) if request.form['ph'] else None,
            notes=request.form['notes']
        )
        db.session.add(fermentation)
        db.session.commit()
        return redirect(url_for('fermentation.index'))
    except Exception as e:
        print(f"Error al crear: {e}")
        return "Error al crear la fermentación"

@fermentation_bp.route('/edit/<string:id>')
def edit(id):
    fermentation = Fermentation.query.get_or_404(id)
    return render_template('fermentation/edit.html', fermentation=fermentation)

@fermentation_bp.route('/update/<string:id>', methods=['POST'])
def update(id):
    fermentation = Fermentation.query.get_or_404(id)
    try:
        fermentation.reception_id = request.form['reception_id']
        fermentation.start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
        fermentation.end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d') if request.form['end_date'] else None
        fermentation.temperature = float(request.form['temperature']) if request.form['temperature'] else None
        fermentation.acidity = float(request.form['acidity']) if request.form['acidity'] else None
        fermentation.ph = float(request.form['ph']) if request.form['ph'] else None
        fermentation.notes = request.form['notes']

        db.session.commit()
        return redirect(url_for('fermentation.index'))
    except Exception as e:
        print(f"Error al actualizar: {e}")
        return "Error al actualizar la fermentación"

@fermentation_bp.route('/delete/<string:id>', methods=['POST'])
def delete(id):
    fermentation = Fermentation.query.get_or_404(id)
    try:
        db.session.delete(fermentation)
        db.session.commit()
        return redirect(url_for('fermentation.index'))
    except Exception as e:
        print(f"Error al eliminar: {e}")
        return "Error al eliminar la fermentación"
