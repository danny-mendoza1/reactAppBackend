from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static')

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


@app.route('/signup', methods=['POST'])
def signup():
    user_data = request.get_json()  # Get the JSON data sent by the client

    # Here, you would typically validate the user data and add it to your database.
    # Since we're not connecting to a database yet, we'll just print the data to the console.

    print(user_data)

    return jsonify({"message": "User signed up successfully"}), 201


if __name__ == "__main__":
    app.run(debug=True, port=3001)
