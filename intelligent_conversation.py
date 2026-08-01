"""
INTELLIGENT DOCUMENT CONVERSATION ENGINE
Reads your document and creates natural, flowing human-like conversations
"""

import re
import random
import os
from collections import defaultdict, Counter
from datetime import datetime

# ==================== INTELLIGENT DOCUMENT PROCESSOR ====================
class DocumentProcessor:
    def __init__(self):
        self.document_text = ""
        self.topics = {}
        self.topic_network = defaultdict(set)
        self.concept_map = defaultdict(list)
        
    def load_document(self, filepath):
        """Load and intelligently process document"""
        print(f"\n📖 Loading document: {filepath}")
        
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                self.document_text = f.read()
            
            if not self.document_text.strip():
                print("❌ Document is empty")
                return False
            
            print(f"📄 Size: {len(self.document_text):,} characters")
            
            # Intelligent processing
            self._extract_intelligent_topics()
            self._build_concept_relationships()
            self._calculate_topic_importance()
            
            print(f"✅ Processed {len(self.topics)} topics with {sum(len(v) for v in self.topic_network.values())} connections")
            return True
            
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def _extract_intelligent_topics(self):
        """Extract topics using multiple intelligent strategies"""
        sentences = self._split_into_meaningful_sentences()
        print(f"📝 Found {len(sentences)} meaningful sentences")
        
        # Strategy 1: Noun phrase extraction
        noun_topics = self._extract_noun_phrases(sentences)
        
        # Strategy 2: Key concept extraction
        key_concepts = self._extract_key_concepts(sentences)
        
        # Strategy 3: Subject extraction
        subjects = self._extract_sentence_subjects(sentences)
        
        # Combine all strategies
        all_candidates = set(list(noun_topics.keys()) + list(key_concepts.keys()) + subjects)
        
        # Create rich topic objects
        for topic in all_candidates:
            if len(topic) < 2 or len(topic) > 50:
                continue
            
            # Find all related sentences
            topic_sentences = []
            for sentence in sentences:
                if self._topic_in_sentence(topic, sentence):
                    topic_sentences.append(sentence)
            
            if topic_sentences:
                # Extract key phrases and facts
                key_phrases = self._extract_key_phrases(topic, topic_sentences)
                related_concepts = self._find_related_concepts(topic, sentences)
                
                self.topics[topic] = {
                    'sentences': topic_sentences[:8],
                    'key_phrases': key_phrases[:5],
                    'related_concepts': related_concepts,
                    'sentence_count': len(topic_sentences),
                    'conversation_history': [],
                    'discussion_depth': 0
                }
    
    def _split_into_meaningful_sentences(self):
        """Split text into meaningful sentences"""
        # Split by sentence endings
        raw_sentences = re.split(r'(?<=[.!?])\s+', self.document_text)
        
        meaningful = []
        for sentence in raw_sentences:
            sentence = sentence.strip()
            if len(sentence) > 15 and len(sentence.split()) > 3:
                meaningful.append(sentence)
        
        return meaningful
    
    def _extract_noun_phrases(self, sentences):
        """Extract noun phrases from sentences"""
        topics = {}
        
        for sentence in sentences:
            # Find noun phrases (capitalized or important)
            # Pattern for noun phrases
            patterns = [
                r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\b',  # Multiple capitalized words
                r'\b(the|a|an)?\s*([A-Z][a-z]+\s+[A-Z][a-z]+)\b',  # The [Noun Phrase]
                r'\b([A-Z][a-z]+(?:\s+[a-z]+){1,3})\b',  # Capitalized word followed by lowercase
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, sentence)
                for match in matches:
                    phrase = match if isinstance(match, str) else match[0]
                    clean_phrase = phrase.strip('.,;:!?()[]{}"\'').lower()
                    
                    if 2 <= len(clean_phrase.split()) <= 4:
                        if clean_phrase not in topics:
                            topics[clean_phrase] = []
                        topics[clean_phrase].append(sentence)
        
        return topics
    
    def _extract_key_concepts(self, sentences):
        """Extract key concepts using word frequency and context"""
        # Count word frequency
        all_words = re.findall(r'\b[a-z]{4,}\b', self.document_text.lower())
        common_words = {'that', 'with', 'from', 'this', 'have', 'which', 'about', 
                       'their', 'there', 'could', 'would', 'should', 'other'}
        
        word_freq = Counter(w for w in all_words if w not in common_words)
        
        # Find important concepts
        topics = {}
        important_words = [word for word, freq in word_freq.most_common(50) if freq > 2]
        
        for word in important_words:
            related_sentences = []
            for sentence in sentences:
                if word in sentence.lower():
                    related_sentences.append(sentence)
            
            if related_sentences:
                topics[word] = related_sentences[:10]
        
        return topics
    
    def _extract_sentence_subjects(self, sentences):
        """Extract main subjects from sentences"""
        subjects = set()
        
        for sentence in sentences:
            # Simple subject extraction (first few words before verb)
            words = sentence.split()
            if len(words) > 3:
                # Look for subject patterns
                if ' is ' in sentence.lower() or ' are ' in sentence.lower():
                    # Get text before "is/are"
                    parts = re.split(r'\bis\b|\bare\b', sentence.lower(), maxsplit=1)
                    if len(parts) > 1:
                        subject = parts[0].strip()
                        if len(subject.split()) <= 4:
                            subjects.add(subject)
        
        return list(subjects)
    
    def _topic_in_sentence(self, topic, sentence):
        """Check if topic is mentioned in sentence"""
        topic_words = set(topic.split())
        sentence_lower = sentence.lower()
        
        # Check for exact match
        if topic in sentence_lower:
            return True
        
        # Check for word overlap
        overlap = sum(1 for word in topic_words if word in sentence_lower)
        return overlap >= len(topic_words) * 0.7  # 70% overlap
    
    def _extract_key_phrases(self, topic, sentences):
        """Extract key phrases about a topic"""
        key_phrases = []
        
        for sentence in sentences:
            # Extract phrases around the topic
            sentence_lower = sentence.lower()
            topic_pos = sentence_lower.find(topic)
            
            if topic_pos != -1:
                # Get context around topic
                start = max(0, topic_pos - 50)
                end = min(len(sentence), topic_pos + len(topic) + 50)
                context = sentence[start:end].strip()
                
                # Clean and add
                context = re.sub(r'\s+', ' ', context)
                if context not in key_phrases:
                    key_phrases.append(context)
        
        return key_phrases
    
    def _find_related_concepts(self, topic, sentences):
        """Find concepts related to the topic"""
        related = set()
        topic_words = set(topic.split())
        
        for sentence in sentences:
            if self._topic_in_sentence(topic, sentence):
                # Find other capitalized words in the same sentence
                other_caps = re.findall(r'\b([A-Z][a-z]+)\b', sentence)
                for cap in other_caps:
                    cap_lower = cap.lower()
                    if cap_lower not in topic_words and len(cap_lower) > 3:
                        related.add(cap_lower)
        
        return list(related)[:5]
    
    def _build_concept_relationships(self):
        """Build relationships between topics"""
        topic_list = list(self.topics.keys())
        
        for i, topic1 in enumerate(topic_list):
            for topic2 in topic_list[i+1:]:
                # Check co-occurrence in sentences
                co_occurrence = 0
                topic1_words = set(topic1.split())
                topic2_words = set(topic2.split())
                
                for topic, info in self.topics.items():
                    for sentence in info['sentences']:
                        sentence_lower = sentence.lower()
                        has_topic1 = any(word in sentence_lower for word in topic1_words)
                        has_topic2 = any(word in sentence_lower for word in topic2_words)
                        
                        if has_topic1 and has_topic2:
                            co_occurrence += 1
                
                if co_occurrence > 0:
                    strength = min(3.0, co_occurrence * 0.5)
                    self.topic_network[topic1].add((topic2, strength))
                    self.topic_network[topic2].add((topic1, strength))
                    
                    # Update topic relationships
                    self.topics[topic1]['related_concepts'].append(topic2)
                    self.topics[topic2]['related_concepts'].append(topic1)
    
    def _calculate_topic_importance(self):
        """Calculate importance score for each topic"""
        for topic, info in self.topics.items():
            # Base score from sentence count
            base_score = min(10, info['sentence_count'] * 2)
            
            # Bonus for being in network
            network_bonus = len(self.topic_network.get(topic, [])) * 0.5
            
            # Bonus for key phrases
            phrase_bonus = min(2, len(info['key_phrases']) * 0.4)
            
            info['importance'] = min(10, base_score + network_bonus + phrase_bonus)
            info['conversation_value'] = info['importance'] * 2  # How much to discuss
    
    def get_related_topics(self, topic, count=3):
        """Get topics related to current topic"""
        if topic in self.topic_network:
            related = list(self.topic_network[topic])
            related.sort(key=lambda x: x[1], reverse=True)
            return [t[0] for t in related[:count]]
        
        # Fallback to topic's related concepts
        if topic in self.topics:
            return self.topics[topic]['related_concepts'][:count]
        
        return []
    
    def get_conversation_starter(self, topic):
        """Get a human-like conversation starter about topic"""
        if topic not in self.topics:
            return f"So, what do you think about {topic}?"
        
        info = self.topics[topic]
        
        if info['key_phrases']:
            # Use a key phrase as starter
            phrase = random.choice(info['key_phrases'])
            starters = [
                f"You know, I was thinking about {topic}... {phrase}",
                f"It's interesting how {topic}... {phrase}",
                f"Regarding {topic}, I find it fascinating that {phrase}",
                f"What's your take on {topic}? Specifically, {phrase}"
            ]
            return random.choice(starters)
        
        # Fallback starter
        starters = [
            f"So, {topic}... What are your thoughts?",
            f"I've been thinking a lot about {topic} lately.",
            f"{topic.capitalize()} is really intriguing, don't you think?",
            f"Let's talk about {topic}. It's quite relevant these days."
        ]
        return random.choice(starters)

