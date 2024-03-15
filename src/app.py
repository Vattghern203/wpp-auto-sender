import os

from flask import Flask, request, jsonify, render_template

from werkzeug.utils import secure_filename

from utils.FileManager import FileManager
from utils.ListManager import ListManager
from utils.PhoneNumberCleaner import PhoneNumberCleaner


app = Flask(__name__)

UPLOAD_FOLDER = 'src/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        phone_list = request.files['phone-list']

        file_manager = FileManager(phone_list)

        if file_manager.verify_existance_on_uploads():

            print(f'{phone_list.name} is already in the database.')

            return render_template('index.html')
        
        filename = secure_filename(phone_list.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        phone_list.save(file_path)
        
        list_manager = ListManager(file_path)

        print(phone_list.content_type)

        try:

            cleaned_list = list_manager.read_file()

            file_manager.remove_file()

            return render_template('index.html', cleaned_numbers=cleaned_list)

            #return (jsonify({'cleaned_number': cleaned_list}), 200)
        
        except ValueError as e:

            return jsonify({'error': str(e)}), 400
        
        except Exception as e:

            return jsonify({'error': str(e), 'message': 'An unexpected error has occured'})
    else:

        return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)
