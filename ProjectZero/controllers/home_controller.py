
def route(app):

    @app.route("/", methods=['GET','POST'])
    def hello():
        name = "Charles"
        print(f'Hi, welcome to your web tools for the new banking platform. I am {name}, enjoy the new tool.')

    @app.route("/contact")
    def contact():
        return "Contact us via EMAIL: charles.stersic@revature.net or by phone 777-777-7777"
