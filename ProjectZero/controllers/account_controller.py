from exceptions.resource_amount_insufficient import ResourceAmountInsufficient
from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_unavailable import ResourceUnavailable
from model.accounts import Account
from flask import request, jsonify
from services.account_service import AccountService

def route(app):

    # create account(client())
    @app.route("/clients/<client_id>/accounts", methods=['POST'])
    def create_account(client_id):
        try:
            account = Account.json_parse(request.json)
            account.account_client_id = int(client_id)
            account = AccountService.create_account(account)
            return jsonify(account.json()), 201
        except ResourceNotFound as r:
            return r.message, 404

    # update account(client_id, account_id)
    @app.route("/clients/<client_id>/accounts/<account_id>", methods=['PUT'])
    def update_account(client_id, account_id):
        try:
            account = Account.json_parse(request.json)
            account.account_id = int(account_id)
            account.account_client_id = int(client_id)
            AccountService.update_account(account)
            return jsonify(account.json()), 201
        except ResourceNotFound as r:
            return r.message, 404

    # delete account(client_id, account_id)
    @app.route("/clients/<client_id>/accounts/<account_id>", methods=['DELETE'])
    def delete_account(client_id, account_id):
        try:
            account = Account(int(account_id), "", 0, int(client_id))
            account = AccountService.delete_account(account)
            return jsonify(account.json()), 205  # 205 if success && 404 if no such account
        except ResourceNotFound as r:
            return r.message, 404

    # get all accounts(client_id)
    @app.route("/clients/<client_id>/accounts", methods=['GET'])
    def get_all_accounts(client_id):
        try:
            less_than = request.args.get("amountLessThan")
            greater_than = request.args.get("amountGreaterThan")
            filter_list = []
            if type(less_than) == type("") and type(greater_than) == type(""):
                temp_list = AccountService.get_all_accounts(int(client_id))
                for item in temp_list:
                    if float(less_than) > item["amount"] and float(greater_than) < item["amount"]:
                        filter_list.append(item)
                return jsonify(filter_list), 200
            else:
                return jsonify(AccountService.get_all_accounts(int(client_id))), 200
        except ResourceNotFound as r:
            return r.message, 404

        # get all accounts(client_id)

    @app.route("/clients/<client_id>/accounts/<account_id>", methods=['GET'])
    def get_account(client_id,account_id):
        try:
            account = Account(account_id, "",0,client_id)
            return jsonify(AccountService.get_account(account)), 200
        except ResourceNotFound as r:
            return r.message, 404

    # Withdraw/deposit given amount (body: {"deposit":500} or {"withdrawal":250}
    @app.route("/clients/<client_id>/accounts/<account_id>", methods=['PATCH'])
    def change_account_amount(client_id, account_id):
        try:
            content = request.get_json()
            try:
                withdrawal_amount = content['withdrawal']
                account = Account(int(account_id), "", float(withdrawal_amount),int(client_id))
                update_item = AccountService.get_withdrawal(account).json()
                return jsonify(AccountService.update_account_amount(update_item)), 200
            except KeyError:
                print("caught key error")
                pass
            deposit_amount = content['deposit']
            account = Account(int(account_id), "", float(deposit_amount), int(client_id))
            update_item = AccountService.get_deposit(account)
            return jsonify(AccountService.update_account_amount(update_item)), 200
        except ResourceNotFound as r:
            return r.message, 404
        except ResourceAmountInsufficient as rai:
            return rai.message, 422
        except ResourceUnavailable as ru:
            return ru.message, 403

    #transfer funds from account to account (body: {"amount":500}) PATCH 404 DNE 422 insufficient funds
    @app.route("/clients/5/accounts/<id_from>/transfer/<id_into>", methods=['PATCH'])
    def transfer_between_accounts(id_from, id_into):
        try:
            try:
                content = request.get_json()
                withdrawal_amount = float(content['amount'])
                account_from = Account(id_from, "", withdrawal_amount, 5)
                update_item = AccountService.get_transfer_account_from(account_from)
                final_account_something = AccountService.update_accounts_after_transfer(update_item)
            except KeyError:
                print("caught key error")
                pass
            deposit_amount = content['amount']
            account_into = Account(id_into, "", deposit_amount, 5)
            update_item = AccountService.get_transfer_account_into(account_into)
            return (jsonify(final_account_something,AccountService.update_accounts_after_transfer(update_item))), 200
        except ResourceNotFound as r:
            return r.message, 404
        except ResourceAmountInsufficient as rai:
            return rai.message, 422
        except ResourceUnavailable as ru:
            return ru.message, 403