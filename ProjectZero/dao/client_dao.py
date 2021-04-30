from abc import ABC, abstractmethod

class ClientDAO:

    # create client with no args
    @abstractmethod
    def create_client(self, client):
        # return 201 status code
        pass

    # get clinets at client.at
    @abstractmethod
    def get_client(self, client_id):
        # return 404 status code if no such client exists
        pass

    # get all clients with no args
    @abstractmethod
    def get_all_clients(self):
        # return 200 status code
        pass

    # update client at client.id
    @abstractmethod
    def update_client(self, client):
        # return 404 status code if no such client exists
        pass

    # delete client at client.id
    @abstractmethod
    def delete_client(self, client_id):
        # return 404 status code if no such client exists
        # return 205 status code if success
        pass
