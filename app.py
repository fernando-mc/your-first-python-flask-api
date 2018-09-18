import json

from flask import Flask
    
app = Flask(__name__)

@app.route('/weather/<date>')
def weather(date):
    with open('./seattle-data.json', 'r') as jsonfile:
        file_data = json.loads(jsonfile.read())
    return json.dumps(file_data[str(date)])

if __name__ == '__main__':
    app.run(debug=True)