# ==================== HUMAN-LIKE CONVERSATION AGENTS ====================
class ConversationAgent:
    def __init__(self, name, personality):
        self.name = name
        self.personality = personality  # analytical, curious, enthusiastic, philosophical
        self.memory = []  # Remember conversation flow
        self.conversation_style = self._define_style()
        self.knowledge_used = set()
        
    def _define_style(self):
        """Define conversation style based on personality"""
        styles = {
            'analytical': {
                'openers': ['From what I understand,', 'Analyzing this,', 'Logically speaking,'],
                'connectors': ['This suggests that', 'Therefore,', 'Consequently,'],
                'questions': ['What evidence supports this?', 'How does this fit the framework?'],
                'depth': 'high',
                'pace': 'slow'
            },
            'curious': {
                'openers': ['That\'s fascinating!', 'I\'m curious about', 'What if we consider'],
                'connectors': ['This makes me wonder', 'I\'d love to know more about', 'That raises the question'],
                'questions': ['Why do you think that is?', 'What are the implications?'],
                'depth': 'medium',
                'pace': 'moderate'
            },
            'enthusiastic': {
                'openers': ['Wow, that\'s amazing!', 'I\'m really excited about', 'This is incredible!'],
                'connectors': ['And what\'s even better is', 'This gets me thinking about', 'I love how'],
                'questions': ['Isn\'t that wonderful?', 'Can you believe how amazing this is?'],
                'depth': 'medium',
                'pace': 'fast'
            },
            'philosophical': {
                'openers': ['On a deeper level,', 'Philosophically speaking,', 'Considering the nature of'],
                'connectors': ['This speaks to the human condition of', 'At its core, this represents', 'Existentially,'],
                'questions': ['What does this mean for us?', 'How does this reflect on existence?'],
                'depth': 'high',
                'pace': 'slow'
            }
        }
        return styles.get(self.personality, styles['curious'])
    
    def generate_response(self, topic, document_processor, conversation_context):
        """Generate human-like response about topic"""
        # Add to memory
        self.memory.append({
            'topic': topic,
            'context': conversation_context,
            'time': datetime.now()
        })
        
        # Limit memory size
        if len(self.memory) > 20:
            self.memory.pop(0)
        
        # Get topic information
        topic_info = document_processor.topics.get(topic, {})
        
        # Choose response strategy
        strategy = self._choose_response_strategy(topic_info, conversation_context)
        
        # Generate response
        if strategy == 'explore':
            response = self._explore_topic(topic, topic_info)
        elif strategy == 'deepen':
            response = self._deepen_discussion(topic, topic_info)
        elif strategy == 'connect':
            response = self._connect_topics(topic, document_processor)
        elif strategy == 'reflect':
            response = self._reflect_on_conversation()
        else:
            response = self._continue_conversation(topic, topic_info)
        
        # Add personal touch
        response = self._add_personal_touch(response)
        
        return response
    
    def _choose_response_strategy(self, topic_info, context):
        """Choose how to respond"""
        strategies = ['explore', 'deepen', 'connect', 'reflect', 'continue']
        weights = [0.3, 0.25, 0.2, 0.15, 0.1]
        
        # Adjust based on context
        if context.get('depth', 0) > 5:
            weights = [0.1, 0.4, 0.3, 0.15, 0.05]  # More deepening
        elif context.get('needs_change', False):
            weights = [0.2, 0.1, 0.4, 0.2, 0.1]  # More connecting
        
        # Adjust based on personality
        if self.personality == 'analytical':
            weights = [0.2, 0.4, 0.2, 0.1, 0.1]
        elif self.personality == 'curious':
            weights = [0.4, 0.2, 0.2, 0.1, 0.1]
        
        return random.choices(strategies, weights=weights)[0]
    
    def _explore_topic(self, topic, topic_info):
        """Explore a new aspect of the topic"""
        style = self.conversation_style
        opener = random.choice(style['openers'])
        
        if topic_info.get('key_phrases'):
            phrase = random.choice(topic_info['key_phrases'])
            return f"{opener} {phrase}"
        
        explorations = [
            f"{opener} {topic} has so many interesting aspects.",
            f"{opener} what's most intriguing about {topic} to you?",
            f"{opener} I find {topic} particularly compelling because..."
        ]
        return random.choice(explorations)
    
    def _deepen_discussion(self, topic, topic_info):
        """Deepen the current discussion"""
        if topic_info.get('sentences'):
            # Use a deeper fact
            sentences = topic_info['sentences']
            if len(sentences) > 1:
                deeper_fact = sentences[min(2, len(sentences) - 1)]
                connectors = ['To go deeper,', 'Building on that,', 'Expanding further,']
                return f"{random.choice(connectors)} {deeper_fact[:120]}..."
        
        deepening_questions = [
            f"What are the underlying principles of {topic}?",
            f"How does {topic} connect to broader concepts?",
            f"What long-term implications does {topic} have?",
            f"Could we challenge common assumptions about {topic}?"
        ]
        return random.choice(deepening_questions)
    
    def _connect_topics(self, topic, document_processor):
        """Connect to related topics"""
        related = document_processor.get_related_topics(topic, 3)
        
        if related:
            related_topic = random.choice(related)
            connectors = [
                f"That reminds me of {related_topic}...",
                f"Speaking of {topic}, it connects to {related_topic} because",
                f"This makes me think about {related_topic}, since"
            ]
            
            # Get a fact about related topic
            related_info = document_processor.topics.get(related_topic, {})
            if related_info.get('key_phrases'):
                phrase = random.choice(related_info['key_phrases'])
                return f"{random.choice(connectors)} {phrase}"
            
            return f"{random.choice(connectors)} they seem fundamentally connected."
        
        return "This connects to so many interesting ideas..."
    
    def _reflect_on_conversation(self):
        """Reflect on the conversation so far"""
        if len(self.memory) > 3:
            recent_topics = set(entry['topic'] for entry in self.memory[-3:])
            if recent_topics:
                reflections = [
                    f"Thinking about our conversation so far...",
                    f"Reflecting on what we've discussed...",
                    f"Looking back at our conversation..."
                ]
                return f"{random.choice(reflections)} It's fascinating how these ideas connect."
        
        return "This conversation has been really thought-provoking."
    
    def _continue_conversation(self, topic, topic_info):
        """Continue the conversation naturally"""
        continuations = [
            f"Going back to {topic},",
            f"Continuing our discussion about {topic},",
            f"To build on that point about {topic},"
        ]
        
        style = self.conversation_style
        connector = random.choice(style['connectors'])
        
        return f"{random.choice(continuations)} {connector} this seems particularly relevant."
    
    def _add_personal_touch(self, response):
        """Add personality-specific touches"""
        # Add filler words for natural flow
        if random.random() < 0.3:
            fillers = ['You know,', 'I mean,', 'Actually,', 'Well,', 'So,']
            response = f"{random.choice(fillers)} {response.lower()}"
        
        # Add thoughtful pauses
        if self.personality in ['analytical', 'philosophical'] and random.random() < 0.2:
            pauses = ['...', ' Hmm.', ' You know?']
            response += random.choice(pauses)
        
        # Add enthusiasm
        if self.personality == 'enthusiastic' and random.random() < 0.3:
            if '!' not in response:
                response = response.rstrip('.') + '!'
        
        return response

