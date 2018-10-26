from tkinter import *


class StarterGUI:

    def __init__(self):
        self.window = Tk()
        self.window.title("Connect to database")
        self.add_text_labels()
        self.add_button()
        self.entries = self.Entries(self.window)
        self.window.mainloop()

    def add_text_labels(self):
        tName = Label(self.window, text="Name:")
        tName.grid(row=0, column=0)
        tUser = Label(self.window, text="User:")
        tUser.grid(row=1, column=0)
        tPassword = Label(self.window, text="Password:")
        tPassword.grid(row=0, column=2)
        tHost = Label(self.window, text="Host:")
        tHost.grid(row=1, column=2)
        tPort = Label(self.window, text="Port:")
        tPort.grid(row=2, column=0)

    def add_button(self):
        bConnect = Button(self.window, text="Connect", width=16, command=self.connect_to_database)
        bConnect.grid(row=2, column=3)

    def connect_to_database(self):
        self.port = self.entries.ePort.get()
        self.password = self.entries.ePassword.get()
        self.user = self.entries.eUser.get()
        self.host = self.entries.eHost.get()
        self.name = self.entries.eName.get()
        self.window.quit()

    class Entries:
        def __init__(self, MainWindow):
            self.eName = Entry(MainWindow, text="")
            self.eName.grid(row=0, column=1)
            self.eUser = Entry(MainWindow, text="")
            self.eUser.grid(row=1, column=1)
            self.ePassword = Entry(MainWindow, show='*')
            self.ePassword.grid(row=0, column=3)
            self.eHost = Entry(MainWindow, text="")
            self.eHost.grid(row=1, column=3)
            self.ePort = Entry(MainWindow, text="")
            self.ePort.grid(row=2, column=1)


if __name__ == '__main__':
    test = StarterGUI()
