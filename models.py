from main import db

class encurta_link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String)
    link_encurtado = db.Column(db.String)

    def __repr__(self):
        return self.link