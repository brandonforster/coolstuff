from flask import Flask, json, request
import linkedlist
from node import Node

api = Flask(__name__)


@api.route('/dump', methods=['GET'])
def dump():
    one = Node("one")
    two = Node("two")
    three = Node("three")
    ll = linkedlist.LinkedList(one)
    ll.add(two)
    ll.add(three)
    enc = json.JSONEncoder()
    try:
        return enc.encode(ll), 200
    except TypeError as err:
        return json.dumps(err.args), 500


@api.route('/reverse', methods=['POST'])
def post_to_reverse():
    err = None
    body = request.get_json()
    if err is not None:
        return json.dumps({"errorMsg": err}), 500

    return json.dumps({"success": True}), 201


if __name__ == '__main__':
    api.run()
