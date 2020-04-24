from tkinter import *
import tkinter as tk
from tkinter import messagebox

#Sets grammar for is/are depending on if there is 1 item or are more than 1 item or less than 1 item
def Is_or_Are(stock):
    stock = int(stock)
    if stock != 1:
        Is_Are = "are"
    else:
        Is_Are = "is"
    return(Is_Are)

#Updates variables within the code using data from the csv file
def Update_Files():
    global fp
    global AllData
    global Items_in_VM_Database
    global item_name_1
    global item_name_2
    global item_name_3
    global item_name_4
    global item_name_5
    global item_name_6
    global item_price_1
    global item_price_2
    global item_price_3
    global item_price_4
    global item_price_5
    global item_price_6
    global item_stock_1
    global item_stock_2
    global item_stock_3
    global item_stock_4
    global item_stock_5
    global item_stock_6


    fp = open("VM_Database.csv","r")
    AllData = fp.readlines()
    Items_in_VM_Database = len(AllData)
    fp.close()

    ProcessedData = 0
    AllData_2 = AllData
    while ProcessedData < Items_in_VM_Database:
        AllData_2[ProcessedData] = AllData_2[ProcessedData].split(",")
        ProcessedData = ProcessedData + 1
    item_name_1 = AllData_2[0][0]+", "+AllData_2[0][1]
    item_name_2 = AllData_2[1][0]+", "+AllData_2[1][1]
    item_name_3 = AllData_2[2][0]+", "+AllData_2[2][1]
    item_name_4 = AllData_2[3][0]+", "+AllData_2[3][1]
    item_name_5 = AllData_2[4][0]+", "+AllData_2[4][1]
    item_name_6 = AllData_2[5][0]+", "+AllData_2[5][1]
    item_price_1 = AllData_2[0][2]
    item_price_2 = AllData_2[1][2]
    item_price_3 = AllData_2[2][2]
    item_price_4 = AllData_2[3][2]
    item_price_5 = AllData_2[4][2]
    item_price_6 = AllData_2[5][2]
    item_stock_1 = int(AllData_2[0][3])
    item_stock_2 = int(AllData_2[1][3])
    item_stock_3 = int(AllData_2[2][3])
    item_stock_4 = int(AllData_2[3][3])
    item_stock_5 = int(AllData_2[4][3])
    item_stock_6 = int(AllData_2[5][3])

#Sets the text color of food with stock avaliable to green, otherwise to red
def Set_Item_Color():
    global item_stock_1
    global item_stock_2
    global item_stock_3
    global item_stock_4
    global item_stock_5
    global item_stock_6
    global item_color_1
    global item_color_2
    global item_color_3
    global item_color_4
    global item_color_5
    global item_color_6

    if item_stock_1 == 0:
        item_color_1 = "red"
    else:
        item_color_1 = "green"
    if item_stock_2 == 0:
        item_color_2 = "red"
    else:
        item_color_2 = "green"
    if item_stock_3 == 0:
        item_color_3 = "red"
    else:
        item_color_3 = "green"
    if item_stock_4 == 0:
        item_color_4 = "red"
    else:
        item_color_4 = "green"
    if item_stock_5 == 0:
        item_color_5 = "red"
    else:
        item_color_5 = "green"
    if item_stock_6 == 0:
        item_color_6 = "red"
    else:
        item_color_6 = "green"

#Extracts all data from the csv file and returns it in a list
def Get_Data():
    fp = open("VM_Database.csv","r")
    AllData = fp.readlines()
    Items_in_VM_Database = len(AllData)
    fp.close()
    return(AllData)

#Writes the parameter's data into the csv file
def WriteData(Data):
    fp = open("VM_Database.csv","w")
    fp.writelines(Data)
    fp.close()

