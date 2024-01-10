from flask import Flask, request, render_template
from src.mlproject.pipelines.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Route for a home page
# @app.route('/')
# def index():
#     return render_template('test.html')

# Route for predicting data
@app.route('/', methods=['GET', 'POST'])
def predict_datapoint():
    
    if request.method == 'GET':
        return render_template('result.html')
    else:
        data = CustomData(
            age=float(request.form.get('age')),
            sex=request.form.get('sex'),
            bmi=float(request.form.get('bmi')),
            children=float(request.form.get('children')),
            smoker=request.form.get('smoker'),
            region=request.form.get('region')
        )
        pred_df = data.get_data_as_data_frame()

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        # Include the form values in the rendered template
        return render_template('result.html', results="{:.2f}".format(results[0]), age=data.age, sex=data.sex, bmi=data.bmi, children=data.children, smoker=data.smoker, region=data.region)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)




# http://127.0.0.1:5000/
