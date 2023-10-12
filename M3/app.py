import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="numpy")


from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import joblib
import plotly.express as px
import plotly.offline as pyo

from flask import render_template


from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

app=Flask(__name__)
import joblib
model_SARIMA_fit=joblib.load('./SARIMA')
model_Arima_fit=joblib.load('./ARIMA')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    if request.method =='GET':
        return render_template('home.html')
    else:
        data=int(request.form.get('data'))
        datas=pd.read_csv('traindata.csv')
        test=datas.iloc[139:144]

        

        forecast_steps = data
        arima_forecast = model_Arima_fit.get_forecast(steps=forecast_steps)
        sarima_forecast = model_SARIMA_fit.get_forecast(steps=forecast_steps)

        # Get predicted values from both models
        arima_predicted_values = arima_forecast.predicted_mean
        sarima_predicted_values = sarima_forecast.predicted_mean

        # Create DataFrames for both models
        arima_forecast_df = pd.DataFrame({
            'weeks': range(140, 140 + forecast_steps),
            'Predicted_ARIMA': arima_predicted_values
        })


        # Merge DataFrames on the 'weeks' column
        combined_forecast_df = pd.merge(arima_forecast_df, on='weeks')


        
        test=test[['week','num_orders']]
        # Assuming combined_forecast_df is already defined
        fig = px.line(combined_forecast_df, x='weeks', y=['Predicted_ARIMA', 'Predicted_SARIMA'],
              labels={'value': 'Predicted No of Orders', 'weeks': 'Weeks'},
              title='Combined ARIMA and SARIMA Forecast',
              color_discrete_map={'Predicted_ARIMA': 'violet', 'Predicted_SARIMA': 'orange'})

# Add actual predictions from the test DataFrame with a different color
        fig.add_trace(px.line(test, x='week', y='num_orders', color_discrete_map={'num_orders': 'orange'}).data[0])



        
            
        # Show the plot
        html_file_path = "./templates/forecast_plot.html"
        pyo.plot(fig, filename=html_file_path, auto_open=False)


        # Convert Plotly figure to HTML
        #plot_html = pyo.plot(fig, include_plotlyjs=False, output_type='div')

        plot_html = fig.to_html(full_html=False)

        # Render the template with the HTML of the Plotly graph
        return render_template('home.html', results=data, plot_html=plot_html)

    
@app.route('/show')
def show():
    return render_template('forecast_plot.html')




if __name__=='__main__':
    app.run(debug=True)
