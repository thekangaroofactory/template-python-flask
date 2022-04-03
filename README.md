# Flask: web-app-template
A very basic Flask web application template with Python:
  * Create App Factory 
  * Blueprints 
  * Base component is in a Package (with only index page)

- Python : 3.8.12
  * Flask : flask-2.0.2 
  * Docker : docker-5.0.3

Reminder of the Terminal command:

Run the Flask app:
------------------
flask run

Build the container image:
--------------------------
docker build --tag template-flask .

Run the container image:
-----------------------
docker run --name FlaskApp -d -p 5000:5000 template-flask