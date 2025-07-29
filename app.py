from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
try:
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predictor')
def predictor():
    return render_template('predictor.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded'})
    
    try:
        # Get data from form
        data = request.json
        
        # Convert to numpy array and reshape for prediction
        features = np.array([
            float(data['x']),
            float(data['y']),
            float(data['z'])
        ]).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features)
        
        # Return simple yes/no result
        if prediction[0] == 1:
            return jsonify({
                'result': 'Yes', 
                'message': 'Potential fault detected! Please check your parameters.',
                'icon': 'exclamation-triangle'
            })
        else:
            return jsonify({
                'result': 'No', 
                'message': 'No problems detected. You can continue working.',
                'icon': 'check-circle'
            })
            
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)