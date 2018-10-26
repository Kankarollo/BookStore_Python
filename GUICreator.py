from tkinter import *


class GUICreator:
    def __init__(self, _postgresLiteManager):
        self.postgresLiteManager = _postgresLiteManager
        self.MainWindow = Tk()
        self.MainWindow.title("Book Store")
        self.add_buttons()
        self.entries = self.Entries(self.MainWindow)
        self.add_text_labels()
        self.listbox = self.add_list_box()
        self.scrollbar = self.add_scroll_bar()
        self.index = None
        self.MainWindow.mainloop()

    def add_buttons(self, ):
        bView = Button(self.MainWindow, text="View all", width=16, command=self.command_view)
        bView.grid(row=3, column=3)
        bAdd = Button(self.MainWindow, text="Add book", width=16, command=self.command_add_book)
        bAdd.grid(row=4, column=3)
        bDelete = Button(self.MainWindow, text="Delete selected", width=16, command=self.command_delete_selected)
        bDelete.grid(row=5, column=3)
        bUpdate = Button(self.MainWindow, text="Update selected", width=16, command=self.command_update_selected)
        bUpdate.grid(row=6, column=3)
        bSearch = Button(self.MainWindow, text="Search for book", width=16, command=self.command_search_for)
        bSearch.grid(row=7, column=3)
        bClose = Button(self.MainWindow, text="Close", width=16, command=self.MainWindow.quit)
        bClose.grid(row=8, column=3)

    def add_list_box(self):
        listbox = Listbox(self.MainWindow, width=35)
        listbox.grid(row=3, column=0, rowspan=6, columnspan=2)
        return listbox

    def add_scroll_bar(self):
        scrollbar = Scrollbar(self.MainWindow)
        scrollbar.grid(row=3, column=2, rowspan=6)
        return scrollbar

    def configure_list_box_with_scroll_bar(self):
        self.listbox.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.listbox.yview)

    def add_text_labels(self):
        tTitle = Label(self.MainWindow, text="Title:")
        tTitle.grid(row=0, column=0)
        tYear = Label(self.MainWindow, text="Year:")
        tYear.grid(row=1, column=0)
        tAuthor = Label(self.MainWindow, text="Author:")
        tAuthor.grid(row=0, column=2)
        tISBN = Label(self.MainWindow, text="ISBN:")
        tISBN.grid(row=1, column=2)

    def select_book(self):
        self.listbox.bind('<<ListboxSelect>>', self.get_selected)

    def get_selected(self,event):
        self.index = self.get_index()
        if self.index is not None:
            selected_book = self.listbox.get(self.index)
            self.entries.eTitle.delete(0, END)
            self.entries.eTitle.insert(END, selected_book[0])
            self.entries.eAuthor.delete(0, END)
            self.entries.eAuthor.insert(END, selected_book[1])
            self.entries.eYear.delete(0, END)
            self.entries.eYear.insert(END, selected_book[2])
            self.entries.eISBN.delete(0, END)
            self.entries.eISBN.insert(END, selected_book[3])

    def command_view(self):
        self.select_book()
        self.listbox.delete(0, END)
        for row in self.postgresLiteManager.view():
            self.listbox.insert(END, row)

    def command_add_book(self):
        self.listbox.delete(0, END)
        title = self.entries.eTitle.get()
        author = self.entries.eAuthor.get()
        year = self.entries.eYear.get()
        isbn = self.entries.eISBN.get()
        self.postgresLiteManager.addProducts(title, author, year, isbn)
        for row in self.postgresLiteManager.view():
            self.listbox.insert(END, row)

    def command_search_for(self):
        self.listbox.delete(0, END)
        title = self.entries.eTitle.get()
        author = self.entries.eAuthor.get()
        if self.entries.eYear.get() == "":
            year = 0
        else:
            year = self.entries.eYear.get()
        isbn = self.entries.eISBN.get()
        for row in self.postgresLiteManager.searchFor(title, author, year, isbn):
            self.listbox.insert(END, row)

    def command_delete_selected(self):
        if self.index is not None:
            selected_book = self.listbox.get(self.index)
            title = selected_book[0]
            self.postgresLiteManager.deleteItem(title)
        self.command_view()

    def command_update_selected(self):
        if self.index is not None:
            selected_book = self.listbox.get(self.index)
            title = selected_book[0]
            author = self.entries.eAuthor.get()
            year = self.entries.eYear.get()
            isbn = self.entries.eISBN.get()
            self.postgresLiteManager.update(title, author, year, isbn)
        self.command_view()

    def get_index(self):
        try:
            return self.listbox.curselection()[0]
        except IndexError:
            return None

    class Entries:
        def __init__(self, MainWindow):
            self.eTitle = Entry(MainWindow, text="title")
            self.eTitle.grid(row=0, column=1)
            self.eYear = Entry(MainWindow, text="year")
            self.eYear.grid(row=1, column=1)
            self.eAuthor = Entry(MainWindow, text="author")
            self.eAuthor.grid(row=0, column=3)
            self.eISBN = Entry(MainWindow, text="ISBN")
            self.eISBN.grid(row=1, column=3)


if __name__ == '__main__':
    pass
