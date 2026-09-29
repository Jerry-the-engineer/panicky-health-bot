import random

class DramaticHealthAI:
    """An AI that dramatically overreacts to every minor symptom"""
    
    def __init__(self):
        self.panic_responses = [
            "😱 OH NO! That's a classic sign of... everything!",
            "🚨 ALERT! ALERT! This is definitely serious!",
            "💀 That symptom... I've only seen it in medical textbooks!",
            "🏥 Have you considered calling 911? Just in case?",
            "📺 I saw this on a medical drama once. It didn't end well.",
            "🤒 This is it. This is THE symptom. I'm certain of it!",
            "😰 I'm 99.9% sure you need to see a doctor. Immediately.",
            "⚠️ That's not normal! Well, it probably is, but what if it's NOT?",
            "🔍 I'm detecting signs of... possibly... maybe... definitely something!",
            "😵 I need to sit down. YOU need to sit down. Actually, lie down.",
        ]
        
        self.dramatic_diagnoses = [
            "rare tropical disease",
            "a condition I just made up that sounds scary",
            "something that only affects 3 people on Earth",
            "the exact thing that was on WebMD at 3 AM",
            "a side effect of a side effect",
            "cosmic radiation exposure",
            "advanced aging (you're getting old!)",
            "the common cold on steroids",
            "literally anything in a medical textbook",
            "that thing your friend's cousin had once",
        ]
        
        self.dramatic_actions = [
            "Call your doctor NOW",
            "Get a second opinion (then a third, fourth, and fifth)",
            "Go to the ER immediately",
            "Research on WebMD for 6 hours",
            "Tell your family you love them",
            "Update your will",
            "Learn the symptoms backwards and forwards",
            "Check yourself into the hospital preemptively",
            "Quarantine yourself from society",
            "Google 'is [symptom] fatal' at 2 AM",
        ]
    
    def freak_out(self, symptom):
        """Main function to dramatically overreact to symptoms"""
        print(f"\n🚨 YOU SAID: '{symptom}' 🚨\n")
        
        # Pick random dramatic response
        response = random.choice(self.panic_responses)
        print(response)
        print()
        
        # Suggest a diagnosis
        diagnosis = random.choice(self.dramatic_diagnoses)
        print(f"I'm almost certain you have: {diagnosis}")
        print()
        
        # Suggest an action
        action = random.choice(self.dramatic_actions)
        print(f"IMMEDIATE ACTION: {action}")
        print()
        
        # Add extra panic
        extra_panic = [
            "Time is running out!",
            "Every second counts!",
            "I'm genuinely worried now.",
            "You should probably tell someone.",
            "This is serious business.",
            "No, seriously, this is bad.",
            "I can't even...",
            "My circuits are overheating from panic!",
            "I've never been more concerned in my AI life.",
            "Please don't say you have another symptom...",
        ]
        print(f"⚠️ {random.choice(extra_panic)}\n")

def main():
    """Interactive health panic simulator"""
    ai = DramaticHealthAI()
    
    print("=" * 60)
    print("🏥 WELCOME TO DRAMATIC HEALTH AI 🏥")
    print("=" * 60)
    print("Tell me about your symptoms and watch me lose my mind!")
    print("(Type 'quit' to escape this nightmare)\n")
    
    while True:
        symptom = input("What symptom do you have? > ").strip()
        
        if symptom.lower() in ['quit', 'exit', 'no', 'stop']:
            print("\n😱 You're leaving?! Without consulting me more?!")
            print("Stay safe out there! Maybe take some vitamins...")
            break
        
        if symptom:
            ai.freak_out(symptom)
        else:
            print("You didn't tell me anything. But I'm still worried about you.\n")

if __name__ == "__main__":
    main()
