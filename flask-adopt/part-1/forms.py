from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    # Field for entering the pet's name
    name = StringField(
        "Pet Name",
        validators=[InputRequired()],  # Ensures that the name is provided
    )

    # Dropdown field for selecting the species of the pet
    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")],  # Provides species options
    )

    # Field for entering the URL of the pet's photo
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],  # The URL is optional but must be a valid URL if provided
    )

    # Field for entering the age of the pet
    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=30)],  # Age is optional but must be between 0 and 30 if provided
    )

    # Text area for entering additional comments about the pet
    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],  # Comments are optional but must be at least 10 characters long if provided
    )

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    # Field for updating the URL of the pet's photo
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],  # The URL is optional but must be a valid URL if provided
    )

    # Text area for updating additional comments about the pet
    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],  # Comments are optional but must be at least 10 characters long if provided
    )

    # Checkbox to indicate whether the pet is available for adoption
    available = BooleanField("Available?")

