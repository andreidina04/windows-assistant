import os
import webbrowser
import subprocess
import datetime
from pathlib import Path
import platform

def open_links(user_text):
    websites = {"google": "https://www.google.com",
                "youtube": "https://www.youtube.com",
                "github": "https://www.github.com"}
    for key, url in websites.items():
        if key in user_text:
            webbrowser.open(url)
            return f"Opened {key.capitalize()}! Enjoy!"

    browser_keywords = ["browser", "chrome", "google", "internet", "brave", "edge"]
    if any(word in user_text for word in browser_keywords):
        webbrowser.open("https://www.google.com")
        return f"Opened the browser for you!"

    ytb_keywords = ["ytb", "yt"]
    if any(word in user_text for word in ytb_keywords):
        webbrowser.open("https://www.youtube.com")
        return f"Opened Youtube for you! Enjoy watching!"
    return "I couldn't figure out which website to open."


def create_folder(user_text):
    folder_keywords = ["create folder", "directory", "mkdir"]
    extracted_text = user_text.lower()
    for word in folder_keywords:
        extracted_text = extracted_text.replace(word, "")
    folder_name = extracted_text.strip()
    if not folder_name:
        return "Please use the command 'create folder folder_name'"
    try:
        desktop_path = Path.home() / "Desktop" / folder_name
        desktop_path.mkdir(parents=True, exist_ok=True)
        return f"Created the folder '{folder_name}' on Desktop for you!"
    except Exception as e:
        return f"Error: {str(e)}"

def create_file(user_text):
    folder_keywords = ["create file", "file"]
    extracted_text = user_text.lower()
    for word in folder_keywords:
        extracted_text = extracted_text.replace(word, "")
    file_name = extracted_text.strip()
    if not file_name:
        return "Please use the command 'create file file_name'"
    try:
        file_path = Path.home() / "Desktop" / file_name
        file_path.touch()
        return f"Created the file '{file_name}' on Desktop for you!"
    except Exception as e:
        return f"Error: {str(e)}"

def greetings(user_text):
        return "Glad to help! Everytime when you need me I'm here."

def close_app(user_text):
    return "Bye! The application is closing..."

def show_time(user_text):
    current_time = datetime.datetime.now()
    return current_time.strftime("Date: %d.%m.%Y | Hour: %H:%M:%S")

def computer_info(user_text):
    my_system = platform.uname()
    return (f"\nSystem Information\n"
            "---------------------\n"
            f"OS : {my_system.system}\n"
            f"Node Name : {my_system.node}\n"
            f"Release : {my_system.release}\n"
            f"Version : {my_system.version}\n"
            f"Machine : {my_system.machine}\n"
            f"Processor : {my_system.processor}")
