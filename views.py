from flask import Flask, request

app = Flask(__name__)


@app.route('/chain/<data>', methods=['GET', 'POST'])
def post_chain(data):
    content = request.json
    return content['data']
