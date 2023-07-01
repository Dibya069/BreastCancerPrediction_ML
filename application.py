from flask import Flask, request, render_template, jsonify, send_file
from src.exception import CustomException
import sys

from src.pipe.predict_pipeline import PredictPipelines

application = Flask(__name__)

app=application

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    try:
        if request.method == "POST":
            data = dict(request.form.items())
            print(data)
            return jsonify("done")
    except Exception as e:
        raise CustomException(e,sys)

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)