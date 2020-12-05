from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route('/temperature.html', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+'&us&appid='YOUR_KEY')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    loca_2 = float(json_object['coord']['lon'])
    loca_1 = float(json_object['coord']['lat'])
    temp_f = (temp_k - 273.15) * 1.8 + 32
    return render_template('temperature.html', temp= temp_f, lat= loca_1, lon= loca_2)



# @app.route('/leaf.js')
# def box_map():
#     mymap = L.map('mapid').setView(0, 0, 1);


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
