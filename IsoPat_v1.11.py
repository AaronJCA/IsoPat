from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure
from pylab import figure, show
import matplotlib.pyplot as plt
import tkinter
import numpy as np
import math
from tkinter import ttk
import re


iconData = '''iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAYAAABw4pVUAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADs
MAAA7DAcdvqGQAAAAYdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjAuOWwzfk4AAAWdSURBVHhe7dwxbp5VEIVhCsoUFCwoBSUFS2A
Z7IIyJT19akroWAJCFBQswlxLHOtN/GrEDLa+CfqKR4iT46M7fyxoLH/28PBwW0TD23U0vF1Hw9t1NLxdR8PbdTS8XUfD23U0vF1H
w9t1NLxdR8P/ox9/eXh7fPv4T/vzLTT8Pzl/AW+On44HePz3L6x/NQ3/jXPQJ/Edd973/cG/jHhn/atpWDmHfFLfceddv+Gd9Kf1r
6Zh5RzySX3HyTufsLeFhpVzyCf1HSfvfMLeFhpW7LBgbwt7Z7C3hYYVOyzY28LeGextoWHFDgv2trB3BntbaFixw4K9Leydwd4WGl
bssGBvC3tnsLeFhhU7LNjbwt4Z7G2hYcUOC/a2sHcGe1toWLHDgr0t7J3B3hYaVuywYG8Le2ewt4WGFTss2NvC3hnsbaFhxQ4L9ra
wdwZ7W2hYscOCvS3sncHeFhpW7LBgbwt7Z7C3hYYVOyzY28LeGextoWHFDgv2trB3BntbaFixw4K9Leydwd4WGlbssGBvC3tnsLeF
hhU7LNjbwt4Z7G2hYcUOC/a2sHcGe1toWLHDgr3/4my92I8Y5W2GvS00rNhhwd7E2XjxHzH6aOsD7G2hYcUOC/YmzsaL/4iRbD1hb
wsNK3ZYsDdxNl78R4xk6wl7W2hYscOCvQnbDPY6bCvY20LDih0W7E3YZrDXYVvB3hYaVuywYG/CNoO9DtsK9rbQsGKHBXsTthnsdd
hWsLeFhhU7LNibsM1gr8O2gr0tNKzYYcHehG0Gex22FextoWHFDgv2Jmwz2OuwrWBvCw0rdliwN2GbwV6HbQV7W2hYscOCvQnbDPY
6bCvY20LDih0W7E3YZrDXYVvB3hYaVuywYG/CNoO9DtsK9rbQsGKHBXsTthnsddhWsLeFhhU7LNibsM1gr8O2gr0tNKzYYcHehG0G
ex22FextoWHFDgv2Jmwz2OuwrWBvCw0rdliwN2GbwV6HbQV7W2hYscOCvQnbDPY6bCvY20LDih0W7E3YZrDXYVvB3hYaVuywYG/CN
oO9DtsK9rbQsGKHBXsTthnsddhWsLeFhhU7LNibsM1gr8O2gr0tNKzYYcHehG0Gex22FexNnI0X/51hGlZyjGFvwjaDvQ7bCvY6zt
e+2u8M07Dy0SM+wN6EbQZ7HbYV7HWcr3213xmmYUUe8YS9CdsM9jpsK9jrOF/7ar8zTMOKPOIJexO2Gex12Faw12Fbwd6EhhV7RLA
3YZvBXodtBXsdthXsTWhYsUcEexO2Gex12Faw12Fbwd6EhhV7RLA3YZvBXodtBXsdthXsTWhYsUcEexO2Gex12Faw12Fbwd6EhhV7
RLA3YZvBXodtBXsdthXsTWhYsUcEexO2Gex12Faw12Fbwd6EhhV7RLA3YZvBXodtBXsdthXsTWhYsUcEexO2Gex12Faw12Fbwd6Eh
hV7RLA3YZvBXodtBXsdthXsTWhYsUcEexO2Gex12Faw12Fbwd6EhhV7RLA3YZvBXodtBXsdthXsTWhYsUcEexO2Gex12Faw12Fbwd
6EhhV7RLA3YZvBXodtBXsdthXsTWhYsUcEexO2Gex12Faw12Fbwd6EhhV7RLA3YZvBXodtBXsdthXsTWhYsUcEexO2Gex12Faw12F
bwd6EhhV7RLA3YZvBXodtBXsdthXsTWhYsUcEexO2Gex12Faw12Fbwd6Ehg/vf39zfH/8djzcXswfx+Pn+kY/90PD8wU//TNwex0/
H5/bZ/8sOMW3+MLb6/n62Wd/PAtO8duPvvD2Or579tkfz4JT/OqjL7y9jm+effbHs+AUPz8e/xtnI7eX8evxL/8f8uj9718c744/D
xu8zfx1/HB8qZ/7oeHtOhrerqPh7Toa3q6j4e06Gt6uo+HtOhrerqPh7SoPn/0NLaKvpXlS//UAAAAASUVORK5CYII=
'''

ionChoices0 = []
ionChoices1 = []
ionChoices2 = []
ionChoices3 = []
ionChoices4 = []
ionChoices5 = []

ionChoices0 = [
    '[M]'
]

ionChoices1 = [
    '[M+H]',
    '[M+]',
    '[M-H2O+H]',
    '[M-2(H2O)+H]',
    '[M-3(H2O)+H]',
    '[M-H2O+Na]',
    '[M-H2O+NH4]',
    '[M+NH4]',
    '[M+Na]',
    '[M+K]',
    '[M+Li]',
    '[M+Ag]',
    '[M-HCl+H]',
    '[M-HBr+H]',
    '[M-SO3+H]',
    '[M-H+Fe2+]',
    '[M-2H+Fe3+]',
    '[2M+H]',
    '[2M+NH4]',
    '[2M+Na]',
    '[2M+K]',
    '[3M+H]',
    '[3M+NH4]',
    '[3M+Na]',
    '[3M+K]',
    '[3M-2H+Fe3+]',
]

ionChoices2 = [
    '[M+2H]',
    '[M-H2O+2H]',
    '[M-2(H2O)+2H]',
    '[M-3(H2O)+2H]',
    '[M+NH4+H]',
    '[M+Na+H]',
    '[M+K+H]',
    '[M+Li+H]',
    '[M+2(NH4)]',
    '[M+2Na]',
    '[M+2K]',
    '[M-HCl+2H]',
    '[M-HBr+2H]',
    '[M-SO3+2H]',
    '[M+Fe2+]',
    '[M-H+Fe3+]',
    '[2M+2H]',
    '[2M+NH4+H]',
    '[2M+Na+H]',
    '[2M+K+H]',
    '[3M+2H]',
    '[3M+NH4+H]',
    '[3M+Na+H]',
    '[3M+K+H]',
    '[3M-H+Fe3+]',
]

ionChoices3 = [
    '[M+3H]',
    '[M-H2O+3H]',
    '[M-2(H2O)+3H]',
    '[M-3(H2O)+3H]',
    '[M+NH4+2H]',
    '[M+Na+2H]',
    '[M+K+2H]',
    '[M+Li+2H]',
    '[M+2(NH4)+H]',
    '[M+2Na+H]',
    '[M+2K+H]',
    '[M+3(NH4)]',
    '[M+3Na]',
    '[M+3K]',
    '[M+NH4+Na+H]',
    '[M+NH4+2Na]',
    '[M+2(NH4)+Na]',
    '[M-HCl+3H]',
    '[M-HBr+3H]',
    '[M-SO3+3H]',
    '[M+H+Fe2+]',
    '[M+Fe3+]',
    '[M+Na+Fe2+]',
    '[M+NH4+Fe2+]',
]

ionChoices4 = [
    '[M+4H]',
    '[M-H2O+4H]',
    '[M-2(H2O)+4H]',
    '[M-3(H2O)+4H]',
    '[M+NH4+3H]',
    '[M+Na+3H]',
    '[M+K+3H]',
    '[M+Li+3H]',
    '[M+2(NH4)+2H]',
    '[M+2Na+2H]',
    '[M+2K+2H]',
    '[M+3(NH4)+H]',
    '[M+3Na+H]',
    '[M+3K+H]',
    '[M+4(NH4)]',
    '[M+4Na]',
    '[M+4K]',
    '[M+NH4+Na+2H]',
    '[M+NH4+2Na+H]',
    '[M+2(NH4)+Na+H]',
    '[M-HCl+4H]',
    '[M-HBr+4H]',
    '[M-SO3+4H]',
    '[M+2H+Fe2+]',
    '[M+Na+H+Fe2+]',
    '[M+NH4+H+Fe2+]',
    '[M+H+Fe3+]',
    '[M+Na+Fe3+]',
    '[M+NH4+Fe3+]',
]

ionChoices5 = [
    '[M+5H]',
    '[M-H2O+5H]',
    '[M-2(H2O)+5H]',
    '[M-3(H2O)+5H]',
    '[M+NH4+4H]',
    '[M+Na+4H]',
    '[M+K+4H]',
    '[M+2(NH4)+3H]',
    '[M+2Na+3H]',
    '[M+2K+3H]',
    '[M+3(NH4)+2H]',
    '[M+3Na+2H]',
    '[M+3K+2H]',
    '[M+4(NH4)+H]',
    '[M+4Na+H]',
    '[M+4K+H]',
    '[M+5(NH4)]',
    '[M+5Na]',
    '[M+5K]',
    '[M+NH4+Na+3H]',
    '[M+NH4+2Na+2H]',
    '[M+2(NH4)+Na+2H]',
    '[M-HCl+5H]',
    '[M-HBr+5H]',
    '[M-SO3+5H]',
    '[M+3H+Fe2+]',
    '[M+Na+2H+Fe2+]',
    '[M+NH4+2H+Fe2+]',
    '[M+2Na+H+Fe2+]',
    '[M+2(NH4)+H+Fe2+]',
    '[M+2H+Fe3+]',
    '[M+Na+H+Fe3+]',
    '[M+NH4+H+Fe3+]',
    '[M+2Na+Fe3+]',
    '[M+2(NH4)+Fe3+]'
]


ionChoices6 = []
ionChoices7 = []
ionChoices8 = []
ionChoices9 = []
ionChoices10 = []

ionChoices6 = [
    '[M-H]',
    '[M-]',
    '[M+HCOOH-H]',
    '[M+CH3COOH-H]',
    '[M+Na+HCOOH-2H]',
    '[M+Na+CH3COOH-2H]',
    '[M-H2O-H]',
    '[M-2(H2O)-H]',
    '[M-3(H2O)-H]',
    '[M+NH4-2H]',
    '[M+Na-2H]',
    '[M+K-2H]',
    '[M+Cl]',
    '[M+Br]',
    '[M+NaCl+Cl]',
    '[M+NaCl+HCOOH-H]',
    '[M+Na+2(HCOOH)-2H]',
    '[2M-H]',
    '[2M+NH4-2H]',
    '[2M+Na-2H]',
    '[2M+K-2H]',
]

ionChoices7 = [
    '[M-2H]',
    '[M+HCOOH-2H]',
    '[M+CH3COOH-2H]',
    '[M+Na+HCOOH-3H]',
    '[M+Na+CH3COOH-3H]',
    '[M-H2O-2H]',
    '[M-2(H2O)-2H]',
    '[M-3(H2O)-2H]',
    '[M+NH4-3H]',
    '[M+Na-3H]',
    '[M+K-3H]',
    '[M+Cl-H]',
    '[M+2Cl]',
    '[M+Br-H]',
    '[M+2Br]',
]

ionChoices8 = [
    '[M-3H]',
    '[M+HCOOH-3H]',
    '[M+CH3COOH-3H]',
    '[M+Na+HCOOH-4H]',
    '[M+Na+CH3COOH-4H]',
    '[M-H2O-3H]',
    '[M-2(H2O)-3H]',
    '[M-3(H2O)-3H]',
    '[M+NH4-4H]',
    '[M+Na-4H]',
    '[M+K-4H]',
    '[M+Cl-2H]', 
    '[M+3Cl]',
    '[M+Br-2H]',
    '[M+3Br]',
]

ionChoices9 = [
    '[M-4H]',
    '[M+HCOOH-4H]',
    '[M+CH3COOH-4H]',
    '[M+Na+HCOOH-5H]',
    '[M+Na+CH3COOH-5H]',
    '[M-H2O-4H]',
    '[M-2(H2O)-4H]',
    '[M-3(H2O)-4H]',
    '[M+NH4-5H]',
    '[M+Na-5H]',
    '[M+K-5H]',
    '[M+Cl-3H]',
    '[M+4Cl]',
    '[M+Br-3H]',
    '[M+4Br]',
]

ionChoices10 = [
    '[M-5H]',
    '[M+HCOOH-5H]',
    '[M+CH3COOH-5H]',
    '[M+Na+HCOOH-6H]',
    '[M+Na+CH3COOH-6H]',
    '[M-H2O-5H]',
    '[M-2(H2O)-5H]',
    '[M-3(H2O)-5H]',
    '[M+NH4-6H]',
    '[M+Na-6H]',
    '[M+K-6H]',
    '[M+Cl-4H]',
    '[M+5Cl]',
    '[M+Br-4H]',
    '[M+5Br]',
]

