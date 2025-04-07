from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Your PhyPhox device IP
PHYPHOX_URL = "http://192.168.180.219:8080/get?accX&accY&accZ&gyrX&gyrY&gyrZ"

@app.route('/get_data', methods=['GET'])
def get_sensor_data():
    try:
        response = requests.get(PHYPHOX_URL)
        data = response.json()

        # Extract latest values of accelerometer and gyroscope data
        acc_x = data['buffer']['accX'][-1]
        acc_y = data['buffer']['accY'][-1]
        acc_z = data['buffer']['accZ'][-1]

        gyr_x = data['buffer']['gyrX'][-1]
        gyr_y = data['buffer']['gyrY'][-1]
        gyr_z = data['buffer']['gyrZ'][-1]

        return jsonify({
            "accX": acc_x, "accY": acc_y, "accZ": acc_z,
            "gyrX": gyr_x, "gyrY": gyr_y, "gyrZ": gyr_z
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
