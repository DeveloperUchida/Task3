import PySimpleGUI as sg
import datetime

sg.theme("DarkBrown3")

layout = [
    [sg.Text("0:00:00.000000", font=("Arial", 30), key="text", size=(15, 1), justification="center")],
    [sg.Push(), sg.Button("START/STOP", key="btn", size=(11, 1)), sg.Push()]
]

win = sg.Window("ストップウォッチ", layout, font=(None, 14), size=(400, 120), keep_on_top=True)

startflag = False
start = None

while True:
    event, values = win.read(timeout=50)

    if event == sg.WIN_CLOSED:
        break

    if event == "btn":
        if startflag:
            startflag = False
        else:
            start = datetime.datetime.now()
            startflag = True

    if startflag:
        now = datetime.datetime.now()
        elapsed_time = now - start
        # 経過時間を適切に表示するためにフォーマット
        formatted_time = "{:02}:{:02}:{:02}.{:06}".format(
            elapsed_time.seconds // 3600,
            (elapsed_time.seconds // 60) % 60,
            elapsed_time.seconds % 60,
            elapsed_time.microseconds
        )
        win["text"].update(formatted_time)

win.close()
