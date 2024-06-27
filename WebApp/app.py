from flask import Flask, render_template, request
import pickle
import numpy as np

# setup application
app = Flask(__name__)

def prediction(lst):
    filename = r'C:\Users\SAMARASINGHAGMV\Documents\Car price prediction\WebApp\model\predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
    # return "Hello World"
    pred_value = 0
    if request.method == 'POST':
        year = request.form['year']
        kmdriven = request.form['km_driven']
        milleage = request.form['mileage(km/ltr/kg)']
        engine = request.form['engine']
        maxpower = request.form['max_power']
        seats = request.form['seats']
        name = request.form['name']
        fuel = request.form['fuel']
        sellerType = request.form['seller_type']
        transmission = request.form['transmission']
        owner = request.form['owner']
        
        feature_list = []

        feature_list.append(int(year))
        feature_list.append(float(kmdriven))
        feature_list.append(len(milleage))
        feature_list.append(len(engine))
        feature_list.append(len(maxpower))
        feature_list.append(len(seats))

        name_list = ['BMW X4 M Sport X xDrive20d','Maruti Alto 800 LXI','Maruti Alto LXi','Maruti Swift Dzire VDI','Maruti Swift VDI','Other']
        fuel_list = ['CNG','Diesel','LPG','Petrol']
        sellerType_list = ['Dealer','Individual','type_Trustmark Dealer']
        transmission_list = ['Automatic', 'Manual']
        owner_list = ['First Owner','Fourth & Above Owner', 'Second Owner','Test Drive Car','Third Owner']

        # for item in company_list:
        #     if item == company:
        #         feature_list.append(1)
        #     else:
        #         feature_list.append(0)

        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)
        
        traverse_list(name_list, name)
        traverse_list(fuel_list, fuel)
        traverse_list(sellerType_list, sellerType)
        traverse_list(transmission_list, transmission)
        traverse_list(owner_list, owner)

        pred_value = prediction(feature_list)
        pred_value = np.round(pred_value[0],2)*221

    return render_template('index.html', pred_value=pred_value)


if __name__ == '__main__':
    app.run(debug=True)