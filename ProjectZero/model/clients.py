class Client:

    def __init__(self, client_id=0, client_name=""):
        self.client_id = client_id
        self.client_name = client_name

    def json(self):
        return {
            'clientId': self.client_id,
            'name': self.client_name
        }

    @staticmethod
    def json_parse(json):
        client = Client()
        client.client_id = json["clientId"] if "clientId" in json else 0
        client.client_name = json["name"]
        return client

    def __repr__(self):
        return str(self.json())