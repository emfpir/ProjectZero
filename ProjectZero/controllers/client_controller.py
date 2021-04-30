from flask import jsonify, request

from exceptions.bad_request_input import BadRequestInput
from exceptions.resource_not_found import ResourceNotFound
from model.clients import Client
from services.client_service import ClientService

def route(app):

    #create()
    @app.route("/clients", methods=["POST"])
    def post_client():
        client = Client.json_parse(request.json)
        client = ClientService.create_client(client)
        return jsonify(client.json()), 201

    #update(client_id)
    @app.route("/clients/<client_id>", methods=["PUT"])
    def put_client(client_id):
        try:
            client = Client.json_parse(request.json)
            client.client_id = int(client_id)
            ClientService.update_client(client)
            #404 no such client exists
            return jsonify(client.json()), 200
        except ResourceNotFound as r:
            return r.message, 404

    #detele(client_id)
    @app.route("/clients/<client_id>", methods=["DELETE"])
    def delete_client(client_id):
        try:
            client = ClientService.delete_client(int(client_id))
            return jsonify(client.json()), 205
        except ResourceNotFound as r:
            return r.message, 404
        except BadRequestInput as bri:
            return bri.messaeg, 400

    #get all client()
    @app.route("/clients", methods=['GET'])
    def get_all_clients():
        return jsonify(ClientService.get_all_clients()), 200

    #get client(client_id) 200 or 404
    @app.route("/clients/<client_id>", methods=['GET'])
    def get_client(client_id):
        try:
            client = ClientService.get_client(int(client_id))
            return jsonify(client.json()), 200
        except ValueError as e:
            return "Not a valid Id", 400  # bad request
        except ResourceNotFound as r:
            return r.message, 404
