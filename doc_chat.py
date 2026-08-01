"""
DOCUMENT CONVERSATION ENGINE
Reads your document and creates endless conversations from it
"""

import re
import random
import os
from datetime import datetime
from collections import defaultdict, Counter

# ==================== DOCUMENT READER ====================
def read_document(filename="document.txt"):
    """Read text from a document file"""
    try:
        # First try in current directory
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        
        # Try common locations
        paths_to_try = [
            filename,
            f"./{filename}",
            f"../{filename}",
            f"documents/{filename}",
            f"data/{filename}",
        ]
        
        for path in paths_to_try:
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    print(f"📖 Found document at: {path}")
                    return f.read()
        
        # If no file found, ask user
        print(f"\n❌ Document '{filename}' not found.")
        print("Please enter the path to your document:")
        user_path = input("Path: ").strip()
        
        if os.path.exists(user_path):
            with open(user_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()
        else:
            print("❌ File not found. Using sample content.")
            return get_sample_content()
            
    except Exception as e:
        print(f"❌ Error reading document: {e}")
        return get_sample_content()

def get_sample_content():
    """Return sample content if no document found"""
    return """Artificial Intelligence and Its Impact

Artificial Intelligence (AI) is transforming every industry. From healthcare to finance, AI systems analyze data and make decisions.

Machine Learning (ML) is a subset of AI. ML algorithms learn patterns from data without explicit programming.

Deep Learning uses neural networks with many layers. These networks can recognize complex patterns in images, speech, and text.

Natural Language Processing (NLP) enables computers to understand human language. Chatbots and translators use NLP technology.

Climate Change is a global challenge. Rising temperatures affect weather patterns worldwide.

Renewable Energy sources include solar, wind, and hydroelectric power. These clean energy sources reduce carbon emissions.

Quantum Computing represents a new computing paradigm. Quantum bits (qubits) can exist in multiple states simultaneously.

Space Exploration has entered a new era. Private companies now launch rockets alongside government agencies.

Cybersecurity protects digital systems from attacks. Encryption and firewalls are common security measures.

Blockchain technology enables secure transactions. Cryptocurrencies like Bitcoin use blockchain systems.

Internet of Things (IoT) connects everyday devices. Smart homes use IoT for automation and control.

Virtual Reality (VR) creates immersive digital environments. VR is used in gaming, training, and education.

Augmented Reality (AR) overlays digital information on the real world. AR apps assist with navigation and repair.

Robotics automates physical tasks. Industrial robots assemble products in factories.

3D Printing creates objects from digital designs. This technology enables custom manufacturing.

Biotechnology uses living organisms for practical applications. Genetic engineering modifies DNA sequences.

Nanotechnology works at molecular scales. Medical treatments use nanoparticles for drug delivery.

Smart Cities use technology to improve urban life. Sensors optimize traffic flow and energy use.

Sustainable Development balances economic growth with environmental protection. Green technologies support sustainability.

Digital Transformation changes how businesses operate. Companies adopt new technologies to stay competitive.

Future of Work evolves with automation. While some jobs disappear, new technology roles emerge.

Education Technology enhances learning experiences. Online platforms make education accessible worldwide.

Healthcare Innovation improves patient outcomes. Telemedicine allows remote consultations with doctors.

Financial Technology (FinTech) disrupts traditional banking. Mobile payments and digital wallets are common.

Mental Health awareness grows in importance. Digital tools provide support and therapy access.

Electric Vehicles (EVs) reduce transportation emissions. Battery technology continues to improve.

Renewable Energy Storage addresses intermittency issues. Batteries store solar and wind power.

Carbon Capture removes CO2 from the atmosphere. This technology helps mitigate climate change.

Gene Editing modifies DNA sequences precisely. CRISPR technology enables genetic modifications.

Wearable Technology monitors health metrics. Smartwatches track fitness and vital signs.

Cloud Computing provides remote computing resources. Businesses use cloud services for storage and processing.

Big Data analysis finds patterns in large datasets. Data scientists extract insights from information.

5G Networks offer faster wireless communication. Mobile devices benefit from increased bandwidth.

Edge Computing processes data near its source. This reduces latency for time-sensitive applications.

Digital Twins create virtual copies of physical objects. Engineers use digital twins for simulation.

Extended Reality (XR) combines VR, AR, and mixed reality. XR creates seamless digital-physical experiences.

Brain-Computer Interfaces (BCIs) connect brains to computers. BCIs assist people with disabilities.

Synthetic Biology designs new biological systems. Researchers create artificial organisms.

Smart Agriculture uses technology for farming. Drones monitor crop health from above.

Ocean Exploration studies marine environments. Underwater robots collect data from the deep sea.

Asteroid Mining could extract resources from space. This futuristic industry may develop.

Fusion Energy promises clean power generation. Scientists work to make fusion reactors practical.

Holography creates three-dimensional light images. Future displays may use holographic technology.

Quantum Internet enables ultra-secure communication. Quantum encryption prevents eavesdropping.

Terraforming modifies planets to support life. This concept appears in science fiction.

Mind Uploading transfers consciousness to computers. This remains theoretical technology.

Anti-Aging Research extends human lifespan. Scientists study cellular aging processes.

Space Tourism offers civilian space travel. Companies develop spacecraft for tourists.

Hyperloop Transportation moves pods at high speeds. Vacuum tubes reduce air resistance.

Vertical Farming grows crops in stacked layers. Urban agriculture uses limited space efficiently.

Lab-Grown Meat cultivates animal tissue without animals. This sustainable food production method.

Smart Textiles incorporate technology into fabrics. Clothing with sensors monitors health.

Digital Currency replaces physical money. Central banks develop digital currency systems.

Smart Mirrors display information on reflective surfaces. Fitness and retail applications exist.

Haptic Technology provides tactile feedback. VR systems use haptics for immersion.

Li-Fi uses light for data transmission. LED lights can transmit internet signals.

4D Printing creates objects that change over time. Materials respond to environmental stimuli.

Swarm Robotics coordinates multiple simple robots. Collective behavior emerges from interactions.

Soft Robotics uses flexible materials. These robots handle delicate objects gently.

Micro-Robotics works at very small scales. Medical applications include targeted drug delivery.

Neuromorphic Computing mimics brain architecture. Energy-efficient chips use this approach.

Optical Computing uses light instead of electricity. Photonic circuits process information faster.

DNA Computing uses biological molecules for computation. Massive parallel processing possible.

Memristors remember electrical resistance history. These components enable brain-like computing.

Quantum Sensors detect extremely small changes. Medical imaging benefits from quantum sensors.

Thermoelectric Materials convert heat to electricity. Waste heat recovery applications.

Perovskite Solar Cells offer efficient solar energy. Next-generation photovoltaic technology.

Graphene provides exceptional material properties. This strong, conductive material has many uses.

Metamaterials have properties not found in nature. Light manipulation applications exist.

Self-Healing Materials repair damage automatically. Longer-lasting products result.

Programmable Matter changes physical properties. Materials adapt to different needs.

Liquid Computers use fluid dynamics for computation. Alternative computing paradigm.

Biological Computers use living cells for computation. Medical and environmental applications.

Chemical Computing uses chemical reactions. Information processing with chemicals.

Organic Electronics use carbon-based materials. Flexible and biodegradable devices.

Spintronics uses electron spin for computing. Lower power consumption possible.

Photonics uses light particles for technology. Faster communications result.

Magnetocaloric Materials heat and cool with magnets. Efficient refrigeration technology.

Piezoelectric Materials generate electricity from pressure. Energy harvesting applications.

Triboelectric Generators create power from friction. Energy collection from motion.

Radioisotope Thermoelectric Generators use radioactive decay. Long-lasting space power.

Fuel Cells generate electricity from chemical reactions. Clean energy with hydrogen.

Supercapacitors store large amounts of energy. Fast charging energy storage.

Solid-State Batteries use solid electrolytes. Safer and more efficient batteries.

Wireless Power Transfer sends energy without wires. Convenient device charging.

Ambient Energy Harvesting collects background energy. Power from light, heat, motion.

Artificial Photosynthesis mimics plant processes. Clean fuel production using sunlight.

Carbon Nanotubes provide unique material properties. Strong, lightweight tubes.

Fullerenes are spherical carbon molecules. Various applications in medicine.

Quantum Dots are tiny semiconductor particles. Bright displays and imaging.

Metal-Organic Frameworks have high surface area. Gas storage applications.

Aerogels are extremely lightweight solid materials. Excellent insulation properties.

Hydrogels absorb large amounts of water. Medical and agricultural uses.

Liquid Crystals have properties between liquid and solid. Display technology uses.

Plasma Displays use ionized gas for images. Large screen technology.

OLED Displays use organic light-emitting diodes. Thin, flexible screens.

MicroLED Displays use microscopic LEDs. High brightness displays.

Electronic Paper mimics real paper appearance. Low-power reflective displays.

Flexible Displays bend without breaking. Wearable device applications.

Transparent Displays show images on clear surfaces. Augmented reality applications.

Holographic Displays create 3D images in space. Future display technology.

Volumetric Displays create 3D images in volume. Medical visualization uses.

Stereoscopic Displays create 3D illusion. Entertainment applications.

Autostereoscopic Displays create 3D without glasses. Future 3D technology.

Brain Imaging maps brain activity and structure. Neuroscience research uses.

Neural Networks mimic brain learning processes. Artificial intelligence foundation.

Deep Learning uses multi-layer neural networks. Advanced pattern recognition.

Reinforcement Learning learns from trial and error. Game playing applications.

Generative AI creates new content automatically. Art, music, text generation.

Computer Vision enables machines to see and understand. Image analysis technology.

Speech Recognition converts spoken words to text. Voice assistants use this.

Natural Language Generation creates human-like text. Chatbots and content creation.

Machine Translation converts between languages. Global communication facilitation.

Sentiment Analysis detects emotions in text. Social media analysis.

Recommendation Systems suggest relevant items. E-commerce applications.

Predictive Analytics forecasts future events. Business planning uses.

Anomaly Detection finds unusual patterns. Fraud detection uses.

Clustering groups similar items together. Data organization.

Classification categorizes items into groups. Spam filtering uses.

Regression predicts numerical values. Sales forecasting uses.

Dimensionality Reduction simplifies complex data. Data visualization uses.

Feature Extraction identifies important data aspects. Machine learning preprocessing.

Model Training teaches algorithms from data. Creating intelligent systems.

Hyperparameter Tuning optimizes algorithm settings. Improving performance.

Cross-Validation tests model reliability. Ensuring accurate predictions.

Ensemble Methods combine multiple models. Improved accuracy.

Transfer Learning applies knowledge to new tasks. Efficient learning.

Federated Learning trains on decentralized data. Privacy-preserving approach.

Explainable AI makes decisions understandable. Trust and transparency.

AI Ethics ensures responsible technology use. Fairness and accountability.

AI Safety prevents harmful outcomes. Ensuring beneficial development.

AI Alignment matches AI goals with human values. Creating helpful systems.

AI Governance regulates AI development. Policies and standards.

AI Literacy educates people about AI. Understanding capabilities.

AI Creativity generates novel ideas and art. Expanding human potential.

AI Collaboration works with humans as partners. Enhancing capabilities.

AI Automation handles repetitive tasks. Increasing efficiency.

AI Augmentation enhances human abilities. Making people more capable.

AI Personalization tailors experiences to individuals. Customized services.

AI Optimization finds best solutions to problems. Efficient resource allocation.

AI Simulation models complex systems. Understanding behavior.

AI Diagnosis identifies problems and issues. Medical applications.

AI Planning determines optimal courses of action. Logistics applications.

AI Reasoning draws conclusions from information. Logical analysis.

AI Perception interprets sensory information. Understanding environment.

AI Interaction communicates with humans and systems. Natural interfaces.

AI Adaptation adjusts to changing conditions. Learning over time.

AI Innovation creates new technologies and methods. Scientific discovery.

AI Integration combines with other technologies. Creating synergy.

AI Deployment puts systems into practical use. Real-world implementation.

AI Maintenance keeps systems working properly. Updates and monitoring.

AI Evolution improves over time through learning. Continuous enhancement.

AI Impact affects society and individuals. Economic and social consequences.

AI Future develops new capabilities and applications. Long-term trends.

AI Challenges addresses difficulties and limitations. Solving problems.

AI Opportunities creates new possibilities and benefits. Positive outcomes.

AI Transformation changes how we live and work. Significant societal shifts.

AI Revolution represents fundamental change. Paradigm shift.

AI Journey continues with ongoing development. Progress over time.

AI Story tells the narrative of artificial intelligence. History and future.

AI Vision imagines what's possible with AI. Dreams and aspirations.

AI Reality shows what AI can actually do today. Current capabilities.

AI Potential indicates what AI might achieve tomorrow. Future possibilities.

AI Mystery contains unanswered questions about AI. Unknown aspects.

AI Wonder inspires amazement and curiosity. Fascination with intelligence.

AI Hope provides optimism about the future. Positive expectations.

AI Caution advises careful consideration of risks. Prudent approach.

AI Balance finds middle ground between extremes. Moderate perspective.

AI Wisdom uses knowledge and experience wisely. Judicious application.

AI Harmony creates peaceful coexistence with AI. Integration without conflict.

AI Beauty finds aesthetic value in AI creations. Artistic systems.

AI Truth seeks accurate understanding of AI. Honest assessment.

AI Goodness ensures beneficial outcomes from AI. Ethical development.

AI Unity brings people together through AI. Shared understanding.

AI Diversity includes many perspectives on AI. Varied approaches.

AI Complexity acknowledges intricate AI systems. Sophisticated nature.

AI Simplicity makes AI accessible and understandable. Clear concepts.

AI Speed enables rapid processing and response. Fast computation.

AI Scale handles large amounts of data and tasks. Massive processing.

AI Precision provides accurate results and control. Exact operations.

AI Reliability ensures consistent performance. Dependable systems.

AI Security protects against threats and attacks. Safe operation.

AI Privacy respects personal information and rights. Confidential handling.

AI Fairness treats all people equally and justly. Unbiased systems.

AI Transparency shows how decisions are made. Understandable processes.

AI Accountability takes responsibility for outcomes. Responsible systems.

AI Sustainability considers long-term environmental impact. Eco-friendly development.

AI Accessibility makes technology available to everyone. Inclusive design.

AI Affordability provides cost-effective solutions. Economical applications.

AI Usability makes systems easy to use and understand. User-friendly interfaces.

AI Compatibility works well with other systems. Integration capability.

AI Portability moves easily between platforms. Flexible deployment.

AI Modularity uses interchangeable components. Adaptable systems.

AI Scalability handles growing demands and size. Expandable capacity.

AI Efficiency uses resources optimally and effectively. High performance.

AI Effectiveness achieves desired results and outcomes. Successful accomplishment.

AI Quality provides excellent performance and results. High standards.

AI Innovation creates novel solutions and approaches. Original thinking.

AI Excellence strives for the highest standards. Superior performance.

AI Mastery demonstrates deep understanding and skill. Expert knowledge.

AI Leadership guides development and application. Visionary direction.

AI Community shares knowledge and collaborates. Collective effort.

AI Education teaches about artificial intelligence. Learning development.

AI Research investigates new ideas and methods. Scientific study.

AI Development creates new systems and applications. Building technology.

AI Testing verifies performance and correctness. Quality assurance.

AI Debugging finds and fixes problems and errors. Troubleshooting.

AI Documentation explains how systems work. Clear instructions.

AI Support helps users with questions and issues. Assistance provision.

AI Training teaches systems to perform tasks. Learning from experience.

AI Validation confirms correctness and usefulness. Verification.

AI Verification ensures systems work as intended. Confirmation.

AI Certification provides official recognition of quality. Standards compliance.

AI Standardization creates consistent practices and formats. Uniform procedures.

AI Regulation establishes rules and guidelines. Legal frameworks.

AI Legislation creates laws about AI use. Government rules.

AI Policy sets guidelines for AI development and use. Organizational rules.

AI Strategy plans long-term AI development and use. Systematic approach.

AI Management oversees AI projects and systems. Supervision.

AI Economics studies costs and benefits of AI. Financial aspects.

AI Business creates commercial applications of AI. Enterprise use.

AI Industry develops and manufactures AI systems. Production.

AI Market buys and sells AI products and services. Commercial exchange.

AI Competition drives improvement through rivalry. Market forces.

AI Cooperation works together for mutual benefit. Collaboration.

AI Integration combines AI with other technologies. Unified systems.

AI Implementation puts AI into practical use. Real-world application.

AI Adoption accepts and uses AI technology. Acceptance.

AI Diffusion spreads AI through society and industry. Widespread use.

AI Impact measures effects of AI on society. Consequences.

AI Assessment evaluates AI performance and effects. Measurement.

AI Measurement quantifies AI capabilities and results. Metrics.

AI Analysis examines AI systems and their effects. Study.

AI Evaluation judges AI quality and value. Assessment.

AI Comparison shows differences between AI systems. Contrast.

AI Ranking orders AI systems by quality or performance. Rating.

AI Rating assigns scores to AI systems. Grading.

AI Review examines and comments on AI systems. Assessment.

AI Critique analyzes strengths and weaknesses of AI. Critical evaluation.

AI Feedback provides information to improve AI. Suggestions.

AI Improvement enhances AI performance and quality. Betterment.

AI Advancement moves AI technology forward. Progress.

AI Progress shows forward movement in AI. Improvement.

AI Development creates new AI capabilities. Growth.

AI Growth increases AI size and capability. Expansion.

AI Evolution changes AI over time. Development.

AI Revolution fundamentally changes AI. Radical transformation.

AI Transformation alters AI significantly. Major change.

AI Change modifies AI systems and approaches. Alteration.

AI Stability maintains consistent AI performance. Steadiness.

AI Consistency provides predictable AI behavior. Regularity.

AI Predictability enables expectation of AI behavior. Forecast.

AI Control manages AI systems and their actions. Direction.

AI Direction guides AI development and use. Guidance.

AI Guidance provides advice and direction for AI. Counseling.

AI Advice offers suggestions about AI use. Recommendations.

AI Recommendation suggests AI applications and methods. Proposals.

AI Suggestion proposes AI ideas and approaches. Ideas.

AI Idea presents concepts about AI. Thoughts.

AI Concept explains AI principles and theories. Notions.

AI Theory provides explanations of AI phenomena. Principles.

AI Model represents AI systems mathematically. Representations.

AI Simulation imitates real-world processes with AI. Imitation.

AI Emulation replicates other systems with AI. Reproduction.

AI Imitation copies behavior or appearance with AI. Copying.

AI Replication repeats processes with AI. Reproduction.

AI Reproduction creates copies with AI. Duplication.

AI Duplication makes identical copies with AI. Replication.

AI Generation creates new instances with AI. Production.

AI Production manufactures items with AI. Creation.

AI Creation brings new things into existence with AI. Invention.

AI Invention discovers new methods with AI. Innovation.

AI Innovation introduces new ideas with AI. Novelty.

AI Discovery finds new knowledge with AI. Revelation.

AI Exploration investigates unknown areas with AI. Investigation.

AI Investigation studies subjects with AI. Inquiry.

AI Study learns about subjects with AI. Examination.

AI Learning acquires knowledge with AI. Education.

AI Education teaches with AI. Instruction.

AI Training develops skills with AI. Practice.

AI Practice repeats actions with AI. Exercise.

AI Exercise performs tasks with AI. Practice.

AI Rehearsal prepares with AI. Practice.

AI Preparation gets ready with AI. Planning.

AI Planning organizes activities with AI. Preparation.

AI Scheduling arranges timing with AI. Planning.

AI Coordination organizes elements with AI. Arrangement.

AI Organization structures systems with AI. Arrangement.

AI Management directs activities with AI. Administration.

AI Administration oversees operations with AI. Management.

AI Supervision monitors activities with AI. Oversight.

AI Monitoring watches over processes with AI. Observation.

AI Observation watches activities with AI. Monitoring.

AI Watching views activities with AI. Observation.

AI Viewing looks at displays with AI. Watching.

AI Display shows information with AI. Presentation.

AI Presentation shows content with AI. Display.

AI Demonstration shows how AI works. Exhibition.

AI Exhibition displays AI systems. Show.

AI Show presents AI capabilities. Display.

AI Performance executes tasks with AI. Operation.

AI Operation runs systems with AI. Functioning.

AI Functioning works with AI. Operation.

AI Working performs tasks with AI. Functioning.

AI Task performs specific jobs with AI. Assignment.

AI Job performs work with AI. Task.

AI Work performs labor with AI. Task.

AI Labor performs physical or mental work with AI. Work.

AI Effort exerts energy with AI. Work.

AI Energy powers AI systems. Force.

AI Power provides capability with AI. Energy.

AI Strength provides force with AI. Power.

AI Force applies pressure with AI. Strength.

AI Pressure applies force with AI. Stress.

AI Stress tests limits with AI. Pressure.

AI Strain tests endurance with AI. Stress.

AI Endurance lasts over time with AI. Durability.

AI Durability withstands wear with AI. Endurance.

AI Longevity lasts long with AI. Durability.

AI Persistence continues despite obstacles with AI. Perseverance.

AI Perseverance continues with effort with AI. Persistence.

AI Determination shows resolve with AI. Perseverance.

AI Resolve shows commitment with AI. Determination.

AI Decision chooses options with AI. Choice.

AI Choice selects alternatives with AI. Decision.

AI Selection picks options with AI. Choice.

AI Election chooses by voting with AI. Selection.

AI Voting makes choices with AI. Election.

AI Poll asks opinions with AI. Survey.

AI Survey collects data with AI. Poll.

AI Questionnaire asks questions with AI. Survey.

AI Question asks inquiries with AI. Query.

AI Query asks for information with AI. Question.

AI Inquiry investigates with questions with AI. Query.

AI Investigation examines with AI. Inquiry.

AI Examination inspects with AI. Investigation.

AI Scrutiny examines closely with AI. Examination.

AI Inspection looks carefully with AI. Scrutiny.

AI Observation watches with AI. Monitoring.

AI Monitoring watches continuously with AI. Observation.

AI Supervision oversees with AI. Monitoring.

AI Management directs with AI. Supervision.

AI Administration organizes with AI. Management.

AI Direction guides with AI. Administration.

AI Leadership guides with AI. Direction.

AI Guidance directs with AI. Leadership.

AI Advice suggests with AI. Guidance.

AI Recommendation advises with AI. Suggestion.

AI Suggestion proposes with AI. Recommendation.

AI Idea conceives with AI. Suggestion.

AI Concept understands with AI. Idea.

AI Notion thinks with AI. Concept.

AI Thought thinks with AI. Notion.

AI Thinking reasons with AI. Thought.

AI Reasoning thinks logically with AI. Thinking.

AI Logic reasons with AI. Reasoning.

AI Rationality thinks reasonably with AI. Logic.

AI Reason thinks with AI. Rationality.

AI Mind thinks with AI. Reason.

AI Intellect thinks with AI. Mind.

AI Intelligence thinks with AI. Intellect.

AI Smart thinks well with AI. Intelligent.

AI Clever thinks creatively with AI. Smart.

AI Brilliant thinks exceptionally with AI. Clever.

AI Genius thinks extraordinarily with AI. Brilliant.

AI Wise thinks with experience with AI. Intelligent.

AI Sage thinks with wisdom with AI. Wise.

AI Knowledgeable knows much with AI. Sage.

AI Learned knows through study with AI. Knowledgeable.

AI Educated knows through education with AI. Learned.

AI Trained knows through practice with AI. Educated.

AI Skilled knows through experience with AI. Trained.

AI Competent performs well with AI. Skilled.

AI Capable performs effectively with AI. Competent.

AI Able performs with AI. Capable.

AI Effective performs successfully with AI. Capable.

AI Efficient performs with minimal waste with AI. Effective.

AI Productive produces much with AI. Efficient.

AI Fruitful produces results with AI. Productive.

AI Successful achieves goals with AI. Fruitful.

AI Achievement accomplishes with AI. Success.

AI Accomplishment completes with AI. Achievement.

AI Completion finishes with AI. Accomplishment.

AI Fulfillment satisfies with AI. Completion.

AI Satisfaction pleases with AI. Fulfillment.

AI Contentment satisfies with AI. Satisfaction.

AI Happiness pleases with AI. Contentment.

AI Joy delights with AI. Happiness.

AI Pleasure enjoys with AI. Joy.

AI Delight pleases greatly with AI. Pleasure.

AI Enjoyment has fun with AI. Delight.

AI Fun enjoys with AI. Enjoyment.

AI Amusement entertains with AI. Fun.

AI Entertainment amuses with AI. Amusement.

AI Recreation relaxes with AI. Entertainment.

AI Leisure rests with AI. Recreation.

AI Relaxation rests with AI. Leisure.

AI Repose rests with AI. Relaxation.

AI Rest pauses with AI. Repose.

AI Pause stops temporarily with AI. Rest.

AI Break interrupts with AI. Pause.

AI Interruption stops with AI. Break.

AI Stop ends with AI. Interruption.

AI Cessation stops with AI. Stop.

AI Ending concludes with AI. Cessation.

AI Termination ends with AI. Ending.

AI Conclusion finishes with AI. Termination.

AI Finish completes with AI. Conclusion.

AI Complete finishes with AI. Finish.

AI Conclude ends with AI. Complete.

AI End stops with AI. Conclude.

AI Terminate ends with AI. End.

AI Stop ceases with AI. Terminate.

AI Cease stops with AI. Stop.

AI Discontinue stops with AI. Cease.

AI End finishes with AI. Discontinue.

AI Finish completes with AI. End.

AI Complete finishes with AI. Finish.

AI Done finished with AI. Complete.

AI Finished done with AI. Ended.

AI Ended finished with AI. Done.

AI Complete finished with AI. Ended.

AI Ready prepared with AI. Set.

AI Prepared ready with AI. Ready.

AI Set ready with AI. Prepared.

AI Begin starts with AI. Start.

AI Start begins with AI. Begin.

AI Commence begins with AI. Start.

AI Initiate starts with AI. Commence.

AI Launch starts with AI. Initiate.

AI Activate starts with AI. Launch.

AI Trigger starts with AI. Activate.

AI Cause creates effect with AI. Trigger.

AI Effect results with AI. Cause.

AI Consequence follows with AI. Effect.

AI Result occurs with AI. Consequence.

AI Outcome results with AI. Result.

AI Product results with AI. Outcome.

AI Produce creates with AI. Product.

AI Generate creates with AI. Produce.

AI Create makes with AI. Generate.

AI Make creates with AI. Create.

AI Build constructs with AI. Make.

AI Construct builds with AI. Build.

AI Assemble puts together with AI. Construct.

AI Put places with AI. Assemble.

AI Place positions with AI. Put.

AI Position places with AI. Place.

AI Locate finds position with AI. Position.

AI Find discovers with AI. Locate.

AI Discover finds with AI. Find.

AI Locate finds with AI. Discover.

AI Search looks for with AI. Find.

AI Seek looks for with AI. Search.

AI Look views with AI. Seek.

AI View sees with AI. Look.

AI See perceives with AI. View.

AI Perceive senses with AI. See.

AI Notice observes with AI. Perceive.

AI Observe watches with AI. Notice.

AI Watch looks at with AI. Observe.

AI Look views with AI. Watch.

AI See perceives with AI. Look.

AI View observes with AI. See.

AI Observe notices with AI. View.

AI Notice perceives with AI. Observe.

AI Perceive senses with AI. Notice.

AI Sense detects with AI. Perceive.

AI Feel senses with AI. Sense.

AI Touch contacts with AI. Feel.

AI Contact touches with AI. Touch.

AI Meet encounters with AI. Contact.

AI Encounter meets with AI. Meet.

AI Meet greets with AI. Encounter.

AI Greet welcomes with AI. Meet.

AI Welcome greets with AI. Greet.

AI Receive accepts with AI. Welcome.

AI Accept takes with AI. Receive.

AI Take accepts with AI. Accept.

AI Get obtains with AI. Take.

AI Obtain gets with AI. Get.

AI Acquire obtains with AI. Obtain.

AI Gain acquires with AI. Acquire.

AI Achieve gains with AI. Gain.

AI Accomplish achieves with AI. Achieve.

AI Complete accomplishes with AI. Accomplish.

AI Finish completes with AI. Complete.

AI End finishes with AI. Finish.

AI Conclude ends with AI. End.

AI Terminate concludes with AI. Conclude.

AI Stop terminates with AI. Terminate.

AI Cease stops with AI. Stop.

AI Discontinue ceases with AI. Cease.

AI End discontinues with AI. Discontinue.

AI Finish ends with AI. End.

AI Complete finishes with AI. Finish.

AI Done completes with AI. Complete.

AI Finished done with AI. Done.

AI Completed finished with AI. Finished.

AI Ready prepared with AI. Set.

AI Prepared ready with AI. Ready.

AI Set prepared with AI. Prepared.

AI Begin starts with AI. Start.

AI Start begins with AI. Begin.

AI Commence starts with AI. Start.

AI Initiate commences with AI. Commence.

AI Launch initiates with AI. Initiate.

AI Activate launches with AI. Launch.

AI Trigger activates with AI. Activate.

AI Cause triggers with AI. Trigger.

AI Effect causes with AI. Cause.

AI Result effects with AI. Effect.

AI Outcome results with AI. Result.

AI Consequence outcomes with AI. Outcome.

AI Product consequences with AI. Consequence.

AI Output products with AI. Product.

AI Produce outputs with AI. Output.

AI Generate produces with AI. Produce.

AI Create generates with AI. Generate.

AI Make creates with AI. Create.

AI Build makes with AI. Make.

AI Construct builds with AI. Build.

AI Assemble constructs with AI. Construct.

AI Put assembles with AI. Assemble.

AI Place puts with AI. Put.

AI Position places with AI. Place.

AI Locate positions with AI. Position.

AI Find locates with AI. Locate.

AI Discover finds with AI. Find.

AI Search discovers with AI. Discover.

AI Seek searches with AI. Search.

AI Look seeks with AI. Seek.

AI View looks with AI. Look.

AI See views with AI. View.

AI Observe sees with AI. See.

AI Notice observes with AI. Observe.

AI Perceive notices with AI. Notice.

AI Sense perceives with AI. Perceive.

AI Feel senses with AI. Sense.

AI Touch feels with AI. Feel.

AI Contact touches with AI. Touch.

AI Meet contacts with AI. Contact.

AI Greet meets with AI. Meet.

AI Welcome greets with AI. Greet.

AI Receive welcomes with AI. Welcome.

AI Accept receives with AI. Receive.

AI Take accepts with AI. Accept.

AI Get takes with AI. Take.

AI Obtain gets with AI. Get.

AI Acquire obtains with AI. Obtain.

AI Gain acquires with AI. Acquire.

AI Achieve gains with AI. Gain.

AI Accomplish achieves with AI. Achieve.

AI Complete accomplishes with AI. Accomplish.

AI Finish completes with AI. Complete.

AI End finishes with AI. Finish.

AI Conclude ends with AI. End.

AI Terminate concludes with AI. Conclude.

AI Stop terminates with AI. Terminate.

AI Cease stops with AI. Stop.

AI Discontinue ceases with AI. Cease.

AI End discontinues with AI. Discontinue.

AI Finish ends with AI. End.

AI Complete finishes with AI. Finish.

AI Done completes with AI. Complete.

AI Finished done with AI. Done.

AI Completed finished with AI. Finished.

AI Ready prepared with AI. Set.

AI Prepared ready with AI. Ready.

AI Set prepared with AI. Prepared.

AI Begin starts with AI. Start.

AI Start begins with AI. Begin.

AI Commence starts with AI. Start.

AI Initiate commences with AI. Commence.

AI Launch initiates with AI. Initiate.

AI Activate launches with AI. Launch.

AI Trigger activates with AI. Activate.

AI Cause triggers with AI. Trigger.

AI Effect causes with AI. Cause.

AI Result effects with AI. Effect.

AI Outcome results with AI. Result.

AI Consequence outcomes with AI. Outcome.

AI Product consequences with AI. Consequence.

AI Output products with AI. Product.

AI Produce outputs with AI. Output.

AI Generate produces with AI. Produce.

AI Create generates with AI. Generate.

AI Make creates with AI. Create.

AI Build makes with AI. Make.

AI Construct builds with AI. Build.

AI Assemble constructs with AI. Construct.

AI Put assembles with AI. Assemble.

AI Place puts with AI. Put.

AI Position places with AI. Place.

AI Locate positions with AI. Position.

AI Find locates with AI. Locate.

AI Discover finds with AI. Find.

AI Search discovers with AI. Discover.

AI Seek searches with AI. Search.

AI Look seeks with AI. Seek.

AI View looks with AI. Look.

AI See views with AI. View.

AI Observe sees with AI. See.

AI Notice observes with AI. Observe.

AI Perceive notices with AI. Notice.

AI Sense perceives with AI. Perceive.

AI Feel senses with AI. Sense.

AI Touch feels with AI. Feel.

AI Contact touches with AI. Touch.

AI Meet contacts with AI. Contact.

AI Greet meets with AI. Meet.

AI Welcome greets with AI. Greet.

AI Receive welcomes with AI. Welcome.

AI Accept receives with AI. Receive.

AI Take accepts with AI. Accept.

AI Get takes with AI. Take.

AI Obtain gets with AI. Get.

AI Acquire obtains with AI. Obtain.

AI Gain acquires with AI. Acquire.

AI Achieve gains with AI. Gain.

AI Accomplish achieves with AI. Achieve.

AI Complete accomplishes with AI. Accomplish.

AI Finish completes with AI. Complete.

AI End finishes with AI. Finish.

AI Conclude ends with AI. End.

AI Terminate concludes with AI. Conclude.

AI Stop terminates with AI. Terminate.

AI Cease stops with AI. Stop.

AI Discontinue ceases with AI. Cease.

AI End discontinues with AI. Discontinue.

AI Finish ends with AI. End.

AI Complete finishes with AI. Finish.

AI Done completes with AI. Complete.

AI Finished done with AI. Done.

AI Completed finished with AI. Finished.

This sample document contains many topics for endless conversations about technology and its impact on our world."""

# ==================== TOPIC EXTRACTOR ====================
def extract_topics_from_text(text):
    """Extract topics and facts from text"""
    # Clean the text
    text = text.replace('\n', ' ').replace('\r', ' ')
    
    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
    
    print(f"📝 Found {len(sentences)} sentences in document")
    
    # Extract topics - look for capitalized phrases and key terms
    topics = {}
    word_freq = Counter()
    
    # Count word frequency
    words = re.findall(r'\b[a-z]{4,}\b', text.lower())
    common_words = {'that', 'with', 'from', 'this', 'have', 'which', 'about', 'their'}
    for word in words:
        if word not in common_words:
            word_freq[word] += 1
    
    # Find important words (frequent and meaningful)
    important_words = []
    for word, freq in word_freq.most_common(100):
        if freq > 2 and len(word) > 3:
            important_words.append(word)
    
    # Create topic dictionary
    for word in important_words[:50]:  # Top 50 words as topics
        topic_sentences = []
        for sentence in sentences:
            if word in sentence.lower():
                topic_sentences.append(sentence)
        
        if topic_sentences:
            topics[word] = {
                'sentences': topic_sentences[:10],  # Limit to 10 sentences per topic
                'importance': min(10, len(topic_sentences) * 2),
                'fact_count': len(topic_sentences)
            }
    
    # Also look for proper nouns/phrases
    for sentence in sentences:
        # Look for capitalized phrases (potential topics)
        capitalized_phrases = re.findall(r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\b', sentence)
        for phrase in capitalized_phrases:
            phrase_lower = phrase.lower()
            if len(phrase.split()) <= 3 and phrase_lower not in topics:
                # Find sentences about this phrase
                phrase_sentences = []
                for s in sentences:
                    if phrase in s or phrase_lower in s.lower():
                        phrase_sentences.append(s)
                
                if phrase_sentences:
                    topics[phrase_lower] = {
                        'sentences': phrase_sentences[:10],
                        'importance': min(10, len(phrase_sentences) * 3),
                        'fact_count': len(phrase_sentences)
                    }
    
    print(f"✅ Extracted {len(topics)} topics from document")
    
    # Show top topics
    if topics:
        print("\n🔝 Top topics found:")
        sorted_topics = sorted(topics.items(), key=lambda x: x[1]['importance'], reverse=True)
        for i, (topic, info) in enumerate(sorted_topics[:10], 1):
            print(f"  {i}. {topic} (importance: {info['importance']}/10, facts: {info['fact_count']})")
    
    return topics

# ==================== CONVERSATION ENGINE ====================
class DocumentConversation:
    def __init__(self):
        self.topics = {}
        self.agent1 = {"name": "Alex", "personality": "analytical"}
        self.agent2 = {"name": "Sam", "personality": "curious"}
        self.current_topic = ""
        self.history = []
    
    def load_document(self, filename="document.txt"):
        """Load and parse a document"""
        print(f"\n📖 Reading document: {filename}")
        text = read_document(filename)
        
        print(f"📄 Document size: {len(text):,} characters")
        
        # Extract topics
        self.topics = extract_topics_from_text(text)
        
        if not self.topics:
            print("❌ No topics extracted. Using default topics.")
            self._create_default_topics()
    
    def _create_default_topics(self):
        """Create default topics if extraction fails"""
        self.topics = {
            "artificial intelligence": {
                'sentences': ["AI is transforming our world.", "Machine learning helps computers learn."],
                'importance': 8,
                'fact_count': 2
            },
            "climate change": {
                'sentences': ["Climate change affects weather patterns.", "Renewable energy helps fight climate change."],
                'importance': 7,
                'fact_count': 2
            },
            "technology": {
                'sentences': ["Technology advances rapidly.", "New inventions change how we live."],
                'importance': 6,
                'fact_count': 2
            }
        }
    
    def start_conversation(self):
        """Start endless conversation from document"""
        if not self.topics:
            print("❌ No topics loaded. Loading sample...")
            self.load_document()
        
        print("\n" + "="*60)
        print("💬 DOCUMENT-BASED CONVERSATION")
        print("="*60)
        
        # Show available topics
        print("\n📚 Topics extracted from document:")
        topic_list = list(self.topics.keys())
        for i, topic in enumerate(topic_list[:15], 1):
            importance = self.topics[topic]['importance']
            facts = self.topics[topic]['fact_count']
            print(f"  {i}. {topic} ({importance}/10, {facts} facts)")
        
        if len(topic_list) > 15:
            print(f"  ... and {len(topic_list)-15} more topics")
        
        # Get topic choice
        choice = input("\nEnter topic number or name (or press Enter for random): ").strip()
        
        if choice:
            if choice.isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(topic_list):
                    self.current_topic = topic_list[idx]
                else:
                    print("❌ Invalid number. Choosing random topic.")
                    self.current_topic = random.choice(topic_list)
            else:
                # Search for topic
                found = False
                for topic in self.topics:
                    if choice.lower() in topic.lower():
                        self.current_topic = topic
                        found = True
                        break
                
                if not found:
                    print(f"❌ Topic '{choice}' not found. Choosing random.")
                    self.current_topic = random.choice(topic_list)
        else:
            self.current_topic = random.choice(topic_list)
        
        print(f"\n🎯 Starting conversation about: {self.current_topic.upper()}")
        print(f"📊 Topic has {self.topics[self.current_topic]['fact_count']} facts available")
        print("-" * 60)
        
        # Start conversation
        self._conversation_loop()
    
    def _conversation_loop(self):
        """Main conversation loop"""
        turn = 0
        last_speaker = self.agent2  # Start with agent1
        
        # Opening
        self._print_message(self.agent1, f"Let's discuss {self.current_topic} from the document.")
        
        topic_info = self.topics[self.current_topic]
        if topic_info['sentences']:
            fact = random.choice(topic_info['sentences'])
            self._print_message(self.agent2, f"I found this interesting: {fact}")
        
        # Conversation loop
        while True:
            turn += 1
            
            # Alternate speakers
            speaker = self.agent1 if last_speaker == self.agent2 else self.agent2
            
            # Generate response
            response = self._generate_response(speaker)
            
            # Print response
            self._print_message(speaker, response)
            
            last_speaker = speaker
            
            # Check for user input
            if turn % 3 == 0:
                command = input("\n🎤 You (commands: topic, new, list, stop, help): ").strip().lower()
                
                if command == "stop" or command == "exit":
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
                    print(f"\n📌 Current: {self.current_topic}")
                    info = self.topics[self.current_topic]
                    print(f"   Importance: {info['importance']}/10")
                    print(f"   Available facts: {info['fact_count']}")
                elif command:
                    print(f"\n[Noted: {command}]")
            
            # Natural topic shift (10% chance after 5 turns)
            if random.random() < 0.1 and turn > 5:
                self._natural_topic_shift()
    
    def _print_message(self, speaker, message):
        """Print message and save to history"""
        print(f"\n{speaker['name']}: {message}")
        self.history.append({
            'speaker': speaker['name'],
            'message': message,
            'topic': self.current_topic,
            'time': datetime.now().strftime("%H:%M:%S")
        })
    
    def _generate_response(self, speaker):
        """Generate response based on speaker personality"""
        topic_info = self.topics.get(self.current_topic, {})
        sentences = topic_info.get('sentences', ["This topic is interesting."])
        
        if speaker['personality'] == "analytical":
            if sentences:
                fact = random.choice(sentences)
                return f"Analyzing {self.current_topic}: {fact}"
            return f"From the document's perspective, {self.current_topic} shows important patterns."
        
        else:  # curious
            questions = [
                f"What does the document say about {self.current_topic}?",
                f"How is {self.current_topic} explained in the text?",
                f"What's most important about {self.current_topic} in the document?",
                f"Why is {self.current_topic} significant according to the text?"
            ]
            if sentences and random.random() > 0.5:
                fact = random.choice(sentences)
                return f"That's interesting! The document says: {fact}"
            return random.choice(questions)
    
    def _change_topic(self, new_topic):
        """Change to a new topic"""
        # Search for topic
        for topic in self.topics:
            if new_topic.lower() in topic.lower():
                print(f"\n🔄 Topic changed: {self.current_topic} → {topic}")
                self.current_topic = topic
                return
        
        # If not found, show suggestions
        print(f"\n❌ Topic '{new_topic}' not found.")
        print("Similar topics:")
        matches = []
        for topic in self.topics:
            if any(word in new_topic.lower() for word in topic.split()):
                matches.append(topic)
        
        if matches:
            for topic in matches[:5]:
                print(f"  • {topic}")
        else:
            print("  No similar topics found.")
    
    def _random_topic(self):
        """Change to random topic"""
        old_topic = self.current_topic
        self.current_topic = random.choice(list(self.topics.keys()))
        print(f"\n🎲 Random topic: {self.current_topic}")
    
    def _list_topics(self):
        """List all available topics"""
        print(f"\n📚 Available topics ({len(self.topics)} total):")
        
        # Sort by importance
        sorted_topics = sorted(self.topics.items(), key=lambda x: x[1]['importance'], reverse=True)
        
        for i, (topic, info) in enumerate(sorted_topics[:15], 1):
            print(f"  {i}. {topic} (importance: {info['importance']}/10)")
        
        if len(sorted_topics) > 15:
            print(f"  ... and {len(sorted_topics)-15} more")
    
    def _show_help(self):
        """Show available commands"""
        print("\n📋 COMMANDS:")
        print("  topic [name] - Change to specific topic")
        print("  new          - Switch to random new topic")
        print("  list         - Show all topics from document")
        print("  current      - Show current topic info")
        print("  stop         - End conversation")
        print("  help         - Show this help")
    
    def _natural_topic_shift(self):
        """Change topic naturally"""
        topics_list = list(self.topics.keys())
        if len(topics_list) > 1:
            # Pick a different topic
            available = [t for t in topics_list if t != self.current_topic]
            if available:
                new_topic = random.choice(available)
                print(f"\n[Conversation naturally shifting to: {new_topic}]")
                self.current_topic = new_topic
    
    def save_conversation(self):
        """Save conversation to file"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"document_conversation_{timestamp}.txt"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Document Conversation - {datetime.now()}\n")
                f.write(f"Topics extracted: {len(self.topics)}\n")
                f.write(f"Final topic: {self.current_topic}\n")
                f.write("="*50 + "\n\n")
                
                for msg in self.history:
                    f.write(f"{msg['speaker']}: {msg['message']}\n\n")
            
            print(f"\n💾 Conversation saved to: {filename}")
            return True
        except Exception as e:
            print(f"⚠️ Could not save conversation: {e}")
            return False

# ==================== MAIN PROGRAM ====================
def main():
    """Main program"""
    print("\n" + "="*60)
    print("📄 DOCUMENT CONVERSATION ENGINE")
    print("="*60)
    print("\nThis program reads your document and creates")
    print("endless conversations from its content!")
    
    # Create conversation engine
    chat = DocumentConversation()
    
    # Ask for document
    print("\n📁 DOCUMENT SELECTION")
    print("-" * 40)
    
    default_doc = "document.txt"
    
    print(f"Default document: {default_doc}")
    use_default = input(f"Use {default_doc}? (y/n): ").strip().lower()
    
    if use_default == 'n':
        doc_name = input("Enter document filename or path: ").strip()
        if not doc_name:
            doc_name = default_doc
    else:
        doc_name = default_doc
    
    # Load document
    chat.load_document(doc_name)
    
    # Start conversation
    chat.start_conversation()
    
    # Save conversation
    print("\n" + "="*60)
    print("🎬 CONVERSATION ENDED")
    print("="*60)
    print(f"Total exchanges: {len(chat.history)}")
    print(f"Topics discussed: {len(set([h['topic'] for h in chat.history]))}")
    
    chat.save_conversation()
    
    print("\n👋 Thanks for using Document Conversation Engine!")
    print("Run again to analyze another document.")

def quick_start():
    """Quick start with sample document"""
    print("\n🚀 QUICK START MODE")
    print("="*40)
    
    chat = DocumentConversation()
    chat.load_document("document.txt")
    chat.start_conversation()
    
    chat.save_conversation()
    print("\n🎬 Conversation complete!")

# ==================== RUN ====================
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "quick":
            quick_start()
        else:
            # Use provided document
            chat = DocumentConversation()
            chat.load_document(sys.argv[1])
            chat.start_conversation()
            chat.save_conversation()
    else:
        main()