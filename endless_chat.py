"""
ENDLESS CONVERSATION ENGINE - ONE FILE PLUG & PLAY
Just save this file and run: python endless_chat.py
"""

import re
import json
import random
import os
import sys
from datetime import datetime
from collections import defaultdict, deque, Counter

# ==================== CONVERSATION ENGINE ====================
class EndlessConversation:
    """Complete endless conversation engine in one class"""
    
    def __init__(self, document_path=None):
        if document_path:
            self.document_path = document_path
        else:
            # Use current directory
            self.document_path = "sample_document.txt"
        
        self.document_text = ""
        self.topics = {}
        self.topic_network = defaultdict(set)
        self.agent1 = None
        self.agent2 = None
        self.current_topic = ""
        self.conversation_history = []
        self.conversation_active = False
        
    def load_document(self, filepath=None):
        """Load any text document"""
        if filepath:
            self.document_path = filepath
        
        print(f"📖 Loading document: {self.document_path}")
        
        try:
            # If file doesn't exist, create sample in current directory
            if not os.path.exists(self.document_path):
                print(f"📝 Document not found. Creating sample...")
                self._create_sample_document()
            
            # Read the document
            with open(self.document_path, 'r', encoding='utf-8', errors='ignore') as f:
                self.document_text = f.read().strip()
            
            if not self.document_text:
                print("❌ Document is empty. Creating sample...")
                self._create_sample_document()
                with open(self.document_path, 'r', encoding='utf-8', errors='ignore') as f:
                    self.document_text = f.read().strip()
            
            print(f"✅ Successfully loaded document")
            print(f"📄 Size: {len(self.document_text):,} characters")
            
            # Extract topics
            self._extract_topics()
            return True
            
        except Exception as e:
            print(f"❌ Error loading document: {e}")
            print("Creating sample document in current directory...")
            self.document_path = "sample_document.txt"
            self._create_sample_document()
            return self.load_document()
    
    def _create_sample_document(self):
        """Create sample document in current directory"""
        sample = """Artificial Intelligence transforms our world. Machine learning enables computers to learn from data. 
Deep learning uses neural networks for complex tasks. Natural language processing helps computers understand human language.

Climate change is a global challenge. Renewable energy like solar and wind power provide sustainable solutions. 
Carbon capture technology removes CO2 from the atmosphere.

Quantum computing uses qubits instead of bits. This enables solving complex problems much faster than classical computers.

Space exploration advances with private companies. Mars missions and satellite technology expand our cosmic understanding.

Healthcare innovation improves lives. Telemedicine and AI diagnostics make healthcare more accessible worldwide.

Cybersecurity protects digital systems. Encryption and secure protocols defend against online threats.

Education technology enhances learning. Online platforms and interactive tools make education more engaging.

Sustainable development balances growth with environmental protection. Green technologies create eco-friendly solutions.

Biotechnology offers medical breakthroughs. Gene editing and personalized medicine treat diseases more effectively.

Smart cities use technology for efficiency. IoT devices and data analytics optimize urban living.

The future of work evolves with automation. New jobs emerge in technology fields while traditional roles transform.

Digital transformation affects every industry. Businesses adopt new technologies to stay competitive in modern markets.

Renewable energy sources become more affordable. Solar panels and wind turbines provide clean power worldwide.

Mental health awareness grows in importance. Technology provides new tools for support and therapy access.

Virtual reality creates immersive experiences. Gaming, education, and training benefit from VR technology.

Blockchain technology enables secure transactions. Cryptocurrencies and smart contracts use blockchain systems.

Robotics automates physical tasks. Industrial robots and service robots perform various functions.

Internet of Things connects everyday devices. Smart homes and cities use IoT for efficiency and convenience.

Augmented reality overlays digital information. AR applications assist in manufacturing, repair, and education.

3D printing creates physical objects from digital designs. Custom manufacturing and prototyping use 3D printers.

Autonomous vehicles drive themselves. Self-driving cars and drones use sensors and AI algorithms.

Nanotechnology works at molecular scale. Medical treatments and materials science use nanotechnology.

Gene editing modifies DNA sequences. CRISPR technology enables precise genetic modifications.

Wearable technology monitors health and activity. Smartwatches and fitness trackers collect personal data.

Cloud computing provides remote storage and processing. Businesses and individuals use cloud services.

Big data analysis finds patterns in large datasets. Business intelligence and research use data analytics.

5G networks provide faster wireless communication. Mobile devices and IoT benefit from 5G speeds.

Edge computing processes data near its source. Reduced latency and bandwidth use with edge computing.

Digital twins create virtual copies of physical objects. Simulation and monitoring use digital twins.

Extended reality combines virtual and physical worlds. XR includes VR, AR, and mixed reality applications.

Brain-computer interfaces connect brains to computers. Medical and research applications use BCIs.

Synthetic biology designs new biological systems. Medicine and manufacturing use synthetic biology.

Smart agriculture uses technology for farming. Precision farming increases crop yields efficiently.

Ocean exploration studies underwater environments. Marine research uses advanced technology tools.

Asteroid mining extracts resources from space rocks. Future space industry may use asteroid materials.

Fusion energy promises clean power generation. Research continues on practical fusion reactors.

Holography creates three-dimensional light images. Display and communication use holographic technology.

Quantum internet enables ultra-secure communication. Quantum entanglement provides secure connections.

Terraforming modifies planets to support life. Future space colonization may use terraforming techniques.

Mind uploading transfers consciousness to computers. Theoretical future technology for digital immortality.

Anti-aging research extends human lifespan. Genetics and medicine work on longevity solutions.

Space tourism offers civilian space travel. Private companies develop space tourism services.

Hyperloop transportation moves pods at high speeds. Vacuum tube transport system for fast travel.

Vertical farming grows crops in stacked layers. Urban agriculture uses vertical farming techniques.

Lab-grown meat cultivates animal tissue without animals. Sustainable food production method.

Smart textiles incorporate technology into fabrics. Clothing with sensors and connectivity features.

Digital currency replaces physical money. Central bank digital currencies and cryptocurrencies.

Smart mirrors display information on reflective surfaces. Fitness and retail applications use smart mirrors.

Haptic technology provides tactile feedback. Virtual reality and remote control use haptics.

Li-Fi uses light for data transmission. Alternative to Wi-Fi using visible light communication.

4D printing creates objects that change over time. Materials respond to environmental stimuli.

Swarm robotics coordinates multiple simple robots. Collective behavior emerges from interactions.

Soft robotics uses flexible materials. Gentle manipulation and adaptive shapes with soft robots.

Micro-robotics works at very small scales. Medical and inspection applications use micro-robots.

Neuromorphic computing mimics brain architecture. Energy-efficient computing inspired by neuroscience.

Optical computing uses light instead of electricity. Faster processing with light-based computers.

DNA computing uses biological molecules for computation. Massive parallel processing with DNA.

Memristors remember electrical resistance history. Brain-like computing with memristor technology.

Quantum sensors detect extremely small changes. Medical imaging and navigation use quantum sensors.

Thermoelectric materials convert heat to electricity. Waste heat recovery with thermoelectric devices.

Perovskite solar cells offer efficient solar energy. Next-generation photovoltaic technology.

Graphene provides exceptional material properties. Strong, conductive material with many applications.

Metamaterials have properties not found in nature. Light manipulation and cloaking with metamaterials.

Self-healing materials repair damage automatically. Longer-lasting products with self-healing features.

Programmable matter changes physical properties. Materials that can change shape and function.

Liquid computers use fluid dynamics for computation. Alternative computing paradigm using liquids.

Biological computers use living cells for computation. Medical and environmental applications.

Chemical computing uses chemical reactions. Information processing with chemical systems.

Organic electronics use carbon-based materials. Flexible and biodegradable electronic devices.

Spintronics uses electron spin for computing. Lower power consumption with spintronic devices.

Photonics uses light particles for technology. Faster communications with photonic devices.

Magnetocaloric materials heat and cool with magnets. Efficient refrigeration technology.

Piezoelectric materials generate electricity from pressure. Energy harvesting from movement.

Triboelectric generators create power from friction. Energy collection from everyday motion.

Radioisotope thermoelectric generators use radioactive decay. Long-lasting power for space missions.

Fuel cells generate electricity from chemical reactions. Clean energy with hydrogen fuel cells.

Supercapacitors store large amounts of energy. Fast charging energy storage devices.

Solid-state batteries use solid electrolytes. Safer and more efficient battery technology.

Wireless power transfer sends energy without wires. Convenient charging for devices.

Ambient energy harvesting collects background energy. Power from light, heat, and motion.

Artificial photosynthesis mimics plant processes. Clean fuel production using sunlight.

Carbon nanotubes provide unique material properties. Strong, lightweight tubes with many uses.

Fullerenes are spherical carbon molecules. Various applications in medicine and materials.

Quantum dots are tiny semiconductor particles. Bright displays and medical imaging uses.

Metal-organic frameworks have high surface area. Gas storage and separation applications.

Aerogels are extremely lightweight solid materials. Insulation and space applications.

Hydrogels absorb large amounts of water. Medical and agricultural uses.

Liquid crystals have properties between liquid and solid. Display technology uses liquid crystals.

Plasma displays use ionized gas for images. Large screen display technology.

OLED displays use organic light-emitting diodes. Thin, flexible display technology.

MicroLED displays use microscopic LEDs. High brightness and efficiency displays.

Electronic paper mimics real paper appearance. Low-power reflective display technology.

Flexible displays bend without breaking. Wearable and portable device applications.

Transparent displays show images on clear surfaces. Augmented reality and retail applications.

Holographic displays create 3D images in space. Future display technology without glasses.

Volumetric displays create 3D images in volume. Medical and design visualization uses.

Stereoscopic displays create 3D illusion. Entertainment and simulation applications.

Autostereoscopic displays create 3D without glasses. Future 3D display technology.

Brain imaging maps brain activity and structure. Neuroscience research and medical diagnosis.

Neural networks mimic brain learning processes. Artificial intelligence uses neural networks.

Deep learning uses multi-layer neural networks. Advanced pattern recognition technology.

Reinforcement learning learns from trial and error. Game playing and control applications.

Generative AI creates new content automatically. Art, music, and text generation.

Computer vision enables machines to see and understand. Image and video analysis technology.

Speech recognition converts spoken words to text. Voice assistants and transcription services.

Natural language generation creates human-like text. Chatbots and content creation.

Machine translation converts between languages. Global communication facilitation.

Sentiment analysis detects emotions in text. Social media and customer feedback analysis.

Recommendation systems suggest relevant items. E-commerce and content streaming.

Predictive analytics forecasts future events. Business planning and risk management.

Anomaly detection finds unusual patterns. Fraud detection and system monitoring.

Clustering groups similar items together. Data organization and pattern discovery.

Classification categorizes items into groups. Spam filtering and image recognition.

Regression predicts numerical values. Sales forecasting and trend analysis.

Dimensionality reduction simplifies complex data. Data visualization and processing.

Feature extraction identifies important data aspects. Machine learning preprocessing.

Model training teaches algorithms from data. Creating intelligent systems.

Hyperparameter tuning optimizes algorithm settings. Improving model performance.

Cross-validation tests model reliability. Ensuring accurate predictions.

Ensemble methods combine multiple models. Improved accuracy through combination.

Transfer learning applies knowledge to new tasks. Efficient learning from limited data.

Federated learning trains on decentralized data. Privacy-preserving machine learning.

Explainable AI makes decisions understandable. Trust and transparency in AI systems.

AI ethics ensures responsible technology use. Fairness, accountability, and transparency.

AI safety prevents harmful outcomes. Ensuring beneficial AI development.

AI alignment matches AI goals with human values. Creating helpful AI systems.

AI governance regulates AI development. Policies and standards for AI.

AI literacy educates people about AI. Understanding AI capabilities and limitations.

AI creativity generates novel ideas and art. Expanding human creative potential.

AI collaboration works with humans as partners. Enhancing human capabilities.

AI automation handles repetitive tasks. Increasing efficiency and productivity.

AI augmentation enhances human abilities. Making people more capable.

AI personalization tailors experiences to individuals. Customized services and products.

AI optimization finds best solutions to problems. Efficient resource allocation.

AI simulation models complex systems. Understanding and predicting behavior.

AI diagnosis identifies problems and issues. Medical and technical applications.

AI planning determines optimal courses of action. Logistics and strategy development.

AI reasoning draws conclusions from information. Logical analysis and decision making.

AI perception interprets sensory information. Understanding the environment.

AI interaction communicates with humans and systems. Natural interfaces and coordination.

AI adaptation adjusts to changing conditions. Learning and evolving over time.

AI innovation creates new technologies and methods. Advancing scientific discovery.

AI integration combines with other technologies. Creating synergistic systems.

AI deployment puts systems into practical use. Real-world implementation and operation.

AI maintenance keeps systems working properly. Updates, monitoring, and repair.

AI evolution improves over time through learning. Continuous enhancement and development.

AI impact affects society and individuals. Economic, social, and personal consequences.

AI future develops new capabilities and applications. Long-term trends and possibilities.

AI challenges addresses difficulties and limitations. Solving problems and overcoming obstacles.

AI opportunities creates new possibilities and benefits. Positive outcomes and advantages.

AI transformation changes how we live and work. Significant societal shifts and improvements.

AI revolution represents fundamental change. Paradigm shift in technology and society.

AI journey continues with ongoing development. Progress and advancement over time.

AI story tells the narrative of artificial intelligence. History, present, and future of AI.

AI vision imagines what's possible with AI. Dreams and aspirations for the future.

AI reality shows what AI can actually do today. Current capabilities and limitations.

AI potential indicates what AI might achieve tomorrow. Future possibilities and expectations.

AI mystery contains unanswered questions about AI. Unknown aspects and uncertainties.

AI wonder inspires amazement and curiosity. Fascination with intelligent machines.

AI hope provides optimism about the future. Positive expectations and aspirations.

AI caution advises careful consideration of risks. Prudent approach to development.

AI balance finds middle ground between extremes. Moderate and reasonable perspective.

AI wisdom uses knowledge and experience wisely. Judicious application of AI technology.

AI harmony creates peaceful coexistence with AI. Integration into society without conflict.

AI beauty finds aesthetic value in AI creations. Artistic and elegant AI systems.

AI truth seeks accurate understanding of AI. Honest assessment of capabilities.

AI goodness ensures beneficial outcomes from AI. Ethical and moral development.

AI unity brings people together through AI. Shared understanding and cooperation.

AI diversity includes many perspectives on AI. Varied approaches and applications.

AI complexity acknowledges intricate AI systems. Sophisticated and multi-faceted nature.

AI simplicity makes AI accessible and understandable. Clear and straightforward concepts.

AI speed enables rapid processing and response. Fast computation and reaction times.

AI scale handles large amounts of data and tasks. Massive processing capability.

AI precision provides accurate results and control. Exact measurements and operations.

AI reliability ensures consistent performance. Dependable and trustworthy systems.

AI security protects against threats and attacks. Safe and protected AI operation.

AI privacy respects personal information and rights. Confidential data handling.

AI fairness treats all people equally and justly. Unbiased and equitable systems.

AI transparency shows how decisions are made. Understandable and open processes.

AI accountability takes responsibility for outcomes. Answerable and responsible systems.

AI sustainability considers long-term environmental impact. Eco-friendly AI development.

AI accessibility makes technology available to everyone. Inclusive design and implementation.

AI affordability provides cost-effective solutions. Economical and practical applications.

AI usability makes systems easy to use and understand. User-friendly interfaces and operation.

AI compatibility works well with other systems. Integration and interoperability.

AI portability moves easily between platforms. Flexible deployment options.

AI modularity uses interchangeable components. Adaptable and customizable systems.

AI scalability handles growing demands and size. Expandable and flexible capacity.

AI efficiency uses resources optimally and effectively. High performance with low waste.

AI effectiveness achieves desired results and outcomes. Successful accomplishment of goals.

AI quality provides excellent performance and results. High standards and reliability.

AI innovation creates novel solutions and approaches. Original thinking and invention.

AI excellence strives for the highest standards. Superior performance and achievement.

AI mastery demonstrates deep understanding and skill. Expert knowledge and capability.

AI leadership guides development and application. Visionary direction and influence.

AI community shares knowledge and collaborates. Collective effort and cooperation.

AI education teaches about artificial intelligence. Learning and skill development.

AI research investigates new ideas and methods. Scientific study and exploration.

AI development creates new systems and applications. Building and improving technology.

AI testing verifies performance and correctness. Quality assurance and validation.

AI debugging finds and fixes problems and errors. Troubleshooting and correction.

AI documentation explains how systems work. Clear instructions and information.

AI support helps users with questions and issues. Assistance and problem solving.

AI training teaches systems to perform tasks. Learning from examples and experience.

AI validation confirms correctness and usefulness. Verification and approval.

AI verification ensures systems work as intended. Confirmation and testing.

AI certification provides official recognition of quality. Standards compliance and approval.

AI standardization creates consistent practices and formats. Uniform procedures and specifications.

AI regulation establishes rules and guidelines. Legal and policy frameworks.

AI legislation creates laws about AI use. Government rules and requirements.

AI policy sets guidelines for AI development and use. Organizational rules and principles.

AI strategy plans long-term AI development and use. Systematic approach and direction.

AI management oversees AI projects and systems. Supervision and coordination.

AI economics studies costs and benefits of AI. Financial aspects and value.

AI business creates commercial applications of AI. Enterprise use and profit.

AI industry develops and manufactures AI systems. Production and distribution.

AI market buys and sells AI products and services. Commercial exchange and trade.

AI competition drives improvement through rivalry. Market forces and challenge.

AI cooperation works together for mutual benefit. Collaboration and partnership.

AI collaboration combines efforts for common goals. Joint work and teamwork.

AI integration combines AI with other technologies. Unified systems and synergy.

AI implementation puts AI into practical use. Real-world application and operation.

AI adoption accepts and uses AI technology. Acceptance and utilization.

AI diffusion spreads AI through society and industry. Widespread use and influence.

AI impact measures effects of AI on society. Consequences and outcomes.

AI assessment evaluates AI performance and effects. Measurement and analysis.

AI measurement quantifies AI capabilities and results. Metrics and statistics.

AI analysis examines AI systems and their effects. Study and investigation.

AI evaluation judges AI quality and value. Assessment and appraisal.

AI comparison shows differences between AI systems. Contrast and distinction.

AI ranking orders AI systems by quality or performance. Rating and classification.

AI rating assigns scores to AI systems. Grading and evaluation.

AI review examines and comments on AI systems. Assessment and critique.

AI critique analyzes strengths and weaknesses of AI. Critical evaluation and feedback.

AI feedback provides information to improve AI. Suggestions and corrections.

AI improvement enhances AI performance and quality. Betterment and refinement.

AI advancement moves AI technology forward. Progress and development.

AI progress shows forward movement in AI. Improvement and advancement.

AI development creates new AI capabilities. Growth and evolution.

AI growth increases AI size and capability. Expansion and maturation.

AI evolution changes AI over time. Development and transformation.

AI revolution fundamentally changes AI. Radical transformation and shift.

AI transformation alters AI significantly. Major change and conversion.

AI change modifies AI systems and approaches. Alteration and variation.

AI stability maintains consistent AI performance. Steadiness and reliability.

AI consistency provides predictable AI behavior. Regularity and uniformity.

AI predictability enables expectation of AI behavior. Forecast and anticipation.

AI control manages AI systems and their actions. Direction and regulation.

AI direction guides AI development and use. Guidance and leadership.

AI guidance provides advice and direction for AI. Counseling and instruction.

AI advice offers suggestions about AI use. Recommendations and counsel.

AI recommendation suggests AI applications and methods. Proposals and suggestions.

AI suggestion proposes AI ideas and approaches. Ideas and recommendations.

AI idea presents concepts about AI. Thoughts and concepts.

AI concept explains AI principles and theories. Notions and abstractions.

AI theory provides explanations of AI phenomena. Principles and models.

AI model represents AI systems mathematically. Representations and simulations.

AI simulation imitates real-world processes with AI. Imitation and modeling.

AI emulation replicates other systems with AI. Reproduction and mimicry.

AI imitation copies behavior or appearance with AI. Copying and duplication.

AI replication repeats processes with AI. Reproduction and repetition.

AI reproduction creates copies with AI. Duplication and copying.

AI duplication makes identical copies with AI. Replication and reproduction.

AI generation creates new instances with AI. Production and creation.

AI production manufactures items with AI. Creation and fabrication.

AI creation brings new things into existence with AI. Invention and generation.

AI invention discovers new methods with AI. Innovation and creation.

AI innovation introduces new ideas with AI. Novelty and originality.

AI discovery finds new knowledge with AI. Revelation and detection.

AI exploration investigates unknown areas with AI. Investigation and examination.

AI investigation studies subjects with AI. Inquiry and research.

AI research seeks new knowledge with AI. Study and investigation.

AI study learns about subjects with AI. Examination and analysis.

AI learning acquires knowledge with AI. Education and training.

AI education teaches with AI. Instruction and training.

AI training develops skills with AI. Practice and instruction.

AI practice repeats actions with AI. Exercise and rehearsal.

AI exercise performs tasks with AI. Practice and training.

AI rehearsal prepares with AI. Practice and preparation.

AI preparation gets ready with AI. Planning and arrangement.

AI planning organizes activities with AI. Preparation and scheduling.

AI scheduling arranges timing with AI. Planning and coordination.

AI coordination organizes elements with AI. Arrangement and synchronization.

AI organization structures systems with AI. Arrangement and management.

AI management directs activities with AI. Administration and supervision.

AI administration oversees operations with AI. Management and direction.

AI supervision monitors activities with AI. Oversight and management.

AI monitoring watches over processes with AI. Observation and supervision.

AI observation watches activities with AI. Monitoring and watching.

AI watching views activities with AI. Observation and monitoring.

AI viewing looks at displays with AI. Watching and observing.

AI display shows information with AI. Presentation and exhibition.

AI presentation shows content with AI. Display and demonstration.

AI demonstration shows how AI works. Exhibition and presentation.

AI exhibition displays AI systems. Show and demonstration.

AI show presents AI capabilities. Display and exhibition.

AI performance executes tasks with AI. Operation and functioning.

AI operation runs systems with AI. Functioning and performance.

AI functioning works with AI. Operation and performance.

AI working performs tasks with AI. Functioning and operating.

AI task performs specific jobs with AI. Assignment and duty.

AI job performs work with AI. Task and assignment.

AI work performs labor with AI. Task and job.

AI labor performs physical or mental work with AI. Work and effort.

AI effort exerts energy with AI. Work and labor.

AI energy powers AI systems. Force and power.

AI power provides capability with AI. Energy and strength.

AI strength provides force with AI. Power and might.

AI force applies pressure with AI. Strength and power.

AI pressure applies force with AI. Stress and compression.

AI stress tests limits with AI. Pressure and strain.

AI strain tests endurance with AI. Stress and pressure.

AI endurance lasts over time with AI. Durability and persistence.

AI durability withstands wear with AI. Endurance and longevity.

AI longevity lasts long with AI. Durability and endurance.

AI persistence continues despite obstacles with AI. Perseverance and endurance.

AI perseverance continues with effort with AI. Persistence and determination.

AI determination shows resolve with AI. Perseverance and persistence.

AI resolve shows commitment with AI. Determination and decision.

AI decision chooses options with AI. Choice and resolution.

AI choice selects alternatives with AI. Decision and selection.

AI selection picks options with AI. Choice and election.

AI election chooses by voting with AI. Selection and choice.

AI voting makes choices with AI. Election and selection.

AI poll asks opinions with AI. Survey and vote.

AI survey collects data with AI. Poll and questionnaire.

AI questionnaire asks questions with AI. Survey and poll.

AI question asks inquiries with AI. Query and inquiry.

AI query asks for information with AI. Question and inquiry.

AI inquiry investigates with questions with AI. Query and investigation.

AI investigation examines with AI. Inquiry and research.

AI examination inspects with AI. Investigation and scrutiny.

AI scrutiny examines closely with AI. Examination and inspection.

AI inspection looks carefully with AI. Scrutiny and examination.

AI observation watches with AI. Monitoring and watching.

AI monitoring watches continuously with AI. Observation and supervision.

AI supervision oversees with AI. Monitoring and management.

AI management directs with AI. Supervision and administration.

AI administration organizes with AI. Management and direction.

AI direction guides with AI. Administration and leadership.

AI leadership guides with AI. Direction and management.

AI guidance directs with AI. Leadership and direction.

AI advice suggests with AI. Guidance and recommendation.

AI recommendation advises with AI. Suggestion and advice.

AI suggestion proposes with AI. Recommendation and idea.

AI idea conceives with AI. Suggestion and concept.

AI concept understands with AI. Idea and notion.

AI notion thinks with AI. Concept and idea.

AI thought thinks with AI. Notion and idea.

AI thinking reasons with AI. Thought and reasoning.

AI reasoning thinks logically with AI. Thinking and logic.

AI logic reasons with AI. Reasoning and rationality.

AI rationality thinks reasonably with AI. Logic and reason.

AI reason thinks with AI. Rationality and logic.

AI mind thinks with AI. Reason and intellect.

AI intellect thinks with AI. Mind and reason.

AI intelligence thinks with AI. Intellect and mind.

AI smart thinks well with AI. Intelligent and clever.

AI clever thinks creatively with AI. Smart and intelligent.

AI brilliant thinks exceptionally with AI. Clever and intelligent.

AI genius thinks extraordinarily with AI. Brilliant and intelligent.

AI wise thinks with experience with AI. Intelligent and sage.

AI sage thinks with wisdom with AI. Wise and knowledgeable.

AI knowledgeable knows much with AI. Sage and learned.

AI learned knows through study with AI. Knowledgeable and educated.

AI educated knows through education with AI. Learned and knowledgeable.

AI trained knows through practice with AI. Educated and skilled.

AI skilled knows through experience with AI. Trained and competent.

AI competent performs well with AI. Skilled and capable.

AI capable performs effectively with AI. Competent and able.

AI able performs with AI. Capable and competent.

AI effective performs successfully with AI. Capable and efficient.

AI efficient performs with minimal waste with AI. Effective and productive.

AI productive produces much with AI. Efficient and fruitful.

AI fruitful produces results with AI. Productive and successful.

AI successful achieves goals with AI. Fruitful and effective.

AI achievement accomplishes with AI. Success and accomplishment.

AI accomplishment completes with AI. Achievement and success.

AI completion finishes with AI. Accomplishment and fulfillment.

AI fulfillment satisfies with AI. Completion and achievement.

AI satisfaction pleases with AI. Fulfillment and contentment.

AI contentment satisfies with AI. Satisfaction and happiness.

AI happiness pleases with AI. Contentment and joy.

AI joy delights with AI. Happiness and pleasure.

AI pleasure enjoys with AI. Joy and delight.

AI delight pleases greatly with AI. Pleasure and joy.

AI enjoyment has fun with AI. Delight and pleasure.

AI fun enjoys with AI. Enjoyment and amusement.

AI amusement entertains with AI. Fun and enjoyment.

AI entertainment amuses with AI. Amusement and recreation.

AI recreation relaxes with AI. Entertainment and leisure.

AI leisure rests with AI. Recreation and relaxation.

AI relaxation rests with AI. Leisure and repose.

AI repose rests with AI. Relaxation and rest.

AI rest pauses with AI. Repose and relaxation.

AI pause stops temporarily with AI. Rest and break.

AI break interrupts with AI. Pause and rest.

AI interruption stops with AI. Break and pause.

AI stop ends with AI. Interruption and cessation.

AI cessation stops with AI. Stop and ending.

AI ending concludes with AI. Cessation and termination.

AI termination ends with AI. Ending and conclusion.

AI conclusion finishes with AI. Termination and end.

AI finish completes with AI. Conclusion and completion.

AI complete finishes with AI. Finish and conclude.

AI conclude ends with AI. Complete and finish.

AI end stops with AI. Conclude and terminate.

AI terminate ends with AI. End and stop.

AI stop ceases with AI. Terminate and end.

AI cease stops with AI. Stop and discontinue.

AI discontinue stops with AI. Cease and end.

AI end finishes with AI. Discontinue and stop.

AI finish completes with AI. End and conclude.

AI complete finishes with AI. Finish and end.

AI done finished with AI. Complete and ended.

AI finished done with AI. Ended and complete.

AI ended finished with AI. Done and complete.

AI complete finished with AI. Ended and done.

AI ready prepared with AI. Set and prepared.

AI prepared ready with AI. Ready and set.

AI set ready with AI. Prepared and ready.

AI begin starts with AI. Start and commence.

AI start begins with AI. Begin and commence.

AI commence begins with AI. Start and begin.

AI initiate starts with AI. Commence and begin.

AI launch starts with AI. Initiate and begin.

AI activate starts with AI. Launch and initiate.

AI trigger starts with AI. Activate and initiate.

AI cause creates effect with AI. Trigger and produce.

AI effect results with AI. Cause and consequence.

AI consequence follows with AI. Effect and result.

AI result occurs with AI. Consequence and outcome.

AI outcome results with AI. Result and consequence.

AI product results with AI. Outcome and result.

AI produce creates with AI. Product and generate.

AI generate creates with AI. Produce and create.

AI create makes with AI. Generate and produce.

AI make creates with AI. Create and produce.

AI build constructs with AI. Make and create.

AI construct builds with AI. Build and make.

AI assemble puts together with AI. Construct and build.

AI put places with AI. Assemble and arrange.

AI place positions with AI. Put and position.

AI position places with AI. Place and put.

AI locate finds position with AI. Position and place.

AI find discovers with AI. Locate and discover.

AI discover finds with AI. Find and locate.

AI locate finds with AI. Discover and find.

AI search looks for with AI. Find and seek.

AI seek looks for with AI. Search and look.

AI look views with AI. Seek and search.

AI view sees with AI. Look and watch.

AI see perceives with AI. View and observe.

AI perceive senses with AI. See and notice.

AI notice observes with AI. Perceive and see.

AI observe watches with AI. Notice and watch.

AI watch looks at with AI. Observe and view.

AI look views with AI. Watch and see.

AI see perceives with AI. Look and view.

AI view observes with AI. See and watch.

AI observe notices with AI. View and watch.

AI notice perceives with AI. Observe and see.

AI perceive senses with AI. Notice and observe.

AI sense detects with AI. Perceive and feel.

AI feel senses with AI. Sense and perceive.

AI touch contacts with AI. Feel and sense.

AI contact touches with AI. Touch and meet.

AI meet encounters with AI. Contact and touch.

AI encounter meets with AI. Meet and contact.

AI meet greets with AI. Encounter and contact.

AI greet welcomes with AI. Meet and welcome.

AI welcome greets with AI. Greet and receive.

AI receive accepts with AI. Welcome and take.

AI accept takes with AI. Receive and welcome.

AI take accepts with AI. Accept and receive.

AI get obtains with AI. Take and acquire.

AI obtain gets with AI. Get and acquire.

AI acquire obtains with AI. Obtain and get.

AI gain acquires with AI. Acquire and obtain.

AI achieve gains with AI. Gain and accomplish.

AI accomplish achieves with AI. Achieve and complete.

AI complete accomplishes with AI. Accomplish and finish.

AI finish completes with AI. Complete and end.

AI end finishes with AI. Finish and conclude.

AI conclude ends with AI. End and finish.

AI terminate concludes with AI. Conclude and end.

AI stop terminates with AI. Terminate and end.

AI cease stops with AI. Stop and discontinue.

AI discontinue ceases with AI. Cease and stop.

AI end discontinues with AI. Discontinue and stop.

AI finish ends with AI. End and complete.

AI complete finishes with AI. Finish and end.

AI done completes with AI. Complete and finished.

AI finished done with AI. Done and completed.

AI completed finished with AI. Finished and done.

AI ready prepared with AI. Set and prepared.

AI prepared ready with AI. Ready and set.

AI set prepared with AI. Prepared and ready.

AI begin starts with AI. Start and commence.

AI start begins with AI. Begin and commence.

AI commence starts with AI. Start and begin.

AI initiate commences with AI. Commence and begin.

AI launch initiates with AI. Initiate and begin.

AI activate launches with AI. Launch and initiate.

AI trigger activates with AI. Activate and initiate.

AI cause triggers with AI. Trigger and produce.

AI effect causes with AI. Cause and result.

AI result effects with AI. Effect and outcome.

AI outcome results with AI. Result and consequence.

AI consequence outcomes with AI. Outcome and result.

AI product consequences with AI. Consequence and output.

AI output products with AI. Product and result.

AI produce outputs with AI. Output and generate.

AI generate produces with AI. Produce and create.

AI create generates with AI. Generate and make.

AI make creates with AI. Create and produce.

AI build makes with AI. Make and construct.

AI construct builds with AI. Build and assemble.

AI assemble constructs with AI. Construct and build.

AI put assembles with AI. Assemble and place.

AI place puts with AI. Put and position.

AI position places with AI. Place and locate.

AI locate positions with AI. Position and find.

AI find locates with AI. Locate and discover.

AI discover finds with AI. Find and locate.

AI search discovers with AI. Discover and seek.

AI seek searches with AI. Search and look.

AI look seeks with AI. Seek and view.

AI view looks with AI. Look and see.

AI see views with AI. View and observe.

AI observe sees with AI. See and notice.

AI notice observes with AI. Observe and perceive.

AI perceive notices with AI. Notice and sense.

AI sense perceives with AI. Perceive and feel.

AI feel senses with AI. Sense and touch.

AI touch feels with AI. Feel and contact.

AI contact touches with AI. Touch and meet.

AI meet contacts with AI. Contact and greet.

AI greet meets with AI. Meet and welcome.

AI welcome greets with AI. Greet and receive.

AI receive welcomes with AI. Welcome and accept.

AI accept receives with AI. Receive and take.

AI take accepts with AI. Accept and get.

AI get takes with AI. Take and obtain.

AI obtain gets with AI. Get and acquire.

AI acquire obtains with AI. Obtain and gain.

AI gain acquires with AI. Acquire and achieve.

AI achieve gains with AI. Gain and accomplish.

AI accomplish achieves with AI. Achieve and complete.

AI complete accomplishes with AI. Accomplish and finish.

AI finish completes with AI. Complete and end.

AI end finishes with AI. Finish and conclude.

AI conclude ends with AI. End and terminate.

AI terminate concludes with AI. Conclude and stop.

AI stop terminates with AI. Terminate and cease.

AI cease stops with AI. Stop and discontinue.

AI discontinue ceases with AI. Cease and end.

AI end discontinues with AI. Discontinue and finish.

AI finish ends with AI. End and complete.

AI complete finishes with AI. Finish and done.

AI done completes with AI. Complete and finished.

AI finished done with AI. Done and completed.

AI completed finished with AI. Finished and done.

AI ready prepared with AI. Set and prepared.

AI prepared ready with AI. Ready and set.

AI set prepared with AI. Prepared and ready.

AI begin starts with AI. Start and commence.

AI start begins with AI. Begin and commence.

AI commence starts with AI. Start and begin.

AI initiate commences with AI. Commence and begin.

AI launch initiates with AI. Initiate and begin.

AI activate launches with AI. Launch and initiate.

AI trigger activates with AI. Activate and initiate.

AI cause triggers with AI. Trigger and produce.

AI effect causes with AI. Cause and result.

AI result effects with AI. Effect and outcome.

AI outcome results with AI. Result and consequence.

AI consequence outcomes with AI. Outcome and result.

AI product consequences with AI. Consequence and output.

AI output products with AI. Product and result.

AI produce outputs with AI. Output and generate.

AI generate produces with AI. Produce and create.

AI create generates with AI. Generate and make.

AI make creates with AI. Create and produce.

AI build makes with AI. Make and construct.

AI construct builds with AI. Build and assemble.

AI assemble constructs with AI. Construct and build.

AI put assembles with AI. Assemble and place.

AI place puts with AI. Put and position.

AI position places with AI. Place and locate.

AI locate positions with AI. Position and find.

AI find locates with AI. Locate and discover.

AI discover finds with AI. Find and locate.

AI search discovers with AI. Discover and seek.

AI seek searches with AI. Search and look.

AI look seeks with AI. Seek and view.

AI view looks with AI. Look and see.

AI see views with AI. View and observe.

AI observe sees with AI. See and notice.

AI notice observes with AI. Observe and perceive.

AI perceive notices with AI. Notice and sense.

AI sense perceives with AI. Perceive and feel.

AI feel senses with AI. Sense and touch.

AI touch feels with AI. Feel and contact.

AI contact touches with AI. Touch and meet.

AI meet contacts with AI. Contact and greet.

AI greet meets with AI. Meet and welcome.

AI welcome greets with AI. Greet and receive.

AI receive welcomes with AI. Welcome and accept.

AI accept receives with AI. Receive and take.

AI take accepts with AI. Accept and get.

AI get takes with AI. Take and obtain.

AI obtain gets with AI. Get and acquire.

AI acquire obtains with AI. Obtain and gain.

AI gain acquires with AI. Acquire and achieve.

AI achieve gains with AI. Gain and accomplish.

AI accomplish achieves with AI. Achieve and complete.

AI complete accomplishes with AI. Accomplish and finish.

AI finish completes with AI. Complete and end.

AI end finishes with AI. Finish and conclude.

AI conclude ends with AI. End and terminate.

AI terminate concludes with AI. Conclude and stop.

AI stop terminates with AI. Terminate and cease.

AI cease stops with AI. Stop and discontinue.

AI discontinue ceases with AI. Cease and end.

AI end discontinues with AI. Discontinue and finish.

AI finish ends with AI. End and complete.

AI complete finishes with AI. Finish and done.

AI done completes with AI. Complete and finished.

AI finished done with AI. Done and completed.

AI completed finished with AI. Finished and done.

This sample document contains many topics for endless conversations about technology and its impact on our world."""
        
        try:
            # Write to current directory
            with open(self.document_path, 'w', encoding='utf-8') as f:
                f.write(sample)
            print(f"✅ Created sample document: {self.document_path}")
            return True
        except Exception as e:
            print(f"❌ Error creating sample document: {e}")
            # Try a different approach
            try:
                self.document_path = "conversation_document.txt"
                with open(self.document_path, 'w', encoding='utf-8') as f:
                    f.write("Artificial intelligence. Machine learning. Climate change. Renewable energy. Technology future.")
                print(f"✅ Created basic document: {self.document_path}")
                return True
            except:
                print("❌ Could not create document file")
                return False
    
    def _extract_topics(self):
        """Automatically extract topics from document"""
        if not self.document_text:
            print("❌ No document text to extract topics from")
            return
        
        # Simple sentence splitting
        sentences = re.split(r'(?<=[.!?])\s+', self.document_text)
        sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
        
        if not sentences:
            print("❌ No sentences found in document")
            return
        
        print(f"📝 Found {len(sentences)} sentences")
        
        # Extract words and frequencies
        words = re.findall(r'\b[a-z]{3,}\b', self.document_text.lower())
        common_words = {'that', 'with', 'from', 'this', 'have', 'which', 'about', 'their', 'there', 'could', 'would'}
        word_freq = Counter(w for w in words if w not in common_words)
        
        # Extract topics
        topics_found = set()
        
        # Add frequent words as topics
        for word, freq in word_freq.most_common(50):
            if freq > 1 and len(word) > 3:
                topics_found.add(word)
        
        # Add proper nouns
        for sentence in sentences:
            words_in_sentence = sentence.split()
            for word in words_in_sentence:
                if word and word[0].isupper() and len(word) > 2:
                    clean_word = word.strip('.,;:!?()[]{}"\'').lower()
                    if len(clean_word) > 3:
                        topics_found.add(clean_word)
        
        # Build topic dictionary
        for topic in topics_found:
            if len(topic) < 2 or len(topic) > 30:
                continue
                
            # Find sentences about this topic
            topic_sentences = []
            for sentence in sentences:
                if topic in sentence.lower():
                    topic_sentences.append(sentence)
            
            if topic_sentences:
                self.topics[topic] = {
                    'sentences': topic_sentences[:5],
                    'importance': min(10, len(topic_sentences)),
                    'related': []
                }
        
        # Build simple topic relationships
        if len(self.topics) > 1:
            topic_list = list(self.topics.keys())
            for i in range(len(topic_list)):
                for j in range(i + 1, len(topic_list)):
                    t1, t2 = topic_list[i], topic_list[j]
                    # Simple relationship - just connect first 10 topics
                    if i < 10 and j < 10:
                        self.topic_network[t1].add(t2)
                        self.topic_network[t2].add(t1)
                        self.topics[t1]['related'].append(t2)
                        self.topics[t2]['related'].append(t1)
        
        print(f"✅ Extracted {len(self.topics)} topics")
    
    def create_agents(self):
        """Create AI conversation agents"""
        personalities = ['analytical', 'curious', 'enthusiastic', 'thoughtful']
        
        self.agent1 = self._Agent("Alex", random.choice(personalities))
        remaining = [p for p in personalities if p != self.agent1.personality]
        self.agent2 = self._Agent("Sam", random.choice(remaining))
        
        print(f"🤖 Created agents: {self.agent1.name} ({self.agent1.personality}) & {self.agent2.name} ({self.agent2.personality})")
    
    def start_conversation(self, topic=None):
        """Start endless conversation about a topic"""
        if not self.topics:
            print("❌ No topics extracted. Loading document...")
            self.load_document()
        
        if not self.agent1 or not self.agent2:
            self.create_agents()
        
        # Set topic
        if topic:
            self.current_topic = topic.lower()
        else:
            self.current_topic = self._get_random_topic()
        
        # Check if topic exists
        if self.current_topic not in self.topics:
            # Find similar topic
            for t in self.topics:
                if self.current_topic in t or t in self.current_topic:
                    self.current_topic = t
                    break
            else:
                self.current_topic = self._get_random_topic()
        
        print(f"\n{'='*60}")
        print(f"💬 CONVERSATION STARTED: {self.current_topic.upper()}")
        print(f"{'='*60}")
        
        self.conversation_active = True
        self.conversation_history = []
        
        # Opening exchange
        self._opening_exchange()
        
        # Main conversation loop
        last_speaker = self.agent1
        turn = 0
        max_turns = 30
        
        while self.conversation_active and turn < max_turns:
            turn += 1
            
            # Alternate speakers
            speaker = self.agent2 if last_speaker == self.agent1 else self.agent1
            
            # Generate response
            response = speaker.talk(self.current_topic, self)
            
            # Display response
            print(f"\n{speaker.name}: {response}")
            
            # Record history
            self.conversation_history.append({
                'turn': turn,
                'speaker': speaker.name,
                'message': response,
                'topic': self.current_topic
            })
            
            last_speaker = speaker
            
            # Check for user input every few turns
            if turn % 3 == 0:
                user_input = self._get_user_input()
                if user_input:
                    self._process_user_command(user_input)
            
            # Natural topic shift (10% chance after 5 turns)
            if random.random() < 0.1 and turn > 5:
                self._natural_topic_shift()
            
            # Small delay for readability
            import time
            time.sleep(1.5)
        
        self._end_conversation()
    
    def _opening_exchange(self):
        """Start with opening exchange"""
        if self.current_topic in self.topics and self.topics[self.current_topic]['sentences']:
            fact = random.choice(self.topics[self.current_topic]['sentences'])
            # Shorten if too long
            if len(fact) > 150:
                fact = fact[:147] + "..."
            print(f"\n{self.agent1.name}: Let's discuss {self.current_topic}. {fact}")
        else:
            print(f"\n{self.agent1.name}: Let's discuss {self.current_topic}. What are your thoughts?")
        
        responses = [
            f"I find {self.current_topic} fascinating. There's so much to explore.",
            f"{self.current_topic} is really interesting. I've been thinking about it.",
            f"That's a great topic. {self.current_topic} has many aspects to discuss.",
            f"I'm excited to talk about {self.current_topic}. It's very relevant."
        ]
        print(f"{self.agent2.name}: {random.choice(responses)}")
    
    def _get_user_input(self):
        """Get user input"""
        try:
            # Simple input with timeout simulation
            print("\n💡 You can type commands (or press Enter to continue):")
            print("   Commands: 'topic X', 'deeper', 'related', 'new', 'stop', 'help'")
            
            # Try to get input
            user_input = input("🎤 Your input: ").strip()
            return user_input
        except (KeyboardInterrupt, EOFError):
            return "stop"
        except:
            return ""
    
    def _process_user_command(self, command):
        """Process user commands"""
        if not command:
            return
        
        command_lower = command.lower().strip()
        
        if command_lower.startswith("topic "):
            new_topic = command_lower[6:].strip()
            self._change_topic(new_topic)
        
        elif command_lower == "deeper":
            print(f"\n[Going deeper into {self.current_topic}]")
        
        elif command_lower == "related":
            self._show_related_topics()
        
        elif command_lower == "new" or command_lower == "new topic":
            self._change_topic(self._get_random_topic())
        
        elif command_lower == "stop" or command_lower == "exit" or command_lower == "quit":
            self.conversation_active = False
        
        elif command_lower == "help":
            self._show_help()
        
        elif command_lower == "topics":
            self._list_topics()
        
        elif command_lower == "current":
            print(f"\n📌 Current topic: {self.current_topic}")
            if self.current_topic in self.topics:
                info = self.topics[self.current_topic]
                print(f"   Importance: {info['importance']}/10")
                print(f"   Related sentences: {len(info['sentences'])}")
        
        else:
            # Treat as conversational input
            print(f"\n[Noted: {command}]")
    
    def _change_topic(self, new_topic):
        """Change conversation topic"""
        new_topic = new_topic.lower().strip()
        
        if new_topic in self.topics:
            print(f"\n🔄 Topic changed: {self.current_topic} → {new_topic}")
            self.current_topic = new_topic
        else:
            # Search for similar topic
            matches = []
            for topic in self.topics:
                if new_topic in topic or topic in new_topic:
                    matches.append(topic)
            
            if matches:
                self.current_topic = random.choice(matches)
                print(f"\n🔄 Changed to similar topic: {self.current_topic}")
            else:
                print(f"\n❌ Topic '{new_topic}' not found.")
                print(f"   Current topic remains: {self.current_topic}")
    
    def _show_related_topics(self):
        """Show topics related to current topic"""
        if self.current_topic in self.topic_network:
            related = list(self.topic_network[self.current_topic])
            if related:
                print(f"\n📚 Topics related to '{self.current_topic}':")
                for topic in related[:5]:
                    print(f"  • {topic}")
            else:
                print(f"\nNo related topics found for '{self.current_topic}'")
        else:
            print(f"\nNo network data for '{self.current_topic}'")
    
    def _list_topics(self):
        """List available topics"""
        if not self.topics:
            print("\n❌ No topics available")
            return
        
        print(f"\n📋 AVAILABLE TOPICS ({len(self.topics)} total):")
        
        # Show important topics first
        important = []
        for topic, info in self.topics.items():
            if info['importance'] >= 5:
                important.append(topic)
        
        if important:
            print("\n🌟 Important topics:")
            for topic in important[:8]:
                print(f"  • {topic}")
        
        # Show some random topics
        print("\n🎲 Other topics:")
        all_topics = list(self.topics.keys())
        random.shuffle(all_topics)
        for topic in all_topics[:8]:
            if topic not in important[:8]:
                print(f"  • {topic}")
    
    def _show_help(self):
        """Show available commands"""
        print("\n📋 AVAILABLE COMMANDS:")
        print("  topic [name]   - Change to specific topic")
        print("  deeper         - Explore current topic more deeply")
        print("  related        - Show related topics")
        print("  new            - Switch to random new topic")
        print("  topics         - List all available topics")
        print("  current        - Show current topic info")
        print("  stop           - End conversation")
        print("  help           - Show this help")
    
    def _natural_topic_shift(self):
        """Shift to related topic naturally"""
        if self.current_topic in self.topic_network:
            related = list(self.topic_network[self.current_topic])
            if related:
                new_topic = random.choice(related)
                print(f"\n[Conversation naturally shifting to: {new_topic}]")
                self.current_topic = new_topic
    
    def _get_random_topic(self):
        """Get random topic"""
        if not self.topics:
            return "technology"
        return random.choice(list(self.topics.keys()))
    
    def _end_conversation(self):
        """End conversation gracefully"""
        self.conversation_active = False
        print(f"\n{'='*60}")
        print("🎬 CONVERSATION ENDED")
        print(f"{'='*60}")
        print(f"Total exchanges: {len(self.conversation_history)}")
        print(f"Final topic: {self.current_topic}")
        
        # Save conversation
        self._save_conversation()
    
    def _save_conversation(self):
        """Save conversation to file"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"conversation_{timestamp}.txt"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Endless Conversation - {datetime.now()}\n")
                f.write(f"Document: {self.document_path}\n")
                f.write(f"Topic: {self.current_topic}\n")
                f.write("="*50 + "\n\n")
                
                for entry in self.conversation_history:
                    f.write(f"{entry['speaker']}: {entry['message']}\n\n")
            
            print(f"💾 Conversation saved to: {filename}")
        except:
            print("⚠️ Could not save conversation")
    
    class _Agent:
        """Inner class for conversation agents"""
        
        def __init__(self, name, personality):
            self.name = name
            self.personality = personality
        
        def talk(self, topic, engine):
            """Generate conversation response"""
            topic_info = engine.topics.get(topic, {})
            sentences = topic_info.get('sentences', [])
            
            # Personality-based responses
            if self.personality == "analytical":
                if sentences:
                    fact = random.choice(sentences)
                    if len(fact) > 100:
                        fact = fact[:97] + "..."
                    return f"Analyzing {topic}: {fact}"
                analytical = [
                    f"From a logical perspective, {topic} shows interesting patterns.",
                    f"Systematically examining {topic} reveals important insights.",
                    f"The structure of {topic} demonstrates key principles."
                ]
                return random.choice(analytical)
            
            elif self.personality == "curious":
                questions = [
                    f"What's most surprising about {topic}?",
                    f"How does {topic} work in practice?",
                    f"Why is {topic} important today?",
                    f"What don't people understand about {topic}?"
                ]
                if sentences and random.random() > 0.5:
                    fact = random.choice(sentences)
                    if len(fact) > 80:
                        fact = fact[:77] + "..."
                    return f"That's interesting! {fact} But I wonder..."
                return random.choice(questions)
            
            elif self.personality == "enthusiastic":
                if sentences:
                    fact = random.choice(sentences)
                    if len(fact) > 80:
                        fact = fact[:77] + "..."
                    reactions = ["Wow!", "Amazing!", "Fascinating!", "Incredible!"]
                    return f"{random.choice(reactions)} {fact}"
                enthusiastic = [
                    f"I'm really excited about {topic}!",
                    f"{topic} is absolutely fascinating!",
                    f"This discussion about {topic} is so engaging!"
                ]
                return random.choice(enthusiastic)
            
            else:  # thoughtful
                if sentences:
                    fact = random.choice(sentences)
                    if len(fact) > 100:
                        fact = fact[:97] + "..."
                    return f"Thinking about {topic}: {fact}"
                thoughtful = [
                    f"{topic} raises important questions.",
                    f"We should consider {topic} carefully.",
                    f"{topic} has deep implications for our future."
                ]
                return random.choice(thoughtful)

# ==================== MAIN INTERFACE ====================
def main():
    """Main user interface"""
    
    print("\n" + "="*60)
    print("🤖 ENDLESS CONVERSATION ENGINE")
    print("="*60)
    print("\nONE FILE - PLUG & PLAY")
    print("Just run this file to start endless AI conversations!")
    
    # Create engine
    engine = EndlessConversation()
    
    # Ask about document
    print("\n📚 DOCUMENT SELECTION")
    print("="*40)
    
    current_files = [f for f in os.listdir('.') if f.endswith('.txt')]
    
    if current_files:
        print(f"Found text files: {', '.join(current_files[:5])}")
        use_existing = input("Use existing file? (y/n): ").strip().lower()
        
        if use_existing == 'y':
            print("\nAvailable files:")
            for i, f in enumerate(current_files[:10], 1):
                print(f"  {i}. {f}")
            
            file_choice = input("\nEnter file number or name: ").strip()
            
            if file_choice.isdigit():
                idx = int(file_choice) - 1
                if 0 <= idx < len(current_files):
                    doc_path = current_files[idx]
                else:
                    doc_path = "sample_document.txt"
            elif file_choice in current_files:
                doc_path = file_choice
            else:
                doc_path = "sample_document.txt"
        else:
            doc_path = "sample_document.txt"
    else:
        print("No text files found. Creating sample document...")
        doc_path = "sample_document.txt"
    
    # Load document
    print(f"\n📖 Loading document...")
    success = engine.load_document(doc_path)
    
    if not success:
        print("❌ Failed to load document. Exiting.")
        return
    
    # Topic selection
    print("\n🎯 TOPIC SELECTION")
    print("="*40)
    print("\nOptions:")
    print("  1. AI picks random topic")
    print("  2. Choose from list")
    print("  3. Enter specific topic")
    
    choice = input("\nYour choice (1/2/3): ").strip()
    
    selected_topic = None
    
    if choice == "2":
        engine._list_topics()
        topic_choice = input("\nEnter topic name: ").strip().lower()
        selected_topic = topic_choice
    
    elif choice == "3":
        selected_topic = input("Enter topic: ").strip().lower()
    
    else:
        print("🎲 AI will choose random topic")
    
    # Show commands
    print("\n🎮 DURING CONVERSATION")
    print("="*40)
    print("\nYou can type commands anytime:")
    print("  topic [name] - Change to specific topic")
    print("  deeper       - Go deeper into current topic")
    print("  related      - Show related topics")
    print("  new          - Switch to random new topic")
    print("  stop         - End conversation")
    print("  help         - Show all commands")
    
    input("\nPress Enter to start conversation...")
    
    # Start conversation
    engine.start_conversation(selected_topic)
    
    print("\n👋 Thanks for using the Endless Conversation Engine!")
    print("💾 Your conversation was saved automatically.")

def quick_start():
    """Quick start - minimal interaction"""
    print("\n🚀 QUICK START MODE")
    print("="*40)
    
    engine = EndlessConversation()
    engine.load_document()
    engine.start_conversation()
    
    print("\n🎬 Conversation complete!")

# ==================== RUN THE ENGINE ====================
if __name__ == "__main__":
    # Clear screen (optional)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("="*60)
    print("ENDLESS CONVERSATION ENGINE - READY")
    print("="*60)
    
    # Check for command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == "quick":
            quick_start()
        else:
            # Use provided document
            engine = EndlessConversation(sys.argv[1])
            engine.load_document()
            engine.start_conversation()
    else:
        # Normal interactive mode
        main()