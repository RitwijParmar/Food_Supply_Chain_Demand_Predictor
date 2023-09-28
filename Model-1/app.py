import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="numpy")


from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import joblib


from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

    
@app.route('/show')
def show():
    return render_template('forecast_plot.html')




if __name__=='__main__':
    app.run(debug=True)
