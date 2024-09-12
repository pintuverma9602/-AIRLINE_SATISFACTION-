from flask import Flask, render_template, request
import joblib

# Load the model
model_file_path = "./models/logisticregre.lb"  # Update the path if needed
model = joblib.load(model_file_path)

app = Flask(__name__)

@app.route('/')  # http://127.0.0.1:5000/
def home():
    return render_template('home.html')

@app.route('/about.html')  # http://127.0.0.1:5000/about
def about():
    return render_template('about.html')

@app.route('/intro.html')  # http://127.0.0.1:5000/intro
def intro():
    return render_template('intro.html')

@app.route('/output.html')  # http://127.0.0.1:5000/output
def output():
    return render_template('output.html')

@app.route('/pic.html')  # http://127.0.0.1:5000/pic
def pic():
    return render_template('pic.html')

@app.route('/thank_you.html')  # http://127.0.0.1:5000/thank_you
def thank_you():
    return render_template('thank_you.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Retrieve form data
        age = int(request.form['age'])
        flight_distance = int(request.form['flight_distance'])
        inflight_entertainment = int(request.form['inflight_entertainment'])
        baggage_handling = int(request.form['baggage_handling'])
        cleanliness = int(request.form['cleanliness'])
        departure_delay = int(request.form['departure_delay'])
        arrival_delay = int(request.form['arrival_delay'])
        gender = int(request.form['gender'])
        customer_type = int(request.form['customer_type'])
        travel_type = int(request.form['travel_type'])
        class_type = request.form['class_type']

        # Encode class type
        economy = 0
        economy_plus = 0
        if class_type == "ECO":
            economy = 1
        elif class_type == "ECO_PLUS":
            economy_plus = 1

        # Prepare data for prediction
        UNSEEN_DATA = [[age, flight_distance, inflight_entertainment, baggage_handling, cleanliness,
                        departure_delay, arrival_delay, gender, customer_type, travel_type, economy, economy_plus]]

        # Predict
        PREDICTION = model.predict(UNSEEN_DATA)[0]

        # Map prediction to label
        label_dict = {0: 'Dissatisfied', 1: 'Satisfied'}
        return render_template('output.html', output=label_dict[PREDICTION])

if __name__ == "__main__": 
    app.run(debug=True)
