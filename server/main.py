from flask import request, jsonify
from config import app, db
from models import Contact

# Decorator for contact using the get method.

@app.route("/contact", methods =["GET"])


def get_contacts():
    contacts = Contact.query.all() # Get all context  from Contact db.

# Convert each contact object in the 'contacts' list to a JSON-serializable dictionary
# using the 'to_json' method, and store the resulting list of dictionaries in 'json_contacts'.
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return (jsonify({"contacts": json_contacts})), 200 # data is returned in json format

# Decorator for contact using the post method.

@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or email:
        return(
            jsonify({"message": "Must include first name, last name and email"}), 400, # bad request
        )
 # add to db.
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()

# used to show errors when wrong data is entered in the db.
    except Exception as e:
        return jsonify({"message":str(e)}), 400  

    # When user is created.

    return jsonify({"message": "User Created!"}), 201
              

    
# Run the application.
if __name__ == "__main__":
    # Check if the script is being run directly (not imported as a module).
    with app.app_context():
        # Create an application context which is necessary for database operations.
        db.create_all()
        # Create all tables defined in SQLAlchemy models if they don't exist already.
    app.run(debug=True)
    # Run the Flask application with debugging enabled for easier development.
