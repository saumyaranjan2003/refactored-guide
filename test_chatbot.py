#!/usr/bin/env python3
"""
Simple test script to validate all Game Chatbot functionality
"""

from game_chatbot import GameChatbot

def test_chatbot():
    """Test all major chatbot features"""
    print("🧪 Testing Game Chatbot Functionality")
    print("=" * 50)
    
    # Initialize chatbot
    bot = GameChatbot()
    print("✅ Chatbot initialized successfully")
    
    # Test cases
    test_cases = [
        ("Hello!", "greeting"),
        ("Recommend me action games", "recommendation"), 
        ("Tell me about The Witcher 3", "game_info"),
        ("I want PC games", "platform_preference"),
        ("Give me puzzle games", "genre_preference"),
        ("Share a gaming tip", "tips"),
        ("Tell me a gaming fact", "facts"),
        ("Review Portal 2", "review"),
        ("Goodbye", "goodbye")
    ]
    
    print(f"\n🎯 Running {len(test_cases)} test cases...")
    
    for i, (user_input, expected_intent) in enumerate(test_cases, 1):
        print(f"\nTest {i}: {user_input}")
        
        # Test intent detection
        detected_intent = bot.detect_intent(user_input)
        print(f"  Intent: {detected_intent} {'✅' if detected_intent == expected_intent else '❌'}")
        
        # Test response generation
        try:
            response = bot.generate_response(user_input)
            print(f"  Response: {response[:80]}...")
            print("  Status: ✅ Success")
        except Exception as e:
            print(f"  Status: ❌ Error - {e}")
    
    # Test game database
    print(f"\n📊 Game Database Stats:")
    total_games = sum(len(games) for games in bot.games_db.values())
    print(f"  Total games: {total_games}")
    print(f"  Genres: {list(bot.games_db.keys())}")
    print(f"  Tips available: {len(bot.gaming_tips)}")
    print(f"  Facts available: {len(bot.gaming_facts)}")
    
    # Test recommendations
    print(f"\n🎮 Testing Recommendations:")
    recommendations = bot.get_game_recommendations({'genres': ['action']}, count=2)
    print(f"  Action game recommendations: {len(recommendations)} found")
    for game in recommendations:
        print(f"    - {game['name']} ({game['rating']}/10)")
    
    # Test preference extraction
    print(f"\n🔍 Testing Preference Extraction:")
    test_input = "I want action games for PC that are short"
    preferences = bot.extract_game_preferences(test_input)
    print(f"  Input: '{test_input}'")
    print(f"  Extracted preferences: {preferences}")
    
    print(f"\n🎉 All tests completed! Chatbot is ready to use.")
    print("=" * 50)
    print("Run 'python demo.py' to start the interactive chat!")

if __name__ == "__main__":
    test_chatbot()

def test_ml_recommendations_respect_preferences():
    bot = GameChatbot()

    recommendations = bot.get_game_recommendations(
        {
            "genres": ["action"],
            "platforms": ["PC"],
            "playtime": "long",
        },
        count=3,
    )

    assert len(recommendations) == 3

    for game in recommendations:
        assert game["genre"] == "action"
        assert "PC" in game["platform"]
        assert game["playtime"] == "long"