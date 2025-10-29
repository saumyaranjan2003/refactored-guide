#!/usr/bin/env python3
"""
Game Chatbot Demo
A comprehensive interactive chatbot for game-related conversations, recommendations, and information.
"""

from game_chatbot import GameChatbot
import os
import sys
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something now (You have up to 2 minutes):")
        try:
            audio = recognizer.listen(source, timeout=120, phrase_time_limit=120)
        except sr.WaitTimeoutError:
            return None
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        print("Speech recognition service error. Please check connection.")
        return None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("=" * 80)
    print("🎮 GAME CHATBOT - Your Interactive Gaming Companion 🎮")
    print("=" * 80)
    print("Welcome! I can help you with:")
    print("• Game recommendations based on your preferences")
    print("• Information about specific games")
    print("• Gaming tips and interesting facts")
    print("• Reviews and ratings")
    print("• General gaming conversations")
    print()
    print("Commands:")
    print("• 'help' - Show available commands")
    print("• 'clear' - Clear the screen")
    print("• 'quit' or 'exit' - End the conversation")
    print("=" * 80)
    print()

def print_colored_text(text: str, color_code: str = ""):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'bold': '\033[1m',
        'end': '\033[0m'
    }
    if color_code in colors:
        print(f"{colors[color_code]}{text}{colors['end']}")
    else:
        print(text)

def show_help():
    print_colored_text("\n🆘 HELP - Available Commands and Examples:", "cyan")
    print_colored_text("=" * 60, "blue")
    print("\n📋 Commands:")
    print("• help - Show this help message")
    print("• clear - Clear the screen")
    print("• quit/exit - End the conversation")
    print("\n🎮 Example Questions You Can Ask:")
    print("• 'Recommend me some action games'")
    print("• 'What are good games for PlayStation?'")
    print("• 'Tell me about The Witcher 3'")
    print("• 'I want puzzle games for PC'")
    print("• 'Give me a gaming tip'")
    print("• 'Share an interesting gaming fact'")
    print("• 'What's a good short game?'")
    print("• 'Review Cyberpunk 2077'")
    print("• 'Suggest indie games'")
    print("• 'What games can I play on Switch?'")
    print("\n🎯 Supported Genres:")
    print("Action, Adventure, Strategy, Puzzle, Racing, Indie")
    print("\n📱 Supported Platforms:")
    print("PC, PlayStation, Xbox, Nintendo Switch, Mobile")
    print_colored_text("=" * 60, "blue")

def format_bot_response(response: str) -> str:
    formatted = response.replace("**", "")
    formatted = formatted.replace("🎮", "🎮 ")
    return formatted

def main():
    try:
        chatbot = GameChatbot()
        clear_screen()
        print_header()
        print_colored_text("Hello! I'm your Game Chatbot! 🎮", "green")
        print("Type 'help' for commands or just start chatting about games!")
        print()

        while True:
            try:
                user_input = get_voice_input()
                if user_input is None:
                    print_colored_text("You (type message): ", "yellow")
                    user_input = input().strip()

                if not user_input:
                    print_colored_text("Please say or type something! 🎮", "yellow")
                    continue

                if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                    response = chatbot.generate_response(user_input)
                    print_colored_text(f"\nBot: {format_bot_response(response)}", "purple")
                    speak(response)
                    break

                elif user_input.lower() == 'help':
                    show_help()
                    continue

                elif user_input.lower() == 'clear':
                    clear_screen()
                    print_header()
                    print_colored_text("Screen cleared! Continue our gaming conversation! 🎮", "green")
                    continue

                response = chatbot.generate_response(user_input)
                print_colored_text(f"\nBot: {format_bot_response(response)}", "purple")
                print()
                speak(response)

            except KeyboardInterrupt:
                print_colored_text("\n\nChat interrupted. Thanks for using Game Chatbot! 🎮", "yellow")
                break

            except Exception as e:
                print_colored_text(f"\nSorry, I encountered an error: {str(e)}", "red")
                print_colored_text("Let's continue our conversation! 🎮", "green")
                continue

    except Exception as e:
        print_colored_text(f"Failed to start Game Chatbot: {str(e)}", "red")
        sys.exit(1)

def run_interactive_demo():
    print_colored_text("🎮 INTERACTIVE DEMO MODE", "cyan")
    print_colored_text("=" * 40, "blue")
    chatbot = GameChatbot()
    demo_inputs = [
        "Hello!",
        "Recommend me some action games for PC",
        "Tell me about The Witcher 3",
        "I want short puzzle games",
        "Give me a gaming tip",
        "Share a gaming fact"
    ]
    print("This demo will show how the chatbot responds to various queries:")
    print()
    for i, user_input in enumerate(demo_inputs, 1):
        print_colored_text(f"Demo {i}/6:", "yellow")
        print_colored_text(f"User: {user_input}", "green")
        response = chatbot.generate_response(user_input)
        print_colored_text(f"Bot: {format_bot_response(response)[:200]}...", "purple")
        print("-" * 60)
        input("Press Enter to continue...")
        print()
    print_colored_text("Demo completed! Ready to chat for real? 🎮", "cyan")

if __name__ == "__main__":
    print("🎮 Game Chatbot Launcher 🎮")
    print("1. Start Interactive Chat")
    print("2. Run Demo")
    print("3. Exit")
    try:
        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            main()
        elif choice == "2":
            run_interactive_demo()
            print("\nWould you like to start the interactive chat now? (y/n)")
            if input().lower().startswith('y'):
                main()
        elif choice == "3":
            print_colored_text("Thanks for checking out Game Chatbot! 🎮", "green")
        else:
            print_colored_text("Invalid choice. Starting interactive chat...", "yellow")
            main()
    except KeyboardInterrupt:
        print_colored_text("\nGoodbye! Happy gaming! 🎮", "green")
