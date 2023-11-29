from werkzeug.utils import secure_filename
from flask import url_for, send_from_directory, send_file
import uuid
import os
from ..server_functions import UPLOAD_FOLDER

def random_job_identifier():
    id = uuid.uuid4()
    return id.hex

def create_unique_job_folder(session):
    session["job_id"] = random_job_identifier()
    session["workdir"] = UPLOAD_FOLDER + session["jobid"]+"/"
    while os.path.exists(session["workdir"]):
        session["job_id"] = random_job_identifier()
        session["workdir"] = UPLOAD_FOLDER + session["jobid"]+"/"
    os.makedirs(session["workdir"])