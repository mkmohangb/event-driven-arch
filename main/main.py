from dataclasses import dataclass
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from producer import publish
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)

@dataclass
class Product(db.Model):
    id: int
    title: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

@dataclass
class ProductUser(db.Model):
    user_id: int
    product_id: int

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    __table_args__ = (db.UniqueConstraint('user_id', 'product_id'),)


@app.route('/api/products')
def index():
    return jsonify(Product.query.all())

@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get("http://docker.for.mac.localhost:8000/api/user")
    data = req.json()
    try:
        productUser = ProductUser(user_id = data['id'],
                                  product_id = id)
        db.session.add(productUser)
        db.session.commit()

        publish('product_liked', id)
    except Exception as e:
        print("exception is ", repr(e), flush=True)
        abort(400, 'You already liked this product')

    return jsonify({"message": "success"})



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
