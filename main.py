import os
import model
import manage
from flask import Flask, request, jsonify

app = Flask(__name__)
csv = 'main.csv'
cache = 'cache'
threshold = 0.6

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    sex = request.form['sex']
    sno = request.form['sno']
    photo = request.form['photo']
    college = request.form['college']
    signed = request.form['signed']
    manage.add(csv, name, sex, sno, photo, college, signed)
    model.init(csv, cache)

@app.route('/delete', methods=['POST'])
def delete():
    sno = request.form['sno']
    manage.delete(csv, sno)

@app.route('/photo', methods=['POST'])
def photo():
    path = request.form['path']
    result = model.test(path, threshold)
    if result is not None:
        return jsonify({'result': list(result)})
    else:
        return jsonify({'result': None})

@app.route('/manual', methods=['POST'])
def manual():
    sno = request.form['sno']
    manage.manual(csv, sno)

@app.route('/all', methods=['POST'])
def all():
    return jsonify({'result': manage.all(csv)})

@app.route('/signed', methods=['POST'])
def signed():
    return jsonify({'result': manage.signed(csv)})

if __name__ == '__main__':
    if not os.path.exists(csv):
        open(csv, "w").close()
    model.init(csv, cache)
    app.run(debug=True)