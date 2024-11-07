from prj import app, db


class Contact(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50),nullable = False)
    email = db.Column(db.String(60),nullable = False)
    subject = db.Column(db.Text, nullable = False)
    message = db.Column(db.Text, nullable = False)
    
with app.app_context():
    db.create_all()