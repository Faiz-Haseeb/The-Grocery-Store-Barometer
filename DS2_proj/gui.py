from cProfile import label
from os import remove
import tkinter
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from fenwick_tree import fenwick_tree
from fenwick_tree import backing_array

top = tkinter.Tk()
top.geometry("400x300")


barr = backing_array()
print(barr.create_drop_down_2('Baby Care'))

def NewSaleWindow():
    item_values = []
    item_placeholder = barr.get_items_lst()
    newWindow = Toplevel(top)
    newWindow.geometry("300x300")

    newWindow.title("Add a Sale")

    variable = StringVar(newWindow)
    variable.set("Select an Item")

    dropdown_label = Label(newWindow, text = "Choose Product:")
    dropdown_label.place(x = 30, y = 30)

    def getElement():
        value = newsale_dropdown.curselection()
        return(newsale_dropdown.get(value[0]))

    def confirm():
        sale_val = (getElement(), newsale_text.get(1.0, "end-1c"))
        item_values.append(sale_val)
        print(sale_val)

    def conf_command():
        confirm()
        confirm_msg("sale")



    def sale_complete_command():
        newWindow.destroy()
        barr.add_new_sale(item_values)
        #print(barr.lst_item_sales)


    newsale_dropdown = Listbox(newWindow, selectmode = BROWSE)
    for item in item_placeholder:
        newsale_dropdown.insert(END, item)
    newsale_dropdown.place(x = 30, y = 50)

    textbx_label = Label(newWindow, text = "Enter Amount:")
    textbx_label.place(x = 180, y = 80)

    newsale_text = Text(newWindow, height = 1, width = 10)
    newsale_text.place(x = 180, y = 100)

    newsale_conf = Button(newWindow, text = "Confirm Item", command = lambda: conf_command())
    newsale_conf.place(x = 180, y = 140)

    sale_complete = Button(newWindow, text = "Complete Sale", command = lambda: sale_complete_command())
    sale_complete.place(x=180,y=180)

def TotSalesWindow():

    def pick_SecondCategory(event):
        frst = first_category.get()
        drop_list = barr.create_drop_down_2(frst)
        second_category.config(value = drop_list)

    def pick_ThirdCategory(event):
        frst = first_category.get()
        scnd = second_category.get()
        drop_list = barr.create_drop_down_3(frst, scnd)
        third_category.config(value = drop_list)


    def output():
        if second_category.get() == '' and third_category.get() == '':
            cat = first_category.get()

        elif third_category.get() == '':
            cat = second_category.get()
            
        else:
            cat = third_category.get()
        print(barr.get_sales(cat))
        txt = "Sales: "+str(barr.get_sales(cat))
        msg = messagebox.showinfo("",txt)

    SalesWindow = Toplevel(top)
    SalesWindow.geometry("300x300")

    SalesWindow.title("Get Sale Values")

    Category1 = barr.create_drop_down_1()
  
    #First Category
    first_label = Label(SalesWindow, text = "First Category:")
    first_label.place(x = 20, y = 3)
    first_category = ttk.Combobox(SalesWindow, value = Category1)
    first_category.pack(pady=20)
    first_category.bind("<<ComboboxSelected>>", pick_SecondCategory)

    #Second Category
    second_category = ttk.Combobox(SalesWindow, value = [])
    second_label = Label(SalesWindow, text = "Second Category:")
    second_label.place(x = 20, y = 53)
    second_category.pack(pady=20)
    second_category.bind("<<ComboboxSelected>>", pick_ThirdCategory)

    #Third Category
    third_category = ttk.Combobox(SalesWindow, value = [])
    third_label = Label(SalesWindow, text = "Third Category:")
    third_label.place(x = 20, y = 113)
    third_category.pack(pady=20)

    third = third_category.get()

    get_sales_button = Button(SalesWindow, text = "Get Sales from Category", command = output) #command to be added
    get_sales_button.pack(pady = 25)

def confirm_msg(type, amnt = 0):
    if type == "sale":
        msg = messagebox.showinfo("","Item Added")

    elif type == "item":
        msg = messagebox.showinfo("","Update Excel Sheet to Add Item")

    elif type == "remove":
        msg = messagebox.showinfo("", "Update Excel Sheet To Remove Item")

    elif type == "total":
        sales_str = "Total Sales: "+str(amnt)
        msg = messagebox.showinfo("", sales_str)

newsale_button = tkinter.Button(top, text = "Add a New Sale", command = NewSaleWindow) #command to be added.
newsale_button.place(x = 50, y = 50)

get_tot_button = tkinter.Button(top, text = "Get Total Sales", command = TotSalesWindow) #command to be added.
get_tot_button.place(x = 250, y = 50)

newitem_button = tkinter.Button(top, text = "Add a New Item", command = lambda: confirm_msg("item")) #command to be added.
newitem_button.place(x = 50, y = 150)

removeitem_button = tkinter.Button(top, text = "Remove Item", command = lambda: confirm_msg("remove")) #command to be added.
removeitem_button.place(x = 250, y = 150)

top.mainloop() 


# barr.add_new_sale([('shield-baby-diapers-no-4-7-18kg-large-54-pack', 4), ('shield-baby-diapers-no-3-4-9kg-medium-62-pack', 5)] )
# print(barr.lst_item_sales)
# print(barr.get_sales('Pamper Shield'))
# print(barr.get_sales('Baby Pampers (Diapers)'))
# print(barr.get_sales('Bottle Nuk'))