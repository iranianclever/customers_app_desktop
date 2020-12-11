from tkinter import *
from tkinter import messagebox
from db import Database


# Application of tkinter
class Application:
    """Create frame of screen with tkinter"""

    def __init__(self):
        """Initialization"""
        # App tk root
        self.app = Tk()
        # Title of app
        self.app.title('Application of desktop')
        # Screen size of app
        self.app.geometry('700x450')
        # Selected customer
        self.selected_customer = 0
        # Adding widgets to app
        self.widgets()
        # Database
        self.db = Database()
        # Population list
        self.populate_list()
        # Rendering app
        self.app.mainloop()

    def widgets(self):
        """Combine widgets"""
        self.input_widgets()
        self.button_widgets()
        self.list_widget()

    def input_widgets(self):
        """Create input widgets"""
        # Name Customer
        self.name_text = StringVar()
        self.name_label = Label(self.app, text='Name Customer',
                                font=('bold', 14), pady=20)
        self.name_label.grid(row=0, column=0, sticky=W)
        self.name_entry = Entry(self.app, textvariable=self.name_text)
        self.name_entry.grid(row=0, column=1)
        # Specialty Customer
        self.specialty_text = StringVar()
        self.specialty_label = Label(
            self.app, text='Specialty Customer', font=('bold', 14), pady=20)
        self.specialty_label.grid(row=0, column=2, sticky=W)
        self.specialty_entry = Entry(
            self.app, textvariable=self.specialty_text)
        self.specialty_entry.grid(row=0, column=3)
        # Number Customer
        self.number_text = StringVar()
        self.number_label = Label(
            self.app, text='Number Customer', font=('bold', 14), pady=20)
        self.number_label.grid(row=1, column=0, sticky=W)
        self.number_entry = Entry(self.app, textvariable=self.number_text)
        self.number_entry.grid(row=1, column=1)
        # Salary Customer
        self.salary_text = StringVar()
        self.salary_label = Label(
            self.app, text='Salary Customer', font=('bold', 14), pady=20)
        self.salary_label.grid(row=1, column=2, sticky=W)
        self.salary_entry = Entry(self.app, textvariable=self.salary_text)
        self.salary_entry.grid(row=1, column=3)

    def button_widgets(self):
        """Create button widgets"""
        # Add button
        self.add_button = Button(self.app, text='Add',
                                 width=12, command=self.add)
        self.add_button.grid(row=2, column=0, pady=20)
        # Update button
        self.update_button = Button(
            self.app, text='Update', width=12, command=self.update)
        self.update_button.grid(row=2, column=1)
        # Remove button
        self.remove_button = Button(
            self.app, text='Remove', width=12, command=self.remove)
        self.remove_button.grid(row=2, column=2)
        # Clear button
        self.clear_button = Button(
            self.app, text='Clear', width=12, command=self.clear)
        self.clear_button.grid(row=2, column=3)

    def list_widget(self):
        """Create listbox and scrollbar widgets"""
        # Listbox
        self.list_customers = Listbox(self.app, height=8, width=50, border=0)
        self.list_customers.grid(row=3, column=0, columnspan=3,
                                 rowspan=6, pady=20, padx=20)
        # Scrollbar
        self.scrollbar = Scrollbar(self.app)
        self.scrollbar.grid(row=3, column=3)
        # Connect scrollbar to list
        self.list_customers.configure(yscrollcommand=self.scrollbar.set)
        # Trigger scrolling (Y)
        self.scrollbar.configure(command=self.list_customers.yview)
        # Bind selected list
        self.list_customers.bind('<<ListboxSelect>>', self.selected_list)

    def selected_list(self, event):
        """Selection of list item"""
        try:
            # Get data of selected custmer
            index = self.list_customers.curselection()[0]
            self.selected_customer = self.list_customers.get(index)
            # Assignment data to inputs
            self.name_entry.delete(0, END)
            self.name_entry.insert(END, self.selected_customer[1])
            self.specialty_entry.delete(0, END)
            self.specialty_entry.insert(END, self.selected_customer[2])
            self.number_entry.delete(0, END)
            self.number_entry.insert(END, self.selected_customer[3])
            self.salary_entry.delete(0, END)
            self.salary_entry.insert(END, self.selected_customer[4])
        except IndexError:
            pass

    def populate_list(self):
        """Fetch customers"""
        self.list_customers.delete(0, END)
        for row in self.db.fetch():
            self.list_customers.insert(END, row)

    def clear(self):
        """Clear inputs"""
        self.name_entry.delete(0, END)
        self.specialty_entry.delete(0, END)
        self.number_entry.delete(0, END)
        self.salary_entry.delete(0, END)

    def add(self):
        """Add customer"""
        if self.check_inputs():
            # Getting data from inputs
            data = {}
            data['name'] = self.name_entry.get()
            data['specilaty'] = self.specialty_entry.get()
            data['number'] = self.number_entry.get()
            data['salary'] = self.salary_entry.get()
            # Adding to database
            self.db.insert(data['name'], data['specilaty'],
                           data['number'], data['salary'])
            self.clear()
            self.populate_list()
        else:
            messagebox.showerror('Error inputs', 'Please fill all inputs!')

    def update(self):
        """Update customer"""
        if self.check_inputs():
            self.db.update(self.selected_customer[0], self.name_entry.get(), self.specialty_entry.get(),
                           self.number_entry.get(), self.salary_entry.get())
            self.clear()
            self.populate_list()
        else:
            messagebox.showerror('Error inputs', 'Please fill all inputs!')

    def remove(self):
        """Remove customer"""
        self.db.remove(self.selected_customer[0])
        self.clear()
        self.populate_list()

    def check_inputs(self):
        """Checking value inputs"""
        if (self.name_entry.get() == '' or self.specialty_entry.get() == '' or self.number_entry.get() == '' or self.salary_entry.get() == ''):
            return False
        return True


if __name__ == '__main__':
    """Main method"""

    app = Application()
