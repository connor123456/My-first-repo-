import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("whats your favorite show")

show = pg.prompt("Enter your favorite show below")
if show == "friends":
    speak.Speak("that is my favorite also")
elif show == "the office":
    speak.Speak("good show")
else:
    speak.Speak("I've never seen it")


speak.Speak("what video would you like to watch")

video = pg.prompt("enter video below")
speak.Speak("ok lets look for" + video + " on YouTube")

wb.open("https://www.youtube.com/results?search_query=" + video)
