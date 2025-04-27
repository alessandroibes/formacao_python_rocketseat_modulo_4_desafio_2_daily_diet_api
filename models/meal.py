from database import db
from sqlalchemy.orm import relationship


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    date_time = db.Column(db.DateTime, nullable=False)
    is_on_the_diet = db.Column(db.Boolean, default=False)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = relationship("User", back_populates="meals")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "date_time": self.date_time.strftime("%Y-%m-%d %H:%M:%S"),
            "is_on_the_diet": self.is_on_the_diet,
            "id_user": self.id_user
        }
