import os
import webbrowser
import subprocess

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
