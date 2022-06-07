from flask import Flask, request, jsonify
from datetime import datetime
import pickle

app = Flask(__name__)


@app.route('/hello')
def hello_func():
    name = request.args.get('name')
    return f'hello {name}!'


@app.route('/time')
def current_time():
    time = datetime.now()
    return {'time': time}


@app.route('/add', methods=['POST'])
def add_func():
    print('request.data: ', request.data)
    num = request.json.get('num')
    if num > 10:
        return jsonify('too much'), 400
    return jsonify({'result': num + 1})


@app.route('/predict', methods=['POST'])
def predict_func():
    print('request.data: ', request.data)
    with open('hw1.pkl', 'rb') as f:
        model = pickle.load(f)
    y_pred = model.predict([request.json])
    print(y_pred)
    return {"prediction": y_pred[0]}

if __name__ == '__main__':
    app.run('localhost', 5000)
