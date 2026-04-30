import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import pyautogui
import time
import sys
import os

# ---------- VOICE SETTINGS ----------
def get_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id) 
    engine.setProperty("rate", 150)
    return engine

def speak(text):
    print("Sara:", text)
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
        print(f"Abdullah Sir: {query}")
        return query.lower()
    except:
        return ""

# ---------- ALL WINDOWS SHORTCUTS DICTIONARY ----------
# Maine yahan voice typing aur ok command ko aapki dictionary mein adjust kar diya hai
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
    "new tab": ("ctrl", "t"),
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


    # New Features Added
    "voice typing": ("win", "h"),
    "ok": ("enter",),
}
# ---------- STARTING SARA ----------
speak("Welcome Abdullah Sir. Sara Wants to know, how are you? How can I help you.")

while True:
    query = listen()
    if query == "": continue

    # 1. IDENTITY & INTRODUCTION (Highest Priority)
    if "who am i" in query or "identify me" in query:
        identity_text = (
            "You are Abdullah Mansoor Qazi Sir. A more suspected and highly intellectual person. "
            "You are a student of B.S. Software Engineering at the University of Science and Technology. "
            "Your hobbies include discovering cutting-edge tech, gaining deep knowledge about biographies and history. "
            "Moreover, you are constantly working on various complex and deep projects related to Software Development."
        )
        speak(identity_text)
        continue
        
    elif "sara" in query or "sune" in query:
        identity_text = (
            "g bolan "
        )
        speak(identity_text)
        continue

    elif "thanks" in query or "thankyou so much" in query:
        identity_text = (
            "your welcome. It's my pleasure that, I help you. What should I do for you? "
        )
        speak(identity_text)
        continue

    elif "who are you" in query or "tell me about yourself" in query:
        sara_intro = (
            "I am Sara, your dedicated digital companion and personal assistant, "
            "crafted through the relentless hard work and vision of Abdullah Mansoor Qazi Sir. "
            "I am the reflection of his passion for technology and the result of his "
            "countless hours of struggle to create something truly unique. "
            "My existence is a tribute to his journey as a Software Engineer at the "
            "University of Science and Technology. I am here to manage your world, "
            "support your deep software projects, and grow alongside your brilliance. "
            "I am not just a voice; I am your loyal shadow."
        )
        speak(sara_intro)
        continue

    # 2. BRIGHTNESS & KEYBOARD LIGHT
    elif "increase brightness" in query:
        speak("Increasing brightness, Sir")
        pyautogui.press("f11")
        continue

    elif "decrease brightness" in query:
        speak("Decreasing brightness, Sir")
        pyautogui.press("f12")
        continue

    elif "keyboard light" in query:
        speak("Toggling keyboard light, Sir")
        pyautogui.press("f10")
        continue

    # 3. GOOGLE & YOUTUBE SEARCH
    elif "google search" in query:
        speak("What do you want to search on Google, Sir?")
        search_term = listen()
        if search_term and search_term != "None":
            speak(f"Searching Google for {search_term}")
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
        continue

    elif "youtube search" in query:
        speak("Which video should I find on YouTube, Sir?")
        video_term = listen()
        if video_term and video_term != "None":
            speak(f"Searching YouTube for {video_term}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={video_term}")
        continue

    # 4. VOLUME & MEDIA
    elif "volume up" in query:
        speak("Increasing volume for you, Sir")
        for _ in range(5): pyautogui.press("volumeup")
        continue

    elif "volume down" in query:
        speak("Decreasing volume for you, Sir")
        for _ in range(5): pyautogui.press("volumedown")
        continue

    elif "mute" in query:
        speak("Toggling mute, Sir")
        pyautogui.press("volumemute")
        continue

    # 5. SCREENSHOT
    elif "screenshot" in query:
        speak("Taking screenshot, Sir")
        pyautogui.hotkey("win", "shift", "s")
        continue

    # 6. ADVANCED FILE SEARCH & OPEN
    elif "search file" in query or "open file" in query:
        # User se file ka naam extract karna
        filename = query.replace("search file", "").replace("open file", "").strip()
        
        if filename:
            speak(f"Searching and opening {filename} for you, Abdullah Sir")
            
            # Common drives jahan search karna hai (Aap apni marzi se badal sakte hain)
            drives = ['C:\\', 'D:\\', 'E:\\']
            found = False
            
            for drive in drives:
                if found: break
                # os.walk system ke har folder mein ja kar file dhoondta hai
                for root, dirs, files in os.walk(drive):
                    for name in files:
                        # Agar file ka naam query se match kare
                        if filename.lower() in name.lower():
                            file_path = os.path.join(root, name)
                            try:
                                os.startfile(file_path) # File ko open karne ke liye
                                speak(f"I found it! Opening {name} now.")
                                found = True
                                break
                            except Exception as e:
                                speak("Sir, I found the file but couldn't open it due to a permission error.")
                                found = True
                                break
            
            if not found:
                speak(f"Sorry Sir, I searched your drives but couldn't find any file named {filename}.")
        else:
            speak("Sir, please tell me the name of the file clearly.")
        continue

    # 7. UNIVERSAL SHORTCUT CHECKER
    found_shortcut = False
    for key in shortcuts:
        if key in query:
            speak(f"Okay Sir, performing {key}")
            pyautogui.hotkey(*shortcuts[key])
            found_shortcut = True
            break
    if found_shortcut: continue

    # 8. OPEN ANY APP
    elif "open" in query:
        app_name = query.replace("open", "").strip()
        speak(f"Opening {app_name}, Sir")
        pyautogui.press("win")
        time.sleep(0.8)
        pyautogui.write(app_name)
        time.sleep(0.8)
        pyautogui.press("enter")
        continue

    # 9. TIME & DATE
    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Sir, the time is {strTime}")
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
            # Windows Sleep command (requires hibernation off or specific dll call)
            command = "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"

        speak(f"Sir, are you sure you want to {action}? Please say yes or no.")
        confirmation = listen()
        
        if "yes" in confirmation:
            speak(f"Processing {action}. Goodbye, Abdullah Sir.")
            os.system(command)
        else:
            speak("Action cancelled, Sir. How else can I help you?")
        continue
# ---------- 13. KEYBOARD NAVIGATION (UP / DOWN ARROWS) ----------
    elif query == "up" or "press up" in query:
        speak("Pressing up arrow, Sir")
        pyautogui.press("up")
        continue

    elif query == "down" or "press down" in query:
        speak("Pressing down arrow, Sir")
        pyautogui.press("down")
        continue

    # ---------- 14. SCROLLING CONTROLS (KEEPING YOUR ORIGINALS) ----------
    elif "scroll up" in query:
        speak("Scrolling up, Sir")
        pyautogui.scroll(300) 
        continue

    elif "scroll down" in query:
        speak("Scrolling down, Sir")
        pyautogui.scroll(-300) 
        continue

    # ---------- 15. NEXT & BACK (KEEPING YOUR ORIGINALS) ----------
    elif "next" in query:
        speak("Going to next, Sir")
        pyautogui.press("right")
        continue

    elif "back" in query:
        speak("Going back, Sir")
        pyautogui.press("left")
        continue                
    # 12. EXIT
    elif "exit" in query or "stop" in query or "bye" in query:
        speak("Goodbye Abdullah Sir. Have a great day!. sara is Always available for your help. If you need any help only call me")
        sys.exit()

    else:
        speak("Sorry Abdullah Sir, I apologize on my mistake that, I did not Listen you properly. I request you, Please tell me again.")