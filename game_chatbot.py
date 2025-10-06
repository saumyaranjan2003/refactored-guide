import random
import re
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json

class GameChatbot:
    """
    A comprehensive game chatbot that can discuss games, provide recommendations,
    answer gaming questions, and engage in conversations about video games.
    """
    
    def __init__(self):
        self.user_preferences = {
            'favorite_genres': [],
            'preferred_platforms': [],
            'completed_games': [],
            'wishlist': [],
            'playtime_preference': 'medium'  # short, medium, long
        }
        self.conversation_history = []
        self.current_context = None
        self.initialize_game_database()
        
    def initialize_game_database(self):
        """Initialize the comprehensive game database"""
        self.games_db = {
            'action': [
                {
                    'name': 'The Witcher 3: Wild Hunt',
                    'platform': ['PC', 'PlayStation', 'Xbox', 'Switch'],
                    'rating': 9.3,
                    'year': 2015,
                    'playtime': 'long',
                    'description': 'Open-world RPG with rich storytelling and complex characters',
                    'features': ['open-world', 'story-rich', 'character-customization']
                },
                {
                    'name': 'Red Dead Redemption 2',
                    'platform': ['PC', 'PlayStation', 'Xbox'],
                    'rating': 9.7,
                    'year': 2018,
                    'playtime': 'long',
                    'description': 'Immersive western adventure with stunning details',
                    'features': ['open-world', 'story-rich', 'realistic']
                },
                {
                    'name': 'Cyberpunk 2077',
                    'platform': ['PC', 'PlayStation', 'Xbox'],
                    'rating': 7.8,
                    'year': 2020,
                    'playtime': 'long',
                    'description': 'Futuristic RPG in a dystopian megacity',
                    'features': ['open-world', 'cyberpunk', 'character-customization']
                }
            ],
            'adventure': [
                {
                    'name': 'The Legend of Zelda: Breath of the Wild',
                    'platform': ['Switch', 'Wii U'],
                    'rating': 9.7,
                    'year': 2017,
                    'playtime': 'long',
                    'description': 'Revolutionary open-world adventure with physics-based gameplay',
                    'features': ['open-world', 'exploration', 'puzzle-solving']
                },
                {
                    'name': 'Uncharted 4: A Thief\'s End',
                    'platform': ['PlayStation'],
                    'rating': 9.0,
                    'year': 2016,
                    'playtime': 'medium',
                    'description': 'Cinematic action-adventure with treasure hunting',
                    'features': ['story-rich', 'cinematic', 'action']
                }
            ],
            'strategy': [
                {
                    'name': 'Civilization VI',
                    'platform': ['PC', 'PlayStation', 'Xbox', 'Switch', 'Mobile'],
                    'rating': 8.5,
                    'year': 2016,
                    'playtime': 'long',
                    'description': 'Turn-based strategy game about building civilizations',
                    'features': ['turn-based', 'empire-building', 'multiplayer']
                },
                {
                    'name': 'Total War: Warhammer III',
                    'platform': ['PC'],
                    'rating': 8.2,
                    'year': 2022,
                    'playtime': 'long',
                    'description': 'Epic fantasy strategy with massive battles',
                    'features': ['real-time-strategy', 'fantasy', 'large-scale-battles']
                }
            ],
            'puzzle': [
                {
                    'name': 'Portal 2',
                    'platform': ['PC', 'PlayStation', 'Xbox'],
                    'rating': 9.5,
                    'year': 2011,
                    'playtime': 'short',
                    'description': 'Mind-bending puzzle game with clever mechanics',
                    'features': ['puzzle-solving', 'physics-based', 'co-op']
                },
                {
                    'name': 'The Witness',
                    'platform': ['PC', 'PlayStation', 'Xbox', 'Mobile'],
                    'rating': 8.4,
                    'year': 2016,
                    'playtime': 'medium',
                    'description': 'Beautiful puzzle island with interconnected challenges',
                    'features': ['puzzle-solving', 'exploration', 'philosophical']
                }
            ],
            'racing': [
                {
                    'name': 'Forza Horizon 5',
                    'platform': ['PC', 'Xbox'],
                    'rating': 9.1,
                    'year': 2021,
                    'playtime': 'medium',
                    'description': 'Open-world racing in beautiful Mexico',
                    'features': ['open-world', 'racing', 'multiplayer']
                },
                {
                    'name': 'Gran Turismo 7',
                    'platform': ['PlayStation'],
                    'rating': 8.7,
                    'year': 2022,
                    'playtime': 'long',
                    'description': 'Realistic racing simulator with extensive car collection',
                    'features': ['simulation', 'racing', 'car-collection']
                }
            ],
            'indie': [
                {
                    'name': 'Hades',
                    'platform': ['PC', 'PlayStation', 'Xbox', 'Switch'],
                    'rating': 9.0,
                    'year': 2020,
                    'playtime': 'medium',
                    'description': 'Roguelike action game with excellent storytelling',
                    'features': ['roguelike', 'story-rich', 'fast-paced']
                },
                {
                    'name': 'Celeste',
                    'platform': ['PC', 'PlayStation', 'Xbox', 'Switch'],
                    'rating': 9.4,
                    'year': 2018,
                    'playtime': 'short',
                    'description': 'Challenging platformer with emotional depth',
                    'features': ['platformer', 'challenging', 'emotional-story']
                }
            ]
        }
        
        # Gaming tips and facts
        self.gaming_tips = [
            "Always save your game progress frequently to avoid losing hours of gameplay!",
            "Take regular breaks while gaming to prevent eye strain and maintain focus.",
            "Adjust your display settings and brightness for optimal gaming experience.",
            "Keep your gaming setup ergonomic to prevent strain during long sessions.",
            "Don't rush through games - take time to explore and enjoy the experience.",
            "Join gaming communities to find players with similar interests.",
            "Stay updated with game patches and updates for the best experience.",
            "Try different difficulty levels to find what's most enjoyable for you.",
            "Back up your save files regularly, especially for important progress.",
            "Consider upgrading your hardware gradually based on your gaming needs."
        ]
        
        # Gaming facts
        self.gaming_facts = [
            "The video game industry is now worth over $180 billion globally!",
            "The average gamer is 34 years old, and 41% of gamers are women.",
            "Super Mario Bros. was the best-selling game for over 20 years.",
            "The most expensive game ever developed cost over $500 million to make.",
            "Esports tournaments now have prize pools exceeding $40 million.",
            "The first video game was created in 1958 and was called 'Tennis for Two'.",
            "Minecraft is the best-selling video game of all time with over 300 million copies.",
            "The longest gaming session ever recorded lasted over 138 hours!",
            "Japan produces about 60% of the world's video games.",
            "Gaming can improve hand-eye coordination, problem-solving, and reaction times."
        ]
        
    def detect_intent(self, user_input: str) -> str:
        """Detect user intent from their input"""
        user_input = user_input.lower()
        
        # Recommendation patterns
        if any(word in user_input for word in ['recommend', 'suggestion', 'should i play', 'what game', 'good games']):
            return 'recommendation'
            
        # Game info patterns
        elif any(word in user_input for word in ['tell me about', 'what is', 'information about', 'details']):
            return 'game_info'
            
        # Platform/genre preference patterns
        elif any(word in user_input for word in ['platform', 'console', 'pc', 'playstation', 'xbox', 'switch']):
            return 'platform_preference'
            
        # Genre patterns
        elif any(word in user_input for word in ['action', 'adventure', 'strategy', 'puzzle', 'racing', 'indie', 'genre']):
            return 'genre_preference'
            
        # Tips and advice patterns
        elif any(word in user_input for word in ['tip', 'advice', 'help', 'how to', 'guide']):
            return 'tips'
            
        # Facts patterns
        elif any(word in user_input for word in ['fact', 'interesting', 'did you know', 'trivia']):
            return 'facts'
            
        # Reviews patterns
        elif any(word in user_input for word in ['review', 'opinion', 'rating', 'worth playing']):
            return 'review'
            
        # Greeting patterns
        elif any(word in user_input for word in ['hello', 'hi', 'hey', 'greetings']):
            return 'greeting'
            
        # Goodbye patterns
        elif any(word in user_input for word in ['bye', 'goodbye', 'exit', 'quit']):
            return 'goodbye'
            
        else:
            return 'general_chat'
    
    def extract_game_preferences(self, user_input: str) -> Dict:
        """Extract game preferences from user input"""
        preferences = {}
        user_input = user_input.lower()
        
        # Extract genres
        genres = []
        for genre in self.games_db.keys():
            if genre in user_input:
                genres.append(genre)
        if genres:
            preferences['genres'] = genres
            
        # Extract platforms
        platforms = []
        platform_keywords = {
            'pc': 'PC', 'computer': 'PC',
            'playstation': 'PlayStation', 'ps4': 'PlayStation', 'ps5': 'PlayStation',
            'xbox': 'Xbox', 'switch': 'Switch', 'nintendo': 'Switch'
        }
        for keyword, platform in platform_keywords.items():
            if keyword in user_input:
                platforms.append(platform)
        if platforms:
            preferences['platforms'] = platforms
            
        # Extract playtime preference
        if any(word in user_input for word in ['short', 'quick', 'brief']):
            preferences['playtime'] = 'short'
        elif any(word in user_input for word in ['long', 'lengthy', 'extended']):
            preferences['playtime'] = 'long'
        elif any(word in user_input for word in ['medium', 'moderate']):
            preferences['playtime'] = 'medium'
            
        return preferences
    
    def get_game_recommendations(self, preferences: Dict = None, count: int = 3) -> List[Dict]:
        """Get game recommendations based on user preferences"""
        if not preferences:
            preferences = {}
            
        recommended_games = []
        
        # Get all games from database
        all_games = []
        for genre, games in self.games_db.items():
            for game in games:
                game['genre'] = genre
                all_games.append(game)
        
        # Filter based on preferences
        filtered_games = all_games
        
        if 'genres' in preferences:
            filtered_games = [game for game in filtered_games if game['genre'] in preferences['genres']]
            
        if 'platforms' in preferences:
            filtered_games = [game for game in filtered_games 
                            if any(platform in game['platform'] for platform in preferences['platforms'])]
            
        if 'playtime' in preferences:
            filtered_games = [game for game in filtered_games if game['playtime'] == preferences['playtime']]
        
        # Sort by rating and select top recommendations
        filtered_games.sort(key=lambda x: x['rating'], reverse=True)
        
        return filtered_games[:count] if filtered_games else random.sample(all_games, min(count, len(all_games)))
    
    def find_game_by_name(self, game_name: str) -> Optional[Dict]:
        """Find a specific game by name"""
        game_name = game_name.lower()
        for genre, games in self.games_db.items():
            for game in games:
                if game_name in game['name'].lower():
                    game_copy = game.copy()
                    game_copy['genre'] = genre
                    return game_copy
        return None
    
    def generate_response(self, user_input: str) -> str:
        """Generate appropriate response based on user input"""
        intent = self.detect_intent(user_input)
        self.conversation_history.append(('user', user_input))
        
        if intent == 'greeting':
            response = self.handle_greeting()
            
        elif intent == 'recommendation':
            preferences = self.extract_game_preferences(user_input)
            response = self.handle_recommendation(preferences)
            
        elif intent == 'game_info':
            response = self.handle_game_info(user_input)
            
        elif intent == 'platform_preference':
            preferences = self.extract_game_preferences(user_input)
            response = self.handle_platform_preference(preferences)
            
        elif intent == 'genre_preference':
            preferences = self.extract_game_preferences(user_input)
            response = self.handle_genre_preference(preferences)
            
        elif intent == 'tips':
            response = self.handle_tips()
            
        elif intent == 'facts':
            response = self.handle_facts()
            
        elif intent == 'review':
            response = self.handle_review(user_input)
            
        elif intent == 'goodbye':
            response = self.handle_goodbye()
            
        else:
            response = self.handle_general_chat(user_input)
        
        self.conversation_history.append(('bot', response))
        return response
    
    def handle_greeting(self) -> str:
        """Handle greeting messages"""
        greetings = [
            "Hello! I'm your friendly game chatbot! 🎮 I can help you discover new games, get recommendations, share gaming tips, and chat about all things gaming!",
            "Hey there, fellow gamer! 🎮 Ready to explore the amazing world of video games? I can recommend games, share facts, and help you find your next gaming adventure!",
            "Greetings, gamer! 🎮 I'm here to help you with game recommendations, reviews, tips, and anything gaming-related. What are you interested in playing today?"
        ]
        return random.choice(greetings)
    
    def handle_recommendation(self, preferences: Dict) -> str:
        """Handle game recommendation requests"""
        recommendations = self.get_game_recommendations(preferences)
        
        if not recommendations:
            return "I couldn't find games matching your exact preferences, but let me suggest some popular games across different genres!"
        
        response = "🎮 Game Recommendations for You:\n\n"
        
        for i, game in enumerate(recommendations, 1):
            response += f"{i}. {game['name']} ({game['year']})\n"
            response += f"   📱 Platforms: {', '.join(game['platform'])}\n"
            response += f"   ⭐ Rating: {game['rating']}/10\n"
            response += f"   🎭 Genre: {game['genre'].title()}\n"
            response += f"   ⏱️ Playtime: {game['playtime'].title()}\n"
            response += f"   📝 {game['description']}\n\n"
        
        response += "Would you like more details about any of these games or different recommendations? 🎮"
        return response
    
    def handle_game_info(self, user_input: str) -> str:
        """Handle requests for specific game information"""
        # Try to extract game name from the input
        words = user_input.split()
        potential_game_names = []
        
        # Look for game names in the input
        for genre, games in self.games_db.items():
            for game in games:
                game_words = game['name'].lower().split()
                if any(word in user_input.lower() for word in game_words):
                    potential_game_names.append((game, genre))
        
        if potential_game_names:
            game, genre = potential_game_names[0]  # Take the first match
            response = f"🎮 {game['name']} ({game['year']})\n\n"
            response += f"📱 Platforms: {', '.join(game['platform'])}\n"
            response += f"⭐ Rating: {game['rating']}/10\n"
            response += f"🎭 Genre: {genre.title()}\n"
            response += f"⏱️ Playtime: {game['playtime'].title()}\n"
            response += f"🏷️ Features: {', '.join(game['features'])}\n\n"
            response += f"📝 Description: {game['description']}\n\n"
            response += "Would you like recommendations for similar games? 🎮"
            return response
        else:
            return "I'd love to help you learn about a specific game! Could you tell me which game you're interested in? I have information about many popular titles across different genres! 🎮"
    
    def handle_platform_preference(self, preferences: Dict) -> str:
        """Handle platform-specific requests"""
        if 'platforms' in preferences:
            platform = preferences['platforms'][0]
            games = self.get_game_recommendations({'platforms': [platform]}, count=5)
            
            response = f"🎮 Great {platform} Games:\n\n"
            for i, game in enumerate(games, 1):
                response += f"{i}. {game['name']} - {game['description'][:50]}... (Rating: {game['rating']}/10)\n"
            
            response += f"\n{platform} is an excellent gaming platform! Would you like detailed info about any of these games? 🎮"
            return response
        else:
            return "Which gaming platform are you interested in? I can recommend games for PC, PlayStation, Xbox, Nintendo Switch, and mobile! 🎮"
    
    def handle_genre_preference(self, preferences: Dict) -> str:
        """Handle genre-specific requests"""
        if 'genres' in preferences:
            genre = preferences['genres'][0]
            if genre in self.games_db:
                games = self.games_db[genre]
                response = f"🎮 {genre.title()} Games You'll Love:\n\n"
                
                for i, game in enumerate(games, 1):
                    response += f"{i}. {game['name']} ({game['year']})\n"
                    response += f"   ⭐ Rating: {game['rating']}/10\n"
                    response += f"   📝 {game['description']}\n\n"
                
                response += f"{genre.title()} games offer amazing experiences! Want to know more about any specific game? 🎮"
                return response
        
        available_genres = list(self.games_db.keys())
        return f"I can help you explore different game genres! Available genres: {', '.join(g.title() for g in available_genres)}. Which one interests you? 🎮"
    
    def handle_tips(self) -> str:
        """Handle gaming tips requests"""
        tip = random.choice(self.gaming_tips)
        response = f"💡 Gaming Tip:\n{tip}\n\n"
        response += "Would you like another tip or need advice about a specific gaming topic? 🎮"
        return response
    
    def handle_facts(self) -> str:
        """Handle gaming facts requests"""
        fact = random.choice(self.gaming_facts)
        response = f"🤓 Gaming Fact:\n{fact}\n\n"
        response += "Want to hear another interesting gaming fact? 🎮"
        return response
    
    def handle_review(self, user_input: str) -> str:
        """Handle game review requests"""
        game = self.find_game_by_name(user_input)
        if game:
            response = f"🎮 {game['name']} Review:\n\n"
            response += f"⭐ Overall Rating: {game['rating']}/10\n\n"
            
            if game['rating'] >= 9.0:
                response += "🏆 Verdict: Masterpiece! This game is absolutely phenomenal and a must-play for any gamer.\n"
            elif game['rating'] >= 8.0:
                response += "👍 Verdict: Excellent game! Highly recommended with great gameplay and features.\n"
            elif game['rating'] >= 7.0:
                response += "✅ Verdict: Good game worth playing, with some minor flaws but overall enjoyable.\n"
            else:
                response += "⚠️ Verdict: Average game. Might be worth trying if you're interested in the genre.\n"
            
            response += f"\n📝 Description: {game['description']}\n"
            response += f"🎭 Genre: {game['genre'].title()}\n"
            response += f"📱 Platforms: {', '.join(game['platform'])}\n\n"
            response += "Would you like recommendations for similar games? 🎮"
            return response
        else:
            return "Which game would you like me to review? I can share ratings, opinions, and detailed information about many popular games! 🎮"
    
    def handle_goodbye(self) -> str:
        """Handle goodbye messages"""
        goodbyes = [
            "Thanks for chatting about games with me! Happy gaming, and may all your gaming sessions be epic! 🎮✨",
            "Goodbye, fellow gamer! Keep exploring new worlds and having amazing adventures! See you next time! 🎮👋",
            "It was great talking games with you! Don't forget to take breaks and enjoy your gaming journey! 🎮🌟"
        ]
        return random.choice(goodbyes)
    
    def handle_general_chat(self, user_input: str) -> str:
        """Handle general gaming conversation"""
        general_responses = [
            "That's interesting! Gaming has so many fascinating aspects. What specific part of gaming would you like to explore?",
            "I love talking about games! Is there a particular game, genre, or gaming topic you'd like to discuss?",
            "Gaming is such an amazing world! Would you like game recommendations, tips, facts, or just want to chat about gaming?",
            "Tell me more about your gaming interests! I can help with recommendations, reviews, or just have a fun gaming conversation!",
            "That's cool! I'm here to help with all things gaming. What would you like to know or discuss about video games?"
        ]
        return random.choice(general_responses) + " 🎮"
    
    def get_conversation_summary(self) -> str:
        """Get a summary of the current conversation"""
        if not self.conversation_history:
            return "No conversation yet!"
        
        total_messages = len(self.conversation_history)
        user_messages = len([msg for msg in self.conversation_history if msg[0] == 'user'])
        bot_messages = len([msg for msg in self.conversation_history if msg[0] == 'bot'])
        
        return f"Conversation Summary: {total_messages} total messages ({user_messages} from user, {bot_messages} from bot)"