#Adds or minuses the stock count of the specific food item depending on the situation
def Edit_Data(Item_Number,Plus_or_Minus):
    global item_stock_1
    global item_stock_2
    global item_stock_3
    global item_stock_4
    global item_stock_5
    global item_stock_6

    Data = Get_Data()

    if Plus_or_Minus == "+":
        Number = 1
    elif Plus_or_Minus == "-":
        Number = -1

    if Item_Number == 1:
        stock = item_stock_1 + Number
        Line = Data[0]
        Line = Line.split(",")
        Line[3] = str(stock)
        Line[3] = Line[3] + "\n"
        Line = Line[0]+","+Line[1]+","+Line[2]+","+Line[3]
        Data[0] = Line
        WriteData(Data)
    elif Item_Number == 2:
        stock = item_stock_2 + Number
        Line = Data[1]
        Line = Line.split(",")
        Line[3] = str(stock)
        Line[3] = Line[3] + "\n"
        Line = Line[0]+","+Line[1]+","+Line[2]+","+Line[3]
        Data[1] = Line
        WriteData(Data)
    elif Item_Number == 3:
        stock = item_stock_3 + Number
        Line = Data[2]
        Line = Line.split(",")
        Line[3] = str(stock)
        Line[3] = Line[3] + "\n"
        Line = Line[0]+","+Line[1]+","+Line[2]+","+Line[3]
        Data[2] = Line
        WriteData(Data)
    elif Item_Number == 4:
        stock = item_stock_4 + Number
        Line = Data[3]
        Line = Line.split(",")
        Line[3] = str(stock)
        Line[3] = Line[3] + "\n"
        Line = Line[0]+","+Line[1]+","+Line[2]+","+Line[3]
        Data[3] = Line
        WriteData(Data)
    elif Item_Number == 5:
        stock = item_stock_5 + Number
        Line = Data[4]
        Line = Line.split(",")
        Line[3] = str(stock)
        Line[3] = Line[3] + "\n"
        Line = Line[0]+","+Line[1]+","+Line[2]+","+Line[3]
        Data[4] = Line
        WriteData(Data)
    elif Item_Number == 6:
        stock = item_stock_6 + Number
        Line = Data[5]
        Line = Line.split(",")
        Line[3] = str(stock)
        Line[3] = Line[3] + "\n"
        Line = Line[0]+","+Line[1]+","+Line[2]+","+Line[3]
        Data[5] = Line
        WriteData(Data)