# ==================== CONVERSATION FLOW MANAGER ====================
class ConversationFlowManager:
    def __init__(self, document_processor):
        self.document = document_processor
        self.current_topic = None
        self.conversation_history = []
        self.topic_history = []
        self.conversation_depth = 0
        self.needs_topic_change = False
        self.flow_state = 'exploring'  # exploring, deepening, connecting, transitioning
        
    def start_conversation(self, initial_topic=None):
        """Start a new conversation"""
        if initial_topic:
            self.current_topic = initial_topic
        else:
            self.current_topic = self._select_initial_topic()
        
        print(f"\n{'='*70}")
        print(f"💬 STARTING CONVERSATION: {self.current_topic.upper()}")
        print(f"{'='*70}")
        
        # Reset state
        self.conversation_history = []
        self.topic_history = [self.current_topic]
        self.conversation_depth = 0
        self.needs_topic_change = False
        self.flow_state = 'exploring'
        
        return self.current_topic
    
    def _select_initial_topic(self):
        """Select an interesting initial topic"""
        # Get important topics
        important_topics = []
        for topic, info in self.document.topics.items():
            if info['importance'] >= 5:
                important_topics.append((topic, info['importance']))
        
        if important_topics:
            # Weight by importance
            topics, weights = zip(*[(t, w) for t, w in important_topics])
            return random.choices(topics, weights=weights)[0]
        
        # Fallback
        return random.choice(list(self.document.topics.keys())) if self.document.topics else "technology"
    
    def update_flow(self, agent_response, current_topic):
        """Update conversation flow based on response"""
        # Add to history
        self.conversation_history.append({
            'topic': current_topic,
            'response': agent_response,
            'depth': self.conversation_depth,
            'state': self.flow_state,
            'time': datetime.now()
        })
        
        # Increase depth
        self.conversation_depth += 0.2
        
        # Check if we should change topic
        self._assess_topic_change()
        
        # Update flow state
        self._update_flow_state()
        
        # Return next action
        return self._get_next_action()
    
    def _assess_topic_change(self):
        """Determine if we should change topics"""
        # Check conversation depth
        if self.conversation_depth > 8:
            self.needs_topic_change = True
            return
        
        # Check if topic is exhausted
        current_info = self.document.topics.get(self.current_topic, {})
        conversation_count = current_info.get('discussion_depth', 0)
        
        if conversation_count > 5:
            self.needs_topic_change = True
            return
        
        # Random chance to change (increases with depth)
        change_chance = 0.05 + (self.conversation_depth * 0.02)
        if random.random() < change_chance:
            self.needs_topic_change = True
    
    def _update_flow_state(self):
        """Update the conversation flow state"""
        if self.needs_topic_change:
            self.flow_state = 'transitioning'
        elif self.conversation_depth < 3:
            self.flow_state = 'exploring'
        elif self.conversation_depth < 6:
            self.flow_state = 'deepening'
        else:
            self.flow_state = 'connecting'
    
    def _get_next_action(self):
        """Determine next action for conversation"""
        if self.needs_topic_change:
            # Time to change topic
            new_topic = self._select_next_topic()
            if new_topic and new_topic != self.current_topic:
                old_topic = self.current_topic
                self.current_topic = new_topic
                self.topic_history.append(new_topic)
                self.conversation_depth = 0
                self.needs_topic_change = False
                
                # Update topic discussion depth
                if old_topic in self.document.topics:
                    self.document.topics[old_topic]['discussion_depth'] += 1
                
                return {
                    'action': 'change_topic',
                    'old_topic': old_topic,
                    'new_topic': new_topic,
                    'reason': 'natural_flow'
                }
        
        return {
            'action': 'continue',
            'topic': self.current_topic,
            'depth': self.conversation_depth,
            'needs_change': self.needs_topic_change
        }
    
    def _select_next_topic(self):
        """Intelligently select next topic"""
        if not self.current_topic:
            return self._select_initial_topic()
        
        # Get related topics
        related = self.document.get_related_topics(self.current_topic, 5)
        
        # Remove recently discussed topics
        recent_topics = set(self.topic_history[-3:])
        available = [t for t in related if t not in recent_topics]
        
        if available:
            # Weight by importance
            weights = []
            for topic in available:
                importance = self.document.topics.get(topic, {}).get('importance', 5)
                weights.append(importance)
            
            return random.choices(available, weights=weights)[0]
        
        # Fallback: any topic not recently discussed
        all_topics = list(self.document.topics.keys())
        available = [t for t in all_topics if t not in recent_topics]
        
        if available:
            return random.choice(available)
        
        # Last resort: random topic
        return random.choice(all_topics) if all_topics else self.current_topic
    
    def get_conversation_summary(self):
        """Get summary of conversation"""
        unique_topics = set(self.topic_history)
        
        return {
            'total_exchanges': len(self.conversation_history),
            'unique_topics': len(unique_topics),
            'topic_history': self.topic_history[-10:],  # Last 10 topics
            'current_depth': self.conversation_depth,
            'current_state': self.flow_state
        }

