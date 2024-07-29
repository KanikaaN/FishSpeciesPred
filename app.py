from flask import Flask, render_template, request
from predict import predict_species
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extracting inputs from the form
            length1 = float(request.form['length1'])
            length2 = float(request.form['length2'])
            length3 = float(request.form['length3'])
            height = float(request.form['height'])
            width = float(request.form['width'])
            
            # Call the predict_species function with the correct number of arguments
            prediction = predict_species(length1, length2, length3, height, width)
            
            return render_template('result.html', prediction=prediction)
        except ValueError:
            return render_template('index.html', error="Please enter valid numbers for all fields.")
        except Exception as e:
            # Log the error or show a user-friendly message
            return render_template('index.html', error=f"An error occurred: {e}")
    return render_template('index.html')

if __name__ == '__main__':
    # Accessing the PORT environment variable
    port = int(os.environ.get("PORT", 17995))
    app.run(host='0.0.0.0', port=port)