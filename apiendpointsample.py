#from flask import Flask, request, jsonify

#app = Flask(__name__)

#@app.route('/api/total', methods=['POST'])
#def total():
#    data = request.get_json()
#   numbers = data['numbers']
#    return jsonify({'total': sum(numbers)})

#if __name__ == '__main__':
#    app.run(debug=True)

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_total_endpoint(client):
    response = client.post('/api/total', json={'numbers': [1, 2, 3]})
    data = response.get_json()
    assert data['total'] == 6, 'API total calculation failed'

