import PySimpleGUI as sg

sg.theme("DarkAmber")

layout = [[sg.Text("")], [sg.Text("Choose Source folder: ", size=(20, 1)), sg.InputText(), sg.FolderBrowse()], [sg.Text("Choose Destination folder: ", size=(20, 1)), sg.InputText(), sg.FolderBrowse()], [sg.Text("")], [sg.Button("Submit", size=(8, 1))]]

window = sg.Window("Python OS Project", layout, size=(600,200))
    
while True:
    event, values = window.read()

    if values[0] == '':
        print("Source Path can't be empty")
        continue

    if values[1] == '':
        print("Destination Path can't be empty")
        continue
    
    if event == sg.WIN_CLOSED or event=="Exit":
        break
    
    elif event == "Submit":
        source=values[0]
        destination=values[1]
        break