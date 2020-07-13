import werkzeug
from flask import Flask, json, request
from api.model import singlyLinkNode
from api.linkedlist.linkedList import LinkedList
from api.matrix.operations import rotate_image, zero_out
from api.strings.operations import is_unique, is_palindrome

api = Flask(__name__)


@api.route('/ping', methods=['GET'])
def ping():
    return "ack", 200


@api.route('/reverse', methods=['POST'])
def post_to_reverse():
    try:
        body = request.get_json()
        ll = LinkedList()
        last = singlyLinkNode.SinglyLinkedNode

        for data in body:
            cur = singlyLinkNode.SinglyLinkedNode(data)
            # guard clause for the first element
            if last is not None:
                last.next = cur

            ll.add(cur)
    except (AttributeError, ConnectionError, werkzeug.exceptions.BadRequest):
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


@api.route('/rotate', methods=['GET'])
def get_rotate():
    try:
        # cache data = True, parse as text = True
        body = request.get_data(True, True)

    except (AttributeError, ConnectionError, werkzeug.exceptions.BadRequest):
        return "server error, please check input or try again", 500

    return json.dumps(rotate_image(body)), 200


@api.route('/zero', methods=['GET'])
def get_zero():
    try:
        # cache data = True, parse as text = True
        body = request.get_data(True, True)

    except (AttributeError, ConnectionError, werkzeug.exceptions.BadRequest):
        return "server error, please check input or try again", 500

    return json.dumps(zero_out(body)), 200


@api.route('/route', methods=['GET'])
def find_route():
    try:
        # cache data = True, parse as text = True
        body = request.get_data(True, True)
        start = body[0]
        end = body[1]

    except (AttributeError, ConnectionError, werkzeug.exceptions.BadRequest):
        return "server error, please check input or try again", 500

    return json.dumps(find_route(start, end)), 200


if __name__ == '__main__':
    api.run(host='0.0.0.0')
