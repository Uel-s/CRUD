from flask import request, jsonify
from config import app, db
from models import Contact

# Decorator for contact using the GET method.
@app.route("/contact", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()  # Get all contacts from the Contact db.
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts}), 200  # Data is returned in JSON format

# Decorator for contact using the POST (create) method.
@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return jsonify({"message": "Must include first name, last name and email"}), 400  # Bad request

    # Add to db.
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400  # If not a str, return error message, Status code bad request.

    # When user is created.
    return jsonify({"message": "User Created! ✅"}), 201

# To update Contact.
@app.route("/update_contact/<int:user_id>", methods=["PATCH"])  # Update is by id.
def update_contact(user_id):
    contact = Contact.query.get(user_id)
    if not contact:
        return jsonify({"message": "User not found!"}), 404  # Not found

    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)    

    # Make the changes to the db
    db.session.commit()
    return jsonify({"message": "User Updated Successfully✨"}), 200

# Handling Delete request
@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)
    if not contact:
        return jsonify({"message": "Contact not found"}), 404

    db.session.delete(contact)
    db.session.commit()
    return jsonify({"message": "Contact Deleted 🗑"}), 200

# Run the application.
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create all tables defined in SQLAlchemy models if they don't exist already.
    app.run(host = "0.0.0.0", port = 5000, debug=True)  # Run the Flask application with debugging enabled for easier development.
