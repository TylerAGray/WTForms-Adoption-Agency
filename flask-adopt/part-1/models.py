from flask_sqlalchemy import SQLAlchemy

# Default image URL used when a pet photo is not provided
GENERIC_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

# Initialize SQLAlchemy object
db = SQLAlchemy()

class Pet(db.Model):
    """Adoptable pet."""

    # Define the table name in the database
    __tablename__ = "pets"

    # Define the columns in the "pets" table
    id = db.Column(db.Integer, primary_key=True)  # Primary key, auto-incrementing ID
    name = db.Column(db.Text, nullable=False)     # Pet's name, cannot be null
    species = db.Column(db.Text, nullable=False)  # Pet's species, cannot be null
    photo_url = db.Column(db.Text)                # URL to the pet's photo, can be null
    age = db.Column(db.Integer)                   # Age of the pet, can be null
    notes = db.Column(db.Text)                    # Additional notes about the pet, can be null
    available = db.Column(db.Boolean, nullable=False, default=True)  # Availability status, default is True

    def image_url(self):
        """Return the image URL for the pet. If no custom photo is provided, return a generic image URL."""
        return self.photo_url or GENERIC_IMAGE

def connect_db(app):
    """Connect this database to the provided Flask app.

    This function should be called in your Flask app to establish a database connection.
    """
    db.app = app
    db.init_app(app)

