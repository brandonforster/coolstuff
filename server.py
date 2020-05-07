from flask import Flask, json, request
import linkedlist
import node

api = Flask(__name__)


@api.route('/ping', methods=['GET'])
def ping():
    return "ack", 200


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

    return json.dumps(ll.reverse().to_array()), 200


if __name__ == '__main__':
    api.run(host='0.0.0.0')
