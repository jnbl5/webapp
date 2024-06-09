from flask import Flask, request, jsonify
   from google.cloud import storage
   import os

   app = Flask(__name__)

   # Set up Google Cloud Storage
   os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\Users\Jerome Nablo\AppData\Local\Google\Cloud SDK\cbd3354-systems\cbd3354-systems-188ca7c47490.json'
   client = storage.Client()
   bucket = client.get_bucket('ica-systems')

   @app.route('/upload', methods=['POST'])
   def upload_file():
       file = request.files['file']
       if not file:
           return 'No file found', 400

       blob = bucket.blob(file.filename)
       blob.upload_from_string(file.read(), content_type=file.content_type)

       return jsonify({'message': 'File uploaded successfully', 'filename': file.filename})

   if __name__ == '__main__':
       app.run(debug=True, host='0.0.0.0')
