from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')  # decorator
def home():
    return 'Home!'


@app.route('/get-user/<user_id>')
def get_user(user_id):
    user_data = {
        'user_id': user_id,
        'name': 'John Doe',
        'email': 'john@doe.com'
    }
    query = request.args.get('query')
    if query:
        user_data['query'] = query

    return jsonify(user_data), 200


# methods can have more http methods
@app.route('/create-user', methods=["POST"])
def create_user():
    # if(request.method == "POST") check from the array
    data = request.get_json()
    return jsonify(data), 201


if __name__ == "__main__":
    app.run(port=8000, debug=True)
