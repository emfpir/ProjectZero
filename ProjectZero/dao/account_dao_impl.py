from dao.account_dao import AccountDAO
from dao.client_dao_impl import ClientDAOImpl
from exceptions.resource_amount_insufficient import ResourceAmountInsufficient
from exceptions.resource_not_found import ResourceNotFound
from util.db_connection import connection
from model.accounts import Account
from exceptions.resource_unavailable import ResourceUnavailable


class AccountDAOImpl(AccountDAO):

    def create_account(self, account):
        self.client_id_existence_test(int(account.account_client_id))
        sql = "INSERT INTO accounts  (name,amount, account_client_id) VALUES (%s, %s, %s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (account.account_name, account.account_amount, account.account_client_id))
        connection.commit()
        record = cursor.fetchone()
        if record:
            return Account(record[0], record[1], float(record[2]), record[3])
        else:
            raise ResourceNotFound(f"The Client id enter can't be verified. Unable to create an account without an activity client id")

    def update_account(self, account):
        sql = "UPDATE accounts SET name=%s, amount=%s WHERE id = %s AND account_client_id = %s RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql,
                       (account.account_name, account.account_amount, int(account.account_id), int(account.account_client_id)))
        connection.commit()
        record = cursor.fetchone()
        if record:
            changed_account = Account(record[0], record[1], float(record[2]), record[3])
            return changed_account
        else:
            raise ResourceNotFound(f"No account has account and client id provided")

    def delete_account(self, account):
        sql = "DELETE FROM accounts WHERE id=%s AND account_client_id = %s RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (int(account.account_id), int(account.account_client_id)))
        connection.commit()
        record = cursor.fetchone()
        if record:
            changed_account = Account(record[0], record[1], float(record[2]), record[3])
            return changed_account
        else:
            raise ResourceNotFound(f"No account has account and client id provided")

    def get_all_accounts(self, client_id):
        sql = "SELECT * FROM accounts WHERE account_client_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [client_id])
        records = cursor.fetchall()
        account_list = []
        if records:
            for record in records:
                account = Account(record[0], record[1], float(record[2]), record[3])
                account_list.append(account.json())
            return account_list
        else:
            raise ResourceNotFound(f"Client with id: {client_id}  has no accounts.")

    def get_account(self, account):
        sql = "SELECT * FROM accounts WHERE id = %s AND account_client_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (int(account.account_id), int(account.account_client_id)))
        record = cursor.fetchone()
        if record:
            return Account(record[0], record[1], float(record[2]), record[3]).json()
        else:
            raise ResourceNotFound(f"Account id or client account id - NOT FOUND")

    def get_movie_amount_filter(self, account):
        sql = "SELECT * FROM accounts WHERE account_client_id = %s AND ( amount < %s AND amount > s% )"
        cursor = connection.cursor()
        cursor.execute(sql, (int(account.account_client_id),float(account.account_id),float(account.account_amount)))
        records = cursor.fetchall
        account_list = []
        if records:
            for record in records:
                account = Account(record[0], record[1], float(record[2]), record[3])
                account_list.append(account.json())
            return account_list
        else:
            raise ResourceNotFound(f"Client with id: {account.account_client_id}  has no accounts.")

    def get_all_accounts_in_range(self, account):
        sql = "SELECT * FROM accounts WHERE account_client_id = %s"
        less = float(account.account_name)
        more_than = float(account.account_amount)
        cursor = connection.cursor()
        cursor.execute(sql, [account.account_client_id])
        records = cursor.fetchall()
        account_list = []
        if records:
            for record in records:
                temp_account = Account(record[0], record[1], float(record[2]), record[3])
                if less > temp_account.account_amount & temp_account.account_amount > more_than:
                    account_list.append(temp_account.json())
            return account_list
        else:
            raise ResourceNotFound(f"Client with id: {account.account_client_id}  has no accounts.")

    def update_account_amount(self, account):
        sql = "UPDATE accounts SET amount=%s WHERE id = %s AND account_client_id = %s RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [float(account.account_amount)
            ,account.account_id])
        connection.commit()
        record = cursor.fetchone()
        if record:
            return Account(record[0], record[1], float(record[2]), record[3]).json()
        else:
            raise ResourceNotFound(f"No account has account and client id provided")

    def get_deposit(self, account):
        sql = "SELECT * FROM accounts WHERE id = %s AND account_client_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account.account_id, account.account_client_id])
        record = cursor.fetchone()
        if record:
            return Account(record[0], record[1], (float(record[2]) + account.account_amount), record[3]).json()
        else:
            raise ResourceNotFound(f"Client id and account id does not exist.")

    def get_withdrawal(self, account):
        sql = "SELECT * FROM accounts WHERE id = %s AND account_client_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account.account_id, account.account_client_id])
        record = cursor.fetchone()
        if record:
            if float(record[2] > account.account_amount):
                return Account(record[0], record[1], (float(record[2]) - account.account_amount), record[3])
            else:
                raise ResourceAmountInsufficient(f"The account selected has insuffiecient funds for withdrawal")
        else:
            raise ResourceNotFound(f"Client id and account id does not exist.")

    def get_transfer_account_from(self, account):
        sql = "SELECT * FROM accounts WHERE id = %s AND account_client_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account.account_id, account.account_client_id])
        record = cursor.fetchone()
        if record:
            if float(record[2] > account.account_amount):
                return Account(record[0], record[1], (float(record[2]) - account.account_amount), record[3])
            else:
                raise ResourceAmountInsufficient(f"The account selected has insuffiecient funds for withdrawal")
        else:
            raise ResourceNotFound(f"Client id and account id does not exist.")

    def get_transfer_account_into(self, account):
        sql = "SELECT * FROM accounts WHERE id = %s AND account_client_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account.account_id, account.account_client_id])
        record = cursor.fetchone()
        if record:
            new_amount = (float(record[2]) + float(account.account_amount))
            return Account(record[0], record[1], new_amount, record[3])
        else:
            raise ResourceNotFound(f"Client id and account id does not exist.")

    def update_accounts_after_transfer(self, account):
        sql = "UPDATE accounts SET amount=%s WHERE id = %s RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [account.account_amount, account.account_id])
        connection.commit()
        record = cursor.fetchone()
        if record:
            return Account(record[0], record[1], float(record[2]), record[3]).json()
        else:
            raise ResourceNotFound(f"No account has account and client id provided")



    def _test():
        account_dao = AccountDAOImpl()
        client_dao = ClientDAOImpl()
        client_list = client_dao.get_all_clients()
        for client in client_list:
            account = account_dao.get_all_accounts(client[0])
            print(account)
            print(account_dao.get_movie(1))


    if __name__ == '__main__':
        _test()
