from flask import Flask, request, render_template, jsonify
from src.pipe.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app=application

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('prediction.html')
    
    else:
        data = CustomData(
            mean_radius = float(request.form.get('mean radius')),
            mean_texture = float(request.form.get('mean texture')),
            mean_perimeter = float(request.form.get('mean perimeter')),
            mean_area = float(request.form.get('mean area')),
            mean_smoothness = float(request.form.get('mean smoothness')),
            mean_compactness = float(request.form.get('mean compactness')),
            mean_concavity = float(request.form.get('mean concavity')),
            mean_concave_points = float(request.form.get('mean concave points')),
            mean_symmetry = float(request.form.get('mean symmetry')),
            mean_fractal_dimension = float(request.form.get('mean fractal dimension')),
            radius_error = float(request.form.get('radius error')),
            texture_error = float(request.form.get('texture error')),
            perimeter_error = float(request.form.get('perimeter error')),
            area_error = float(request.form.get('area error')),
            smoothness_error = float(request.form.get('smoothness error')),
            compactness_error = float(request.form.get('compactness error')),
            concavity_error = float(request.form.get('concavity error')),
            concave_points_error = float(request.form.get('concave points error')),
            symmetry_error = float(request.form.get('symmetry error')),
            fractal_dimension_error = float(request.form.get('fractal dimension error')),
            worst_radius = float(request.form.get('worst radius')),
            worst_texture = float(request.form.get('worst texture')),
            worst_perimeter = float(request.form.get('worst perimeter')),
            worst_area = float(request.form.get('worst area')),
            worst_smoothness = float(request.form.get('worst smoothness')),
            worst_compactness = float(request.form.get('worst compactness')),
            worst_concavity = float(request.form.get('worst concavity')),
            worst_concave_points = float(request.form.get('worst concave points')),
            worst_symmetry = float(request.form.get('worst symmetry')),
            worst_fractal_dimension = float(request.form.get('worst fractal dimension'))
        )
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=predict_pipeline()
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)

        return render_template('predicttion.html',final_result=results)
    

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)