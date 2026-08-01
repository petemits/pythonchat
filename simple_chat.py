"""
ULTRA SIMPLE ENDLESS CONVERSATION
One file - Just run it!
"""

import re
import random
from datetime import datetime

# ==================== SIMPLE CONVERSATION ENGINE ====================
class SimpleChat:
    def __init__(self):
        # Sample topics built-in (no file loading needed!)
        self.topics = {
            "artificial intelligence": [
                "AI is transforming our world.",
                "Machine learning helps computers learn from data.",
                "ChatGPT can write like humans.",
                "Self-driving cars use AI technology.",
                "AI helps doctors diagnose diseases."
            ],
            "climate change": [
                "Climate change affects weather patterns worldwide.",
                "Rising sea levels threaten coastal cities.",
                "Renewable energy like solar power helps fight climate change.",
                "Electric cars reduce carbon emissions.",
                "Planting trees helps absorb CO2 from the atmosphere."
            ],
            "space exploration": [
                "NASA plans to send humans to Mars.",
                "Private companies like SpaceX launch rockets.",
                "The International Space Station orbits Earth.",
                "Telescopes discover new planets around distant stars.",
                "Astronauts conduct experiments in zero gravity."
            ],
            "technology": [
                "Smartphones connect people worldwide.",
                "5G networks provide faster internet speeds.",
                "Virtual reality creates immersive experiences.",
                "Robots automate factory production.",
                "3D printing creates objects from digital designs."
            ],
            "health": [
                "Regular exercise improves physical and mental health.",
                "Vaccines protect against infectious diseases.",
                "Meditation reduces stress and anxiety.",
                "A balanced diet provides essential nutrients.",
                "Sleep is important for memory and learning."
            ],
            "education": [
                "Online learning makes education accessible everywhere.",
                "Interactive tools make learning more engaging.",
                "Critical thinking skills are essential for problem solving.",
                "Reading expands knowledge and vocabulary.",
                "Hands-on experience complements theoretical learning."
            ]
        }
        
        # Create simple agents
        self.agent1 = {"name": "Alex", "personality": "analytical"}
        self.agent2 = {"name": "Sam", "personality": "curious"}
        
        self.current_topic = "artificial intelligence"
        self.history = []
    
    def start_chat(self):
        """Start endless conversation"""
        print("\n" + "="*50)
        print("🤖 SIMPLE ENDLESS CHAT")
        print("="*50)
        print("\nType commands during conversation:")
        print("  'topic [name]' - Change topic")
        print("  'new' - Random new topic")
        print("  'list' - Show all topics")
        print("  'stop' - End conversation")
        print("  'help' - Show commands")
        print("\n" + "="*50)
        
        # Show available topics
        print("\n📚 Available topics:")
        for i, topic in enumerate(self.topics.keys(), 1):
            print(f"  {i}. {topic}")
        
        # Get starting topic
        choice = input("\nEnter topic number or name (or press Enter for AI): ").strip()
        
        if choice:
            if choice.isdigit():
                idx = int(choice) - 1
                topics_list = list(self.topics.keys())
                if 0 <= idx < len(topics_list):
                    self.current_topic = topics_list[idx]
            else:
                # Check if input matches a topic
                for topic in self.topics:
                    if choice.lower() in topic.lower():
                        self.current_topic = topic
                        break
                else:
                    print(f"Topic '{choice}' not found. Using 'artificial intelligence'")
        
        print(f"\n💬 Starting conversation about: {self.current_topic.upper()}")
        print("-" * 50)
        
        # Opening messages
        self._print_message(self.agent1, f"Let's discuss {self.current_topic}. What are your thoughts?")
        self._print_message(self.agent2, f"I find {self.current_topic} fascinating. There's so much to explore!")
        
        # Conversation loop
        turn = 0
        last_speaker = self.agent2
        
        while True:
            turn += 1
            
            # Alternate speakers
            speaker = self.agent1 if last_speaker == self.agent2 else self.agent2
            
            # Get response
            response = self._get_response(speaker, self.current_topic)
            
            # Print response
            self._print_message(speaker, response)
            
            # Update last speaker
            last_speaker = speaker
            
            # Check for user input every 2-3 turns
            if turn % random.randint(2, 3) == 0:
                command = input("\n🎤 You (or press Enter to continue): ").strip().lower()
                
                if command == "stop" or command == "exit" or command == "quit":
                    break
                elif command.startswith("topic "):
                    new_topic = command[6:].strip()
                    self._change_topic(new_topic)
                elif command == "new":
                    self._random_topic()
                elif command == "list":
                    self._list_topics()
                elif command == "help":
                    self._show_help()
                elif command == "current":
                    print(f"\n📌 Current topic: {self.current_topic}")
                elif command:
                    print(f"\n[Noted: {command}]")
            
            # Occasionally change topic naturally (10% chance)
            if random.random() < 0.1 and turn > 5:
                self._natural_topic_change()
    
    def _print_message(self, speaker, message):
        """Print a message with speaker name"""
        print(f"\n{speaker['name']}: {message}")
        self.history.append({"speaker": speaker['name'], "message": message, "topic": self.current_topic})
    
    def _get_response(self, speaker, topic):
        """Generate response based on speaker personality and topic"""
        facts = self.topics.get(topic, ["This is an interesting topic."])
        
        if speaker['personality'] == "analytical":
            analytical_responses = [
                f"Analyzing {topic}: {random.choice(facts)}",
                f"From a logical perspective, {topic} demonstrates important principles.",
                f"The structure of {topic} reveals interesting patterns."
            ]
            return random.choice(analytical_responses)
        
        else:  # curious
            questions = [
                f"What's most surprising about {topic}?",
                f"How does {topic} work in practice?",
                f"Why is {topic} important in today's world?",
                f"What don't most people understand about {topic}?"
            ]
            curious_responses = [
                f"That's interesting! {random.choice(facts)} But I wonder...",
                random.choice(questions),
                f"I'm curious about {topic}. Can you tell me more?"
            ]
            return random.choice(curious_responses)
    
    def _change_topic(self, new_topic):
        """Change to a new topic"""
        # Check if topic exists
        for topic in self.topics:
            if new_topic.lower() in topic.lower() or topic.lower() in new_topic.lower():
                print(f"\n🔄 Topic changed: {self.current_topic} → {topic}")
                self.current_topic = topic
                return
        
        # If not found, show available topics
        print(f"\n❌ Topic '{new_topic}' not found.")
        print("Available topics:")
        for topic in self.topics:
            print(f"  • {topic}")
    
    def _random_topic(self):
        """Change to random topic"""
        old_topic = self.current_topic
        self.current_topic = random.choice(list(self.topics.keys()))
        print(f"\n🎲 Random topic: {self.current_topic}")
    
    def _list_topics(self):
        """List all available topics"""
        print("\n📚 Available topics:")
        for i, topic in enumerate(self.topics.keys(), 1):
            print(f"  {i}. {topic}")
    
    def _show_help(self):
        """Show available commands"""
        print("\n📋 COMMANDS:")
        print("  topic [name] - Change topic")
        print("  new          - Random new topic")
        print("  list         - Show all topics")
        print("  current      - Show current topic")
        print("  stop         - End conversation")
        print("  help         - Show this help")
    
    def _natural_topic_change(self):
        """Change topic naturally"""
        topics_list = list(self.topics.keys())
        if len(topics_list) > 1:
            # Pick a different topic
            new_topic = random.choice([t for t in topics_list if t != self.current_topic])
            print(f"\n[Conversation naturally shifting to: {new_topic}]")
            self.current_topic = new_topic

