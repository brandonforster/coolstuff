import werkzeug
from flask import Flask, json, request
import linkedlist
import node
from strops import is_unique, is_palindrome

api = Flask(__name__)


@api.route('/ping', methods=['GET'])
def ping():
    return "ack", 200


@api.route('/reverse', methods=['POST'])
def post_to_reverse():
    try:
        body = request.get_json()
        ll = linkedlist.LinkedList()
        last = node.Node

        for data in body:
            cur = node.Node(data)
            # guard clause for the first element
            if last is not None:
                last.next = cur

            ll.add(cur)
    except (AttributeError, ConnectionError, werkzeug.exceptions.BadRequest) as err:
        return "server error, please check input or try again", 500

    return json.dumps(ll.reverse().to_array()), 200


@api.route('/isunique', methods=['GET'])
def get_is_unique():
    try:
        # cache data = True, parse as text = True
        body = request.get_data(True, True)

    except (AttributeError, ConnectionError, werkzeug.exceptions.BadRequest):
        return "server error, please check input or try again", 500

    return json.dumps(is_unique(body)), 200


@api.route('/ispalindrome', methods=['GET'])
def get_is_palindrome():
    try:
        # cache data = True, parse as text = True
        body = request.get_data(True, True)

    except (AttributeError, ConnectionError, werkzeug.exceptions.BadRequest):
        return "server error, please check input or try again", 500

    return json.dumps(is_palindrome(body)), 200


if __name__ == '__main__':
    api.run(host='0.0.0.0')
