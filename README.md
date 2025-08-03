# Terminal Chatbot using Django and ChatterBot

This project implements a simple terminal-based chatbot using Django and ChatterBot.  
The chatbot is trained using the ChatterBot corpus and responds to basic conversations through the command-line interface.

Django management command has been used to run the chatbot, which keeps the implementation clean and easy to use.

---

##  Features

- Terminal-based interaction with the chatbot  
- Learns from conversations using ChatterBot Corpus  
- Uses Django’s custom command to run chatbot logic  
- Clean and minimal setup – no web UI or forms  

---

##  Requirements

- Python 3.11 (tested on both)  
- Django (v3.2 or later recommended)  
- ChatterBot (installed from GitHub)  
- `spacy` and `pyyaml` for language model and corpus training  

---

##  Installation

1. Create a virtual environment:
```bash
python -m venv chatbot_env
```

2. Activate the environment:

**Windows**:
```bash
chatbot_env\Scripts\activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Download the SpaCy language model:
```bash
python -m spacy download en_core_web_sm
```

---

## How to Train & Run the Chatbot

Once all dependencies are installed:

```bash
python manage.py terminal_bot
```

The chatbot will start in the terminal and you can begin chatting. Type `quit` to exit.


---

## Author

**Sagar Bhetwal**  
University of the Cumberlands – Advanced Artificial Intelligence  
Instructor: Dr. Primus Vekuh  
August 03 2025


