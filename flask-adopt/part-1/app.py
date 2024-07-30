from flask import Flask, url_for, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

# Secret key for session management and CSRF protection
app.config['SECRET_KEY'] = "J4n$kR8x"

# Configuration for the SQLAlchemy database connection
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Connect the database to the Flask app and create tables
connect_db(app)
db.create_all()

# Enable the Flask Debug Toolbar
toolbar = DebugToolbarExtension(app)


##############################################################################

@app.route("/")
def list_pets():
    """List all pets."""
    # Query all pets from the database
    pets = Pet.query.all()
    # Render the pet list template with the pets data
    return render_template("pet_list.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet."""
    # Initialize the form for adding a new pet
    form = AddPetForm()

    # If the form is submitted and valid
    if form.validate_on_submit():
        # Collect form data, excluding CSRF token
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        # Create a new Pet instance with the form data
        new_pet = Pet(**data)
        # Add the new pet to the database
        db.session.add(new_pet)
        db.session.commit()
        # Flash a success message
        flash(f"{new_pet.name} added.")
        # Redirect to the list of pets
        return redirect(url_for('list_pets'))
    else:
        # If the form validation fails, re-present the form for correction
        return render_template("pet_add_form.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""
    # Query the pet by ID or return 404 if not found
    pet = Pet.query.get_or_404(pet_id)
    # Initialize the form with the pet's current data
    form = EditPetForm(obj=pet)

    # If the form is submitted and valid
    if form.validate_on_submit():
        # Update the pet's attributes with form data
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        # Flash a success message
        flash(f"{pet.name} updated.")
        # Redirect to the list of pets
        return redirect(url_for('list_pets'))
    else:
        # If the form validation fails, re-present the form for correction
        return render_template("pet_edit_form.html", form=form, pet=pet)

@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return basic info about pet in JSON."""
    # Query the pet by ID or return 404 if not found
    pet = Pet.query.get_or_404(pet_id)
    # Prepare the data to be returned as JSON
    info = {"name": pet.name, "age": pet.age}
    return jsonify(info)
