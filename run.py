from src.main import Passmanager
import signal

def main():
    # Starting the app
    app = Passmanager()
    app.Login()

    # Dealing with unexpected interruptions
    signal.signal(signal.SIGTERM, app.Exit)
    signal.signal(signal.SIGINT, app.Exit)

    # Menu to interact with the User
    app.Menu()

if __name__ == "__main__":
    main()
