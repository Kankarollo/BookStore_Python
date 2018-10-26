from GUICreator import GUICreator
from StarterGUI import StarterGUI
from postgreLiteManager import PostgresManager

starterGui = StarterGUI()
database_name = starterGui.name
user = starterGui.user
password = starterGui.password
host = starterGui.host
port = starterGui.port
postgresManager = PostgresManager(database_name, user, password, host, port)
MainWindow = GUICreator(postgresManager)

