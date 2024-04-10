from flask import Blueprint, jsonify, request
import json
import os

transaction_blueprint = Blueprint('transactions', __name__)

@transaction_blueprint.route('/transaction/<id>', methods=['GET'])
def get_transaction(id):
    with open('transactions.json') as data_file:
        transactions_data = json.load(data_file)
    transaction = transactions_data.get(id, None)
    return jsonify(transaction), 200

@transaction_blueprint.route('/transaction', methods=['POST'])
def add_transaction():
    #TODO
    return

@transaction_blueprint.route('/transaction/<id>', methods=['PUT'])
def update_transaction(id):
    #TODO
    return

@transaction_blueprint.route('/transaction/<id>', methods=['DELETE'])
def delete_transaction(id):
    #TODO
    return


# TODO : ADD A GET ALL TRANSACTIONS ENDPOINT ASWELL