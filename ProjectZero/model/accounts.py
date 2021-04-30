class Account:

    def __init__(self, account_id=0, account_name="", account_amount=0, account_client_id=0):
        self.account_id = account_id
        self.account_name = account_name
        self.account_amount = account_amount
        self.account_client_id = account_client_id

    def json(self):
        return {
            'id': self.account_id,
            'name': self.account_name,
            'amount': self.account_amount,
            'accountClientId': self.account_client_id
        }

    @staticmethod
    def json_parse(json):
        account = Account()
        account.account_id = json["id"] if "id" in json else 0
        account.account_name = json["name"]
        account.account_amount = json["amount"] if "amount" in json else 0
        account.account_client_id = json["accountClientId"] if "accountClientId" in json else 0
        return account

    def __repr__(self):
        return str(self.json())
