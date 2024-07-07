'''
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
]

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        abort(404)
    return jsonify(item)

@app.route('/api/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    new_item["id"] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        abort(404)
    updated_data = request.get_json()
    item.update(updated_data)
    return jsonify(item)

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

'''

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_items(client):
    response = client.get('/api/items')
    data = response.get_json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 2

def test_get_item(client):
    response = client.get('/api/items/1')
    data = response.get_json()
    assert response.status_code == 200
    assert data["name"] == "Item 1"

def test_get_nonexistent_item(client):
    response = client.get('/api/items/999')
    assert response.status_code == 404

def test_create_item(client):
    response = client.post('/api/items', json={"name": "Item 3"})
    data = response.get_json()
    assert response.status_code == 201
    assert data["name"] == "Item 3"
    assert data["id"] == 3

def test_update_item(client):
    response = client.put('/api/items/1', json={"name": "Updated Item 1"})
    data = response.get_json()
    assert response.status_code == 200
    assert data["name"] == "Updated Item 1"

def test_update_nonexistent_item(client):
    response = client.put('/api/items/999', json={"name": "Nonexistent Item"})
    assert response.status_code == 404

def test_delete_item(client):
    response = client.delete('/api/items/1')
    assert response.status_code == 204

    response = client.get('/api/items/1')
    assert response.status_code == 404

def test_delete_nonexistent_item(client):
    response = client.delete('/api/items/999')
    assert response.status_code == 204
