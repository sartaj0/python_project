
from flask import Flask, render_template, request

from modules.database import engine
from modules import models

from routers.user import user_api

models.Base.metadata.create_all(bind=engine)

app = Flask(__name__)
app.register_blueprint(user_api)


@app.route("/", methods=["GET", "POST"])
def main():
	return render_template("main.html")


@app.route("/auth", methods=["GET", "POST"])
def auth():
	return render_template("auth.html")


@app.route("/auth/login", methods=["POST"])
def login():
	print("ok")
	print()
	print(request.content_type)
	print(request.get_data())
	print("hola", request.get_json())
	return jsonify({'json', 'ok'})


@app.route("/auth/signin", methods=["GET", "POST"])
def signin():
	pass


if __name__ == "__main__":
	app.run(debug=True)