### Base Requirements for a Flask application.
from utilities.file_management import *
from utilities.server_functions import *
from utilities.application_functions import *

### Basic startup, sets a secret key and some standard folders
app = Flask(__name__)
app.config['SECRET_KEY'] = "01189998819991197253"
app.config['UPLOAD_FOLDER'] = "/uploads/"
app.config['DATABASE_FOLDER'] = "/database/"
app.config['TEMPLATES_AUTO_RELOAD'] = True


### Starting Page
@app.route('/',methods=['GET', 'POST'])
def start_page():
    if request.method=="POST":
        create_unique_job_folder(session)
        secure_pdb_filename = secure_filename(request.files["PDBfile"])
        secure_mol2_filename = secure_filename(request.files["Mol2file"])
        
        # Do the stuff in the job submission process.
    return render_template("main.html")