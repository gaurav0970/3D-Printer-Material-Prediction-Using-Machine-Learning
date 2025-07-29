# PrintSentry 3D – 3D Printer Material Prediction

PrintSentry 3D is a web-based application that leverages machine learning to predict and diagnose faults in 3D printing processes. It provides a user-friendly interface for entering print parameters and receiving real-time feedback to optimize print quality and reduce errors.

## Features

- **Fault Scanner:** Predicts potential 3D printing faults based on user input.
- **Machine Learning Backend:** Utilizes a trained model (`model.pkl`) for accurate predictions.
- **Interactive Frontend:** Responsive design with HTML, CSS, and JavaScript.
- **Resource Center:** Access to documentation, support, and community links.
- **Contact & Support:** Easy access to support channels.

## Project Structure

```
app.py                        # Main Flask application
model.pkl                     # Trained machine learning model
Model Training/
    Model Training.ipynb      # Jupyter notebook for model training
    model.csv                 # Dataset for training
    SVC_best_model.pkl        # Alternative/best model
static/
    css/style.css             # Stylesheet
    images/                   # Branding and UI images
    js/main.js                # Frontend JavaScript
templates/
    base.html                 # Base template
    index.html                # Home page
    about.html                # About page
    services.html             # Services page
    predictor.html            # Fault scanner page
    contact.html              # Contact page
```

## How It Works

1. **Data Collection & Training:**
   - Historical 3D printing data is collected and stored in `model.csv`.
   - The data is preprocessed and used to train a machine learning model (e.g., SVC) in `Model Training.ipynb`.
   - The trained model is saved as `model.pkl`.

2. **Backend Integration:**
   - The Flask app (`app.py`) loads `model.pkl` at startup.
   - User input from the frontend is processed and passed to the model for prediction.
   - The prediction result is returned to the frontend for display.

3. **Frontend Interaction:**
   - Users interact with the web interface to enter print parameters.
   - Results and recommendations are displayed in real time.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gaurav0970/3D-Printer-Material-Prediction-Using-Machine-Learning.git
   cd 3D-Printer-Material-Prediction-Using-Machine-Learning
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   python app.py
   ```
4. **Access the app:**
   Open your browser and go to link mentioned as local host.

## Requirements
- Python 3.x
- Flask
- scikit-learn
- Jupyter Notebook (for model training)

## Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements.

