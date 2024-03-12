from flask import Flask, request, jsonify, render_template
from utils.PhoneNumberCleaner import PhoneNumberCleaner

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        phone_number = request.form['phone_number']
        phone_cleaner = PhoneNumberCleaner(phone_number)

        try:

            cleaned_number = phone_cleaner.clean_number()

            return (jsonify({'cleaned_number': cleaned_number}), 200)
        
        except ValueError as e:

            return jsonify({'error': str(e)}), 400
    else:

        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
