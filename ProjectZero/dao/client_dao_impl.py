from dao.client_dao import ClientDAO
from exceptions.resource_not_found import ResourceNotFound
from exceptions.bad_request_input import BadRequestInput
from model.clients import Client
from util.db_connection import connection

class ClientDAOImpl(ClientDAO):

    def create_client(self, client):  # 201
        sql = "INSERT INTO clients (name) VALUES (%s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [client.client_name])
        connection.commit()
        record = cursor.fetchone()
        if record:
            return Client(record[0], record[1])
        else:
            raise ResourceNotFound(f"Client could not be created")

    def get_client(self, client_id):  # 404 if no such client exists
        sql = "SELECT * FROM clients WHERE id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [client_id])
        record = cursor.fetchone()
        if record:
            return Client(record[0], record[1])
        else:
            raise ResourceNotFound(f"Client with id: {client_id} - NOT FOUND")

    def get_all_clients(self):  # 200
        sql = "SELECT * FROM clients"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        movie_list = []
        for record in records:
            client = Client(record[0], record[1])
            movie_list.append(client.json())
        return movie_list

    def update_client(self, client):  # 404 if no such client exists
        sql = "UPDATE clients SET name=%s WHERE id= %s RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (client.client_name, int(client.client_id)))
        connection.commit()
        record = cursor.fetchone()
        if record:
            return Client(record[0], record[1])
        else:
            raise ResourceNotFound(f"Client record {client.client_id} does not exist.")

    def delete_client(self, client_id):  # 404 if no such client exists & 205 == success
        sql = "DELETE FROM clients WHERE id=%s RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [client_id])
        connection.commit()
        record = cursor.fetchone()
        if record:
            return Client(record[0], record[1])
        else:
            raise ResourceNotFound(f"Client record {client_id} does not exist.")


def _test():
    client_dao = ClientDAOImpl()
    client = client_dao.get_all_clients()
    print(client)

    print(client_dao.get_movie(1))


if __name__ == '__main__':
    _test()
