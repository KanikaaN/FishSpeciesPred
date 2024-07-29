import pickle

# Load your model and scaler
model = pickle.load(open('fish_species_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

def predict_species(length1, length2, length3, height, width):
    # Perform the prediction
    features = [[length1, length2, length3, height, width]]
    scaled_features = scaler.transform(features)
    prediction = model.predict(scaled_features)
    return prediction[0]
