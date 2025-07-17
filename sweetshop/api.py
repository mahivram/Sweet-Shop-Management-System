from flask import Flask, request, jsonify
from sweetshop.shop import SweetShop
from sweetshop.models import Sweet
from sweetshop.exceptions import SweetAlreadyExistsError, SweetNotFoundError, InsufficientStockError
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- Add this block ---
@app.after_request
def add_cors_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
# ----------------------

shop = SweetShop()
@app.route('/<path:path>', methods=['OPTIONS'])
def options_handler(path):
    return '', 200

@app.route('/sweets', methods=['GET'])
def get_sweets():
    return jsonify(shop.view_sweets())

@app.route('/sweets', methods=['POST'])
def add_sweet():
    data = request.json
    try:
        sweet = Sweet(
            sweet_id=int(data['id']),
            name=data['name'],
            category=data['category'],
            price=float(data['price']),
            quantity=int(data['quantity'])
        )
        shop.add_sweet(sweet)
        return jsonify({'message': 'Sweet added!'}), 201
    except SweetAlreadyExistsError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/sweets/<int:sweet_id>', methods=['DELETE'])
def delete_sweet(sweet_id):
    try:
        shop.delete_sweet(sweet_id)
        return jsonify({'message': 'Sweet deleted!'})
    except SweetNotFoundError as e:
        return jsonify({'error': str(e)}), 404

@app.route('/sweets/search', methods=['GET'])
def search_sweets():
    name = request.args.get('name')
    category = request.args.get('category')
    price_min = request.args.get('price_min', type=float)
    price_max = request.args.get('price_max', type=float)
    results = shop.search_sweets(name=name, category=category, price_min=price_min, price_max=price_max)
    return jsonify(results)

@app.route('/sweets/sort', methods=['GET'])
def sort_sweets():
    by = request.args.get('by', 'name')
    reverse = request.args.get('reverse', 'false').lower() == 'true'
    try:
        results = shop.sort_sweets(by=by, reverse=reverse)
        return jsonify(results)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/sweets/<int:sweet_id>/purchase', methods=['POST'])
def purchase_sweet(sweet_id):
    data = request.json
    quantity = int(data.get('quantity', 1))
    try:
        shop.purchase_sweet(sweet_id, quantity)
        return jsonify({'message': 'Purchase successful!'})
    except (SweetNotFoundError, InsufficientStockError) as e:
        return jsonify({'error': str(e)}), 400

@app.route('/sweets/<int:sweet_id>/restock', methods=['POST'])
def restock_sweet(sweet_id):
    data = request.json
    quantity = int(data.get('quantity', 1))
    try:
        shop.restock_sweet(sweet_id, quantity)
        return jsonify({'message': 'Restock successful!'})
    except SweetNotFoundError as e:
        return jsonify({'error': str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)
