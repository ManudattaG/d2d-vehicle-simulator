from flask import Flask, jsonify
from simulator import Simulator

app = Flask(__name__)

@app.route('/simulator', methods=['GET'])
def get_simulation_result():
    number_of_requests = 5
    bounding_box = (13.34014892578125, 52.52791908000258, 13.506317138671875, 52.562995039558004)
    result = Simulator(bounding_box).simulate(number_of_requests)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
