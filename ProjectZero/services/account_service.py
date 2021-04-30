from dao.account_dao_impl import AccountDAOImpl
from dao.client_dao_impl import ClientDAOImpl


class AccountService:
    client_dao = ClientDAOImpl()
    account_dao = AccountDAOImpl()

    @classmethod
    def create_account(cls, account):
        return cls.account_dao.create_account(account)
    @classmethod
    def update_account(cls, account):
        return cls.account_dao.update_account(account)
    @classmethod
    def delete_account(cls, account):
        return cls.account_dao.delete_account(account)
    @classmethod
    def get_all_accounts(cls, client_id):
        return cls.account_dao.get_all_accounts(client_id)
    @classmethod
    def get_account(cls, account):
        return cls.account_dao.get_account(account)
    @classmethod
    def get_deposit(cls, account):
        return cls.account_dao.get_deposit(account)
    @classmethod
    def get_withdrawal(cls, account):
        return cls.account_dao.get_withdrawal(account)
    @classmethod
    def update_account_amount(cls, account):
        return cls.account_dao.update_account_amount(account)
    @classmethod
    def get_transfer_account_from(cls, account):
        return cls.account_dao.get_transfer_account_from(account)
    @classmethod
    def get_transfer_account_into(cls, account):
        return cls.account_dao.get_transfer_account_into(account)
    @classmethod
    def update_accounts_after_transfer(cls, account):
        return cls.account_dao.update_accounts_after_transfer(account)
    @classmethod
    def get_all_accounts_in_range(cls, account):
        return cls.account_dao.get_all_accounts_in_range(account)