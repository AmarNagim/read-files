import yaml
from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
import time
import tkinter.messagebox as messagebox
import time
import sys


window = Tk()

hoorntjeOrBakjeGlobalList = []
bolletjesGlobalList = 0
literIceGlobalList = 0

flavourUserInputList = {
    'aardbei':0, 
    'chocolade':0, 
    'munt':0, 
    'vanille':0
    }
    
toppingUserInputList = {
    'geen':0,
    'slagroom':0,
    'sprinkels':0, 
    'caramel saus':0
    }


def main():
    window.geometry('500x200')
    window.title('Papi Gelato')
    for widgets in window.winfo_children():
        widgets.destroy()
    def destroyPage():
        for widgets in window.winfo_children():
            widgets.destroy()

    
    titleFrame = Frame(window)
    titleFrame.pack()

    title = Label(titleFrame, text="Welkom bij Papi Gelato", font=("Arial", 20, font.BOLD)).pack(pady=10)

    particulierZakelijkFrame = Frame(window)
    particulierZakelijkFrame.pack()

    particulierZakelijkStringVar = StringVar()
    particulierZakelijkStringVar.set('None')

    particulierZakelijkLabel = Label(particulierZakelijkFrame, text="Bent u een zakelijke of een particuliere klant?").pack(side=LEFT)
    particulierZakelijkRadiobuttonParticulier = Radiobutton(particulierZakelijkFrame, text="particulier", variable=particulierZakelijkStringVar, value='particulier').pack(side=LEFT)
    particulierZakelijkRadiobuttonZakelijk = Radiobutton(particulierZakelijkFrame, text="zakelijk", variable=particulierZakelijkStringVar, value='zakelijk').pack(side=LEFT)

    amountIcecreamFrame = Frame(window)
    amountIcecreamFrame.pack()

    amountIcecreamLabel = Label(amountIcecreamFrame, text="Hoeveel bolletjes wilt u?")
    amountIcecreamEntry = Entry(amountIcecreamFrame, width=5)

    amountIcecreamLiterLabel = Label(amountIcecreamFrame, text="Hoeveel liter ijs wilt u?")
    amountIcecreamLiterEntry = Entry(amountIcecreamFrame, width=5)

    availabilityLabelFrame = Frame(window)
    availabilityLabelFrame.pack()

    availableLabel = Label(availabilityLabelFrame)

    icecreamAvailabilityButtonFrame = Frame(window)
    icecreamAvailabilityButtonFrame.pack()

    def selectionPage():
        global bolletjesGlobalList
        global literIceGlobalList
        destroyPage()
        particulierChoice()
        if amountIcecreamEntryUserInput != '':
            bolletjesGlobalList+= int(amountIcecreamEntryUserInput)
            print(bolletjesGlobalList)
        if amountLiterIceacreamUserInput != '':
            literIceGlobalList+= int(amountLiterIceacreamUserInput)
            print(literIceGlobalList)
        
    def checkAvailabilityFunction():
        global particulierZakelijkUserInput
        global amountIcecreamEntryUserInput
        global amountLiterIceacreamUserInput
        
        particulierZakelijkUserInput = particulierZakelijkStringVar.get()
        amountIcecreamEntryUserInput = amountIcecreamEntry.get()
        amountLiterIceacreamUserInput = amountIcecreamLiterEntry.get()
        
        if particulierZakelijkUserInput == 'particulier':
            if int(amountIcecreamEntryUserInput) < 8:
                availableLabel.config(text=f'We hebben {amountIcecreamEntryUserInput} bolletjes op voorraad', fg='green')
                availableLabel.pack()
                nextPageButton.pack()    

            else:
                availableLabel.config(text=f'Helaas hebben we geen {amountIcecreamEntryUserInput} bolletjes op voorraad', fg='red')
                availableLabel.pack()
                
        else:
            availableLabel.config(text=f'We hebben {amountLiterIceacreamUserInput} liter ijs op voorraad', fg='green')
            availableLabel.pack()  
            nextPageButton.pack()    
    
    icecreamAvailabilityButton = Button(icecreamAvailabilityButtonFrame, command=checkAvailabilityFunction ,text="Bekijk beschikbaarheid")

    nextPageButtonFrame = Frame(window)
    nextPageButtonFrame.pack()
    nextPageButton = Button(nextPageButtonFrame, text='Verder', command=selectionPage)


    def particulierZakelijkFunction(*args):
        icecreamAvailabilityButton.pack()
        particulierZakelijkUserInput = particulierZakelijkStringVar.get()
        if particulierZakelijkUserInput == 'particulier':
            amountIcecreamLiterLabel.forget()
            amountIcecreamLiterEntry.forget()
            amountIcecreamLabel.pack(side=LEFT)
            amountIcecreamEntry.pack(side=LEFT)
        if particulierZakelijkUserInput == 'zakelijk':
            amountIcecreamLabel.forget()
            amountIcecreamEntry.forget()
            amountIcecreamLiterLabel.pack(side=LEFT)
            amountIcecreamLiterEntry.pack(side=LEFT)

    traceCommandParZak = particulierZakelijkStringVar.trace
    traceCommandParZak('w', particulierZakelijkFunction)
    

    def amountOptionMenuFun():
        global flavourStringVar
        global toppingStringVar
        global toppingOptionmenuList
        global flavourOptionmenuList
        particulierZakelijkUserInput
        amountIcecreamEntryUserInput
        amountLiterIceacreamUserInput
        amountOptionMenu = amountIcecreamEntryUserInput + amountLiterIceacreamUserInput
        toppingList = ['geen', 'slagroom', 'sprinkels', 'caramel saus']
        flavourList = ['aardbei', 'chocolade', 'munt', 'vanille']
        toppingOptionmenuList = []
        flavourOptionmenuList = []
        for amount in range(1,int(amountOptionMenu)+1):
            flavourStringVar = StringVar()
            flavourStringVar.set('smaak')
            toppingStringVar = StringVar()
            toppingStringVar.set('topping')
            listAmountFrame = Frame(window)
            listAmountFrame.pack()
            if particulierZakelijkUserInput == 'particulier':
                listAmountLabel = Label(listAmountFrame, text=f'Kies de topping en smaak voor bolletje {amount}').pack(side=LEFT)
                optionMenuToppings = OptionMenu(listAmountFrame, toppingStringVar, *toppingList)
                optionMenuToppings.pack(side=LEFT)
                optionMenuToppings.config(width=7)
                toppingOptionmenuList.append(toppingStringVar)
            else:
                listAmountLabel = Label(listAmountFrame, text=f'Kies de smaak voor liter {amount}').pack(side=LEFT)
            optionMenuFlavours = OptionMenu(listAmountFrame, flavourStringVar, *flavourList)
            optionMenuFlavours.pack(side=LEFT)
            flavourOptionmenuList.append(flavourStringVar)

        addToBaketFrame = Frame(window)
        addToBaketFrame.pack()

        addToBaketButton = Button(addToBaketFrame, text='toevoegen aan winkelwagen', command=addToBasketFunction)
        if particulierZakelijkUserInput == 'zakelijk':
            addToBaketButton.pack()


        def addToBasketButtonAppearFun(*args):
            addToBaketButton.pack()

        traceCommand = hoorntjeOrBakjeStringVar.trace
        traceCommand('w', addToBasketButtonAppearFun) 

        orderAgainFrame = Frame(window)
        orderAgainFrame.pack()
        orderAgainButton = Button(orderAgainFrame, text="opnieuw bestellen", command=main).pack() 

        finishOrderFrame = Frame(window)
        finishOrderFrame.pack()
        finishOrderButton = Button(finishOrderFrame, text="afrekenen", command=endPage).pack()
    
    def addToBasketFunction():
        for i in toppingOptionmenuList:
            toppingChoice = i.get()
            if toppingChoice == 'geen':
                toppingUserInputList['geen'] += 1
            if toppingChoice == 'slagroom':
                toppingUserInputList['slagroom'] += 1
            if toppingChoice == 'sprinkels':
                toppingUserInputList['sprinkels'] +=1
            if toppingChoice == 'caramel saus':
                toppingUserInputList['caramel saus'] +=1  


        for i in flavourOptionmenuList:
            flavourChoice = i.get()
            if flavourChoice == 'aardbei':
                flavourUserInputList['aardbei'] += 1
            if flavourChoice == 'chocolade':
                flavourUserInputList['chocolade'] += 1
            if flavourChoice == 'munt':
                flavourUserInputList['munt'] +=1
            if flavourChoice == 'vanille':
                flavourUserInputList['vanille'] +=1            
        print(toppingUserInputList)
        print(flavourUserInputList)

        hoorntjeOrBakjeGlobalList.append(hoorntjeOrBakjeStringVar.get())
        print(hoorntjeOrBakjeGlobalList)


    def endPage():
        with open("/Users/amarnagim/Library/CloudStorage/OneDrive-DaVinciCollege/Da Vinci College/software_developen/Assignments/jaar_1/periode_1/fase_1/09_data.files.state.save/read-files/settings.yml", "r") as s:
            settings = yaml.safe_load(s)
            print(settings['bolletjes'])
        window.geometry('700x370')    
        for widgets in window.winfo_children():
            widgets.destroy()
        endTitleFrame = Frame(window)
        endTitleFrame.pack()

        endTitleLabel = Label(endTitleFrame, text="Bedankt voor je aankoop. Deze word binnen korte tijd bij je geleverd!", font=('Arial', 18, font.BOLD)).pack(pady=12)

        receiptFrame = Frame(window)
        receiptFrame.pack()

        amountIcecreamEntryUserInput
        hoorntjeOrBakje = hoorntjeOrBakjeStringVar.get()
        bolletjePrice = settings['bolletjes']
        hoorentjePrice = settings['hoorentjes']
        bakjePrice = settings['bakjes']  
        slagroom = settings['toppings']['slagroom']
        if 'bakje' in hoorntjeOrBakjeGlobalList: 
            caramelPrice = settings['toppings']['caramel']['bakje']
        if 'hoorntje' in hoorntjeOrBakjeGlobalList:
            caramelPrice = settings['toppings']['caramel']['hoorentje']
        literPrice = settings['liter']
        btwPrice = settings['btw']
        
        flavourAardbeiAmount = flavourUserInputList['aardbei']
        flavourChocoladeAmount = flavourUserInputList['chocolade']
        flavourMuntAmount = flavourUserInputList['munt']
        flavourVanilleAmount = flavourUserInputList['vanille']

        toppingGeenAmount = toppingUserInputList['geen']
        toppingSlagroomAmount = toppingUserInputList['slagroom']
        toppingSprinkelsAmount = toppingUserInputList['sprinkels']
        toppingCaramelsausAmount = toppingUserInputList['caramel saus']

        subtotalList = []

        receiptTitleLabel = Label(receiptFrame, text='     ---------------------------["Papi Gelato"]---------------------------', font=('Arial', 15, font.BOLD)).pack()
        if particulierZakelijkUserInput == 'zakelijk':
            amountIceCreamUserInputZakelijkPrice = format(float(amountLiterIceacreamUserInput)*literPrice, ".2f")
            subtotalList.append(amountIceCreamUserInputZakelijkPrice)
            receiptLabel = Label(receiptFrame, text=f'      liter                {amountLiterIceacreamUserInput} x €{literPrice}        = €{amountIceCreamUserInputZakelijkPrice}', font=('Arial', 15)).pack()
        if particulierZakelijkUserInput == 'particulier':
            amountIceCreamUserInputParticulierPrice = format(float(amountIcecreamEntryUserInput)*bolletjePrice, ".2f")
            subtotalList.append(amountIceCreamUserInputParticulierPrice)
            receiptLabel = Label(receiptFrame, text=f'      bolletje             {amountIcecreamEntryUserInput} x €{bolletjePrice}        = €{amountIceCreamUserInputParticulierPrice}', font=('Arial', 15)).pack()
        if 'hoorntje' in hoorntjeOrBakjeGlobalList:
            priceHoorntje = format(float(amountIcecreamEntryUserInput)*hoorentjePrice, ".2f")
            subtotalList.append(priceHoorntje)
            receiptLabel = Label(receiptFrame, text=f'      hoorntje(s)          {amountIcecreamEntryUserInput} x €{hoorentjePrice}   = €{priceHoorntje}', font=('Arial', 15)).pack()
        if 'bakje' in hoorntjeOrBakjeGlobalList: 
            priceBakje = format(float(amountIcecreamEntryUserInput)*bakjePrice, ".2f")
            subtotalList.append(priceBakje)
            receiptLabel = Label(receiptFrame, text=f'      bakje(s)          {amountIcecreamEntryUserInput} x €{format(bakjePrice, ".2f")}   = €{priceBakje}', font=('Arial', 15)).pack()
        if flavourAardbeiAmount>0:    
            priceAardbei = format(float(flavourAardbeiAmount)*0.50, ".2f")
            subtotalList.append(priceAardbei)
            receiptLabel = Label(receiptFrame, text=f'      smaak aardbei     {flavourAardbeiAmount} x €0.50   = €{priceAardbei}', font=('Arial', 15)).pack()
        if flavourChocoladeAmount>0:  
            priceChocolade = format(float(flavourChocoladeAmount)*0.75, ".2f")
            subtotalList.append(priceChocolade)
            receiptLabel = Label(receiptFrame, text=f'      smaak chocolade     {flavourChocoladeAmount} x €0.75   = €{priceChocolade}', font=('Arial', 15)).pack()
        if flavourMuntAmount>0:
            priceMunt = format(float(flavourMuntAmount)*0.55, ".2f")
            subtotalList.append(priceMunt)
            receiptLabel = Label(receiptFrame, text=f'      smaak munt     {flavourMuntAmount} x €0.55   = €{priceMunt}', font=('Arial', 15)).pack()
        if flavourVanilleAmount>0:
            priceVanille = format(float(flavourVanilleAmount)*0.60, ".2f")
            subtotalList.append(priceVanille)
            receiptLabel = Label(receiptFrame, text=f'      smaak vanille     {flavourVanilleAmount} x €0.60   = €{priceVanille}', font=('Arial', 15)).pack()
        if toppingSlagroomAmount>0:
            priceSlagroom = format(float(toppingSlagroomAmount)*0.90, ".2f")
            subtotalList.append(priceSlagroom)
            receiptLabel = Label(receiptFrame, text=f'      topping slagroom     {toppingSlagroomAmount} x €0.90   = €{priceSlagroom}', font=('Arial', 15)).pack()
        if toppingSprinkelsAmount>0:
            priceSprinkels = format(float(toppingSprinkelsAmount)*0.85, ".2f")
            subtotalList.append(priceSprinkels)
            receiptLabel = Label(receiptFrame, text=f'      topping sprinkels     {toppingSprinkelsAmount} x €0.85   = €{priceSprinkels}', font=('Arial', 15)).pack()
        if toppingCaramelsausAmount>0:
            priceCaramelsaus = format(float(toppingCaramelsausAmount)*0.87, ".2f")
            subtotalList.append(priceCaramelsaus)
            receiptLabel = Label(receiptFrame, text=f'      topping caramel saus     {toppingCaramelsausAmount} x €0.87   = €{priceCaramelsaus}', font=('Arial', 15)).pack()

        
            
        subtotalListFloats = []

        for item in subtotalList:
            subtotalListFloats.append(float(item))
        print(subtotalListFloats)
        subtotalPrice = format(sum(subtotalListFloats), ".2f")
        btwMultiplyvalue = 100+btwPrice
        totalPrice = format(float(subtotalPrice)/100*btwMultiplyvalue, ".2f")
        receiptLabel = Label(receiptFrame, text=f'          subtotaal                              = €{subtotalPrice}', font=('Arial', 15)).pack()
        receiptLabel = Label(receiptFrame, text=f'          totaal (inc. {btwPrice}% btw)               = €{totalPrice}', font=('Arial', 15)).pack()


            

    def particulierChoice():
        
        global hoorntjeOrBakjeStringVar

        window.geometry('500x350')
        hoorntjeOrBakjeStringVar = StringVar()
        hoorntjeOrBakjeStringVar.set('None')

        hoorntjeOrBakjeFrame = Frame(window)
        hoorntjeOrBakjeFrame.pack()
        if particulierZakelijkUserInput == 'particulier':
            bolletjeOrHoorntjeLabel = Label(hoorntjeOrBakjeFrame, text="Wilt u het ijs in een hoorntje of bakje?").pack(side=LEFT)
            hoorntjeRadiobutton = Radiobutton(hoorntjeOrBakjeFrame, text="hoorntje", variable=hoorntjeOrBakjeStringVar, value='hoorntje').pack(side=LEFT)
            bakjeRadiobutton = Radiobutton(hoorntjeOrBakjeFrame, text="bakje", variable=hoorntjeOrBakjeStringVar, value='bakje').pack(side=LEFT)
        amountOptionMenuFun()
main()
window.mainloop()