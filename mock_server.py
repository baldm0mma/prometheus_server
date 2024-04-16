from flask import Flask, Response
import random
import time

app = Flask(__name__)

@app.route('/metrics')
def metrics():
    mock_data = f'''
# HELP mock_metric A mock metric
# TYPE mock_metric gauge
mock_metric {{label="value1"}} {random.randint(1, 100)}
mock_metric {{label="value2"}} {random.randint(1, 100)}
'''
    return Response(mock_data, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)