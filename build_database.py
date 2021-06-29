import os
from config import db
from models import Record


records = [
    {
        'id': 1,
        'measurement': u'1.2',
        'location': u'daniels room',
        'unit': u'`c'
    },
    {
        'id': 2,
        'measurement': u'1.3',
        'location': u'daniels room',
        'unit': u'`c'
    },
    {
        'id': 3,
        'measurement': u'1.4',
        'location': u'daniels room',
        'unit': u'`c'
    }
]

# Delete database file if it exists currently
if os.path.exists("records.db"):
    os.remove("records.db")


# Create the database
db.create_all()

for record in records:
    t = Record(measurement=record.get("measurement"), location=record.get("location"), value=record.get("value"), unit=record.get("unit"))
    db.session.add(t)

db.session.commit()