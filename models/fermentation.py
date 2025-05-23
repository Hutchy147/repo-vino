import uuid
from database import db

class Fermentation(db.Model):
    __tablename__= "fermentations"

    id = db.Column(db.String(40), primary_key = True, default = lambda: str(uuid.uuid4()))
    reception_id = db.Column(db.String(40), db.ForeignKey("grape_receptions.id"), nullable = False)

    start_date = db.Column(db.Date, nullable = False)
    end_date = db.Column(db.Datte, nullable = False)
    temperature = db.Column(db.Float, nullable = False)
    acidity = db.Column(db.Float, nullable = False)
    ph = db.Column(db.Float, nullable = False)
    notes = db.Column(db.Text, nullable = True)

    def __init__ (self, reception_id, start_date, end_date = None, 
        temperature = None, acidity = None, ph = None, notes = None):

        self.reception_id = reception_id
        self.start_date = start_date
        self.end_date = end_date
        self.temperature = temperature
        self.pf = ph
        self.notes = notes

    def serialize(self):
        return {
            "id": self.id,
            "reception_id": self.reception_id,
            "start_date": self.start_date.isoformat() if self.start_date else None,
            "end_date": self.end_date,
            "temperature": self.temperature,
            "acidity": self.acidity,
            "ph": self.ph,
            "notes": self.notes
        }