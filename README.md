# Fish Species Prediction Project

## Overview
This project aims to predict the species of fish based on various measurements such as length, height, and width. The model uses a dataset of fish measurements and species to train a machine learning model, which is then used to make predictions on new data.

## Project Structure
- `app.py`: The main Flask application file that handles routing and user interactions.
- `predict.py`: Contains the function for making predictions using the trained model.
- `templates/`: Directory containing HTML templates for the web application.
  - `index.html`: The main page where users can input fish measurements.
  - `result.html`: The page that displays the predicted species.
- `model/`: Directory containing the trained machine learning model and scaler.
  - `fish_species_model.pkl`: The trained model for predicting fish species.
  - `scaler.pkl`: The scaler used for normalizing the input data.

## Installation
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask application:**
   ```bash
   python app.py
   ```

## Usage
1. **Home Page:**
   - Visit the home page at `http://localhost:<PORT>`.
   - Input the fish measurements (Length1, Length2, Length3, Height, Width) into the form.
   - Click the "Predict" button to submit the data.

2. **Results Page:**
   - After submission, the result page displays the predicted fish species based on the provided measurements.
   - If there are errors (e.g., invalid inputs), the user will be prompted to enter valid numbers.

## Model Details
- **Model:** The machine learning model used is a [model type, e.g., Random Forest, SVM, etc.].
- **Data Preprocessing:** The input data is scaled using a standard scaler to normalize the measurements.
- **Training Data:** The model was trained on a dataset consisting of fish species and their corresponding measurements.

## Deployment
The application is deployed on Heroku and can be accessed at `<Heroku URL>`.

### Procfile
The `Procfile` specifies the commands that are executed by the app on startup:
```
web: gunicorn app:app
```

## Troubleshooting
- **Error: `Internal Server Error`:** Ensure that all input fields are correctly filled with valid numbers.
- **Model-related issues:** Make sure the model files (`fish_species_model.pkl`, `scaler.pkl`) are correctly placed in the `model/` directory.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.