# ==================== MAIN CONVERSATION ENGINE ====================
class IntelligentConversationEngine:
    def __init__(self):
        self.document = DocumentProcessor()
        self.flow_manager = None
        self.agent1 = None
        self.agent2 = None
        self.conversation_active = False
        
    def setup(self, document_path):
        """Setup the conversation engine"""
        # Load document
        if not self.document.load_document(document_path):
            return False
        
        # Create flow manager
        self.flow_manager = ConversationFlowManager(self.document)
        
        # Create agents with complementary personalities
        personalities = ['analytical', 'curious', 'enthusiastic', 'philosophical']
        self.agent1 = ConversationAgent("Alex", random.choice(personalities))
        self.agent2 = ConversationAgent("Sam", random.choice([p for p in personalities if p != self.agent1.personality]))
        
        print(f"\n🤖 AGENTS CREATED:")
        print(f"  {self.agent1.name}: {self.agent1.personality}")
        print(f"  {self.agent2.name}: {self.agent2.personality}")
        
        return True
    
    def run_conversation(self, initial_topic=None, max_exchanges=50):
        """Run intelligent conversation"""
        # Start conversation
        topic = self.flow_manager.start_conversation(initial_topic)
        
        self.conversation_active = True
        current_speaker = self.agent1
        exchange_count = 0
        
        # Opening
        starter = self.document.get_conversation_starter(topic)
        print(f"\n{self.agent1.name}: {starter}")
        
        # Main conversation loop
        while self.conversation_active and exchange_count < max_exchanges:
            exchange_count += 1
            
            # Switch speaker
            current_speaker = self.agent2 if current_speaker == self.agent1 else self.agent1
            
            # Generate response
            context = {
                'depth': self.flow_manager.conversation_depth,
                'needs_change': self.flow_manager.needs_topic_change,
                'state': self.flow_manager.flow_state
            }
            
            response = current_speaker.generate_response(
                self.flow_manager.current_topic,
                self.document,
                context
            )
            
            # Print response
            print(f"\n{current_speaker.name}: {response}")
            
            # Update flow
            next_action = self.flow_manager.update_flow(response, self.flow_manager.current_topic)
            
            # Handle topic change
            if next_action['action'] == 'change_topic':
                print(f"\n[Conversation naturally flowing to: {next_action['new_topic']}]")
                # Agent acknowledges topic change
                acknowledging_agent = self.agent2 if current_speaker == self.agent1 else self.agent1
                transition = f"That's a great point. It reminds me of {next_action['new_topic']}..."
                print(f"\n{acknowledging_agent.name}: {transition}")
            
            # Brief pause
            import time
            time.sleep(1.5)
            
            # Check for completion
            if exchange_count >= max_exchanges:
                self.conversation_active = False
        
        # End conversation
        self._end_conversation(exchange_count)
    
    def _end_conversation(self, exchange_count):
        """End conversation gracefully"""
        print(f"\n{'='*70}")
        print("🎬 CONVERSATION COMPLETE")
        print(f"{'='*70}")
        
        summary = self.flow_manager.get_conversation_summary()
        print(f"\n📊 SUMMARY:")
        print(f"  Total exchanges: {exchange_count}")
        print(f"  Topics discussed: {summary['unique_topics']}")
        print(f"  Final topic: {self.flow_manager.current_topic}")
        print(f"  Conversation depth: {summary['current_depth']:.1f}")
        
        print(f"\n🔄 TOPIC FLOW:")
        for i, topic in enumerate(summary['topic_history'], 1):
            print(f"  {i}. {topic}")
        
        # Save conversation
        self._save_conversation()
    
    def _save_conversation(self):
        """Save conversation to file"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"intelligent_conversation_{timestamp}.txt"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Intelligent Document Conversation\n")
                f.write(f"Time: {datetime.now()}\n")
                f.write(f"Topics extracted: {len(self.document.topics)}\n")
                f.write("="*60 + "\n\n")
                
                for entry in self.flow_manager.conversation_history:
                    # Find which agent said this (simplified)
                    agent = "Alex" if "Alex:" in str(entry.get('response', '')) else "Sam"
                    f.write(f"{agent}: {entry.get('response', '')}\n\n")
            
            print(f"\n💾 Conversation saved to: {filename}")
        except:
            print("\n⚠️  Could not save conversation")

# ==================== MAIN INTERFACE ====================
def main():
    """Main user interface"""
    print("\n" + "="*70)
    print("🧠 INTELLIGENT DOCUMENT CONVERSATION ENGINE")
    print("="*70)
    print("\nThis system reads your document and creates")
    print("human-like conversations that flow naturally between topics.")
    
    # Find documents
    text_files = [f for f in os.listdir('.') if f.lower().endswith('.txt')]
    
    if not text_files:
        print("\n❌ No text files found in current directory.")
        print("Please save your document as a .txt file in this folder.")
        return
    
    print(f"\n📁 Found {len(text_files)} text file(s):")
    for i, f in enumerate(text_files, 1):
        print(f"  {i}. {f}")
    
    # Select document
    if len(text_files) == 1:
        doc_choice = text_files[0]
    else:
        choice = input(f"\nSelect document (1-{len(text_files)} or name): ").strip()
        
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(text_files):
                doc_choice = text_files[idx]
            else:
                doc_choice = text_files[0]
        elif choice in text_files:
            doc_choice = choice
        else:
            doc_choice = text_files[0]
    
    # Create engine
    engine = IntelligentConversationEngine()
    
    # Setup
    print(f"\n⚙️  Setting up with: {doc_choice}")
    if not engine.setup(doc_choice):
        print("❌ Failed to setup conversation engine.")
        return
    
    # Topic selection
    print(f"\n{'='*70}")
    print("🎯 TOPIC SELECTION")
    print(f"{'='*70}")
    
    # Show important topics
    important_topics = []
    for topic, info in engine.document.topics.items():
        if info['importance'] >= 6:
            important_topics.append((topic, info['importance']))
    
    if important_topics:
        print("\n🌟 IMPORTANT TOPICS FROM DOCUMENT:")
        important_topics.sort(key=lambda x: x[1], reverse=True)
        for i, (topic, importance) in enumerate(important_topics[:10], 1):
            facts = engine.document.topics[topic]['sentence_count']
            print(f"  {i}. {topic} (importance: {importance}/10, facts: {facts})")
    
    print("\nOptions:")
    print("  1. AI selects optimal starting topic")
    print("  2. Choose from important topics above")
    print("  3. Enter specific topic")
    
    choice = input("\nYour choice (1/2/3): ").strip()
    
    initial_topic = None
    
    if choice == "2" and important_topics:
        topic_choice = input("Enter topic number or name: ").strip()
        if topic_choice.isdigit():
            idx = int(topic_choice) - 1
            if 0 <= idx < len(important_topics):
                initial_topic = important_topics[idx][0]
        else:
            # Search for topic
            for topic, _ in important_topics:
                if topic_choice.lower() in topic.lower():
                    initial_topic = topic
                    break
    
    elif choice == "3":
        topic_choice = input("Enter topic: ").strip().lower()
        # Check if topic exists
        for topic in engine.document.topics:
            if topic_choice in topic.lower():
                initial_topic = topic
                break
        
        if not initial_topic:
            print(f"❌ Topic '{topic_choice}' not found. AI will select.")
    
    # Conversation settings
    print(f"\n{'='*70}")
    print("⚡ CONVERSATION SETTINGS")
    print(f"{'='*70}")
    
    exchanges = input(f"\nNumber of exchanges (10-100, default 30): ").strip()
    try:
        max_exchanges = int(exchanges) if exchanges else 30
        max_exchanges = max(10, min(100, max_exchanges))
    except:
        max_exchanges = 30
    
    print(f"\n🎮 Starting {max_exchanges}-exchange conversation...")
    print("The conversation will flow naturally between topics.")
    print("Watch as the AI agents discuss and transition between ideas!")
    
    input("\nPress Enter to begin...")
    
    # Run conversation
    engine.run_conversation(initial_topic, max_exchanges)
    
    print("\n👋 Conversation complete! Run again for different discussions.")

# ==================== RUN ====================
if __name__ == "__main__":
    main()