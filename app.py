from flask import Flask, render_template, request
app = Flask(__name__)
from werkzeug.utils import secure_filename
import os
import boto3
from config import Config
#from dotenv import dotenv_values

#config = dotenv_values(".env")
# s3 = boto3.client('s3',
#                     aws_access_key_id=os.getenv('ACCESS_KEY'),
#                     aws_secret_access_key= os.getenv('ACCESS_SECRET_KEY'),
#                     region_name = os.getenv('REGION_NAME')
#                      )

s3 = boto3.client('s3',
                    aws_access_key_id=Config.ACCESS_KEY,
                    aws_secret_access_key= Config.ACCESS_SECRET_KEY,
                    region_name = Config.REGION_NAME
                     )

BUCKET_NAME=Config.BUCKET_NAME
print("Bucket name : ",BUCKET_NAME)

@app.route("/reva")
def reva_home():
    return {"data" : "It's created."}

@app.route("/access_image")
def access_image():
    return render_template("home.html")

@app.route('/aws')  
def home():
    return render_template("file_upload_to_s3.html")

@app.route('/upload',methods=['post'])
def upload():
    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                img.save(filename)
                s3.upload_file(
                    Bucket = BUCKET_NAME,
                    Filename=filename,
                    Key = filename
                )
                msg = "Upload Done ! "
        return render_template("file_upload_to_s3.html",msg =msg)



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)