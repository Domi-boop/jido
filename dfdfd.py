import tkinter as tk
from tkinter import messagebox, ttk
import time

# Sample dictionaries for different languages
dictionaries = {
    #DOMINION
  "Igala": {
        "hello"  :"kó",
        "thank you": "anẹ",
        "please": "ẹ biko",
        "yes": "ẹẹ",
        "no": "ọda",
        "water": "ama",
        "food": "nra",
        "house": "ụla",
        "book": "akwụkwọ",
        "man": "ọmẹ",
        "woman": "ọb’iyọ",
        "Head": "Oji",
        "Hand": "Ówó",
        "Forehead": "Ógba Oji",
        "Blood": "Ebié",
        "Breath": "Imi",
        "four": "Őnáńá",
        "bench": "Èkpé"

    },
    #RUTH JACE
    "French": {
        "bonjour": "hello",
        "merci": "thank you",
        "au revoir": "goodbye",
        "s'il vous plaît": "please",
        "oui": "yes",
        "non": "no",
        "ami": "friend",
        "famille": "family",
        "amour": "love",
        "eau": "water",
        "nourriture": "food",
        "maison": "house",
        "école": "school",
        "heureux": "happy",
        "triste": "sad",
        "grand": "big",
        "petit": "small",
        "beau": "beautiful",
        "laid": "ugly",
        "fort": "strong",
        "faible": "weak",
        "travail": "work",
        "jouer": "play"
    },
    #ASHUR
      "Italian": {
        "ciao": "hello",
        "grazie": "thank you",
        "arrivederci": "goodbye",
        "per favore": "please",
        "sì": "yes",
        "no": "no",
        "amico": "friend",
        "familia": "family",
        "amore": "love",
        "acqua": "water",
        "cibo": "food",
        "casa": "house",
        "scuola": "school",
        "felice": "happy",
        "triste": "sad",
        "grande": "big",
        "piccolo": "small",
        "bello": "beautiful",
        "brutto": "ugly",
        "forte": "strong",
        "debole": "weak",
        "lavoro": "work",
        "giocare": "play"
    },
    #AZAD
    "German": {
        "hallo": "hello",
        "danke": "thank you",
        "auf wiedersehen": "goodbye",
        "ja": "yes",
        "nein": "no",
        "bitte": "please",
        "entschuldigung": "excuse me/sorry",
        "gut": "good",
        "schlecht": "bad",
        "freund": "friend",
        "haus": "house",
        "wasser": "water",
        "essen": "food",
        "buch": "book",
        "schule": "school",
        "lehrer": "teacher",
        "schüler": "student",
        "arbeit": "work",
        "familie": "family",
        "hilfe": "help"
    },
    #ALEX
    "Hausa": {
        "gida": "house",
        "mota": "car",
        "ruwa": "water",
        "abinci": "food",
        "suna": "name",
        "lafiya": "health",
        "kudi": "money",
        "yara": "children",
        "baba": "father",
        "mama": "mother",
        "doki": "horse",
        "gari": "town",
        "baki": "mouth",
        "hanya": "road",
        "kasa": "land",
        "gaskiya": "truth",
        "zuciya": "heart",
        "sako": "message",
        "fata": "skin",
        "hankali": "wisdom"
    }
}
  
def search_word():
    word = entry.get().strip().lower()
    selected_language = language_var.get()
    dictionary = dictionaries[selected_language]
    
    # Simulate loading effect
    loading_label.config(text="please wait...")
    root.update()
    time.sleep(1)  # Simulate a delay for loading

    meaning = dictionary.get(word)
    loading_label.config(text="")
    
    if meaning:
        messagebox.showinfo("Meaning", f"The meaning of '{word}' in {selected_language} is: {meaning}")
    else:
        messagebox.showwarning("Not Found", f"'{word}' not found in the {selected_language} dictionary.")

# Create the main window
root = tk.Tk()
root.title("Multi-Language Dictionary")
root.geometry("1000x1500")
root.configure(bg='yellow')

# Create a label for language selection
language_var = tk.StringVar(value="French")
language_label = tk.Label(root, text="Select Language:", bg='black', fg='white')
language_label.pack(pady=10)

# Create a dropdown for language selection
language_dropdown = ttk.Combobox(root, textvariable=language_var, values=list(dictionaries.keys()))
language_dropdown.pack(pady=10)

# Create a label for word entry
label = tk.Label(root, text="Enter word:", bg='black', fg='red')
label.pack(pady=10)

# Create an entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a loading label
loading_label = tk.Label(root, text="", bg='black', fg='white')
loading_label.pack(pady=10)

# Create a search button
search_button = tk.Button(root, text="Search", command=search_word, bg='gray', fg='white')
search_button.pack(pady=20)

# Run the application
root.mainloop()

