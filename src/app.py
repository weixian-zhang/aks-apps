from flask import Flask, request, jsonify

app = Flask(__name__)

# Route for the home page
@app.route('/alive')
def home():
    return "alive", 200

# Route for the hello page
@app.route('/ready')
def hello():
    return "ready", 200

# # Route for a dynamic hello page
# @app.route('/hello/<name>')
# def hello_name(name):
#     return f"Hello, {name}!"

# # Route for handling GET and POST requests
# @app.route('/greet', methods=['GET', 'POST'])
# def greet():
#     if request.method == 'POST':
#         data = request.get_json()
#         name = data.get('name', 'World')
#         return jsonify(message=f"Hello, {name}!")
#     else:
#         name = request.args.get('name', 'World')
#         return jsonify(message=f"Hello, {name}!")

if __name__ == '__main__':
    app.run(debug=True)
