from flask import Blueprint, jsonify, json, Response, request

user_api = Blueprint('user', __name__, url_prefix="/users")


@user_api.route("/", methods=["GET"])
def get_users():
	print(request.get_data())
	return Response(
		status=200,
		response=json.dumps({'user': 'sartaj'})
	)


@user_api.route("/<int:idx>", methods=["GET"])
def get_user(idx: int):
	return jsonify({'user': f'{idx}'})


@user_api.route("/<int:idx>/update", methods=["PUT"])
def update_user(idx: int):
	return jsonify({'user': f'{idx}', "message": "user updated successfully"})


@user_api.route("/", methods=["POST"])
def create_user():
	return jsonify({'message': "user created succesfully"})

