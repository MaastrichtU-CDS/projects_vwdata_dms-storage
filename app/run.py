from flask import Flask, Response, request, send_file, abort, render_template
import json
import sqlite3
import os
import uuid

app = Flask('FileService')

#create upload folder if not exists
storageDir = "/storage"
if not os.path.exists(storageDir):
    os.mkdir(storageDir)

app = Flask('FileService')

@app.route('/', methods=["GET"])
def index():
    return render_template("index.html")

@app.route('/', methods=["POST"])
def postFile():
    #store file in folder, using uuid
    fileObj = request.files["fileObject"]
    print(request.args)
    fileName = request.form.get("fileType")
    fileObj.save(os.path.join(storageDir, fileName + ".csv"))

    statusText = "Bestand \"%s\" succesvol geupload" % fileName
    return render_template("index.html", status=statusText)

app.run(debug=True, host='0.0.0.0', port=5000)