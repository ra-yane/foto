from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..managers import users


@jwt_required
def me():
    me_id = get_jwt_identity()['id']
    user = users.get(me_id)
    me = user.get_data()
    return jsonify(me)
