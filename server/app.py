from flask import Flask
from flask import request
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pickle


app = Flask(__name__)


# fn to calculate grade
def getGrade(s):
    if s <= 35:
        return "F"
    elif s <= 45:
        return "D"
    elif s <= 65:
        return "C"
    elif s <= 85:
        return "B"
    else:
        return "A"


def result(s):
    res = (s/300)*100
    return res


def load_model():
    with open(r"C:/Users/BENAIAH/Desktop/Ben/AI/Project/server/model.pkl", 'rb') as f:
        model = pickle.load(f)
    return model


@app.route('/', methods=['POST'])
def index():
    try:
        # Load model from file
        model = load_model()
        maths = request.form.get("maths")
        reading = request.form.get("reading")
        writing = request.form.get("writing")
        # Make prediction
        print(model)
        pred = model.predict([[maths, reading, writing]])
        score = result(pred[0][0])
        grade = getGrade(score)
        return {"score": float("{0:.2f}".format(score)), "grade": grade}, 200
    except Exception as e:
        print(e)
        return f"Error: {e}", 500



if __name__ == '__main__':
    app.run()