#Initiates all widgets including buttons and labels
def Initiate_Widgets():
    global root
    global background_image
    global background_label
    global canvas1
    global WordLabel
    global Food_Dispense_Slot
    global stage
    global item_name_1
    global item_name_2
    global item_name_3
    global item_name_4
    global item_name_5
    global item_name_6
    global item_color_1
    global item_color_2
    global item_color_3
    global item_color_4
    global item_color_5
    global item_color_6
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global Pay_Button
    global Reset_Button

    stage = 1
    root = Tk()
    root.title("Vending Machine Simulator")
    root.geometry("1000x1000")

    background_image = tk.PhotoImage(file = "Tk_bg.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    canvas1 = tk.Canvas(root, width = 500, height = 800)
    canvas1.place(relx=0.25,rely=0.2)

    WordLabel = Label(canvas1, text="This is a vending machine, what item would you like to choose?", fg = "black", relief="solid")
    WordLabel.config(font=("Courier", 10))
    WordLabel.place(relwidth=0.9, relheight=0.08, relx=0.05, rely=0.01)

    Food_Dispense_Slot = tk.Canvas(canvas1, bg = "dark grey")
    Food_Dispense_Slot.place(relwidth=0.8, relheight=0.1, relx=0.1, rely = 0.55)

    button1 = Button(canvas1, text=item_name_1, fg=item_color_1, command=lambda:button_func(1,stage))
    button1.config(font=("Courier",10))
    button1.place(relwidth=0.333, relheight=0.1, relx=0, rely=0.15)
    button2 = Button(canvas1, text=item_name_2, fg=item_color_2, command=lambda:button_func(2,stage))
    button2.config(font=("Courier",10))
    button2.place(relwidth=0.333, relheight=0.1, relx=0.333, rely=0.15)
    button3 = Button(canvas1, text=item_name_3, fg=item_color_3, command=lambda:button_func(3,stage))
    button3.config(font=("Courier",10))
    button3.place(relwidth=0.333, relheight=0.1, relx=0.666, rely=0.15)

    button4 = Button(canvas1, text=item_name_4, fg=item_color_4, command=lambda:button_func(4,stage))
    button4.config(font=("Courier",10))
    button4.place(relwidth=0.333, relheight=0.1, relx=0, rely=0.29)
    button5 = Button(canvas1, text=item_name_5, fg=item_color_5, command=lambda:button_func(5,stage))
    button5.config(font=("Courier",10))
    button5.place(relwidth=0.333, relheight=0.1, relx=0.333, rely=0.29)
    button6 = Button(canvas1, text=item_name_6, fg=item_color_6, command=lambda:button_func(6,stage))
    button6.config(font=("Courier",10))
    button6.place(relwidth=0.333, relheight=0.1, relx=0.666, rely=0.29)

    Pay_Button = Button(canvas1, text="Add Stock", fg="Blue", command=lambda:button_func("Edit/Pay",stage))
    Pay_Button.config(font=("Courier",12))
    Pay_Button.place(relwidth=0.333, relheight=0.1, relx=0.333, rely=0.43)

    Reset_Button = Button(canvas1, text="Buy another item", fg="blue", command=lambda:button_func("Reset",stage))
    Reset_Button.config(font=("Courier",10))
    Reset_Button.place(relwidth=0.2, relheight=0.05, relx=0, rely=0.43)
    Reset_Button["state"] = "disabled"

#Stage 1: User Selects Item
def stage_1(button_number,stock_count="Null"):
    global item_name_1
    global item_name_2
    global item_name_3
    global item_name_4
    global item_name_5
    global item_name_6
    global item_price_1
    global item_price_2
    global item_price_3
    global item_price_4
    global item_price_5
    global item_price_6
    global stage
    global Item_No
    global Name
    global Price
    global WordLabel
    global Pay_Button
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6

    if button_number == 1:
        Name = item_name_1
        Price = item_price_1
        Item_No = 1
    elif button_number == 2:
        Name = item_name_2
        Price = item_price_2
        Item_No = 2
    elif button_number == 3:
        Name = item_name_3
        Price = item_price_3
        Item_No = 3
    elif button_number == 4:
        Name = item_name_4
        Price = item_price_4
        Item_No = 4
    elif button_number == 5:
        Name = item_name_5
        Price = item_price_5
        Item_No = 5
    elif button_number == 6:
        Name = item_name_6
        Price = item_price_6
        Item_No = 6
    elif button_number == "Edit/Pay":
        button1.config(fg="blue")
        button2.config(fg="blue")
        button3.config(fg="blue")
        button4.config(fg="blue")
        button5.config(fg="blue")
        button6.config(fg="blue")
        WordLabel.config(text="Click to add a food item")
        Pay_Button.config(text="Return to buying items", fg="red")

        stage = "Edit"
    if isinstance(button_number,int) and button_number >= 1 and button_number <= 6:
        if stock_count > 0:
            WordLabel.config(text=("Selected "+Name+", "+"Please Pay $"+Price))
            Pay_Button.config(text=("Pay for Item"))
            button1["state"] = "disabled"
            button2["state"] = "disabled"
            button3["state"] = "disabled"
            button4["state"] = "disabled"
            button5["state"] = "disabled"
            button6["state"] = "disabled"
            stage = stage + 1
        else:
            WordLabel.config(text=("Sorry, "+Name+", is currently unavaliable"))
    elif button_number == "Edit/Pay":
        pass

#Stage 2: User pays for the item and the item is dispensed
def stage_2(button_number):
    global WordLabel
    global Pay_Button
    global Reset_Button
    global Food_Box
    global Name
    global stage
    global Item_No
    global Food_Box
    global Food_Package

    if Item_No == 1:
        selected = item_name_1
        stock = str(item_stock_1 - 1)
    elif Item_No == 2:
        selected = item_name_2
        stock = str(item_stock_2 - 1)
    elif Item_No == 3:
        selected = item_name_3
        stock = str(item_stock_3 - 1)
    elif Item_No == 4:
        selected = item_name_4
        stock = str(item_stock_4 - 1)
    elif Item_No == 5:
        selected = item_name_5
        stock = str(item_stock_5 - 1)
    elif Item_No == 6:
        selected = item_name_6
        stock = str(item_stock_6 - 1)

    if isinstance(button_number,str) and button_number == "Edit/Pay":
        WordLabel.config(text=("Thanks for purchasing 1 "+selected+" \n"+"There "+Is_or_Are(stock)+" now "+stock+" of "+selected))

        Food_Box = tk.Canvas(Food_Dispense_Slot, bg = "grey")
        Food_Box.place(relwidth=0.5, relheight=0.5, relx=0.25, rely = 0.4)

        selected = "This box includes:\n"+selected
        Food_Package = Label(Food_Box, text=selected, fg="black", bg="grey")
        Food_Package.config(font=("Courier", 8))
        Food_Package.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.2)

        Edit_Data(Item_No,"-")

        Update_Files()
        Set_Item_Color()

        Pay_Button["state"] = "disable"
        Reset_Button["state"] = "normal"

        stage = stage + 1

#Stage 3: User resets the vending machine simulator and the simulator returns to stage 1 (simulates buying another item)
def stage_3(button_number):
    global stage
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global Pay_Button
    global Reset_Button
    global WordLabel

    stage = 1
    button1.config(fg = item_color_1)
    button2.config(fg = item_color_2)
    button3.config(fg = item_color_3)
    button4.config(fg = item_color_4)
    button5.config(fg = item_color_5)
    button6.config(fg = item_color_6)
    WordLabel.config(text="This is a vending machine, what item would you like to choose?")
    Pay_Button.config(text="Add Stock")

    button1["state"] = "normal"
    button2["state"] = "normal"
    button3["state"] = "normal"
    button4["state"] = "normal"
    button5["state"] = "normal"
    button6["state"] = "normal"
    Pay_Button["state"] = "normal"
    Reset_Button["state"] = "disabled"

    Food_Box.place(relwidth=0, relheight=0, relx=0.25, rely = 0.4)
    Food_Package.place(relwidth=0, relheight=0, relx=0.1, rely=0.2)

