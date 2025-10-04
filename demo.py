#!/usr/bin/env python3
"""
Game Chatbot Demo
A comprehensive interactive chatbot for game-related conversations, recommendations, and information.
"""

from game_chatbot import GameChatbot
import os
import sys

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    """Print the chatbot header"""
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
    """Print colored text to terminal"""
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
    """Show help information"""
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
    """Format bot response with better visual presentation"""
    # Add some spacing and formatting
    formatted = response.replace("**", "")  # Remove markdown bold
    formatted = formatted.replace("🎮", "🎮 ")  # Add space after game emoji
    return formatted

def main():
    """Main function to run the game chatbot"""
    try:
        # Initialize chatbot
        chatbot = GameChatbot()
        
        # Clear screen and show header
        clear_screen()
        print_header()
        
        print_colored_text("Hello! I'm your Game Chatbot! 🎮", "green")
        print("Type 'help' for commands or just start chatting about games!")
        print()
        
        # Main conversation loop
        while True:
            try:
                # Get user input
                print_colored_text("You: ", "yellow")
                user_input = input().strip()
                
                # Handle empty input
                if not user_input:
                    print_colored_text("Please say something! 🎮", "yellow")
                    continue
                
                # Handle special commands
                if user_input.lower() in ['quit', 'exit', 'bye', 'goodbye']:
                    response = chatbot.generate_response(user_input)
                    print_colored_text(f"\nBot: {format_bot_response(response)}", "purple")
                    break
                
                elif user_input.lower() == 'help':
                    show_help()
                    continue
                
                elif user_input.lower() == 'clear':
                    clear_screen()
                    print_header()
                    print_colored_text("Screen cleared! Continue our gaming conversation! 🎮", "green")
                    continue
                
                # Generate and display bot response
                response = chatbot.generate_response(user_input)
                print_colored_text(f"\nBot: {format_bot_response(response)}", "purple")
                print()  # Add spacing
                
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
    """Run an interactive demo with sample conversations"""
    print_colored_text("🎮 INTERACTIVE DEMO MODE", "cyan")
    print_colored_text("=" * 40, "blue")
    
    chatbot = GameChatbot()
    
    # Sample conversations
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
        
        # Pause for readability
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
