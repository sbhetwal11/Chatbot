from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class Command(BaseCommand):
    help = "Runs the terminal chatbot"

    def handle(self, *args, **kwargs):
        chatbot = ChatBot("TerminalBot")
        trainer = ChatterBotCorpusTrainer(chatbot)
        trainer.train("chatterbot.corpus.english")

        print("Hi, I am ready for chatting. Type 'quit' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'quit':
                break
            response = chatbot.get_response(user_input)
            print("Bot:", response)