#Stage Edit: User can add onto the stock count for the items (simulates restocking the vending machine)
def stage_edit(button_number):
    global stage
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global item_name_1
    global item_name_2
    global item_name_3
    global item_name_4
    global item_name_5
    global item_name_6
    global item_stock_1
    global item_stock_2
    global item_stock_3
    global item_stock_4
    global item_stock_5
    global item_stock_6
    global Is_or_Are

    if button_number == 1:
        Edit_Data(1,"+")
        Update_Files()
        Set_Item_Color()
        WordLabel.config(text="Added 1 "+item_name_1+" \n"+"There "+Is_or_Are(item_stock_1)+" now "+str(item_stock_1)+" "+item_name_1)
    elif button_number == 2:
        Edit_Data(2,"+")
        Update_Files()
        Set_Item_Color()
        WordLabel.config(text="Added 1 "+item_name_2+" \n"+"There "+Is_or_Are(item_stock_2)+" now "+str(item_stock_2)+" "+item_name_2)
    elif button_number == 3:
        Edit_Data(3,"+")
        Update_Files()
        Set_Item_Color()
        WordLabel.config(text="Added 1 "+item_name_3+" \n"+"There "+Is_or_Are(item_stock_3)+" now "+str(item_stock_3)+" "+item_name_3)
    elif button_number == 4:
        Edit_Data(4,"+")
        Update_Files()
        Set_Item_Color()
        WordLabel.config(text="Added 1 "+item_name_4+" \n"+"There "+Is_or_Are(item_stock_4)+" now "+str(item_stock_4)+" "+item_name_4)
    elif button_number == 5:
        Edit_Data(5,"+")
        Update_Files()
        Set_Item_Color()
        WordLabel.config(text="Added 1 "+item_name_5+" \n"+"There "+Is_or_Are(item_stock_5)+" now "+str(item_stock_5)+" "+item_name_5)
    elif button_number == 6:
        Edit_Data(6,"+")
        Update_Files()
        Set_Item_Color()
        WordLabel.config(text="Added 1 "+item_name_6+" \n"+"There "+Is_or_Are(item_stock_6)+" now "+str(item_stock_6)+" "+item_name_6)

    elif button_number == "Edit/Pay":
        stage = 1
        button1.config(fg = item_color_1)
        button2.config(fg = item_color_2)
        button3.config(fg = item_color_3)
        button4.config(fg = item_color_4)
        button5.config(fg = item_color_5)
        button6.config(fg = item_color_6)
        Pay_Button.config(text="Add Stock", fg="blue")
        WordLabel.config(text="This is a vending machine, what item would you like to choose?")

#Button_func: The function that each button is linked towards (Includes usage of all 4 stages):
def button_func(button_number, old_stage):
    global stage
    global WordLabel
    global Food_Dispense_Slot
    global selected
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global Pay_Button
    global item_name_1
    global item_name_2
    global item_name_3
    global item_name_4
    global item_name_5
    global item_name_6
    global Item_No
    global AllData
    global Stock
    global item_stock_1
    global item_stock_2
    global item_stock_3
    global item_stock_4
    global item_stock_5
    global item_stock_6
    global change
    global item_color_1
    global item_color_2
    global item_color_3
    global item_color_4
    global item_color_5
    global item_color_6

    if old_stage == 1:
        if button_number == 1:
            stage_1(button_number,item_stock_1)
        elif button_number == 2:
            stage_1(button_number,item_stock_2)
        elif button_number == 3:
            stage_1(button_number,item_stock_3)
        elif button_number == 4:
            stage_1(button_number,item_stock_4)
        elif button_number == 5:
            stage_1(button_number,item_stock_5)
        elif button_number == 6:
            stage_1(button_number,item_stock_6)
        elif button_number == "Edit/Pay":
            stage_1(button_number)

    elif old_stage == 2:
        stage_2(button_number)

    elif old_stage == 3:
        stage_3(button_number)

    elif old_stage == "Edit":
        if button_number == 1:
            stage_edit(button_number)
        elif button_number == 2:
            stage_edit(button_number)
        elif button_number == 3:
            stage_edit(button_number)
        elif button_number == 4:
            stage_edit(button_number)
        elif button_number == 5:
            stage_edit(button_number)
        elif button_number == 6:
            stage_edit(button_number)
        elif button_number == "Edit/Pay":
            stage_edit(button_number)

#All the code compiled into 1 function
def All_Code():
    Update_Files()
    Set_Item_Color()
    Initiate_Widgets()

#Runs the program
All_Code()

#The main loop of the tkinter module for this program
root.mainloop()
