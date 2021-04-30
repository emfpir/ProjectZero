from abc import ABC, abstractmethod


class AccountDAO(ABC):

    # create account at client.id
    @abstractmethod
    def create_account(self, client_id):
        pass

    # update account at client.id and account.id
    @abstractmethod
    def update_account(self, client_id, account_id):
        pass

    # delete account at client.id and account.id
    @abstractmethod
    def delete_account(self, account):
        # return 404 status code if no such account or client exists
        pass

    # get accounts for client.id
    @abstractmethod
    def get_all_accounts(self, client_id):
        # return 404 status code if no such client exists
        pass

    @abstractmethod
    def get_account(self,account):
        #return 404 if no such client
        pass

    # get account by client.id account.id
    @abstractmethod
    def get_account(self, account):
        # return 404 status code if no such client exists
        pass

    @abstractmethod
    def get_movie_amount_filter(self, account):
        # return 404 status code if no such client exists
        pass
        # get account for client.id

    @abstractmethod
    def get_all_accounts_in_range(self, account):
        # return 404 status code if no such client exists
        pass

    @abstractmethod
    def update_account_amount(self, account):
        # return 404 status code if no such client exists
        pass

    @abstractmethod
    def get_deposit(self, account):
        # return 404 status code if no such client exists
        pass

    @abstractmethod
    def get_withdrawal(self, account):
        # return 404 status code if no such client exists
        pass

    # transfer for client.id and 1st account.id to 2nd account.id provided amount
    @abstractmethod
    def get_transfer_account_from(self, account):
        # return 404 if no account or client exists
        # return 422 if insufficient funds
        pass

    @abstractmethod
    def get_transfer_account_into(self, account):
        # return 404 if no account or client exists
        # return 422 if insufficient funds
        pass

    @abstractmethod
    def update_accounts_after_transfer(self, account):
        # return 404 if no account or client exists
        # return 422 if insufficient funds
        pass
