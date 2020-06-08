#importing libraries
import os
import numpy as np
import flask
import pickle
import plotly
import plotly.graph_objects as go 
import chart_studio.plotly as py 
import json
import pandas as pd

from flask import Flask, render_template, request
from datetime import time

#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
# @app.route('/index')
def index():
    return flask.render_template('index.html')

@app.route('/tentang')
def tentang():
    return flask.render_template('tentang.html')

@app.route('/grafik')
def grafik():
    # fn = secure_filename(myFile.filename)
    # df = pd.read_csv(fn)

    df = pd.read_csv('data.csv')
    x = np.array(list(df['Tanggal']))
    y = np.array(list(df['Jumlah Ch']))
    plot = go.Scatter(x=x, y=y)

    plot = [plot]
    plotJSON = json.dumps(plot, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('grafik.html', x=plotJSON)

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,3)
    loaded_model = pickle.load(open("model.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)

        if int(result)>500:
            prediction='Terjadi potensi banjir'
        else:
            prediction='Tidak terjadi potensi banjir'
        return render_template("result.html",prediction=prediction, result=result)