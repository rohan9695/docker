import json
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


with open('restaurant.json') as json_data:
    d = json.load(json_data)
    list_of_foods = []
    for data in d['foods']:
    	list_of_foods.append(data)
    	


@app.route('/', methods =['GET'])
def test():
	return render_template("index.html")

@app.route('/foods', methods =['GET'])
def test1():
	return render_template("index.html",list_data=list_of_foods)

@app.route('/foods/<string:idd>', methods =['GET'])
def test2(idd):
    g1=[]
    for food in list_of_foods:
        if food['id'] == idd:
            g1.append(food)
        else:
            if idd == food['category']:
                g1.append(food)
    return render_template("index.html",list_data=g1)

if __name__ == '__main__':
	 app.run(debug=True, host='0.0.0.0')
