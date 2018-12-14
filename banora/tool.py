from flask import jsonify


def json_return(rule):
    def json_return_rule():
        return jsonify(rule())

    return json_return_rule
