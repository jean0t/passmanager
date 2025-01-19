from src.main import Passmanager
import signal


def main():
    # Starting the app
    app = Passmanager()
    try:
        app.Login()
    except:
        print("no joke bro")
        exit(1)
    # Dealing with unexpected interruptions
    signal.signal(signal.SIGTERM, app.Exit)
    signal.signal(signal.SIGINT, app.Exit)

    # Menu to interact with the User
    app.Menu()


if __name__ == "__main__":
    main()
