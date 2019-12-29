import win32com.client as wincl


def what_time():
    speak = wincl.Dispatch("SAPI.SpVoice")
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    str(current_time)
    return speak.speak(current_time)
