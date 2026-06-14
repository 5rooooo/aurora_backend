from aurora.extensions import db

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False, default="")
    price = db.Column(db.Float, nullable=False, default=0)
    tag = db.Column(db.String(50), nullable=True)
    type = db.Column(db.String(20), nullable=False, default="product")  # product / recipe / story
    image_url = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f"<Product {self.id} {self.title}>"
