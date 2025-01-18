from src.main import Passmanager
import signal

# Starting the app
app = Passmanager()
app.Login()

# Dealing with unexpected interruptions
signal.signal(signal.SIGTERM, app.Exit)
signal.signal(signal.SIGINT, app.Exit)

# Menu to interact with the User
app.Menu()