# ==================== MAIN PROGRAM ====================
def main():
    """Main function - just run this!"""
    print("\n" + "="*60)
    print("🎮 SIMPLE ENDLESS CONVERSATION")
    print("="*60)
    print("\nJust run this file for endless AI conversations!")
    print("No setup, no files needed - everything is built-in!")
    
    # Create and start chat
    chat = SimpleChat()
    
    # Start conversation
    chat.start_chat()
    
    # Show summary
    print("\n" + "="*50)
    print("🎬 CONVERSATION SUMMARY")
    print("="*50)
    print(f"Total exchanges: {len(chat.history)}")
    print(f"Final topic: {chat.current_topic}")
    
    # Save conversation
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"chat_{timestamp}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("Simple Endless Conversation\n")
            f.write(f"Time: {datetime.now()}\n")
            f.write(f"Topic: {chat.current_topic}\n")
            f.write("="*40 + "\n\n")
            for msg in chat.history:
                f.write(f"{msg['speaker']}: {msg['message']}\n\n")
        print(f"💾 Conversation saved to: {filename}")
    except:
        print("⚠️ Could not save conversation (but that's okay!)")
    
    print("\n👋 Thanks for chatting! Run again for more conversations.")

# ==================== RUN IT! ====================
if __name__ == "__main__":
    main()