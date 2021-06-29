from datetime import datetime
from config import db, ma

class Record(db.Model):
    __tablename__ = 'records'
    id = db.Column(db.Integer, primary_key=True)
    measurement = db.Column(db.String(64))
    location = db.Column(db.String(64))     
    value = db.Column(db.String(64))
    unit = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime, 
                        default=datetime.utcnow, 
                        onupdate=datetime.utcnow, index=True)

    def __repr__(self):
        return '<Record {}/{}:{}>'.format(self.measurement,self.location,self.value)  
        
class RecordSchema(ma.ModelSchema):
    class Meta:
        model = Record
        sqla_session = db.session