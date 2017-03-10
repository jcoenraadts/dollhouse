import time
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    content = {
        'name': 'A girly dolls house',
        'title': 'DollsHouse'
    }
    return render_template('index.html', content=content)


@app.route('/temp/', methods=['GET'])
def get_temperature():
    #measure temp
    temp = time.time()
    return jsonify({
        'status': 'ok',
        'temp': temp
    })


@app.route('/gpio/', methods=['POST'])
def set_gpio(): 
    content = request.json
    print (content)
    
    # do the gpio thing
    return jsonify({
        'status': 'ok'
    })


if __name__ == "__main__":
    app.run(debug=True)
