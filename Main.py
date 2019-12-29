"""
Woke up one morning bored and went for a walk.
Decided to try my hand at making a personal assistant named leo.
_Author_ Xavier Naranjo
start date 12/29/2019
"""
import Time
import win32com.client as wincl
import speech_recognition as sr

def main():
    """
the main run time of Leo
 the personal assistant
    """
    speak = wincl.Dispatch("SAPI.SpVoice")
    first_time_starting = "Hello, My name is Leo. I am a personal assistant."
    speak.speak(first_time_starting)
    task_or_question_from_human = str(input(speak.speak("How can I help you ? ")))
    # if task_or_question_from_human == unknown_task_or_question:
    # print("I'm Sorry I do not know how to help you yet. Forgive me I and still learning."
    # "Lets Try something else. ")
    possible_time_related_questions = ["What time is it ?", "What is the time ?", "What's the time ?",
                                       "What time it is ?"]
    while task_or_question_from_human not in possible_time_related_questions:
        speak.speak("I'm Sorry I do not know how to help you yet. Forgive me I am still learning.")
        # "Lets Try something else.")
        task_or_question_from_human = str(input(speak.speak("How can I help you ? ")))
    if task_or_question_from_human in possible_time_related_questions:
        speak.speak("Current Time is "), Time.what_time()


main()
