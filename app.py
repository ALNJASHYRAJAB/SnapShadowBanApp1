
from flask import Flask, request, jsonify
from shadowban_checker import check_shadowban

app = Flask(__name__)

@app.route('/analyze', methods=['GET'])
def analyze():
    username = request.args.get('username')
    if not username:
        return jsonify({'error': 'Missing username'}), 400

    result = check_shadowban(username)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
