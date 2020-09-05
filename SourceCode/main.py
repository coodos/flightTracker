from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from opensky_api import OpenSkyApi

# Variables that we need later down the code
latitudes = []
longitudes = []
altitudes = []

def plotLatLon():
    def plotCoorData(var):
        icao = icaoEntry.get()
        api = OpenSkyApi(username = 'user', password = 'passwd')
        states = api.get_states(icao24=icao)
        for s in states.states:
            latitudes.append(s.latitude)
            longitudes.append(s.longitude)
        plt.cla
        plt.plot(longitudes, latitudes)
    plt.xlabel('Longitde')
    plt.ylabel('Latitude')
    liveData = FuncAnimation(plt.gcf(), plotCoorData, interval = 1000)
    plt.tight_layout()
    plt.show()

def plotAlt():
    def plotAltData(var):
        icao = icaoEntry.get()
        api = OpenSkyApi(username = 'user', password = 'passwd')
        states = api.get_states(icao24=icao)
        for s in states.states:
            altitudes.append(s.baro_altitude)
        plt.cla()
        plt.plot(altitudes)
    liveData = FuncAnimation(plt.gcf(), plotAltData, interval = 1000)
    plt.ylabel('Altitude')
    plt.tight_layout()
    plt.show()

def getData():
    # Loop to get the data
    icao = icaoEntry.get()
    api = OpenSkyApi(username = 'user', password = 'passwd')
    states = api.get_states(icao24=icao)
    for s in states.states:
        # Things to display in output frame
        Label(outputFrame, text = f'Latitude : {s.latitude}', font = subFont).grid(row = 0, column = 0, padx = 10, pady = 2)
        Label(outputFrame, text = f'Longitude : {s.longitude}', font = subFont).grid(row = 1, column = 0, padx = 10, pady = 2)
        Label(outputFrame, text = f'Altitude : {s.baro_altitude}', font = subFont).grid(row = 2, column = 0, padx = 10, pady = 2)
        Label(outputFrame, text = f'Velocity : {s.velocity}', font = subFont).grid(row = 3, column = 0, padx = 10, pady = 2)
        Label(outputFrame, text = f'Heading : {s.heading}', font = subFont).grid(row = 4, column = 0, padx = 10, pady = 2)
        Label(outputFrame, text = f'Country : {s.origin_country}', font = subFont).grid(row = 5, column = 0, padx = 10, pady = 2)

# Main GUI to put frames in
root = Tk()
root.title('Live Aircraft Details | Made by Merul Dhiman')
root.resizable(False, False)

### Frames to containerise areas of the main window

# Main Frames
headingFrame = Frame (root, height = 60, width = 800, bg =  '#3d3d3d')
headingFrame.grid_propagate(0)
headingFrame.grid(column = 0, row = 0)

mainFrame = Frame(height = 400, width = 800)
mainFrame.grid_propagate(0)
mainFrame.grid(column = 0, row = 1)

# Sub-Frames
inputFrame = Frame(mainFrame, height = 400, width = 330, bg = '#b5b5b5')
inputFrame.grid_propagate(0)
inputFrame.grid(column = 0, row = 0)

outputFrame = Frame(mainFrame, height = 300, width = 670)
outputFrame.grid_propagate(0)
outputFrame.grid(column = 1, row = 0, pady = 50)



### Main GUI goes here like all the widgets and stuff


##  Labels
# Fonts as tuples
Font = ('Arial', 18, 'bold')
subFont = ('Arial', 17)
#Labels
Label(headingFrame, text = 'Get Live Flight Details', font = ('Arial', 24, 'bold'), bg = '#3d3d3d', fg = 'white').grid(padx = 200, pady = 5)
Label(inputFrame, text = 'NOTE: Enter the ICAO24 bit Address or the Mode S (hex)', bg = '#ffff82').grid(row = 0, column = 0, padx = 10, pady = 2)
Label(inputFrame, text = 'value from an aircraft available at', bg = '#ffff82').grid(row = 1, column = 0, pady = 2)
Label(inputFrame, text = ' https://opensky-network.org some ICAO24', bg = '#ffff82').grid(row = 2, column = 0, pady = 2)
Label(inputFrame, text = 'addresses may not work! Enter 4ca5b7 for example', bg = '#ffff82').grid(row = 3, column = 0, pady = 2)

## Interactibles 
#Entry
icaoEntry = Entry(inputFrame, width = 40)
icaoEntry.grid(row = 4, column = 0, pady = 30)

#Button
getDataButton = Button(inputFrame, text = 'Get Data', font = subFont, bg = '#3d3d3d', fg = 'white',  command = getData)
getDataButton.grid(row = 5, column = 0)
plotLatLonButton= Button(inputFrame, text = 'Plot Lat/Lon Graph', bg = '#3d3d3d', fg = 'white', width = 14, command = plotLatLon)
plotLatLonButton.grid(row = 6, column = 0, pady = 10) 
plotAltitudeButton = Button(inputFrame, text = 'Plot Altitude Graph', bg = '#3d3d3d', fg = 'white', width = 14, command = plotAlt)
plotAltitudeButton.grid(row = 7, column = 0)

root.mainloop()