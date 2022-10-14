import os
import model
import manage
from flask import Flask, request, jsonify

app = Flask(__name__)
csv = 'main.csv'
tmp = 'tmp.png'
cache = 'cache'
threshold = 0.6

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    sex = request.form['sex']
    sno = request.form['sno']
    college = request.form['college']
    photo = request.form['photo']
    manage.add(csv, name, sex, sno, college, photo, cache, tmp)
    model.init(csv, cache)
    return jsonify({'result': None})

@app.route('/delete', methods=['POST'])
def delete():
    sno = request.form['sno']
    manage.delete(csv, sno)
    return jsonify({'result': None})

@app.route('/photo', methods=['POST'])
def photo():
    photo = request.form['photo']
    result = model.test(photo, threshold, tmp)
    if result is not None:
        return jsonify({'result': list(result)})
    else:
        return jsonify({'result': None})

@app.route('/manual', methods=['POST'])
def manual():
    sno = request.form['sno']
    manage.manual(csv, sno)
    return jsonify({'result': None})

@app.route('/all', methods=['POST'])
def all():
    return jsonify({'result': manage.all(csv)})

@app.route('/signed', methods=['POST'])
def signed():
    return jsonify({'result': manage.signed(csv)})

if __name__ == '__main__':
    if not os.path.exists(cache):
        os.makedirs(cache)
    if not os.path.exists(csv):
        open(csv, "w").close()
    model.init(csv, cache)
    app.run(debug=True)