class simpleapp_tk(tkinter.Tk):
    def __init__(primary,parent):
        tkinter.Tk.__init__(primary,parent)
        primary.parent = parent
        primary.initialize()
        primary.update()
        primary.minsize(primary.winfo_width(), primary.winfo_height())

    def initialize(primary):
        primary.grid()
        primary.grid_rowconfigure(25,weight=1)
        primary.grid_columnconfigure(1,weight=1)
        primary.grid_columnconfigure(2,weight=1) 

        primary.userForm = StringVar()
        primary.chargeState = StringVar()
        primary.numOfAdducts = StringVar()
        primary.userMZ = StringVar()
        primary.carbonAbund = StringVar()
        primary.resolution = StringVar()
        primary.errorMessage = tkinter.StringVar()
        primary.adductIonStr = StringVar()
        primary.coAdductIonStr = StringVar()
        primary.massList = []
        primary.abundanceList = []
        primary.A2IonStr = StringVar()
        primary.A3IonStr = StringVar()
        primary.A4IonStr = StringVar()
        primary.A2abnd = StringVar()
        primary.A3abnd = StringVar()
        primary.A4abnd = StringVar()
        primary.A2cState = StringVar()
        primary.A3cState = StringVar()
        primary.A4cState = StringVar()
        primary.numOfC13 = StringVar()
        primary.numOfN15 = StringVar()
        primary.numOfH2 = StringVar()
        primary.coNumOfC13 = StringVar()
        primary.coNumOfN15 = StringVar()
        primary.coNumOfH2 = StringVar()
        primary.coCarbonAbund = StringVar()
        primary.userCoForm = StringVar()
        primary.coChargeState = StringVar()
        primary.coCompoundNum = StringVar()
        primary.coComAbnd = StringVar()
        primary.labelCutOffPC = StringVar()
        primary.chargeMode = StringVar()
        color = '0.9'

        plotFrame = Frame(primary, width=654, height=500)
        plotFrame.grid_propagate(False)
        plotFrame.grid_rowconfigure(25, weight=1)
        plotFrame.grid_columnconfigure(1, weight=1)
        plotFrame.grid(row=1, column=1, columnspan=2, rowspan=25, sticky="neswn")


        fig = Figure()
        rect = fig.patch
        rect.set_facecolor(color)

        primary.canvas = FigureCanvasTkAgg(fig, plotFrame)
        primary.canvas.get_tk_widget().grid(row=1, column=1, columnspan=2, rowspan=25, sticky="neswn")

        toolbar_frame = Frame(primary)
        toolbar_frame.grid(row = 0, column = 1, columnspan=5, sticky=W)
        toolbar = NavigationToolbar2Tk(primary.canvas, toolbar_frame)
        toolbar.grid(row=0, column=1, columnspan=5, sticky=W)
        toolbar.update()
        
        primary.ax2 = fig.add_subplot(1,1,1)
        primary.ax2.set_xlabel('Mass to charge (m/z)')
        primary.ax2.set_title('Isotope Pattern')
        primary.ax2.set_ylabel('Relative Abundance')
        primary.canvas.draw()

        primary.compoundLabel = Label(primary, text="Molecular formula:")
        primary.compoundLabel.grid(row=3, column=3, sticky=E)
        primary.mzEntry = Entry(primary, width=22, textvariable=primary.userForm)
        primary.mzEntry.bind('<Return>', primary.grph)# Added to allow enter pressing to generate
        primary.mzEntry.grid(row=3, column=4, sticky=W)
        
        primary.adNumLabel = Label(primary, text="# of adducts:")
        primary.adNumLabel.grid(row=5, column=3, sticky=E)
        primary.adNumVal = Spinbox(primary, from_=1, to=4, textvariable=primary.numOfAdducts, width=2, command=primary.AdductRefresh)
        primary.adNumVal.grid(row=5, column=4, sticky=W)

        primary.extraC13Label = Label(primary, text="Incorporated 13C:")
        primary.extraC13Label.grid(row=3, column=5, sticky=E)
        primary.extraC13Val = Spinbox(primary, from_=0, to=20, textvariable=primary.numOfC13, width=2)
        primary.extraC13Val.grid(row=3, column=6, sticky=W)

        primary.carbonLabel = Label(primary, text="13C abundance:")
        primary.carbonLabel.grid(row=3, column=7, sticky=E) 
        primary.carbonVal = Entry(primary, textvariable=primary.carbonAbund, width=5)
        primary.carbonVal.grid(row=3, column=8, sticky=W)
        primary.carbonVal.insert(0, 1.07)
        primary.carbonVal.bind('<Return>', primary.grph)
        primary.carbonValPcLabel = Label(primary, text="%")
        primary.carbonValPcLabel.grid(row=3, column=9, sticky=E)

        primary.extraC13Label = Label(primary, text="15N:")
        primary.extraC13Label.grid(row=4, column=5, sticky=E)
        primary.extraC13Val = Spinbox(primary, from_=0, to=20, textvariable=primary.numOfN15, width=2)
        primary.extraC13Val.grid(row=4, column=6, sticky=W)

        primary.extraC13Label = Label(primary, text="2H:")
        primary.extraC13Label.grid(row=5, column=5, sticky=E)
        primary.extraC13Val = Spinbox(primary, from_=0, to=20, textvariable=primary.numOfH2, width=2)
        primary.extraC13Val.grid(row=5, column=6, sticky=W)

        primary.ionAdLabel = Label(primary, text="Ion adduct:")
        primary.ionAdLabel.grid(row=7, column=3, sticky=E)
        primary.adductOptions = ttk.Combobox(primary, state='readonly', width=22, textvariable=primary.adductIonStr)
        primary.adductOptions["values"] = ionChoices1
        primary.adductOptions.set("[M+H]")
        primary.adductOptions.grid(row=7, column=4, sticky=W)
        primary.adductOptions.bind('<Return>', primary.grph)

        primary.chargeLabel = Label(primary, text="Ion charge:")
        primary.chargeLabel.grid(row=7, column=5, sticky=E)
        primary.chargeState.set("1")
        primary.chargeVal = Spinbox(primary, from_=0, to=5, textvariable=primary.chargeState, width=2, command=primary.ionAdList)
        primary.chargeVal.grid(row=7, column=6, sticky=W)

        primary.ionAbundLabel = Label(primary, text="Abundance:")
        primary.ionAbundLabel.grid(row=7, column=7, sticky=E)
        primary.ionAbundVal = Entry(primary, width=5)
        primary.ionAbundVal.grid(row=7, column=8, sticky=W)
        primary.ionAbundVal.insert(0, 100)
        primary.ionAbundVal.configure(state="disabled")
        primary.ionAbundPcLabel = Label(primary, text="%")
        primary.ionAbundPcLabel.grid(row=7, column=9, sticky=E)

        #####Adduct2

        primary.ionAdLabelA2 = Label(primary, text="Adduct #2:")
        primary.ionAdLabelA2.grid(row=8, column=3, sticky=E)
        primary.adductOptionsA2 = ttk.Combobox(primary, state='readonly', width=22, textvariable=primary.A2IonStr)
        primary.adductOptionsA2["values"] = ionChoices1 #startIons
        primary.adductOptionsA2.set("[M+H]")
        primary.adductOptionsA2.grid(row=8, column=4, sticky=W)
        primary.adductOptionsA2.configure(state="disabled")
        primary.adductOptionsA2.bind('<Return>', primary.grph)
        
        primary.A2cState.set("1")
        primary.A2chargeVal = Spinbox(primary, from_=0, to=5, textvariable=primary.A2cState, width=2, command=primary.ionAdListA2)
        primary.A2chargeVal.grid(row=8, column=6, sticky=W)
        primary.A2chargeVal.configure(state="disabled")

        primary.A2AbundVal = Entry(primary, textvariable=primary.A2abnd, width=5)
        primary.A2AbundVal.grid(row=8, column=8, sticky=W)
        primary.A2AbundVal.insert(0, 100)
        primary.A2AbundVal.bind('<Return>', primary.grph)
        primary.A2AbundVal.configure(state="disabled")
        primary.A2AbundPcLabel = Label(primary, text="%")
        primary.A2AbundPcLabel.grid(row=8, column=9, sticky=E)

        #####Adduct3

        primary.ionAdLabelA3 = Label(primary, text="Adduct #3:")
        primary.ionAdLabelA3.grid(row=9, column=3, sticky=E)
        primary.adductOptionsA3 = ttk.Combobox(primary, state='readonly', width=22, textvariable=primary.A3IonStr)
        primary.adductOptionsA3["values"] = ionChoices1 #startIons
        primary.adductOptionsA3.set("[M+H]")
        primary.adductOptionsA3.grid(row=9, column=4, sticky=W)
        primary.adductOptionsA3.configure(state="disabled")
        primary.adductOptionsA3.bind('<Return>', primary.grph)

        primary.A3cState.set("1")
        primary.A3chargeVal = Spinbox(primary, from_=0, to=5, textvariable=primary.A3cState, width=2, command=primary.ionAdListA3)
        primary.A3chargeVal.grid(row=9, column=6, sticky=W)
        primary.A3chargeVal.configure(state="disabled")

        primary.A3AbundVal = Entry(primary, textvariable=primary.A3abnd, width=5)
        primary.A3AbundVal.grid(row=9, column=8, sticky=W)
        primary.A3AbundVal.insert(0, 100)
        primary.A3AbundVal.bind('<Return>', primary.grph)
        primary.A3AbundVal.configure(state="disabled")
        primary.A3AbundPcLabel = Label(primary, text="%")
        primary.A3AbundPcLabel.grid(row=9, column=9, sticky=E)

        #####Adduct4
        
        primary.ionAdLabelA4 = Label(primary, text="Adduct #4:")
        primary.ionAdLabelA4.grid(row=10, column=3, sticky=E)
        primary.adductOptionsA4 = ttk.Combobox(primary, state='readonly', width=22, textvariable=primary.A4IonStr)
        primary.adductOptionsA4["values"] = ionChoices1 #startIons
        primary.adductOptionsA4.set("[M+H]")
        primary.adductOptionsA4.grid(row=10, column=4, sticky=W)
        primary.adductOptionsA4.configure(state="disabled")
        primary.adductOptionsA4.bind('<Return>', primary.grph)

        primary.A4cState.set("1")
        primary.A4chargeVal = Spinbox(primary, from_=0, to=5, textvariable=primary.A4cState, width=2, command=primary.ionAdListA4)
        primary.A4chargeVal.grid(row=10, column=6, sticky=W)
        primary.A4chargeVal.configure(state="disabled")

        primary.A4AbundVal = Entry(primary, textvariable=primary.A4abnd, width=5)
        primary.A4AbundVal.grid(row=10, column=8, sticky=W)
        primary.A4AbundVal.insert(0, 100)
        primary.A4AbundVal.bind('<Return>', primary.grph)
        primary.A4AbundVal.configure(state="disabled")
        primary.A4AbundPcLabel = Label(primary, text="%")
        primary.A4AbundPcLabel.grid(row=10, column=9, sticky=E)

        #####Co-Compound

        primary.coCompoundLabel = Label(primary, text="Coeluting compounds:")
        primary.coCompoundLabel.grid(row=11, column=3, sticky=E+S, pady=10)
        primary.coCompoundVal = Spinbox(primary, from_=0, to=1, textvariable=primary.coCompoundNum, width=2, command=primary.AdductRefresh)
        primary.coCompoundVal.grid(row=11, column=4, sticky=W)

        primary.coCompoundLabel = Label(primary, text="Molecular formula:")
        primary.coCompoundLabel.grid(row=12, column=3, sticky=E)
        primary.coMZEntry = Entry(primary, width=22, textvariable=primary.userCoForm)
        primary.coMZEntry.grid(row=12, column=4, sticky=W)
        primary.coMZEntry.configure(state="disabled")
        primary.coMZEntry.bind('<Return>', primary.grph)

        primary.coExtraC13Label = Label(primary, text="Incorporated 13C:")
        primary.coExtraC13Label.grid(row=12, column=5, sticky=E)
        primary.coExtraC13Val = Spinbox(primary, from_=0, to=20, textvariable=primary.coNumOfC13, width=2)
        primary.coExtraC13Val.grid(row=12, column=6, sticky=W)
        primary.coExtraC13Val.configure(state="disabled")

        primary.coExtraN15Label = Label(primary, text="15N:")
        primary.coExtraN15Label.grid(row=13, column=5, sticky=E)
        primary.coExtraN15Val = Spinbox(primary, from_=0, to=20, textvariable=primary.coNumOfN15, width=2)
        primary.coExtraN15Val.grid(row=13, column=6, sticky=W)
        primary.coExtraN15Val.configure(state="disabled")

        primary.coExtraH2Label = Label(primary, text="2H")
        primary.coExtraH2Label.grid(row=14, column=5, sticky=E)
        primary.coExtraH2Val = Spinbox(primary, from_=0, to=20, textvariable=primary.coNumOfH2, width=2)
        primary.coExtraH2Val.grid(row=14, column=6, sticky=W)
        primary.coExtraH2Val.configure(state="disabled")

        primary.coCarbonLabel = Label(primary, text="13C abundance:")
        primary.coCarbonLabel.grid(row=12, column=7, sticky=E) 
        primary.coCarbonVal = Entry(primary, textvariable=primary.coCarbonAbund, width=5)
        primary.coCarbonVal.grid(row=12, column=8, sticky=W)
        primary.coCarbonVal.insert(0, 1.07)
        primary.coCarbonVal.configure(state="disabled")
        primary.coCarbonVal.bind('<Return>', primary.grph)
        primary.coCarbonValPcLabel = Label(primary, text="%")
        primary.coCarbonValPcLabel.grid(row=12, column=9, sticky=E)

        primary.coIonAdLabel = Label(primary, text="Co-Ion adduct:")
        primary.coIonAdLabel.grid(row=15, column=3, sticky=E)
        primary.coAdductOptions = ttk.Combobox(primary, state='readonly', width=22, textvariable=primary.coAdductIonStr)
        primary.coAdductOptions["values"] = ionChoices1 #startIons
        primary.coAdductOptions.set("[M+H]")
        primary.coAdductOptions.grid(row=15, column=4, sticky=W)
        primary.coAdductOptions.configure(state="disabled")
        primary.coAdductOptions.bind('<Return>', primary.grph)

        primary.coChargeLabel = Label(primary, text="Ion charge:")
        primary.coChargeLabel.grid(row=15, column=5, sticky=E)
        primary.coChargeState.set("1")
        primary.coChargeVal = Spinbox(primary, from_=0, to=5, textvariable=primary.coChargeState, width=2, command=primary.ionAdListCoCom)
        primary.coChargeVal.grid(row=15, column=6, sticky=W)
        primary.coChargeVal.configure(state="disabled")

        primary.coIonAbundLabel = Label(primary, text="Abundance:")
        primary.coIonAbundLabel.grid(row=15, column=7, sticky=E)
        primary.coIonAbundVal = Entry(primary, textvariable=primary.coComAbnd, width=5)
        primary.coIonAbundVal.grid(row=15, column=8, sticky=W)
        primary.coIonAbundVal.insert(0, 100)
        primary.coIonAbundVal.bind('<Return>', primary.grph)
        primary.coIonAbundVal.configure(state="disabled")
        primary.coIonAbundPcLabel = Label(primary, text="%")
        primary.coIonAbundPcLabel.grid(row=15, column=9, sticky=E)

        ######Mass and Abundance Box

        primary.txt = Text(primary, borderwidth=3, relief="sunken")
        primary.txt.config(font=("consolas", 11), undo=True, wrap='word', width=50, height=15)
        primary.txt.grid(row=20, column=4, columnspan=4, rowspan=4, sticky=E, padx=2, pady=5)
        primary.txt.configure(state="disabled")
        scrollb = Scrollbar(primary, command=primary.txt.yview)
        scrollb.grid(row=20, column=8, rowspan=4, sticky=W+N+S, pady=5)
        primary.txt['yscrollcommand'] = scrollb.set

        ######Below Graph

        primary.resLabel = Label(primary, text="Resolution:")
        primary.resLabel.grid(row=26, column=1, sticky=E)
        primary.resVal = Entry(primary, textvariable=primary.resolution, width=10)
        primary.resVal.grid(row=26, column=2, sticky=W)
        primary.resVal.insert(0, 45000)
        primary.resVal.bind('<Return>', primary.grph)

        primary.cutOffLabel = Label(primary, text="Label cut off %:")
        primary.cutOffLabel.grid(row=28, column=1, sticky=E) 
        primary.cutOfVal = Entry(primary, textvariable=primary.labelCutOffPC, width=10)
        primary.cutOfVal.grid(row=28, column=2, sticky=W)
        primary.cutOfVal.insert(0, 99.0)
        primary.cutOfVal.bind('<Return>', primary.grph)

        primary.chargeModeLabel = Label(primary, text="Ion mode:")
        primary.chargeModeLabel.grid(row=29, column=1, sticky=E)
        primary.chargeMode_value = StringVar()
        primary.chargeMode_value.trace('w', primary.AdductChargeRefresh)
        primary.chargeMode = ttk.Combobox(primary, state='readonly', textvariable=primary.chargeMode_value, width=10)
        primary.chargeMode['values'] = ('Positive', 'Negative')
        primary.chargeMode.set("Positive")
        primary.chargeMode.grid(row=29, column=2, sticky=W)
        primary.chargeMode.bind('<Return>', primary.grph)

        errorLabel = tkinter.Label(primary, textvariable=primary.errorMessage, fg = "red")
        errorLabel.grid(row=25, column=3, columnspan=4)
        primary.errorMessage.set("")
        
    def massCalc(primary, eleForm, charge, carbon13, molecularAdduct, numOfC13s, numOfN15s, numOfH2s):
        compound = eleForm
        removeEleC = numOfC13s
        removeEleN = numOfN15s
        extraRemoveEleH = numOfH2s
        adductForm = molecularAdduct
        resNum = primary.resolution.get()
        removeEleO = 0
        removeEleH = 0
        removeEleBr = 0
        removeEleCl = 0
        removeEleS = 0
        electronChange = 0.000548999
        mNum = 1
        seqN = ""
        atomCombo = ""
        atomList = []
        elementList = []
        atomNumList = []
        comboList = []
        sequenceMass = 0
        sequenceAbundance = 0
        mzList = []
        relAbndList = []
        n = 0
        pattern = '([A-Z])([a-z]*)(\d*)'
        pattern2 = '(\d*)'
        errorBool = 0
        errorEle = ""

        if float(carbon13) > 100:
            carbon13 = 100
        elif float(carbon13) < 0:
            carbon13 = 0

   

   
    

        if adductForm == "[M+H]" or adductForm == "[M+2H]" or adductForm == "[M+3H]" or adductForm == "[M+4H]" or adductForm == "[M+5H]":
            adductForm = "H" + charge
        elif adductForm == "[M+]":
            adductForm = ""
        elif adductForm == "[M-HCl+H]" or adductForm == "[M-HCl+2H]" or adductForm == "[M-HCl+3H]" or adductForm == "[M-HCl+4H]" or adductForm == "[M-HCl+5H]":
            adductForm = "H" + charge
            removeEleCl = 1
            removeEleH = 1
        elif adductForm == "[M-HBr+H]" or adductForm == "[M-HBr+2H]" or adductForm == "[M-HBr+3H]" or adductForm == "[M-HBr+4H]" or adductForm == "[M-HBr+5H]":
            adductForm = "H" + charge
            removeEleBr = 1
            removeEleH = 1
        elif adductForm == "[M-H2O+H]" or adductForm == "[M-H2O+2H]" or adductForm == "[M-H2O+3H]" or adductForm == "[M-H2O+4H]" or adductForm == "[M-H2O+5H]":
            adductForm = "H" + charge
            removeEleO = 1
            removeEleH = 2
        elif adductForm == "[M-H2O+Na]" or adductForm == "[M-H2O+2Na]" or adductForm == "[M-H2O+3Na]" or adductForm == "[M-H2O+4Na]" or adductForm == "[M-H2O+5Na]":
            adductForm = "Na" + charge
            removeEleO = 1
            removeEleH = 2
        elif adductForm == "[M-H2O+NH4]":
            adductForm = "NH4"
            removeEleO = 1
            removeEleH = 2
        elif adductForm == "[M-2(H2O)+H]" or adductForm == "[M-2(H2O)+2H]" or adductForm == "[M-2(H2O)+3H]" or adductForm == "[M-2(H2O)+4H]" or adductForm == "[M-2(H2O)+5H]":
            adductForm = "H" + charge
            removeEleO = 2
            removeEleH = 4
        elif adductForm == "[M-3(H2O)+H]" or adductForm == "[M-3(H2O)+2H]" or adductForm == "[M-3(H2O)+3H]" or adductForm == "[M-3(H2O)+4H]" or adductForm == "[M-3(H2O)+5H]":
            adductForm = "H" + charge
            removeEleO = 3
            removeEleH = 6
        elif adductForm == "[M+NH4]" or adductForm == "[M+NH4+H]" or adductForm == "[M+NH4+2H]" or adductForm == "[M+NH4+3H]" or adductForm == "[M+NH4+4H]":
            adductForm = "NH"  + str((int(charge)+3))
        elif adductForm == "[M+Na]" or adductForm == "[M+2Na]" or adductForm == "[M+3Na]" or adductForm == "[M+4Na]" or adductForm == "[M+5Na]":
            adductForm = "Na" + charge
        elif adductForm == "[M+K]" or adductForm == "[M+2K]" or adductForm == "[M+3K]" or adductForm == "[M+4K]" or adductForm == "[M+5K]":
            adductForm = "K" + charge
        elif adductForm == "[M+Li]" or adductForm == "[M+2Li]" or adductForm == "[M+3Li]" or adductForm == "[M+4Li]":
            adductForm = "Li" + charge
        elif adductForm == "[M+Ag]" or adductForm == "[M+2Ag]" or adductForm == "[M+3Ag]" or adductForm == "[M+4Ag]":
            adductForm = "Ag" + charge
        elif adductForm == "[2M+H]":
            adductForm = "H"
            mNum = 2
        elif adductForm == "[2M+NH4]":
            adductForm = "NH4"
            mNum = 2
        elif adductForm == "[2M+Na]":
            adductForm = "Na"
            mNum = 2
        elif adductForm == "[2M+K]":
            adductForm = "K"
            mNum = 2
        elif adductForm == "[3M+H]":
            adductForm = "H"
            mNum = 3
        elif adductForm == "[3M+NH4]":
            adductForm = "NH4"
            mNum = 3
        elif adductForm == "[3M+Na]":
            adductForm = "Na"
            mNum = 3
        elif adductForm == "[3M-2H+Fe3+]":
            adductForm = "Fe"
            mNum = 3
            removeEleH = 2
        elif adductForm == "[3M+K]":
            adductForm = "K"
            mNum = 3
        elif adductForm == "[M-H+Fe2+]":
            adductForm = "Fe"
            removeEleH = 1
        elif adductForm == "[M-2H+Fe3+]":
            adductForm = "Fe"
            removeEleH = 2
        elif adductForm == "[M-SO3+H]" or adductForm == "[M-SO3+2H]" or adductForm == "[M-SO3+3H]" or adductForm == "[M-SO3+4H]" or adductForm == "[M-SO3+5H]":
            adductForm = "H" + charge
            removeEleO = 3
            removeEleS = 1
            
        #Charge2
        elif adductForm == "[M+Na+H]" or adductForm == "[M+Na+2H]" or adductForm == "[M+Na+3H]" or adductForm == "[M+Na+4H]":
            adductForm = "NaH"  + str((int(charge)-1))
        elif adductForm == "[M+K+H]" or adductForm == "[M+K+2H]" or adductForm == "[M+K+3H]" or adductForm == "[M+K+4H]":
            adductForm = "KH"  + str((int(charge)-1))
        elif adductForm == "[M+Li+H]" or adductForm == "[M+Li+2H]" or adductForm == "[M+Li+3H]":
            adductForm = "LiH"  + str((int(charge)-1))
        elif adductForm == "[M+Ag+H]" or adductForm == "[M+Ag+2H]" or adductForm == "[M+Ag+3H]":
            adductForm = "AgH"  + str((int(charge)-1))
        elif adductForm == "[M+2(NH4)]" or adductForm == "[M+2(NH4)+H]" or adductForm == "[M+2(NH4)+2H]" or adductForm == "[M+2(NH4)+3H]":
            adductForm = "N2H" + str((int(charge)+6))
        elif adductForm == "[M+Na+NH4]" or adductForm == "[M+NH4+Na+H]" or adductForm == "[M+NH4+Na+2H]" or adductForm == "[M+NH4+Na+3H]":
            adductForm = "NaNH" + str((int(charge)+2))
        elif adductForm == "[M+Fe2+]":
            adductForm = "Fe"
        elif adductForm == "[M-H+Fe3+]":
            adductForm = "Fe"
            removeEleH = 1
        elif adductForm == "[2M+2H]":
            adductForm = "H2"
            mNum = 2
        elif adductForm == "[2M+NH4+H]":
            adductForm = "NH5"
            mNum = 2
        elif adductForm == "[2M+Na+H]":
            adductForm = "NaH"
            mNum = 2
        elif adductForm == "[2M+K+H]":
            adductForm = "KH"
            mNum = 2
        elif adductForm == "[3M+2H]":
            adductForm = "H2"
            mNum = 3
        elif adductForm == "[3M+NH4+H]":
            adductForm = "NH5"
            mNum = 3
        elif adductForm == "[3M+Na+H]":
            adductForm = "NaH"
            mNum = 3
        elif adductForm == "[3M+K+H]":
            adductForm = "KH"
            mNum = 3
        elif adductForm == "[3M-H+Fe3+]":
            adductForm = "Fe"
            mNum = 3
            removeEleH = 1
        
        #Charge3 
        elif adductForm == "[M+2Na+H]" or adductForm == "[M+2Na+2H]" or adductForm == "[M+2Na+3H]":
            adductForm = "Na2H" + str((int(charge)-2))
        elif adductForm == "[M+2K+H]" or adductForm == "[M+2K+2H]" or adductForm == "[M+2K+3H]":
            adductForm = "K2H" + str((int(charge)-2))
        elif adductForm == "[M+3(NH4)]":
            adductForm = "N3H12"
        elif adductForm == "[M+NH4+2Na]":
            adductForm = "NH4Na2"
        elif adductForm == "[M+2(NH4)+Na]":
            adductForm = "N2H8Na"
        elif adductForm == "[M+H+Fe2+]":
            adductForm = "HFe"
        elif adductForm == "[M+Fe3+]":
            adductForm = "Fe"
        elif adductForm == "[M+Na+Fe2+]":
            adductForm = "NaFe"
        elif adductForm == "[M+NH4+Fe2+]":
            adductForm = "NH4Fe"
        #Charge4
        elif adductForm == "[M+3K+H]" or adductForm == "[M+3K+2H]":
            adductForm = "K3H"  + str((int(charge)-2))
        elif adductForm == "[M+3(NH4)+H]":
            adductForm = "N3H13"
        elif adductForm == "[M+4(NH4)]":
            adductForm = "N4H16"
        elif adductForm == "[M+3Na+H]" or adductForm == "[M+3Na+2H]":
            adductForm = "Na3H"  + str((int(charge)-2))
        elif adductForm == "[M+NH4+2Na+H]":
            adductForm = "Na2NH5"
        elif adductForm == "[M+2(NH4)+Na+H]":
            adductForm = "NaN2H9"
        elif adductForm == "[M+2H+Fe2+]":
            adductForm = "H2Fe"
        elif adductForm == "[M+Na+H+Fe2+]":
            adductForm = "NaHFe"
        elif adductForm == "[M+NH4+H+Fe2+]":
            adductForm = "NH5Fe"
        elif adductForm == "[M+H+Fe3+]":
            adductForm = "HFe"
        elif adductForm == "[M+Na+Fe3+]":
            adductForm = "NaFe"
        elif adductForm == "[M+NH4+Fe3+]":
            adductForm = "NH4Fe"
        #Charge5 (5+)       
        elif adductForm == "[M+4K+H]":
            adductForm = "K4H"
        elif adductForm == "[M+4(NH4)+H]":
            adductForm = "N4H17"
        elif adductForm == "[M+3(NH4)+2H]":
            adductForm = "N3H14"
        elif adductForm == "[M+5(NH4)]":
            adductForm = "N5H20"
        elif adductForm == "[M+4Na+H]":
            adductForm = "Na4H"
        elif adductForm == "[M+NH4+2Na+2H]":
            adductForm = "Na2NH6"
        elif adductForm == "[M+2(NH4)+Na+2H]":
            adductForm = "NaN2H10"
        elif adductForm == "[M+3H+Fe2+]":
            adductForm = "H3Fe"
        elif adductForm == "[M+Na+2H+Fe2+]":
            adductForm = "NaH2Fe"
        elif adductForm == "[M+NH4+2H+Fe2+]":
            adductForm = "NH6Fe"
        elif adductForm == "[M+2Na+H+Fe2+]":
            adductForm = "Na2HFe"
        elif adductForm == "[M+2(NH4)+H+Fe2+]":
            adductForm = "N2H9Fe"
        elif adductForm == "[M+2H+Fe3+]":
            adductForm = "H2Fe"
        elif adductForm == "[M+Na+H+Fe3+]":
           adductForm = "NaHFe"
        elif adductForm == "[M+NH4+H+Fe3+]":
            adductForm = "NH5Fe"
        elif adductForm == "[M+2Na+Fe3+]":
            adductForm = "Na2Fe"
        elif adductForm == "[M+2(NH4)+Fe3+]":
            adductForm = "N2H8Fe"
        #Charge6 (1 neg)
        elif adductForm == "[M-H]" or adductForm == "[M-2H]" or adductForm == "[M-3H]" or adductForm == "[M-4H]" or adductForm == "[M-5H]":
            removeEleH = int(charge)
            adductForm = ""
            electronChange = -0.000548999
        elif adductForm == "[M-]":
            adductForm = ""
            electronChange = -0.000548999
        elif adductForm == "[M-H2O-H]" or adductForm == "[M-H2O-2H]" or adductForm == "[M-H2O-3H]" or adductForm == "[M-H2O-4H]" or adductForm == "[M-H2O-5H]":
            removeEleO = 1
            removeEleH = 2 + int(charge)
            adductForm = ""
            electronChange = -0.000548999
        elif adductForm == "[M-2(H2O)-H]" or adductForm == "[M-2(H2O)-2H]" or adductForm == "[M-2(H2O)-3H]" or adductForm == "[M-2(H2O)-4H]" or adductForm == "[M-2(H2O)-5H]":
            removeEleO = 2
            removeEleH = 4 + int(charge)
            adductForm = ""
            electronChange = -0.000548999
        elif adductForm == "[M-3(H2O)-H]" or adductForm == "[M-3(H2O)-2H]" or adductForm == "[M-3(H2O)-3H]" or adductForm == "[M-3(H2O)-4H]" or adductForm == "[M-3(H2O)-5H]":
            removeEleO = 3
            removeEleH = 6 + int(charge)
            adductForm = ""
            electronChange = -0.000548999
        elif adductForm == "[M+Cl]" or adductForm == "[M+2Cl]" or adductForm == "[M+3Cl]" or adductForm == "[M+4Cl]" or adductForm == "[M+5Cl]":
            adductForm = "Cl" + charge
            electronChange = -0.000548999
        elif adductForm == "[M+Br]" or adductForm == "[M+2Br]" or adductForm == "[M+3Br]" or adductForm == "[M+4Br]" or adductForm == "[M+5Br]":
            adductForm = "Br" + charge
        elif adductForm == "[M+NH4-2H]" or adductForm == "[M+NH4-3H]" or adductForm == "[M+NH4-4H]" or adductForm == "[M+NH4-5H]" or adductForm == "[M+NH4-6H]":
            adductForm = "NH4"
            removeEleH = 1 + int(charge)
            electronChange = -0.000548999
        elif adductForm == "[M+Na-2H]" or adductForm == "[M+Na-3H]" or adductForm == "[M+Na-4H]" or adductForm == "[M+Na-5H]" or adductForm == "[M+Na-6H]":
            adductForm = "Na"
            removeEleH = 1 + int(charge)
            electronChange = -0.000548999
        elif adductForm == "[M+K-2H]" or adductForm == "[M+K-3H]" or adductForm == "[M+K-4H]" or adductForm == "[M+K-5H]" or adductForm == "[M+K-6H]":
            adductForm = "K"
            removeEleH = 1 + int(charge)
            electronChange = -0.000548999
        elif adductForm == "[M+Cl-H]" or adductForm == "[M+Cl-2H]" or adductForm == "[M+Cl-3H]" or adductForm == "[M+Cl-4H]":
            adductForm = "Cl"
            removeEleH = 1 + int(charge)
            electronChange = -0.000548999
        elif adductForm == "[M+Br-H]" or adductForm == "[M+Br-2H]" or adductForm == "[M+Br-3H]" or adductForm == "[M+Br-4H]":
            adductForm = "Br"
            removeEleH = 1 + int(charge)
            electronChange = -0.000548999
        elif adductForm == "[M+HCOOH-H]" or adductForm == "[M+HCOOH-2H]" or adductForm == "[M+HCOOH-3H]" or adductForm == "[M+HCOOH-4H]" or adductForm == "[M+HCOOH-5H]":
            adductForm = "HCO2"
            removeEleH = -1 + int(charge)
            electronChange = -0.000548999
        elif adductForm == "[M+CH3COOH-H]" or adductForm == "[M+CH3COOH-2H]" or adductForm == "[M+CH3COOH-3H]" or adductForm == "[M+CH3COOH-4H]" or adductForm == "[M+CH3COOH-5H]":
            adductForm = "C2H3O2"
            removeEleH = -1 + int(charge)
            electronChange = -0.000548999
        elif adductForm == "[M+Na+HCOOH-2H]" or adductForm == "[M+Na+HCOOH-3H]" or adductForm == "[M+Na+HCOOH-4H]" or adductForm == "[M+Na+HCOOH-5H]" or adductForm == "[M+Na+HCOOH-6H]":
            adductForm = "NaHCO2"
            removeEleH = int(charge)
            electronChange = -0.000548999
        elif adductForm == "[M+Na+CH3COOH-2H]" or adductForm == "[M+Na+CH3COOH-3H]" or adductForm == "[M+Na+CH3COOH-4H]" or adductForm == "[M+Na+CH3COOH-5H]" or adductForm == "[M+Na+CH3COOH-6H]":
            adductForm = "NaC2H3O2"
            removeEleH = int(charge)
            electronChange = -0.000548999
        elif adductForm == "[M+NaCl+Cl]":
            adductForm = "NaCl2"
            electronChange = -0.000548999
        elif adductForm == "[M+NaCl+HCOOH-H]":
            adductForm = "NaClCHO2"
            electronChange = -0.000548999 
        elif adductForm == "[M+Na+2(HCOOH)-2H]":
            adductForm = "NaC2H2O4"
            electronChange = -0.000548999 
        elif adductForm == "[2M-H]":
            adductForm = "H"
            removeEleH = 2
            mNum = 2
            electronChange = -0.000548999
        elif adductForm == "[2M+NH4-2H]":
            adductForm = "NH4"
            removeEleH = 2
            mNum = 2
            electronChange = -0.000548999
        elif adductForm == "[2M+Na-2H]":
            adductForm = "Na"
            removeEleH = 2
            mNum = 2
            electronChange = -0.000548999
        elif adductForm == "[2M+K-2H]":
            adductForm = "K"
            removeEleH = 2
            mNum = 2
            electronChange = -0.000548999
        elif adductForm == "[M]":
            adductForm = ""
            electronChange = 0
            charge = 1
        else:
            adductForm = "FeClBr4Ag" #crazy adduct form to know something has gone wrong

        compound = compound * mNum + adductForm
        
        def nCr(n,r):
            f = math.factorial
            return f(n) // f(r) // f(n-r)

        def nCrThree(n,b,c):
            f = math.factorial
            return f(n) // (f(n-(b+c)) * f(b) * f(c))

        def nCrFour(n,b,c,d):
            f = math.factorial
            return f(n) // (f(n-(b+c+d)) * f(b) * f(c) * f(d))

        def nCrFive(n,b,c,d,e):
            f = math.factorial
            return f(n) // (f(n-(b+c+d+e)) * f(b) * f(c) * f(d) * f(e))

        def nCrSix(n,b,c,d,e,g):
            f = math.factorial
            return f(n) // (f(n-(b+c+d+e+g)) * f(b) * f(c) * f(d) * f(e) * f(g))

        def nCrSeven(n,b,c,d,e,g,h):
            f = math.factorial
            return f(n) // (f(n-(b+c+d+e+g+h)) * f(b) * f(c) * f(d) * f(e) * f(g) * f(h))

        def nCrEight(n,b,c,d,e,g,h,i):
            f = math.factorial
            return f(n) // (f(n-(b+c+d+e+g+h+i)) * f(b) * f(c) * f(d) * f(e) * f(g) * f(h) * f(i))

        def nCrNine(n,b,c,d,e,g,h,i,j):
            f = math.factorial
            return f(n) // (f(n-(b+c+d+e+g+h+i+j)) * f(b) * f(c) * f(d) * f(e) * f(g) * f(h) * f(i) * f(j))

        def nCrTen(n,b,c,d,e,g,h,i,j,k):
            f = math.factorial
            return f(n) // (f(n-(b+c+d+e+g+h+i+j+k)) * f(b) * f(c) * f(d) * f(e) * f(g) * f(h) * f(i) * f(j) * f(k))

        for match in re.finditer(pattern, compound):
            s = match.start()
            e = match.end()
            elementComp = compound[s:e]
            elementList.append(compound[s:e])

        for item in elementList:
            element = ''.join([i for i in elementList[n] if not i.isdigit()])
            numElement = ''.join([i for i in elementList[n] if i.isdigit()])
            if numElement == "":
                numElement = "1"
            elementList[n] = element + "." + numElement
            n = n + 1

        n = 0

        for item in elementList:

            sepEleList = elementList[n].split(".")
            atomNumList.append(int(sepEleList[1]))
            atomList.append(sepEleList[0])
            n = n + 1

        n = 0
        n1 = 1
        t = 0
        t1 = 0
        countEle = 0
        countEle3 = 0
        countEle4 = 0
        countEle5 = 0
        countEle6 = 0
        countEle7 = 0
        countEle8 = 0
        countEle9 = 0
        countEle10 = 0
        abund1 = 1
        abund2 = 0
        abund3 = 0
        abund4 = 0
        abund5 = 0
        abund6 = 0
        abund7 = 0
        abund8 = 0
        abund9 = 0
        abund10 = 0
        mass1 = 0
        mass2 = 0
        mass3 = 0
        mass4 = 0
        mass5 = 0
        mass6 = 0
        mass7 = 0
        mass8 = 0
        mass9 = 0
        mass10 = 0
        currentAbndList = []
        currentMzList = []
        tempAbndList = []
        tempMzList = []
        numOfHe = 0
        numOfBe = 0
        numOfF = 0
        numOfNa = 0
        numOfAl = 0
        numOfP = 0
        numOfSc = 0
        numOfMn = 0
        numOfCo = 0
        numOfAs = 0
        numOfY = 0
        numOfNb = 0
        numOfRh = 0
        numOfI = 0
        numOfCs = 0
        numOfPr = 0
        numOfTb = 0
        numOfHo = 0
        numOfTm = 0
        numOfAu = 0
        numOfBi = 0
        numOfAc = 0
        numOfTh = 0
        numOfPa = 0
        numOfIsos = 0
        
        ## Loop to combine multiple entries of the same element
        for each in atomList:
            while n1 < len(atomList):
                if atomNumList[n] == 0:
                    atomList[n] = ""
                if atomList[n] == atomList[n1]:
                    atomList[n1] = ""
                    atomNumList[n] = atomNumList[n] + atomNumList[n1]
                    atomNumList[n1] = 0
                    
                    
                n1 = n1 +1

            n = n +1
            n1 = n +1

        n = 0
        n1 = 0
        tempList = []

        ## Loop to rearange the atomList and atomNumList to put oxygens first to make the code run faster
        for each in atomList:
            if atomList[n] == "O":
                tempList.append(atomList[n])
                atomList[n] = ""
                for everyEntry in atomList:
                    tempList.append(everyEntry)
                atomList[:] = tempList[:]
                del tempList[:]
                tempList.append(atomNumList[n])
                atomNumList[n] = 0
                for everyEntry in atomNumList:
                    tempList.append(everyEntry)
                atomNumList[:] = tempList[:]
                del tempList[:]
            n = n +1

        n = 0

        while 0 in atomNumList: atomNumList.remove(0)
        while "" in atomList: atomList.remove("")

        ## Loop to remove elements from the atom list which do not have natural isotopes so they are not
        ## included in relative abundance calculations
        for each in atomList:

            if atomList[n] == "He": #4.00260325415

                numOfHe = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""
                
            elif atomList[n] == "Be": #9.0121822

                numOfBe = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "C": #12

                if atomNumList[n] < int(removeEleC):
                    removeEleC = str(atomNumList[n])

            elif atomList[n] == "N": #14.00307

                if atomNumList[n] < int(removeEleN):
                    removeEleN = str(atomNumList[n])

            elif atomList[n] == "F": #18.99840

                numOfF = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "Na": #22.98977

                numOfNa = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "Al": #26.98153863

                numOfAl = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "P": #30.97376

                numOfP = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "Sc": #44.9559119

                numOfSc = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "Mn": #54.9380451

                numOfMn = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "Co": #58.9331950

                numOfCo = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "As": #74.92160

                numOfAs = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "Y": #88.9058483

                numOfY = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "Nb": #92.9063781

                numOfNb = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "Rh": #102.905504

                numOfRh = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "I": #126.90447

                numOfI = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "Cs": #132.905451933

                numOfCs = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "Pr": #140.9076528

                numOfPr = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "Tb": #158.9253468

                numOfTb = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "Ho": #164.9303221

                numOfHo = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "Tm": #168.9342133

                numOfTm = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "Au": #196.9665687

                numOfAu = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "Bi": #208.9803987

                numOfBi = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "Ac": #227.0277521

                numOfAc = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""
            
            elif atomList[n] == "Th": #232.0380553

                numOfTh = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            elif atomList[n] == "Pa": #231.0358840

                numOfPa = atomNumList[n]
                atomNumList[n] = 0
                atomList[n] = ""

            n = n + 1

        while 0 in atomNumList: atomNumList.remove(0)
        while "" in atomList: atomList.remove("")
        
        n = 0

        for each in atomList:

            n = atomNumList[n1]
            
            if atomList[n1] == "C":

                abund1 = (100 - float(carbon13))/100
                abund2 = (float(carbon13))/100
                mass1 = 12
                mass2 = 13.0033548378
                n = n - int(removeEleC)
                numOfIsos = 2

            elif atomList[n1] == "H":

                abund1 = 0.999885
                abund2 = 0.000115
                mass1 = 1.00782503207
                mass2 = 2.0141017778
                n = n - int(removeEleH) - int(extraRemoveEleH)
                numOfIsos = 2

            elif atomList[n1] == "Li":
    
                abund1 = 0.0759
                abund2 = 0.9241
                mass1 = 6.015122795
                mass2 = 7.01600455
                numOfIsos = 2

            elif atomList[n1] == "B":

                abund1 = 0.199
                abund2 = 0.801
                mass1 = 10.0129370
                mass2 = 11.0093054
                numOfIsos = 2

            elif atomList[n1] == "N":

                abund1 = 0.99636
                abund2 = 0.00364
                mass1 = 14.0030740048
                mass2 = 15.0001088982
                n = n - int(removeEleN)
                numOfIsos = 2

            elif atomList[n1] == "Cl":

                abund1 = 0.7576
                abund2 = 0.2424
                mass1 = 34.96885268
                mass2 = 36.96590259
                n = n - int(removeEleCl)
                numOfIsos = 2

            elif atomList[n1] == "V":
    
                abund1 = 0.00250
                abund2 = 0.99750
                mass1 = 49.9471585
                mass2 = 50.9439595
                numOfIsos = 2

            elif atomList[n1] == "Cu":
                abund1 = 0.6915
                abund2 = 0.3085
                mass1 = 62.9295975
                mass2 = 64.9277895
                numOfIsos = 2

            elif atomList[n1] == "Ga":
    
                abund1 = 0.60108
                abund2 = 0.39892
                mass1 = 68.9255736
                mass2 = 70.9247013
                numOfIsos = 2

            elif atomList[n1] == "Br":

                abund1 = 0.5069
                abund2 = 0.4931
                mass1 = 78.9183371
                mass2 = 80.9162906
                n = n - removeEleBr
                numOfIsos = 2

            elif atomList[n1] == "Rb":
    
                abund1 = 0.7217
                abund2 = 0.2783
                mass1 = 84.911789738
                mass2 = 86.909180527
                numOfIsos = 2

            elif atomList[n1] == "Ag":
    
                abund1 = 0.51839
                abund2 = 0.48161
                mass1 = 106.905097
                mass2 = 108.904752
                numOfIsos = 2

            elif atomList[n1] == "In":
    
                abund1 = 0.0429
                abund2 = 0.9571
                mass1 = 112.904058
                mass2 = 114.903878
                numOfIsos = 2

            elif atomList[n1] == "Sb":
    
                abund1 = 0.5721
                abund2 = 0.4279
                mass1 = 120.903815
                mass2 = 122.9042140
                numOfIsos = 2

            elif atomList[n1] == "La":
    
                abund1 = 0.0009
                abund2 = 0.99910
                mass1 = 137.907112
                mass2 = 138.9063533
                numOfIsos = 2

            elif atomList[n1] == "Eu":
    
                abund1 = 0.4781
                abund2 = 0.5219
                mass1 = 150.9198502
                mass2 = 152.9212303
                numOfIsos = 2

            elif atomList[n1] == "Lu":
    
                abund1 = 0.9741
                abund2 = 0.0259
                mass1 = 174.9407718
                mass2 = 175.9426863
                numOfIsos = 2

            elif atomList[n1] == "Ta":
    
                abund1 = 0.00012
                abund2 = 0.99988
                mass1 = 179.9474648
                mass2 = 180.9479958
                numOfIsos = 2

            elif atomList[n1] == "Re":
    
                abund1 = 0.3740
                abund2 = 0.6260
                mass1 = 184.9529550
                mass2 = 186.9557531
                numOfIsos = 2

            elif atomList[n1] == "Ir":
    
                abund1 = 0.373
                abund2 = 0.627
                mass1 = 190.9605940
                mass2 = 192.9629264
                numOfIsos = 2

            elif atomList[n1] == "Tl":
    
                abund1 = 0.2952
                abund2 = 0.7048
                mass1 = 202.9723442
                mass2 = 204.9744275
                numOfIsos = 2

            #########THREE#########

            elif atomList[n1] == "O":

                abund1 = 0.99757
                abund2 = 0.00205
                abund3 = 0.00038
                mass1 = 15.99491461956
                mass2 = 17.9991610
                mass3 = 16.99913170
                n = n - removeEleO
                numOfIsos = 3

            elif atomList[n1] == "Ne":

                abund1 = 0.9048
                abund2 = 0.0027
                abund3 = 0.0925
                mass1 = 19.9924401754
                mass2 = 20.99384668
                mass3 = 21.991385114
                numOfIsos = 3

            elif atomList[n1] == "Mg":

                abund1 = 0.7899
                abund2 = 0.1000
                abund3 = 0.1101
                mass1 = 23.985041700
                mass2 = 24.98583692
                mass3 = 25.982592929
                numOfIsos = 3

            elif atomList[n1] == "Si":

                abund1 = 0.92223
                abund2 = 0.04685
                abund3 = 0.03092
                mass1 = 27.9769265325
                mass2 = 28.97649470
                mass3 = 29.97377017
                numOfIsos = 3

            elif atomList[n1] == "Ar":

                abund1 = 0.003336
                abund2 = 0.000629
                abund3 = 0.996035
                mass1 = 35.967545106
                mass2 = 37.9627324
                mass3 = 39.9623831225
                numOfIsos = 3

            elif atomList[n1] == "K":

                abund1 = 0.932581
                abund2 = 0.067302
                abund3 = 0.000117
                mass1 = 38.96370668
                mass2 = 40.96182576
                mass3 = 39.96399848
                numOfIsos = 3

            elif atomList[n1] == "U":

                abund1 = 0.000054
                abund2 = 0.007204
                abund3 = 0.992742
                mass1 = 234.0409521
                mass2 = 235.0439299
                mass3 = 238.0507882
                numOfIsos = 3

            #########FOUR#########    

            elif atomList[n1] == "S":
    
                abund1 = 0.9493
                abund2 = 0.0076
                abund3 = 0.0429
                abund4 = 0.0002
                mass1 = 31.97207100
                mass2 = 32.97145876
                mass3 = 33.96786690
                mass4 = 35.96708076
                n = n - removeEleS
                numOfIsos = 4

            elif atomList[n1] == "Cr":

                abund1 = 0.04345
                abund2 = 0.83789
                abund3 = 0.09501
                abund4 = 0.02365
                mass1 = 49.9460442
                mass2 = 51.9405075
                mass3 = 52.9406494
                mass4 = 53.9388804
                numOfIsos = 4

            elif atomList[n1] == "Fe":

                abund1 = 0.05845
                abund2 = 0.91754
                abund3 = 0.02119
                abund4 = 0.00282
                mass1 = 53.9396105
                mass2 = 55.9349375
                mass3 = 56.9353940
                mass4 = 57.9332756
                numOfIsos = 4

            elif atomList[n1] == "Sr":

                abund1 = 0.0056
                abund2 = 0.0986
                abund3 = 0.0700
                abund4 = 0.8258
                mass1 = 83.913425
                mass2 = 85.9092607309
                mass3 = 86.9088774970
                mass4 = 87.905612257
                numOfIsos = 4

            elif atomList[n1] == "Ce":

                abund1 = 0.00185
                abund2 = 0.00251
                abund3 = 0.88450
                abund4 = 0.11114
                mass1 = 135.907172
                mass2 = 137.905991
                mass3 = 139.9054387
                mass4 = 141.909244
                numOfIsos = 4

            elif atomList[n1] == "Pb":

                abund1 = 0.014
                abund2 = 0.241
                abund3 = 0.221
                abund4 = 0.524
                mass1 = 203.9730436
                mass2 = 205.9744653
                mass3 = 206.9758969
                mass4 = 207.9766521
                numOfIsos = 4

            #########FIVE#########

            elif atomList[n1] == "Ti":

                abund1 = 0.0825
                abund2 = 0.0744
                abund3 = 0.7372
                abund4 = 0.0541
                abund5 = 0.0518
                mass1 = 45.9526316
                mass2 = 46.9517631
                mass3 = 47.9479463
                mass4 = 48.9478700
                mass5 = 49.9447912
                numOfIsos = 5

            elif atomList[n1] == "Ni":

                abund1 = 0.680769
                abund2 = 0.262231
                abund3 = 0.011399
                abund4 = 0.036345
                abund5 = 0.009256
                mass1 = 57.9353429
                mass2 = 59.9307864
                mass3 = 60.9310560
                mass4 = 61.9283451
                mass5 = 63.9279660
                numOfIsos = 5

            elif atomList[n1] == "Zn":

                abund1 = 0.4917
                abund2 = 0.2773
                abund3 = 0.0404
                abund4 = 0.1845
                abund5 = 0.0061
                mass1 = 63.9291422
                mass2 = 65.9260334
                mass3 = 66.9271273
                mass4 = 67.9248442
                mass5 = 69.9253193
                numOfIsos = 5

            elif atomList[n1] == "Ge":

                abund1 = 0.2038
                abund2 = 0.2731
                abund3 = 0.0776
                abund4 = 0.3672
                abund5 = 0.0783
                mass1 = 69.9242474
                mass2 = 71.9220758
                mass3 = 72.9234589
                mass4 = 73.9211778
                mass5 = 75.9214026
                numOfIsos = 5

            elif atomList[n1] == "Zr":

                abund1 = 0.5145
                abund2 = 0.1122
                abund3 = 0.1715
                abund4 = 0.1738
                abund5 = 0.0280
                mass1 = 89.9047044
                mass2 = 90.9056458
                mass3 = 91.9050408
                mass4 = 93.9063152
                mass5 = 95.9082734
                numOfIsos = 5

            elif atomList[n1] == "W":

                abund1 = 0.0012
                abund2 = 0.2650
                abund3 = 0.1431
                abund4 = 0.3064
                abund5 = 0.2843
                mass1 = 179.946704
                mass2 = 181.9482042
                mass3 = 182.9502230
                mass4 = 183.9509312
                mass5 = 185.9543641
                numOfIsos = 5

            #########SIX#########

            elif atomList[n1] == "Ca":

                abund1 = 0.96941
                abund2 = 0.00647
                abund3 = 0.00135
                abund4 = 0.02086
                abund5 = 0.00004
                abund6 = 0.00187
                mass1 = 39.96259098
                mass2 = 41.95861801
                mass3 = 42.9587666
                mass4 = 43.9554818
                mass5 = 45.9536926
                mass6 = 47.952534
                numOfIsos = 6

            elif atomList[n1] == "Se":

                abund1 = 0.0089
                abund2 = 0.0937
                abund3 = 0.0763
                abund4 = 0.2377
                abund5 = 0.4961
                abund6 = 0.0873
                mass1 = 73.9224764
                mass2 = 75.9192136
                mass3 = 76.9199140
                mass4 = 77.9173091
                mass5 = 79.9165213
                mass6 = 81.9166994
                numOfIsos = 6

            elif atomList[n1] == "Kr":

                abund1 = 0.00355
                abund2 = 0.02286
                abund3 = 0.11593
                abund4 = 0.11500
                abund5 = 0.56987
                abund6 = 0.17279
                mass1 = 77.9203648
                mass2 = 79.9163790
                mass3 = 81.9134836
                mass4 = 82.914136
                mass5 = 83.91150
                mass6 = 85.91061073
                numOfIsos = 6

            elif atomList[n1] == "Pd":

                abund1 = 0.0102
                abund2 = 0.1114
                abund3 = 0.2233
                abund4 = 0.2733
                abund5 = 0.2646
                abund6 = 0.1172
                mass1 = 101.905609
                mass2 = 103.904036
                mass3 = 104.905085
                mass4 = 105.903486
                mass5 = 107.903892
                mass6 = 109.905153
                numOfIsos = 6

            elif atomList[n1] == "Er":

                abund1 = 0.00139
                abund2 = 0.01601
                abund3 = 0.33503
                abund4 = 0.22869
                abund5 = 0.26978
                abund6 = 0.14910
                mass1 = 161.928778
                mass2 = 163.929200
                mass3 = 165.9302931
                mass4 = 166.9320482
                mass5 = 167.932370
                mass6 = 169.9354643
                numOfIsos = 6

            elif atomList[n1] == "Hf":

                abund1 = 0.0016
                abund2 = 0.0526
                abund3 = 0.1860
                abund4 = 0.2728
                abund5 = 0.1362
                abund6 = 0.3508
                mass1 = 173.940046
                mass2 = 175.9414086
                mass3 = 176.9432207
                mass4 = 177.9436988
                mass5 = 178.9458161
                mass6 = 179.9465500
                numOfIsos = 6

            elif atomList[n1] == "Pt":

                abund1 = 0.00014
                abund2 = 0.00782
                abund3 = 0.32967
                abund4 = 0.33832
                abund5 = 0.25242
                abund6 = 0.07163
                mass1 = 189.959932
                mass2 = 191.9610380
                mass3 = 193.9626803
                mass4 = 194.9647911
                mass5 = 195.9649515
                mass6 = 197.967893
                numOfIsos = 6

            #########SEVEN#########

            elif atomList[n1] == "Mo":
    
                abund1 = 0.14649
                abund2 = 0.09187
                abund3 = 0.15873
                abund4 = 0.16673
                abund5 = 0.09582
                abund6 = 0.24292
                abund7 = 0.09744
                mass1 = 91.906811
                mass2 = 93.9050883
                mass3 = 94.9058421
                mass4 = 95.9046795
                mass5 = 96.9060215
                mass6 = 97.9054082
                mass7 = 99.907477
                numOfIsos = 7

            elif atomList[n1] == "Ru":
    
                abund1 = 0.0554
                abund2 = 0.0187
                abund3 = 0.1276
                abund4 = 0.1260
                abund5 = 0.1706
                abund6 = 0.3155
                abund7 = 0.1862
                mass1 = 95.907598
                mass2 = 97.905287
                mass3 = 98.9059393
                mass4 = 99.904219
                mass5 = 100.9055821
                mass6 = 101.9043493
                mass7 = 103.905433
                numOfIsos = 7

            elif atomList[n1] == "Ba":
    
                abund1 = 0.00106
                abund2 = 0.00101
                abund3 = 0.02417
                abund4 = 0.06592
                abund5 = 0.07854
                abund6 = 0.11232
                abund7 = 0.71698
                mass1 = 129.9063208
                mass2 = 131.9050613
                mass3 = 133.9045084
                mass4 = 134.9056886
                mass5 = 135.9045759
                mass6 = 136.9058274
                mass7 = 137.9052472
                numOfIsos = 7

            elif atomList[n1] == "Nd":
    
                abund1 = 0.272
                abund2 = 0.122
                abund3 = 0.238
                abund4 = 0.083
                abund5 = 0.172
                abund6 = 0.057
                abund7 = 0.056
                mass1 = 141.9077233
                mass2 = 142.9098143
                mass3 = 143.9100873
                mass4 = 144.9125736
                mass5 = 145.9131169
                mass6 = 147.916893
                mass7 = 149.920891
                numOfIsos = 7

            elif atomList[n1] == "Sm":
    
                abund1 = 0.0307
                abund2 = 0.1499
                abund3 = 0.1124
                abund4 = 0.1382
                abund5 = 0.0738
                abund6 = 0.2675
                abund7 = 0.2275
                mass1 = 143.911999
                mass2 = 146.9148979
                mass3 = 147.9148227
                mass4 = 148.9171847
                mass5 = 149.9172755
                mass6 = 151.9197324
                mass7 = 153.9222093
                numOfIsos = 7

            elif atomList[n1] == "Gd":
    
                abund1 = 0.0020
                abund2 = 0.0218
                abund3 = 0.1480
                abund4 = 0.2047
                abund5 = 0.1565
                abund6 = 0.2484
                abund7 = 0.2186
                mass1 = 151.9197910
                mass2 = 153.9208656
                mass3 = 154.9226220
                mass4 = 155.9221227
                mass5 = 156.9239601
                mass6 = 157.9241039
                mass7 = 159.9270541
                numOfIsos = 7

            elif atomList[n1] == "Dy":
    
                abund1 = 0.00056
                abund2 = 0.00095
                abund3 = 0.02329
                abund4 = 0.18889
                abund5 = 0.25475
                abund6 = 0.24896
                abund7 = 0.28260
                mass1 = 155.924283
                mass2 = 157.924409
                mass3 = 159.9251975
                mass4 = 160.9269334
                mass5 = 161.9267984
                mass6 = 162.9287312
                mass7 = 163.9291748
                numOfIsos = 7

            elif atomList[n1] == "Yb":
    
                abund1 = 0.0013
                abund2 = 0.0304
                abund3 = 0.1428
                abund4 = 0.2183
                abund5 = 0.1613
                abund6 = 0.3183
                abund7 = 0.1276
                mass1 = 167.933897
                mass2 = 169.9347618
                mass3 = 170.9363258
                mass4 = 171.9363815
                mass5 = 172.9382108
                mass6 = 173.9388621
                mass7 = 175.9425717
                numOfIsos = 7

            elif atomList[n1] == "Os":
    
                abund1 = 0.0002
                abund2 = 0.0159
                abund3 = 0.0196
                abund4 = 0.1324
                abund5 = 0.1615
                abund6 = 0.2626
                abund7 = 0.4078
                mass1 = 183.9524891
                mass2 = 185.9538382
                mass3 = 186.9557505
                mass4 = 187.9558382
                mass5 = 188.9581475
                mass6 = 189.9584470
                mass7 = 191.9614807
                numOfIsos = 7

            elif atomList[n1] == "Hg":
    
                abund1 = 0.0015
                abund2 = 0.0997
                abund3 = 0.1687
                abund4 = 0.2310
                abund5 = 0.1318
                abund6 = 0.2986
                abund7 = 0.0687
                mass1 = 195.965833
                mass2 = 197.9667690
                mass3 = 198.9682799
                mass4 = 199.9683260
                mass5 = 200.9703023
                mass6 = 201.9706430
                mass7 = 203.9734939
                numOfIsos = 7

            #########EIGHT#########

            elif atomList[n1] == "Cd":
    
                abund1 = 0.0125
                abund2 = 0.0089
                abund3 = 0.1249
                abund4 = 0.1280
                abund5 = 0.2413
                abund6 = 0.1222
                abund7 = 0.2873
                abund8 = 0.0749
                mass1 = 105.906459
                mass2 = 107.904184
                mass3 = 109.9030021
                mass4 = 110.9041781
                mass5 = 111.9027578
                mass6 = 112.9044017
                mass7 = 113.9033585
                mass8 = 115.904756
                numOfIsos = 8

            elif atomList[n1] == "Te":
    
                abund1 = 0.0009
                abund2 = 0.0255
                abund3 = 0.0089
                abund4 = 0.0474
                abund5 = 0.0707
                abund6 = 0.1884
                abund7 = 0.3174
                abund8 = 0.3408
                mass1 = 119.90402
                mass2 = 121.903043
                mass3 = 122.9042700
                mass4 = 123.9028179
                mass5 = 124.9044307
                mass6 = 125.9033117
                mass7 = 127.9044631
                mass8 = 129.9062244
                numOfIsos = 8

            #########NINE#########

            elif atomList[n1] == "Xe":
    
                abund1 = 0.000952
                abund2 = 0.000890
                abund3 = 0.019102
                abund4 = 0.264006
                abund5 = 0.040710
                abund6 = 0.212324
                abund7 = 0.269086
                abund8 = 0.104357
                abund9 = 0.088573
                mass1 = 123.905893
                mass2 = 125.904274
                mass3 = 127.9035313
                mass4 = 128.9047794
                mass5 = 129.9035080
                mass6 = 130.9050824
                mass7 = 131.9041535
                mass8 = 133.9053945
                mass9 = 135.907219
                numOfIsos = 9

            #########TEN#########

            elif atomList[n1] == "Sn":

                abund1 = 0.0097
                abund2 = 0.0066
                abund3 = 0.0034
                abund4 = 0.1454
                abund5 = 0.0768
                abund6 = 0.2422
                abund7 = 0.0859
                abund8 = 0.3258
                abund9 = 0.0463
                abund10 = 0.0579
                mass1 = 111.904818
                mass2 = 113.902779
                mass3 = 114.903342
                mass4 = 115.901741
                mass5 = 116.902952
                mass6 = 117.901603
                mass7 = 118.903308
                mass8 = 119.9021947
                mass9 = 121.9034390
                mass10 = 123.9052739
                numOfIsos = 10

            else:

                errorBool = 1
                errorEle = atomList[n1]
                numOfIsos = 0

            while countEle <= n and errorBool != 1:
                if numOfIsos == 2: #"C,H,Li,B,N,Cl,V,Cu,Ga,Br,Rb,Ag,In,Sb,La,Eu,Lu,Ta,Re,Ir,Tl"
                    currentAbndList.append(((abund1**(n-countEle))*(abund2**countEle))*nCr(n,countEle))
                    currentMzList.append((mass1*(n-countEle)) + (mass2*(countEle)))
                    countEle3 = 100000
                
                while countEle3 <= (n-countEle):
                    if numOfIsos == 3: #"O,U,K,Mg,Si,Ne,Ar"
                        currentAbndList.append(((abund1**(n-countEle-countEle3))*(abund2**countEle)*(abund3**countEle3))*(nCrThree(n, countEle, countEle3)))
                        currentMzList.append((mass1*(n-countEle-countEle3)) + (mass2*(countEle)) + (mass3*(countEle3)))
                        countEle4 = 100000
                        
                    while countEle4 <= (n-countEle-countEle3):
                        if numOfIsos == 4: #"Fe,S,Cr,Sr,Pb,Ce"
                            currentAbndList.append(((abund1**(n-countEle-countEle3-countEle4))*(abund2**countEle)*(abund3**countEle3)*(abund4**countEle4))* \
                                (nCrFour(n, countEle, countEle3,countEle4)))
                            currentMzList.append((mass1*(n-countEle-countEle3-countEle4)) + (mass2*(countEle)) + (mass3*(countEle3)) + (mass4*(countEle4)))
                            countEle5 = 100000
                            
                        while countEle5 <= (n-countEle-countEle3-countEle4):
                            if numOfIsos == 5: #"Ti,Ni,Zn,Ge,Zr,W"
                                currentAbndList.append(((abund1**(n-countEle-countEle3-countEle4-countEle5))*(abund2**countEle)*(abund3**countEle3)* \
                                    (abund4**countEle4)*(abund5**countEle5))*(nCrFive(n, countEle, countEle3, countEle4, countEle5)))
                                currentMzList.append((mass1*(n-countEle-countEle3-countEle4-countEle5)) + (mass2*(countEle)) + (mass3*(countEle3)) + \
                                    (mass4*(countEle4))+(mass5*(countEle5)))
                                countEle6 = 100000
                                
                            while countEle6 <= (n-countEle-countEle3-countEle4-countEle5):
                                if numOfIsos == 6: #"Ca,Se,Pd,Er,Pt,Kr,Hf"
                                    currentAbndList.append(((abund1**(n-countEle-countEle3-countEle4-countEle5-countEle6))*(abund2**countEle)*\
                                        (abund3**countEle3)*(abund4**countEle4)*(abund5**countEle5)*(abund6**countEle6))*\
                                        (nCrSix(n, countEle, countEle3, countEle4, countEle5, countEle6)))
                                    currentMzList.append((mass1*(n-countEle-countEle3-countEle4-countEle5-countEle6)) + (mass2*(countEle)) + \
                                        (mass3*(countEle3)) + (mass4*(countEle4))+(mass5*(countEle5))+(mass6*(countEle6)))
                                    countEle7 = 100000
                                    
                                while countEle7 <= (n-countEle-countEle3-countEle4-countEle5-countEle6):
                                    if numOfIsos == 7: #"Mo,Ru,Ba,Nd,Sm,Gd,Dy,Yb,Os,Hg"
                                        currentAbndList.append(((abund1**(n-countEle-countEle3-countEle4-countEle5-countEle6-countEle7))*(abund2**countEle)*\
                                            (abund3**countEle3)*(abund4**countEle4)*(abund5**countEle5)*(abund6**countEle6)*\
                                            (abund7**countEle7))*\
                                            (nCrSeven(n, countEle, countEle3, countEle4, countEle5, countEle6, countEle7)))
                                        currentMzList.append((mass1*(n-countEle-countEle3-countEle4-countEle5-countEle6-countEle7)) + (mass2*(countEle)) + \
                                            (mass3*(countEle3)) + (mass4*(countEle4))+(mass5*(countEle5))+(mass6*(countEle6))+(mass7*(countEle7)))
                                        countEle8 = 100000
                                    
                                    while countEle8 <= (n-countEle-countEle3-countEle4-countEle5-countEle6-countEle7):
                                        if numOfIsos == 8: #"Te,Cd"
                                            currentAbndList.append(((abund1**(n-countEle-countEle3-countEle4-countEle5-countEle6-countEle7-countEle8))*(abund2**countEle)*\
                                                (abund3**countEle3)*(abund4**countEle4)*(abund5**countEle5)*(abund6**countEle6)*\
                                                (abund7**countEle7)*(abund8**countEle8))*\
                                                (nCrEight(n, countEle, countEle3, countEle4, countEle5, countEle6, countEle7, countEle8)))
                                            currentMzList.append((mass1*(n-countEle-countEle3-countEle4-countEle5-countEle6-countEle7-countEle8)) + (mass2*(countEle)) + \
                                                (mass3*(countEle3)) + (mass4*(countEle4))+(mass5*(countEle5))+(mass6*(countEle6))+(mass7*(countEle7))+(mass8*(countEle8)))
                                            countEle9 = 100000
                                            
                                        while countEle9 <= (n-countEle-countEle3-countEle4-countEle5-countEle6-countEle7-countEle8):
                                            if numOfIsos == 9: #"Xe"
                                                currentAbndList.append(((abund1**(n-countEle-countEle3-countEle4-countEle5-countEle6-countEle7-countEle8-countEle9))*(abund2**countEle)*\
                                                    (abund3**countEle3)*(abund4**countEle4)*(abund5**countEle5)*(abund6**countEle6)*(abund7**countEle7)*(abund8**countEle8)*(abund9**countEle9))*\
                                                    (nCrNine(n, countEle, countEle3, countEle4, countEle5, countEle6, countEle7, countEle8, countEle9)))
                                                currentMzList.append((mass1*(n-countEle-countEle3-countEle4-countEle5-countEle6-countEle7-countEle8-countEle9)) + (mass2*(countEle)) + \
                                                    (mass3*(countEle3)) + (mass4*(countEle4))+(mass5*(countEle5))+(mass6*(countEle6))+(mass7*(countEle7))+(mass8*(countEle8))+(mass9*(countEle9)))
                                                countEle10 = 100000
                                                
                                            while countEle10 <= (n-countEle-countEle3-countEle4-countEle5-countEle6-countEle7-countEle8-countEle9):
                                                if numOfIsos == 10: #"Sn"
                                                    currentAbndList.append(((abund1**(n-countEle-countEle3-countEle4-countEle5-countEle6-countEle7-countEle8-countEle9-countEle10))*(abund2**countEle)*\
                                                        (abund3**countEle3)*(abund4**countEle4)*(abund5**countEle5)*(abund6**countEle6)*(abund7**countEle7)*(abund8**countEle8)*(abund9**countEle9)*\
                                                        (abund10**countEle10))*(nCrTen(n, countEle, countEle3, countEle4, countEle5, countEle6, countEle7, countEle8, countEle9, countEle10)))
                                                    currentMzList.append((mass1*(n-countEle-countEle3-countEle4-countEle5-countEle6-countEle7-countEle8-countEle9-countEle10)) + (mass2*(countEle)) + \
                                                        (mass3*(countEle3)) + (mass4*(countEle4))+(mass5*(countEle5))+(mass6*(countEle6))+(mass7*(countEle7))+(mass8*(countEle8))+(mass9*(countEle9))+\
                                                        (mass10*(countEle10)))
                                                countEle10 = countEle10 + 1
                                            
                                            countEle9 = countEle9 + 1
                                            countEle10 = 0

                                        countEle8 = countEle8 + 1
                                        countEle9 = 0

                                    countEle7 = countEle7 + 1
                                    countEle8 = 0

                                countEle6 = countEle6 + 1
                                countEle7 = 0

                            countEle5 = countEle5 + 1
                            countEle6 = 0
                            
                        countEle4 = countEle4 + 1
                        countEle5 = 0

                    countEle3 = countEle3 + 1
                    countEle4 = 0

                countEle = countEle +1
                countEle3 = 0

            if len(relAbndList) == 0:
                relAbndList[:] = currentAbndList[:]
                mzList[:] = currentMzList[:]
            else:
                while t < len(currentAbndList):
                    while t1 < len(relAbndList):

                        if relAbndList[t1] < 0.000001:
                            if currentAbndList[t] < 0.000001:
                                relAbndList[t1] = 0
                                mzList[t1] = 0
                                currentMzList[t] = 0
                                currentAbndList[t] = 0
                        else:
                            tempAbndList.append(float(relAbndList[t1]) * float(currentAbndList[t]))
                            tempMzList.append((float(currentMzList[t])+float(mzList[t1])))

                        t1 = t1 + 1

                    t = t + 1
                    t1 = 0

                relAbndList[:] = tempAbndList[:]
                mzList[:] = tempMzList[:]
                del tempAbndList[:]
                del tempMzList[:]
              
            n1 = n1 + 1
            t = 0
            t1 = 0
            countEle = 0
            countEle3 = 0
            countEle4 = 0
            countEle5 = 0
            countEle6 = 0
            countEle7 = 0
            countEle8 = 0
            countEle9 = 0
            countEle10 = 0
            abund1 = 0
            abund2 = 0
            abund3 = 0
            abund4 = 0
            abund5 = 0
            abund6 = 0
            abund7 = 0
            abund8 = 0
            abund9 = 0
            abund10 = 0
            mass1 = 0
            mass2 = 0
            mass3 = 0
            mass4 = 0
            mass5 = 0
            mass6 = 0
            mass7 = 0
            mass8 = 0
            mass9 = 0
            mass10 = 0
            numOfIsos = 0
            del currentAbndList[:]
            del currentMzList[:]

        n = 0
        n1 = 1
        currentMZ = 0
        
        for item in relAbndList:

            if relAbndList[t1] < 0.00001:
                relAbndList[t1] = 0
                mzList[t1] = 0

            t1 = t1 + 1

        n = 0

        mzList = list(filter(lambda a: a != 0, mzList))
        relAbndList = list(filter(lambda a: a != 0, relAbndList))
        
        for item in mzList:

            currentMZ = mzList[n]

            while n1 < len(mzList):

                if mzList[n1] > (currentMZ - (currentMZ/float(resNum))):#float(resNum)):
                    if mzList[n1] < (currentMZ + (currentMZ/float(resNum))):#float(resNum)):
                        if currentMZ != 0:
                            currentMZ = mzList[n]*(relAbndList[n]/(relAbndList[n]+relAbndList[n1]))+mzList[n1]*(relAbndList[n1]/(relAbndList[n]+relAbndList[n1]))
                            mzList[n1] = 0
                            mzList[n] = currentMZ
                            relAbndList[n] = relAbndList[n] + relAbndList[n1]
                            relAbndList[n1] = 0
                
                n1 = n1 + 1

            n = n + 1
            n1 = n + 1

        n = 0

        # If statement to include molecular formulas with elements with no isotopes with [M+]
        if len(relAbndList) == 0:

                relAbndList.append(1)

        # If statement to include molecular formulas with elements with no isotopes with [M+]
        if len(mzList) == 0:

                mzList.append(0.0000000001) #adding a very small value so the entry will be picked up by the next if statement
        
        ## Loop to add the masses of the elements which do not have natural isotopes
        for item in mzList:

            if mzList[n] > 0:
                mzList[n] = mzList[n] + (numOfNa * 22.9897692809) + (numOfP * 30.97376163) + (numOfF * 18.99840322) + \
                            (numOfI * 126.904473) + (numOfAs * 74.9215965) + (numOfSc * 44.9559119) + (numOfAl * 26.98153863) + (numOfMn * 54.9380451) + \
                            (numOfCo * 58.9331950) + (numOfBe * 9.0121822) + (int(removeEleC) * 13.0033548378) + (numOfAu * 196.9665687) + \
                            (numOfHe * 4.00260325415) + (int(removeEleN) * 15.0001088982) + (int(extraRemoveEleH) * 2.0141017778) + (numOfY * 88.9058483) + \
                            (numOfNb * 92.9063781) + (numOfRh * 102.905504) + (numOfCs * 132.905451933) + (numOfBi * 208.9803987)  + (numOfTh * 232.0380553) + \
                            (numOfPa * 231.0358840) + (numOfAc * 227.0277521) + (numOfTm * 168.9342133) + (numOfHo * 164.9303221) + (numOfTb * 158.9253468) + \
                            (numOfPr * 140.9076528)
            n = n + 1

        n = 0

        mzList = list(filter(lambda a: a != 0, mzList))
        relAbndList = list(filter(lambda a: a != 0, relAbndList))

        ## Loop to remove the weight of an electron from each mass to give a positive charge and to divide by the charge state
        for item in mzList:

            mzList[n] = mzList[n] - (electronChange * int(charge))
            mzList[n] = mzList[n] / int(charge)
            n = n + 1

        if errorBool == 1:
            del mzList[:]
            mzList.append(1)
            del relAbndList[:]
            relAbndList.append(100)
        
        return (mzList, relAbndList, errorBool, errorEle)

    def ionAdList(primary):

        stateOfCharge = primary.chargeState.get()
        detectorCharge = primary.chargeMode.get()

        if int(stateOfCharge) == 2:

            if detectorCharge == "Positive":
            
                primary.adductOptions.set("[M+2H]")
                primary.adductOptions["values"] = ionChoices2

            else:

                primary.adductOptions.set("[M-2H]")
                primary.adductOptions["values"] = ionChoices7           

        elif int(stateOfCharge) == 3:
            
            if detectorCharge == "Positive":
            
                primary.adductOptions.set("[M+3H]")
                primary.adductOptions["values"] = ionChoices3

            else:

                primary.adductOptions.set("[M-3H]")
                primary.adductOptions["values"] = ionChoices8  

        elif int(stateOfCharge) == 4:
            
            if detectorCharge == "Positive":
                        
                primary.adductOptions.set("[M+4H]")
                primary.adductOptions["values"] = ionChoices4

            else:

                primary.adductOptions.set("[M-4H]")
                primary.adductOptions["values"] = ionChoices9

        elif int(stateOfCharge) == 5:
            
            if detectorCharge == "Positive":
                        
                primary.adductOptions.set("[M+5H]")
                primary.adductOptions["values"] = ionChoices5

            else:

                primary.adductOptions.set("[M-5H]")
                primary.adductOptions["values"] = ionChoices10

        elif int(stateOfCharge) == 0:
                        
            primary.adductOptions.set("[M]")
            primary.adductOptions["values"] = ionChoices0

        else:

            if detectorCharge == "Positive":
            
                primary.adductOptions.set("[M+H]")
                primary.adductOptions["values"] = ionChoices1

            else:

                primary.adductOptions.set("[M-H]")
                primary.adductOptions["values"] = ionChoices6
            
        return

    def ionAdListA2(primary):

        stateOfCharge2 = primary.A2cState.get()
        detectorCharge = primary.chargeMode.get()

        if int(stateOfCharge2) == 2:

            if detectorCharge == "Positive":
            
                primary.adductOptionsA2.set("[M+2H]")
                primary.adductOptionsA2["values"] = ionChoices2

            else:

                primary.adductOptionsA2.set("[M-2H]")
                primary.adductOptionsA2["values"] = ionChoices7

        elif int(stateOfCharge2) == 3:

            if detectorCharge == "Positive":
                        
                primary.adductOptionsA2.set("[M+3H]")
                primary.adductOptionsA2["values"] = ionChoices3

            else:

                primary.adductOptionsA2.set("[M-3H]")
                primary.adductOptionsA2["values"] = ionChoices8                

        elif int(stateOfCharge2) == 4:
            
            if detectorCharge == "Positive":
            
                primary.adductOptionsA2.set("[M+4H]")
                primary.adductOptionsA2["values"] = ionChoices4

            else:
                
                primary.adductOptionsA2.set("[M-4H]")
                primary.adductOptionsA2["values"] = ionChoices9

        elif int(stateOfCharge2) == 5:
            
            if detectorCharge == "Positive":
            
                primary.adductOptionsA2.set("[M+5H]")
                primary.adductOptionsA2["values"] = ionChoices4

            else:
                
                primary.adductOptionsA2.set("[M-5H]")
                primary.adductOptionsA2["values"] = ionChoices10

        elif int(stateOfCharge2) == 0:
                        
            primary.adductOptionsA2.set("[M]")
            primary.adductOptionsA2["values"] = ionChoices0

        else:

            if detectorCharge == "Positive":
            
                primary.adductOptionsA2.set("[M+H]")
                primary.adductOptionsA2["values"] = ionChoices1

            else:

                primary.adductOptionsA2.set("[M-H]")
                primary.adductOptionsA2["values"] = ionChoices6
            
        return

    def ionAdListA3(primary):

        stateOfCharge3 = primary.A3cState.get()
        detectorCharge = primary.chargeMode.get()

        if int(stateOfCharge3) == 2:

            if detectorCharge == "Positive":
            
                primary.adductOptionsA3.set("[M+2H]")
                primary.adductOptionsA3["values"] = ionChoices2

            else:

                primary.adductOptionsA3.set("[M-2H]")
                primary.adductOptionsA3["values"] = ionChoices7

        elif int(stateOfCharge3) == 3:

            if detectorCharge == "Positive":
            
                primary.adductOptionsA3.set("[M+3H]")
                primary.adductOptionsA3["values"] = ionChoices3

            else:

                primary.adductOptionsA3.set("[M-3H]")
                primary.adductOptionsA3["values"] = ionChoices8

        elif int(stateOfCharge3) == 4:

            if detectorCharge == "Positive":
            
                primary.adductOptionsA3.set("[M+4H]")
                primary.adductOptionsA3["values"] = ionChoices4

            else:

                primary.adductOptionsA3.set("[M-4H]")
                primary.adductOptionsA3["values"] = ionChoices9

        elif int(stateOfCharge3) == 5:

            if detectorCharge == "Positive":
            
                primary.adductOptionsA3.set("[M+5H]")
                primary.adductOptionsA3["values"] = ionChoices4

            else:

                primary.adductOptionsA3.set("[M-5H]")
                primary.adductOptionsA3["values"] = ionChoices10

        elif int(stateOfCharge3) == 0:
                        
            primary.adductOptionsA3.set("[M]")
            primary.adductOptionsA3["values"] = ionChoices0

        else:

            if detectorCharge == "Positive":
            
                primary.adductOptionsA3.set("[M+H]")
                primary.adductOptionsA3["values"] = ionChoices1

            else:
                
                primary.adductOptionsA3.set("[M-H]")
                primary.adductOptionsA3["values"] = ionChoices6
            
        return

    def ionAdListA4(primary):

        stateOfCharge4 = primary.A4cState.get()
        detectorCharge = primary.chargeMode.get()

        if int(stateOfCharge4) == 2:

            if detectorCharge == "Positive":
            
                primary.adductOptionsA4.set("[M+2H]")
                primary.adductOptionsA4["values"] = ionChoices2

            else:

                primary.adductOptionsA4.set("[M-2H]")
                primary.adductOptionsA4["values"] = ionChoices7
            

        elif int(stateOfCharge4) == 3:

            if detectorCharge == "Positive":
            
                primary.adductOptionsA4.set("[M+3H]")
                primary.adductOptionsA4["values"] = ionChoices3

            else:

                primary.adductOptionsA4.set("[M-3H]")
                primary.adductOptionsA4["values"] = ionChoices8

        elif int(stateOfCharge4) == 4:

            if detectorCharge == "Positive":
            
                primary.adductOptionsA4.set("[M+4H]")
                primary.adductOptionsA4["values"] = ionChoices4

            else:

                primary.adductOptionsA4.set("[M-4H]")
                primary.adductOptionsA4["values"] = ionChoices9

        elif int(stateOfCharge4) == 5:

            if detectorCharge == "Positive":
            
                primary.adductOptionsA4.set("[M+5H]")
                primary.adductOptionsA4["values"] = ionChoices4

            else:

                primary.adductOptionsA4.set("[M-5H]")
                primary.adductOptionsA4["values"] = ionChoices10

        elif int(stateOfCharge4) == 0:
                        
            primary.adductOptionsA4.set("[M]")
            primary.adductOptionsA4["values"] = ionChoices0
            
        else:

            if detectorCharge == "Positive":
            
                primary.adductOptionsA4.set("[M+H]")
                primary.adductOptionsA4["values"] = ionChoices1

            else:
            
                primary.adductOptionsA4.set("[M-H]")
                primary.adductOptionsA4["values"] = ionChoices6
            
        return

    def ionAdListCoCom(primary):

        coStateOfCharge = primary.coChargeState.get()
        detectorCharge = primary.chargeMode.get()

        if int(coStateOfCharge) == 2:

            if detectorCharge == "Positive":
            
                primary.coAdductOptions.set("[M+2H]")
                primary.coAdductOptions["values"] = ionChoices2

            else:

                primary.coAdductOptions.set("[M-2H]")
                primary.coAdductOptions["values"] = ionChoices7
            
        elif int(coStateOfCharge) == 3:

            if detectorCharge == "Positive":
            
                primary.coAdductOptions.set("[M+3H]")
                primary.coAdductOptions["values"] = ionChoices3

            else:

                primary.coAdductOptions.set("[M-3H]")
                primary.coAdductOptions["values"] = ionChoices8

        elif int(coStateOfCharge) == 4:

            if detectorCharge == "Positive":
            
                primary.coAdductOptions.set("[M+4H]")
                primary.coAdductOptions["values"] = ionChoices4

            else:
            
                primary.coAdductOptions.set("[M-4H]")
                primary.coAdductOptions["values"] = ionChoices9

        elif int(coStateOfCharge) == 5:

            if detectorCharge == "Positive":
            
                primary.coAdductOptions.set("[M+5H]")
                primary.coAdductOptions["values"] = ionChoices4

            else:
            
                primary.coAdductOptions.set("[M-5H]")
                primary.coAdductOptions["values"] = ionChoices10

        elif int(coStateOfCharge) == 0:
                        
            primary.coAdductOptions.set("[M]")
            primary.coAdductOptions["values"] = ionChoices0
                            
        else:

            if detectorCharge == "Positive":
            
                primary.coAdductOptions.set("[M+H]")
                primary.coAdductOptions["values"] = ionChoices1

            else:

                primary.coAdductOptions.set("[M-H]")
                primary.coAdductOptions["values"] = ionChoices6            
            
        return

    def grph(primary, event):

        tempMassList = []
        isoMassList = []
        tempAbundanceList = []
        currentMass = 0
        adductCount = primary.numOfAdducts.get()
        resNum = primary.resolution.get()
        #resNum = 1/float(resNum)*225
        coCompoundCount = primary.coCompoundNum.get()
        labelMax = primary.labelCutOffPC.get()
        maxCounts = 0

        if labelMax != "NA":
            labelMax = float(labelMax)
            if labelMax < 0:
                labelMax = 0
            labelMax = labelMax/100
            
        intNum = 0
        n = 0
        testList = []
        
        while intNum < int(adductCount):
            
            if intNum == 0:
                massList, abundanceList, boolErr, eleSybError = primary.massCalc(primary.userForm.get(), primary.chargeState.get(), primary.carbonAbund.get(),
                                                                                 primary.adductIonStr.get(), primary.numOfC13.get(), primary.numOfN15.get(),
                                                                                 primary.numOfH2.get())
                maxCounts = max(abundanceList)*100
                for each in abundanceList:
                    abundanceList[n] = each / (maxCounts/100)
                    n = n + 1
            elif intNum == 1:
                massList, abundanceList, boolErr, eleSybError = primary.massCalc(primary.userForm.get(), primary.A2cState.get(), primary.carbonAbund.get(),
                                                                                 primary.A2IonStr.get(), primary.numOfC13.get(), primary.numOfN15.get(),
                                                                                 primary.numOfH2.get())
                maxCounts = max(abundanceList)*100
                for each in abundanceList:
                    abundanceList[n] = each / (maxCounts/100)
                    n = n + 1
                abundanceList = [x*((float(primary.A2abnd.get()))/100) for x in abundanceList]
            elif intNum == 2:
                massList, abundanceList, boolErr, eleSybError = primary.massCalc(primary.userForm.get(), primary.A3cState.get(), primary.carbonAbund.get(),
                                                                                 primary.A3IonStr.get(), primary.numOfC13.get(), primary.numOfN15.get(),
                                                                                 primary.numOfH2.get())
                maxCounts = max(abundanceList)*100
                for each in abundanceList:
                    abundanceList[n] = each / (maxCounts/100)
                    n = n + 1
                abundanceList = [x*((float(primary.A3abnd.get()))/100) for x in abundanceList]
            elif intNum == 3:
                massList, abundanceList, boolErr, eleSybError = primary.massCalc(primary.userForm.get(), primary.A4cState.get(), primary.carbonAbund.get(),
                                                                                 primary.A4IonStr.get(), primary.numOfC13.get(), primary.numOfN15.get(),
                                                                                 primary.numOfH2.get())
                maxCounts = max(abundanceList)*100
                for each in abundanceList:
                    abundanceList[n] = each / (maxCounts/100)
                    n = n + 1
                abundanceList = [x*((float(primary.A4abnd.get()))/100) for x in abundanceList]
                
            tempMassList = tempMassList + massList
            tempAbundanceList = tempAbundanceList + abundanceList
            intNum = intNum + 1
            n = 0

        if int(coCompoundCount) == 1:
            massList, abundanceList, boolErr, eleSybError = primary.massCalc(primary.userCoForm.get(), primary.coChargeState.get(), primary.coCarbonAbund.get(),
                                                                             primary.coAdductIonStr.get(), primary.coNumOfC13.get(), primary.coNumOfN15.get(),
                                                                             primary.coNumOfH2.get())
            maxCounts = max(abundanceList)*100
            for each in abundanceList:
                abundanceList[n] = each / (maxCounts/100)
                n = n + 1
            abundanceList = [x*((float(primary.coComAbnd.get()))/100) for x in abundanceList]
            tempMassList = tempMassList + massList
            tempAbundanceList = tempAbundanceList + abundanceList

        intNum = 0   
        abundanceList = tempAbundanceList
        massList = tempMassList
        n = 0
        n1 = 1
        
        massList, abundanceList = zip(*sorted(zip(massList, abundanceList)))
        massList, abundanceList = (list(t) for t in zip(*sorted(zip(massList, abundanceList))))
        
        for item in massList:

            currentMass = massList[n]

            while n1 < len(massList):

                if massList[n1] > (currentMass - (currentMass/float(resNum))):
                    if massList[n1] < (currentMass + (currentMass/float(resNum))):
                        if currentMass != 0:
                            currentMass = massList[n]*(abundanceList[n]/(abundanceList[n]+abundanceList[n1]))+massList[n1]*(abundanceList[n1]/(abundanceList[n]+abundanceList[n1]))
                            massList[n1] = 0
                            massList[n] = currentMass
                            abundanceList[n] = abundanceList[n] + abundanceList[n1]
                            abundanceList[n1] = 0
                
                n1 = n1 + 1

            n = n + 1
            n1 = n + 1

        massList = list(filter(lambda a: a != 0, massList))
        abundanceList = list(filter(lambda a: a != 0, abundanceList))

        intNum = 0
        counts = 1
        maxCounts = counts
        maxMass = 0
        minMass = 1000000000
        resVal = StringVar()
        resVal = primary.resolution.get()
        labelHeight = 0
        primary.ax2.clear()
        colorNum = 0.2
        #colorNum2 = 0.9
        colorChange = 0

        if boolErr == 1:
            primary.errorMessage.set("Error: Symbol " + eleSybError + " not available.")
        else:
            primary.errorMessage.set("")

        maxCounts = max(abundanceList)*100

        intNum = 0
        
        for each in massList:
            if massList[intNum] > maxMass:
                maxMass = massList[intNum]  + 0.5
            if massList[intNum] < minMass:
                minMass = massList[intNum]  - 0.5
                
            intNum = intNum + 1

        labelHeight = (maxCounts+100/4)*0.03
        
        intNum = len(massList)-1

        primary.txt.configure(state="normal")
        primary.txt.delete(1.0, END)
        massText = StringVar()
        abundText = StringVar()

        for each in massList:

            massText = "%.5f" % float(massList[intNum])
            abundText = "%.4f" % float((abundanceList[intNum])*100)
            primary.txt.insert('1.0', massText + ': ' + abundText + '\n')
            intNum = intNum - 1
        
        primary.txt.configure(state="disabled")
        intNum = 0

        colorsMap = [(0.976,0.333,0.518), (0.976,0.333,0.518), (0.976,0.333,0.518)]
        
        while intNum < len(abundanceList):
          
            #primary.ax2.plot([massList[intNum] - (massList[intNum]/float(resVal)),massList[intNum]], [0,(abundanceList[intNum]*100)], color = (colorNum,1-colorNum,0.952)) #"b")
            #primary.ax2.plot([massList[intNum] + (massList[intNum]/float(resVal)),massList[intNum]], [0,(abundanceList[intNum]*100)], color = (colorNum,1-colorNum,0.952)) #"b")
            x = np.linspace(massList[intNum] - (massList[intNum]/float(resVal)), massList[intNum] + (massList[intNum]/float(resVal)), 200)
            y = (abundanceList[intNum]*50)*np.sin((np.pi*(1/(massList[intNum]/float(resVal)*2)*2))*x-((massList[intNum]-((massList[intNum]/float(resVal)*0.5)))*(np.pi*(1/(massList[intNum]/float(resVal)*2)*2)))) + (abundanceList[intNum]*50)
            primary.ax2.plot(x, y, color = (colorNum,1-colorNum,0.952))
            #primary.ax2.plot([massList[intNum],massList[intNum]], [0,(abundanceList[intNum]*100)], color = (colorNum,1-colorNum,0.952))
            primary.ax2.plot([0,30000], [0,0], "b", linewidth=0.5)

            if labelMax != "NA":
                if abundanceList[intNum] > float(labelMax):
                    primary.ax2.text(massList[intNum], (abundanceList[intNum]*100)+labelHeight, str(format(massList[intNum],'.4f')), fontsize=9, rotation=80)
                if abundanceList[intNum] <= float(labelMax):
                    if (intNum > 3) and (intNum+4 < len(abundanceList)):
                        if (abundanceList[intNum] > abundanceList[intNum+1]) and (abundanceList[intNum] > abundanceList[intNum+2]) \
                           and (abundanceList[intNum] > abundanceList[intNum+3]) and (abundanceList[intNum] > abundanceList[intNum+4]):
                            if (abundanceList[intNum] > abundanceList[intNum-1]) and (abundanceList[intNum] > abundanceList[intNum-2]) \
                               and (abundanceList[intNum] > abundanceList[intNum-3]) and (abundanceList[intNum] > abundanceList[intNum-4]):
                                primary.ax2.text(massList[intNum], (abundanceList[intNum]*100)+labelHeight, str(format(massList[intNum],'.4f')), fontsize=9, rotation=80)
                    elif (intNum == 3) and (intNum+1 < len(abundanceList)) and (abundanceList[intNum] > abundanceList[intNum+1]) \
                         and (abundanceList[intNum] > abundanceList[intNum-1]) and (abundanceList[intNum] > abundanceList[intNum-2]):
                        primary.ax2.text(massList[intNum], (abundanceList[intNum]*100)+labelHeight, str(format(massList[intNum],'.4f')), fontsize=9, rotation=80)
                    elif (intNum == 2) and (intNum+1 < len(abundanceList)) and (abundanceList[intNum] > abundanceList[intNum+1]) \
                         and (abundanceList[intNum] > abundanceList[intNum-1]) and (abundanceList[intNum] > abundanceList[intNum-2]):
                        primary.ax2.text(massList[intNum], (abundanceList[intNum]*100)+labelHeight, str(format(massList[intNum],'.4f')), fontsize=9, rotation=80)
                    elif (intNum == 1) and (intNum+1 < len(abundanceList)) and (abundanceList[intNum] > abundanceList[intNum+1]) and (abundanceList[intNum] > abundanceList[intNum-1]):
                        primary.ax2.text(massList[intNum], (abundanceList[intNum]*100)+labelHeight, str(format(massList[intNum],'.4f')), fontsize=9, rotation=80)
                    elif (intNum == 0) and (intNum+1 < len(abundanceList)) and (abundanceList[intNum] > abundanceList[intNum+1]) and (abundanceList[intNum] > abundanceList[intNum+2]):
                        primary.ax2.text(massList[intNum], (abundanceList[intNum]*100)+labelHeight, str(format(massList[intNum],'.4f')), fontsize=9, rotation=80)
                
            primary.ax2.set_xlabel('Mass to charge (m/z)')
            primary.ax2.set_title('Isotope Pattern')
            primary.ax2.set_ylabel('Relative Abundance')

            if colorChange == 0:
                colorNum = colorNum + 0.02

            if colorChange == 1:
                colorNum = colorNum - 0.02
      
            #colorNum2 = colorNum2 - 0.01
            
            if colorNum > 1:
                colorNum = colorNum - 0.04
                colorChange = 1

            if colorNum < 0.2:
                colorNum = colorNum + 0.04
                colorChange = 0

            #if colorNum2 < 0.5:
            #    colorNum2 = 0.9

            intNum = intNum + 1

        primary.ax2.set_ylim( ((-(100+100/4))/50,maxCounts+maxCounts/4) )
        primary.ax2.set_xlim( (minMass - ((maxMass-minMass)*0.1), maxMass + ((maxMass-minMass)*0.1)) )
        primary.canvas.draw()
        
        return

    def AdductChargeRefresh(primary, *args):

        result = getattr(primary, 'ionAdList')()
        result = getattr(primary, 'ionAdListA2')()
        result = getattr(primary, 'ionAdListA3')()
        result = getattr(primary, 'ionAdListA4')()
        result = getattr(primary, 'ionAdListCoCom')()

        return

    def AdductRefresh(primary):
        
        numOfAds1 = primary.numOfAdducts.get()
        numOfMols = primary.coCompoundNum.get()

        if numOfAds1 == "1":
            
            primary.adductOptionsA2.configure(state="disabled")
            primary.adductOptionsA3.configure(state="disabled")
            primary.adductOptionsA4.configure(state="disabled")
            primary.A2AbundVal.configure(state="disabled")
            primary.A3AbundVal.configure(state="disabled")
            primary.A4AbundVal.configure(state="disabled")
            primary.A2chargeVal.configure(state="disabled")
            primary.A3chargeVal.configure(state="disabled")
            primary.A4chargeVal.configure(state="disabled")
            
        if numOfAds1 == "2":

            primary.adductOptionsA2.configure(state="enabled")
            primary.adductOptionsA3.configure(state="disabled")
            primary.adductOptionsA4.configure(state="disabled")
            primary.A2AbundVal.configure(state="normal")
            primary.A3AbundVal.configure(state="disabled")
            primary.A4AbundVal.configure(state="disabled")
            primary.A2chargeVal.configure(state="normal")
            primary.A3chargeVal.configure(state="disabled")
            primary.A4chargeVal.configure(state="disabled")
            
        if numOfAds1 == "3":

            primary.adductOptionsA2.configure(state="enabled")
            primary.adductOptionsA3.configure(state="enabled")
            primary.adductOptionsA4.configure(state="disabled")
            primary.A2AbundVal.configure(state="normal")
            primary.A3AbundVal.configure(state="normal")
            primary.A4AbundVal.configure(state="disabled")
            primary.A2chargeVal.configure(state="normal")
            primary.A3chargeVal.configure(state="normal")
            primary.A4chargeVal.configure(state="disabled")

        if numOfAds1 == "4":

            primary.adductOptionsA2.configure(state="enabled")
            primary.adductOptionsA3.configure(state="enabled")
            primary.adductOptionsA4.configure(state="enabled")
            primary.A2AbundVal.configure(state="normal")
            primary.A3AbundVal.configure(state="normal")
            primary.A4AbundVal.configure(state="normal")
            primary.A2chargeVal.configure(state="normal")
            primary.A3chargeVal.configure(state="normal")
            primary.A4chargeVal.configure(state="normal")

        if numOfMols != "0":

            primary.coAdductOptions.configure(state="normal")
            primary.coIonAbundVal.configure(state="normal")
            primary.coMZEntry.configure(state="normal")
            primary.coChargeVal.configure(state="normal")
            primary.coExtraC13Val.configure(state="normal")
            primary.coCarbonVal.configure(state="normal")
            primary.coExtraN15Val.configure(state="normal")
            primary.coExtraH2Val.configure(state="normal")

        else:

            primary.coAdductOptions.configure(state="disabled")
            primary.coIonAbundVal.configure(state="disabled")
            primary.coMZEntry.configure(state="disabled")
            primary.coChargeVal.configure(state="disabled")
            primary.coExtraC13Val.configure(state="disabled")
            primary.coCarbonVal.configure(state="disabled")
            primary.coExtraN15Val.configure(state="disabled")
            primary.coExtraH2Val.configure(state="disabled")
        
        return

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('IsoPat 1.11')
    img = PhotoImage(data=iconData)
    app.tk.call('wm', 'iconphoto', app._w, img)
    app.mainloop()

