import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import pyautogui
import time
import sys
import os

# ---------- GLOBAL SESSION MEMORY ----------
user_name = ""
user_info = ""

# ---------- VOICE SETTINGS ----------
def get_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id) 
    engine.setProperty("rate", 150)
    return engine

def speak(text):
    print("Zahra:", text)
    engine = get_engine()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ---------- LISTEN FUNCTION ----------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="en-in")
        print(f"User ({user_name if user_name else 'Unknown'}): {query}")
        return query.lower()
    except:
        return ""

# ---------- ALL WINDOWS SHORTCUTS DICTIONARY ----------
shortcuts = {
    "copy": ("ctrl", "c"),
    "paste": ("ctrl", "v"),
    "cut": ("ctrl", "x"),
    "undo": ("ctrl", "z"),
    "redo": ("ctrl", "y"),
    "select all": ("ctrl", "a"),
    "save": ("ctrl", "s"),
    "print": ("ctrl", "p"),
    "delete": ("delete",),
    
    # Window Management
    "close window": ("alt", "f4"),
    "close tab": ("ctrl", "w"),
    "new tab": ("ctrl" , "t"),
    "switch window": ("alt", "tab"),
    "minimise window": ("win", "down"),
    "maximize window": ("win", "up"),
    "show desktop": ("win", "d"),
    "minimise all": ("win", "m"),
    "show windows": ("win", "tab"),
    "working windows": ("alt", "ctrl", "tab"),    

    # System Apps
    "task manager": ("ctrl", "shift", "esc"),
    "settings": ("win", "i"),
    "file explorer": ("win", "e"),
    "run": ("win", "r"),
    "windows search": ("win", "s"),
    "safe zone": ("win", "l"),
    "action center": ("win", "a"),
    "game bar": ("win", "g"),
    "clipboard history": ("win", "v"),
    "projection": ("win", "p"),
    "zoom in": ("win","="),
    "zoom out": ("win","-"),

    # Features Added
    "voice typing": ("win", "h"),
    "ok": ("enter",),
}

# ---------- STARTING ZAHRA ----------
speak("Welcome. Zahra is available for help.")
speak("What is your name?")

# Name Capture at Startup
captured_name = listen()
if captured_name:
    user_name = captured_name.title()
else:
    user_name = "Guest"

speak(f"Hello {user_name}, how can I help you today?")

