import tkinter as tk

root = tk.Tk(screenName="Discount Calculator", baseName=None, className='Discount Calculator', useTk=1)
root.geometry("400x400")

root.minsize(400, 400)
root.maxsize(400, 400)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

def calc():
    price = original_entry.get()
    disc = discount_entry.get()

    if (len(price)==0):
        final.config(text="Price can not be empty")
        return
    elif (len(disc)==0):
        final.config(text="Discount can not be empty")
        return 
    
    if (int(disc)>100):
        final.config(text="Discount can't be higher than 100%")
    else :
        final_price = int(price) * (100-int(disc))/100
        final.config(text="Final Price: "+str(final_price))

    return

def validate_entry(text):
    return text.isdecimal()

original = tk.Label(root, text="Original Price:").grid(row=0, column=1)
original_entry = tk.Entry(root, validate="key",validatecommand=(root.register(validate_entry), "%S"), width=20)
original_entry.grid(row=1, column=1)

discount = tk.Label(root, text="Discount (%):").grid(row=2, column=1)
discount_entry = tk.Entry(root, validate="key",validatecommand=(root.register(validate_entry), "%S"), width=10)
discount_entry.grid(row=3, column=1)

button = tk.Button(root, text="Calculate", command=calc).grid(row=4, column=1)
final = tk.Label(root, text="Final Price")
final.grid(row=5, column=1)

root.mainloop()