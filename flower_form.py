# The code snippet provided defines a FlaskForm class called FlowerForm. 
# This class inherits from FlaskForm provided by the flask_wtf module, which is used for creating web forms in Flask applications.
# The FlowerForm class defines fields for inputting the measurements of a flower. 
# The form has four fields, each represented by a StringField from the wtforms module. The fields are:
# - SepalLengthCm: Represents the sepal length of a flower.
# - SepalWidthCm: Represents the sepal width of a flower.
# - PetalLengthCm: Represents the petal length of a flower.
# - PetalWidthCm: Represents the petal width of a flower.
# The form also includes a submit field, represented by a SubmitField. This field is used to submit the form and trigger the prediction process.
# By using this form, users can enter the measurements of a flower and submit the form to get a prediction based on the trained model.



from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class FlowerForm(FlaskForm):
    SepalLengthCm = StringField("Sepal Length")
    SepalWidthCm = StringField("Sepal Width")
    PetalLengthCm = StringField("Petal Length")
    PetalWidthCm = StringField("Petal With")

    submit = SubmitField("Predict")
