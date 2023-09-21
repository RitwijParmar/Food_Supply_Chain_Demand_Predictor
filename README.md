# Food Supply Chain Demand Predictor

## Overview

The Food Supply Chain Demand Predictor is a Flask web application designed to forecast food demand using ARIMA and SARIMA time series models. This tool enables users to predict the number of food orders for a specified number of weeks into the future, based on historical data.

## Features

- Forecast food demand using pre-trained ARIMA and SARIMA models.
- Visualize the predicted demand alongside actual historical data.
- Interactive web interface for input and result visualization.

## Prerequisites

- Python 3.x
- Flask
- NumPy
- Pandas
- Joblib
- Plotly
- Statsmodels

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/food-supply-chain-demand-predictor.git
    cd food-supply-chain-demand-predictor
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Open a web browser and navigate to `http://127.0.0.1:5000/`.

3. Use the interface to input the number of weeks for which you want to forecast the demand.

## File Structure

- `app.py`: Main application script.
- `templates/`: Directory containing HTML templates.
  - `index.html`: Main page.
  - `home.html`: Prediction input and result page.
  - `forecast_plot.html`: Page displaying the forecast plot.
- `requirements.txt`: List of required Python packages.
- `traindata.csv`: Historical training data.

## Code Explanation
### Loading Pre-trained Models
These lines load pre-trained SARIMA and ARIMA models using `joblib`.

### Defining Routes

#### Index Route
This defines the root route (`/`) which renders the `index.html` template.

#### Show Route
This route (`/show`) renders the `forecast_plot.html` template.

### Running the Flask Application


This runs the Flask application with debug mode enabled.
