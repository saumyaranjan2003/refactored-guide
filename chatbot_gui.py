import flet as ft
from game_chatbot import GameChatbot
import os
import sys

def main(page: ft.Page):
    page.title = "Game Chatbot"
    page.vertical_alignment = ft.MainAxisAlignment.END
    page.fonts = {
        "emoji": "assets/fonts/NotoColorEmoji.ttf"
    }
    page.theme = ft.Theme(font_family = "emoji")

    chatbot = GameChatbot()

    #Scrollable chat area
    chat_column = ft.ListView(expand=True, spacing=10, auto_scroll=True)

    #Text for initial talk
    chat_header = """ 🎮 GAME CHATBOT - Your Interactive Gaming Companion 🎮 
    Welcome! I can help you with:
    • Game recommendations based on your preferences
    • Information about specific games
    • Gaming tips and interesting facts
    • Reviews and ratings
    • General gaming conversations"""

    #Text fo Help section
    chat_help = """  ❓ HELP - Available Commands and Examples:
    🎮 Example Questions You Can Ask:
    • 'Recommend me some action games'
    • 'What are good games for PlayStation?'
    • 'Tell me about The Witcher 3'
    • 'I want puzzle games for PC'
    • 'Give me a gaming tip'
    • 'Share an interesting gaming fact'
    • 'What's a good short game?'
    • 'Review Cyberpunk 2077'
    • 'Suggest indie games'
    • 'What games can I play on Switch?'
    \n 🎮 Supported Genres:
    Action, Adventure, Strategy, Puzzle, Racing, Indie
    \n 🎮 Supported Platforms:
    PC, PlayStation, Xbox, Nintendo Switch, Mobile"""

    #Function to change theme mode
    def change_theme_mode(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        page.update()

    theme_button = ft.Switch(tooltip = "Theme Mode", on_change = change_theme_mode, value = False, adaptive = True)

    #Function to handle user message
    def send_message(e):
        user_msg = chat_textfield.value.strip()
        if user_msg == "":
            return

        # Add user message (Right aligned)
        chat_column.controls.append(
            ft.Row(
                [
                    ft.Container(
                        content=ft.Text(user_msg, color=ft.Colors.WHITE),
                        bgcolor=ft.Colors.BLUE_400,
                        padding=10,
                        border_radius=20,
                    )
                ],
                alignment=ft.MainAxisAlignment.END,
            )
        )

        chat_textfield.value = ""
        page.update()

        # Simulate bot reply
        page.update()
        bot_reply(user_msg)

    #Function to handle bot message
    def bot_reply(user_msg, custom_msg = False, color = ft.Colors.ORANGE_300):
        # (For now a simple dummy response)
        response = chatbot.generate_response(user_msg) if custom_msg is False else user_msg
        chat_column.controls.append(
            ft.Row(
                [
                    ft.Container(
                        content=ft.Text(response, color = ft.Colors.BLACK),
                        bgcolor= color,
                        padding=10,
                        border_radius=20,
                    )
                ],
                alignment=ft.MainAxisAlignment.START,
            )
        )
        page.update()

    #Function to clean the chat
    def clean_chat(e):
        chat_column.controls.clear()
        page.update()

    bot_reply(chat_header, custom_msg = True)

    #Page appbar
    page.appbar = ft.AppBar(
        title = ft.Text("Game Chatbot", weight = "Bold"),
        center_title = True,
        bgcolor = ft.Colors.SURFACE_CONTAINER_HIGHEST,
        actions = [
            #ft.IconButton(icon = ft.Icons.LIGHTBULB, tooltip = "Demo"),
            ft.IconButton(icon = ft.Icons.HELP, tooltip = "Help", on_click =lambda e:bot_reply(chat_help, custom_msg = True, color = ft.Colors.CYAN)),
            theme_button,
            ft.IconButton(icon = ft.Icons.CLEANING_SERVICES, tooltip = "Clear Screen", on_click = clean_chat)
        ]
    )

    #Textfield for accepting user input
    chat_textfield = ft.TextField(hint_text = "Let's start chatting...", expand = True, autofocus = True, border_radius = 20,
    on_submit = lambda e:send_message(None))

    # Bottom input bar
    input_bar = ft.Row(
        [
            chat_textfield,
            ft.IconButton(icon=ft.Icons.SEND, on_click=send_message, tooltip = "Send"),
        ]
    )

    page.add(ft.Column([
        chat_column,
        input_bar
    ],
    expand = True))

ft.app(target = main, assets_dir = "assets")