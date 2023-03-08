from datetime import datetime
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
        <html>
            <head>
                <meta charset="UTF-8">
                <title>Realtime Clock</title>
                <script>
                    function updateTime() {
                        fetch('/api/time')
                            .then(response => response.json())
                            .then(data => {
                                var timeString = data.time;
                                document.getElementById("clock").innerHTML = timeString;
                            });
                    }
                    setInterval(updateTime, 1000);
                </script>
            </head>
            <body>
                <h1>Hello, World!</h1>
                <p>The current time is <span id="clock"></span>.</p>
            </body>
        </html>
    '''

@app.route('/api/time')
def get_time():
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({'time': time})

# if __name__ == '__main__':
#     app.run(port=5000)

if __name__ == '__main__':
    app.run(port=os.environ.get('PORT', 5000))
