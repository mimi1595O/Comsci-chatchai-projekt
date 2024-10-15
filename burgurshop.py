import tkinter as tk
from tkinter import messagebox
import pyfiglet

# Data from the original script
checklist = ["0828042646", "0865212221", "0838290808", "191", "070910712446", "0968497243"]  # Examples
sizelist = {"Small": 1, "Medium": 1.5, "Large": 2}
meat = {"pork": 80, "chicken": 60, "beef": 100, "synthesis meat": 500}
sauce = {"tomato": 10, "mayo": 10, "mustard": 20}
drinks = {"cokee": 20, "split": 20, "redwater": 25, "Refill": 40}
addition = {"French fries normal": 30, "French fries Large": 50, "mashed potato": 45}

# Helper variables
appendinglist = []
size_multiplier = 1.0
discount = 1.0
sumprice = 0.0


class BurgerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Burger Order System")
        self.root.geometry("600x600")  # Make the window larger

        self.show_welcome_page()

    def reset_order(self):
        # Reset all necessary variables and clear any selections
        global appendinglist, size_multiplier, discount, sumprice
        appendinglist.clear()
        size_multiplier = 1.0
        discount = 1.0
        sumprice = 0.0

        # Clear any widgets on the current page
        for widget in self.root.winfo_children():
            widget.destroy()

        # Start the process again
        self.show_welcome_page()

    def show_welcome_page(self):
        # Welcome Page
        welcome_message = pyfiglet.figlet_format("Welcome")
        self.label_welcome = tk.Label(self.root, text=welcome_message, font=("Courier", 12), justify="center")
        self.label_welcome.place(relx=0.5, rely=0.4, anchor="center")  # Centering the welcome message

        self.start_button = tk.Button(self.root, text="Start Order", command=self.show_main_page)
        self.start_button.place(relx=0.5, rely=0.6, anchor="center")  # Centering the start button

    def show_main_page(self):
        self.label_welcome.place_forget()
        self.start_button.place_forget()

        # Create a frame for the scrollable area
        main_frame = tk.Frame(self.root)
        main_frame.place(relx=0.5, rely=0.5, anchor="center")  # Centering the main page

        # Create a canvas for the scrollbar
        canvas = tk.Canvas(main_frame, width=500, height=500)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        # Add a scrollbar to the canvas
        scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Create another frame inside the canvas
        second_frame = tk.Frame(canvas)

        # Add that new frame to a window in the canvas
        canvas.create_window((0, 0), window=second_frame, anchor="nw")

        # Size selection
        self.label_size = tk.Label(second_frame, text="Please choose burger size:")
        self.label_size.pack()

        self.size_var = tk.StringVar()  # No default value selected
        for size in sizelist.keys():
            tk.Radiobutton(second_frame, text=size, variable=self.size_var, value=size, command=self.update_price).pack()

        # Ingredients section
        self.label_meat = tk.Label(second_frame, text="Choose Meat:")
        self.label_meat.pack()

        self.meat_var = tk.StringVar()  # No default value selected
        for m in meat.keys():
            tk.Radiobutton(second_frame, text=m, variable=self.meat_var, value=m, command=self.update_price).pack()

        self.label_sauce = tk.Label(second_frame, text="Choose Sauce:")
        self.label_sauce.pack()

        self.sauce_var = tk.StringVar()  # No default value selected
        for s in sauce.keys():
            tk.Radiobutton(second_frame, text=s, variable=self.sauce_var, value=s, command=self.update_price).pack()

        self.label_drink = tk.Label(second_frame, text="Choose Drink:")
        self.label_drink.pack()

        self.drink_var = tk.StringVar()  # No default value selected
        for d in drinks.keys():
            tk.Radiobutton(second_frame, text=d, variable=self.drink_var, value=d, command=self.update_price).pack()

        self.label_addition = tk.Label(second_frame, text="Choose Additions:")
        self.label_addition.pack()

        self.addition_var = tk.StringVar()  # No default value selected
        for a in addition.keys():
            tk.Radiobutton(second_frame, text=a, variable=self.addition_var, value=a, command=self.update_price).pack()

        # Real-time price label
        self.label_price = tk.Label(second_frame, text="Total Price: 0 THB", font=("Arial", 14))
        self.label_price.pack()

        # Membership verification section
        self.label_member = tk.Label(second_frame, text="Are you a member?")
        self.label_member.pack()

        self.phone_var = tk.StringVar()
        self.entry_phone = tk.Entry(second_frame, textvariable=self.phone_var)
        self.entry_phone.pack()

        self.button_verify = tk.Button(second_frame, text="Verify Membership", command=self.verify_membership)
        self.button_verify.pack()

        # Button to finalize the order
        self.button_finalize = tk.Button(second_frame, text="Finalize Order", command=self.show_bill)
        self.button_finalize.pack()

    def update_price(self):
        global sumprice, size_multiplier, appendinglist
        # Reset the price list and recalculate based on the current selections
        appendinglist.clear()

        # If the user has selected a size, meat, sauce, drink, and addition, update the price
        if self.size_var.get():
            size_multiplier = sizelist[self.size_var.get()]

        if self.meat_var.get():
            appendinglist.append(meat[self.meat_var.get()] * size_multiplier)

        if self.sauce_var.get():
            appendinglist.append(sauce[self.sauce_var.get()])

        if self.drink_var.get():
            appendinglist.append(drinks[self.drink_var.get()])

        if self.addition_var.get():
            appendinglist.append(addition[self.addition_var.get()])

        # Update the sum price
        sumprice = sum(appendinglist)
        self.label_price.config(text=f"Total Price: {sumprice} THB")

    def verify_membership(self):
        global discount
        phone_number = self.phone_var.get()
        if phone_number in checklist:
            discount = 0.85  # Member discount
            messagebox.showinfo("Membership Verified", "You are a member! 15% discount applied.")
        else:
            self.register(phone_number)

    def register(self, phone_number):
        # Ask the user if they want to register
        response = messagebox.askyesno("Not a member", "You are not a member. Would you like to register?")
        if response:
            # Add the phone number to the checklist and confirm registration
            checklist.append(phone_number)
            discount = 0.90  # Registration discount
            messagebox.showinfo("Registration Complete", f"Phone number {phone_number} registered! 10% discount applied.")
        else:
            discount = 1.0  # No discount applied
            messagebox.showinfo("No Membership", "No discount applied.")

    def show_bill(self):
        # Calculate the final price with discount and VAT
        finalprice = round(sumprice * discount * 1.07)  # VAT 7%

        # Show the final bill in a message box
        bill_text = (
            f"--------------------------\n"
            f"|           Bill         |\n"
            f"|       price = {sumprice}  THB     |\n"
            f"| you get discount = {100 - discount*100}%|\n"
            f"|    Net = {finalprice} THB (VAT 7%)|\n"
            f"--------------------------"
        )

        messagebox.showinfo("Final Bill", bill_text)

        # Display thank-you message
        self.label_thanks = tk.Label(self.root, text=pyfiglet.figlet_format("Thank you"), font=("Courier", 12))
        self.label_thanks.pack()

        # Restart the order process after showing the thank-you message
        self.root.after(3000, self.reset_order)  # Wait 3 seconds, then restart the order process


# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = BurgerApp(root)
    root.mainloop()
