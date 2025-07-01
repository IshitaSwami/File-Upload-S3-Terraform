from flask import Flask, request, render_template_string
from dotenv import load_dotenv
import boto3
import os

load_dotenv()

app = Flask(__name__)
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
S3_BUCKET = os.getenv("S3_BUCKET")

s3 = boto3.client('s3')

upload_form = '''
        <!doctype html>
        <html>
        <head>
            <title>Upload File</title>
        </head>
        <body>
            <h1>Upload File to S3</h1>
            <form method="post" action="/upload" enctype="multipart/form-data">
                <input type="file" name="file" />
                <input type="submit" value="Upload" />
            </form>
        </body>
        </html>
'''
@app.route("/upload", methods=["GET","POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file selected", 400
        file = request.files["file"]
        if file.filename == "":
            return "Empty filename", 400
        
        try:
            s3.upload_fileobj(file, S3_BUCKET, file.filename)
            return f"File {file.filename} uploaded successfully to bucket {S3_BUCKET}", 200
        except Exception as e:
            return f"Error uploading file: {str(e)}", 500
        
    return render_template_string(upload_form)

@app.route("/healthz", methods=["GET"])
def health_check():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
