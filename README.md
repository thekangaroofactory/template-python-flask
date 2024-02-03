# Flask: web-app-template
A very basic Flask web application template with Python:
  * Create App Factory 
  * Blueprints 
  * Base component is in a Package (with only index page)

- Versions
  * See requirements.txt

# Reminder of the Terminal command:

Run the Flask app:
------------------
flask run

Build the container image:
--------------------------
docker build --tag template-flask .

Run the container image:
-----------------------
docker run --name FlaskApp -d -p 5000:5000 template-flask