while True:
    query = listen()
    if query == "": 
        continue

    # 1. IDENTITY & INTRODUCTION (Highest Priority)
    if "who am i" in query or "identify me" in query:
        # Check if the captured name refers to Abdullah Mansoor Qazi Sir
        if "abdullah" in user_name.lower():
            identity_text = (
                "You are Abdullah Mansoor Qazi Sir. A more suspected and highly intellectual person. "
                "You are a student of B.S. Software Engineering at the University of Science and Technology. "
                "Your hobbies include discovering cutting-edge tech, gaining deep knowledge about biographies and history. "
                "Moreover, you are constantly working on various complex and deep projects related to Software Development."
            )
            speak(identity_text)
        else:
            if not user_info:
                speak(f"You are {user_name}. I know nothing about you, so tell me about yourself.")
                info_input = listen()
                if info_input:
                    user_info = info_input
                    speak(f"Thank you {user_name}. I have remembered your information for this session.")
                else:
                    speak("I couldn't hear your details properly. Please ask me again whenever you are ready.")
            else:
                speak(f"You are {user_name}. Here is what you told me about yourself: {user_info}")
        continue
        
    elif "zahra" in query or "sune" in query:
        speak("g bolan")
        continue

    elif "thanks" in query or "thankyou so much" in query:
        speak("Your welcome. It's my pleasure that I help you. What should I do for you?")
        continue

    elif "who are you" in query or "tell me about yourself" in query:
        zahra_intro = (
            "I am Zahra, your dedicated digital companion and personal assistant, "
            "crafted through the relentless hard work and vision of Abdullah Mansoor Qazi Sir. "
            "I am the reflection of his passion for technology and the result of his "
            "countless hours of struggle to create something truly unique. "
            "My existence is a tribute to his journey as a Software Engineer at the "
            "University of Science and Technology. I am here to manage your world, "
            "support your deep software projects, and grow alongside your brilliance. "
            "I am not just a voice; I am your loyal shadow."
        )
        speak(zahra_intro)
        continue

    # 2. BRIGHTNESS & KEYBOARD LIGHT
    elif "increase brightness" in query:
        speak(f"Increasing brightness for you, {user_name}")
        pyautogui.press("f11")
        continue

    elif "decrease brightness" in query:
        speak(f"Decreasing brightness for you, {user_name}")
        pyautogui.press("f12")
        continue

    elif "keyboard light" in query:
        speak(f"Toggling keyboard light for you, {user_name}")
        pyautogui.press("f10")
        continue

    # 3. GOOGLE & YOUTUBE SEARCH
    elif "google search" in query:
        speak(f"What do you want to search on Google, {user_name}?")
        search_term = listen()
        if search_term and search_term != "none":
            speak(f"Searching Google for {search_term}")
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
        continue

    elif "youtube search" in query:
        speak(f"Which video should I find on YouTube, {user_name}?")
        video_term = listen()
        if video_term and video_term != "none":
            speak(f"Searching YouTube for {video_term}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={video_term}")
        continue

    # 4. VOLUME & MEDIA
    elif "volume up" in query:
        speak(f"Increasing volume for you, {user_name}")
        for _ in range(5): 
            pyautogui.press("volumeup")
        continue

    elif "volume down" in query:
        speak(f"Decreasing volume for you, {user_name}")
        for _ in range(5): 
            pyautogui.press("volumedown")
        continue

    elif "mute" in query:
        speak(f"Toggling mute for you, {user_name}")
        pyautogui.press("volumemute")
        continue

    # 5. SCREENSHOT
    elif "screenshot" in query:
        speak(f"Taking screenshot for you, {user_name}")
        pyautogui.hotkey("win", "shift", "s")
        continue

    # 6. ADVANCED FILE SEARCH & OPEN
    elif "search file" in query or "open file" in query:
        filename = query.replace("search file", "").replace("open file", "").strip()
        
        if filename:
            speak(f"Searching and opening {filename} for you, {user_name}")
            
            drives = ['C:\\', 'D:\\', 'E:\\']
            found = False
            
            for drive in drives:
                if found: 
                    break
                for root, dirs, files in os.walk(drive):
                    for name in files:
                        if filename.lower() in name.lower():
                            file_path = os.path.join(root, name)
                            try:
                                os.startfile(file_path)
                                speak(f"I found it! Opening {name} now.")
                                found = True
                                break
                            except Exception as e:
                                speak(f"{user_name}, I found the file but couldn't open it due to a permission error.")
                                found = True
                                break
            
            if not found:
                speak(f"Sorry {user_name}, I searched your drives but couldn't find any file named {filename}.")
        else:
            speak(f"{user_name}, please tell me the name of the file clearly.")
        continue

    # 7. UNIVERSAL SHORTCUT CHECKER
    found_shortcut = False
    for key in shortcuts:
        if key in query:
            speak(f"Okay {user_name}, performing {key}")
            pyautogui.hotkey(*shortcuts[key])
            found_shortcut = True
            break
    if found_shortcut: 
        continue

    # 8. OPEN ANY APP
    elif "open" in query:
        app_name = query.replace("open", "").strip()
        speak(f"Opening {app_name}, {user_name}")
        pyautogui.press("win")
        time.sleep(0.8)
        pyautogui.write(app_name)
        time.sleep(0.8)
        pyautogui.press("enter")
        continue

    # 9. TIME & DATE
    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"{user_name}, the time is {strTime}")
        continue

    elif "date" in query:
        strDate = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {strDate}")
        continue

    # 11. SYSTEM CONTROL (Shutdown, Restart, Sleep)
    elif any(cmd in query for cmd in ["shutdown", "restart", "sleep mode"]):
        if "shutdown" in query:
            action = "shut down"
            command = "shutdown /s /t 1"
        elif "restart" in query:
            action = "restart"
            command = "shutdown /r /t 1"
        elif "sleep mode" in query:
            action = "put the system to sleep"
            command = "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"

        speak(f"{user_name}, are you sure you want to {action}? Please say yes or no.")
        confirmation = listen()
        
        if "yes" in confirmation:
            speak(f"Processing {action}. Goodbye, {user_name}.")
            # Clear session memory prior to system action
            user_name = ""
            user_info = ""
            os.system(command)
        else:
            speak(f"Action cancelled, {user_name}. How else can I help you?")
        continue

    # 13. KEYBOARD NAVIGATION
    elif query == "up" or "press up" in query:
        speak("Pressing up arrow")
        pyautogui.press("up")
        continue

    elif query == "down" or "press down" in query:
        speak("Pressing down arrow")
        pyautogui.press("down")
        continue

    # 14. SCROLLING CONTROLS
    elif "scroll up" in query:
        speak("Scrolling up")
        pyautogui.scroll(300) 
        continue

    elif "scroll down" in query:
        speak("Scrolling down")
        pyautogui.scroll(-300) 
        continue

    # 15. NEXT & BACK
    elif "next" in query:
        speak("Going to next")
        pyautogui.press("right")
        continue

    elif "back" in query:
        speak("Going back")
        pyautogui.press("left")
        continue                

    # 12. EXIT
    elif "exit" in query or "stop" in query or "bye" in query:
        speak(f"Goodbye {user_name}. Have a great day! Zahra is always available for your help. If you need any help, only call me.")
        # Reset session variables and exit process
        user_name = ""
        user_info = ""
        sys.exit()

    else:
        speak(f"Sorry {user_name}, I apologize. I did not hear you properly. Please tell me again.")