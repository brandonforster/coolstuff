from flask import Flask, json, request
import linkedlist
import node
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
        return enc.encode(ll.to_array()), 200
    except TypeError as err:
        return json.dumps(err.args), 500


@api.route('/reverse', methods=['POST'])
def post_to_reverse():
    err = None
    body = request.get_json()
    ll = linkedlist.LinkedList()
    last = node.Node

    for data in body:
        cur = node.Node(data)
        # guard clause for the first element
        if last is not None:
            last.next = cur

        ll.add(cur)

    if err is not None:
        return json.dumps({"errorMsg": err}), 500

    return json.dumps(ll.to_array()), 200


if __name__ == '__main__':
    api.run()
