__author__ = 'hooper-p'

from flask import Flask, jsonify, request, abort
import uuid

# Configuration
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return 'Hello, World'


class Bike(object):
    def __init__(self, brand, model, price, _id=None):
        self.brand = brand
        self.model = model
        self.price = price
        self._id = uuid.uuid4().hex if _id is None else _id

    def json(self):
        return {
            "brand": self.brand,
            "model": self.model,
            "price": self.price,
            "_id": self._id
        }


bikes = []


@app.route('/bikeapp/api/v1/bikes', methods=['GET'])
def get_bikes():
    return jsonify({'bikes': bikes})


@app.route('/bikeapp/api/v1/bikes/<string:bike_id>', methods=['GET'])
def get_bike(bike_id):
    bike = [bike for bike in bikes if bike['_id'] == bike_id]
    if len(bike) == 0:
        abort(404)
    return jsonify({'bike': bike[0]})


@app.route('/bikeapp/api/v1/bikes', methods=['POST'])
def create_bike():
    bike = Bike(brand=request.json['brand'], model=request.json['model'], price=request.json['price'])
    bikes.append(bike.json())

    return jsonify(bike.json()), 201


@app.route('/bikeapp/api/v1/bikes/<string:bike_id>', methods=['PUT'])
def update_bike(bike_id):
    bike = [bike for bike in bikes if bike['_id'] == bike_id]
    if len(bike) == 0:
        abort(404)
    else:
        bike[0]['brand'] = request.json['brand']
        bike[0]['model'] = request.json['model']
        bike[0]['price'] = request.json['price']
        return jsonify({'bike': bike[0]})


@app.route('/bikeapp/api/v1/bikes/<string:bike_id>', methods=['DELETE'])
def delete_bike(bike_id):
    bike = [bike for bike in bikes if bike['_id'] == bike_id]
    if len(bike) == 0:
        abort(404)
    bikes.remove(bike[0])
    return jsonify({'result': True})

