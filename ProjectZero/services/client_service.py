from time import time
from dao.client_dao_impl import ClientDAOImpl

from exceptions.resource_unavailable import ResourceUnavailable


class ClientService:
    client_dao = ClientDAOImpl()

    @classmethod
    def create_client(cls, client):
        return cls.client_dao.create_client(client)

    @classmethod
    def get_all_clients(cls):
        return cls.client_dao.get_all_clients()

    @classmethod
    def get_client(cls, client_id):
        return cls.client_dao.get_client(client_id)

    @classmethod
    def update_client(cls, client):
        return cls.client_dao.update_client(client)

    @classmethod
    def delete_client(cls, client_id):
        return cls.client_dao.delete_client(client_id)
