from src.mlproject.exception import CustomException
from src.mlproject.logger import logging


from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig

from src.mlproject.components.data_transformation import DataTransformationConfig,DataTransformation

from src.mlproject.components.model_tranier import ModelTrainerConfig,ModelTrainer

import sys


from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.mlproject.pipelines.prediction_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            age=float(request.form.get('age')),
            sex=request.form.get('sex'),
            bmi=float(request.form.get('bmi')),
            children=float(request.form.get('children')),
            smoker=request.form.get('smoker'),
            region=request.form.get('region')


        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)        






# if __name__=="__main__":
#     logging.info("The execution has started")

#     try:
#         # #data_ingestion_config=DataIngestionConfig()
#         data_ingestion=DataIngestion()
#         train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

#         # data_transformation_config=DataTransformationConfig()
#         data_transformation=DataTransformation()
#         train_arr,test_arr,_=data_transformation.initiate_data_transormation(train_data_path,test_data_path)

#         # ## Model Training

#         model_trainer=ModelTrainer()
#         print(model_trainer.initiate_model_trainer(train_arr,test_arr))
#         # a = 1/00
        
#     except Exception as e:
#         logging.info("Custom Exception")
#         raise CustomException(e,sys)