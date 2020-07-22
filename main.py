import PySimpleGUI as sg
from pytube import YouTube
import ffmpeg
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Youtube Downloader')],
            [sg.Text('Link:'), sg.InputText(key="link")],
            [sg.Button('MP3'),sg.Button('MP4'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('bruh', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'MP4':
        print('Downloading..')
        YouTube(values['link']).streams.first().download()
        sg.popup('Success.', title='MP4 File was downloaded.')
    if event == 'MP3':
        print('Downloading..')
        input = ffmpeg.input(YouTube(values['link']).streams.first().download())
        audio = input.audio.filter("aecho", 0.8, 0.9, 1000, 0.3)
        video = input.video.hflip()
        out = ffmpeg.output(audio, 'convert.mp3')
        sg.popup('Success.', title='MP3 file was downloaded.')


    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break


window.close()
