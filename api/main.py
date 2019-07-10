from infra.waf.responder.server import Server


app = Server()


def main():
    app.set_router()
    app.run()


if __name__ == '__main__':
    main()
