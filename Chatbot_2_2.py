from nltk.chat.util import Chat, reflections
from datetime import datetime

# Updated response pairs specific to the coaching institute chatbot
pairs = [
    # Greeting and Introduction
    [
        r"(hi, i am (.*)|hi i am (.*)|my name is (.*)|hlo i am (.*)|hi,i m (.*)|hi i m (.*)|hlo i m (.*)|hlo, my name is (.*)|hi, my name is (.*))",
        ["Hello %1! Welcome to our Coaching Institute. How can I assist you today?"]
    ],
    [
        r"hi|hello|whats up|hi dear|hlo",
        ["Hello! How can I help you today?"]
    ],
    [
        r"namaste|namaskar|good morning",
        ["Namaste! How may I assist you?"]
    ],
    
    # Asking about courses
    [
        r"(.*)(course|courses|programs|program)(.*)",
        ["We offer various courses like Mathematics, Science, English, and Computer Science. Would you like more details about a specific course?"]
    ],
    [
        r"(.*)(batch|batches)(.*)",
        ["We have different batches for different courses. Which course are you interested in? We have Academic batches and also Competitive batches."]
    ],

    # Asking about fees
    [
        r"(.*)(fee|fees|tuition|cost)(.*)",
        ["The fee structure varies depending on the course. Can you specify the course you are interested in?"]
    ],
    
    # Asking about schedule
    [
        r"(.*)(schedule|timing|class hours|timings)(.*)",
        ["Our classes are scheduled both in the morning and evening. For specific course timings, please mention the course name."]
    ],
    
    # Thank you
    [
        r"thank you|thanku|thanx|thx|thank you very much|thankyou|thanks",
        ["You're welcome! Happy to help."]
    ],
    
    # Inquiry about services
    [
        r"(i have a)(query|problem|question|issue)(.*)",
        ["Please feel free to ask your question! I'm here to help."]
    ],
    
    # Asking about chatbot's well-being
    [
        r"how are you",
        ["I am just a chatbot, but I'm functioning well! How can I assist you today?"]
    ],

    # User is feeling well
    [
        r"i am good|i'm good|i am fine|i'm fine|i feel good|i am doing well",
        ["That's great to hear! How can I assist you today?"]
    ],
    
    # Asking for contact details or support
    [
        r"(.*)(contact|support|help|contact info)(.*)",
        ["You can reach out to us at our support email: vidhyaclassesbijnor183@gmail.com or call us at +91 8057509745, +91 9058113227."]
    ],

    # User ends the conversation
    [
        r"bye|goodbye|see you|exit",
        ["Goodbye! Feel free to reach out anytime. Have a great day!"]
    ],

    [
        r"canyou gave me details of coaching|coaching details|details about your coaching|give me the details of vidhya classes",
        ["Our coaching classes are conducted by experienced teachers. We provide coaching for classes 6th to 12th and also provide Competitive batches like UP police, Railways, UPTET, NEET, SSC and more."]
    ],
    [
        r"(.*)(co-founder|founder|co-founders|founders)(.*)",
        ["Our co-founders are Mr. Pavitr Arya and Mr. Deepanshu Jain."]
    ],
    [
        r"(.*)(details|detail|about)(this coaching|vidhya classes|this institute)(.*)",
        ["Vidhya Classes is a premier coaching institute dedicated to empowering students with the knowledge, skills and guidance needed to achieve academic and career excellence. Founded on the principles of quality education and holistic development, we strive to shape future leaders and innovators."]
    ],
    [
        r"(.*)(address|add|location)(.*)",
        ["The address of vidhya classes is 'Near Jain Temple, Moh. Brhamanan, Bijnor, Dist. Bijnor, U.P., India'."]
    ],
    [
        r"What is Vidhya Classes|about vidhya classes| about this coaching|about this institute",
        ["Vidhya Classes is a coaching institute that provides quality education to students."]
    ],
    [
        r"What is Vidhya Classes motto",
        ["Our motto is 'Guiding You to Greatness'."]
    ],
    [
        r"What is Vidhya Classes vision",
        ["Our vision is to provide quality education to students and help them achieve their goals."]
    ],
    [
        r"What is Vidhya Classes mission",
        ["Our mission is 'To empower students with knowledge and skills that lead to academic and personal excellence, fostering leaders for a brighter tomorrow'."]
    ],
    [
        r"How can I enroll in a course",
        ["You can visit our center or register online through our Application."]
    ]
]

def chatbot_response(user_input):
    chat = Chat(pairs, reflections)
    return chat.respond(user_input)

def greeting_based_on_time():
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good Morning! How can I assist you today?"
    elif 12 <= current_hour < 18:
        return "Good Afternoon! How can I assist you today?"
    else:
        return "Good Evening! How can I assist you today?"

if __name__ == "__main__":
    print("Hi, I am the Vidhya Classes Coaching Institute Chatbot.")
    print(greeting_based_on_time())  # Initial greeting based on the time
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)
        if response in ["Goodbye! Feel free to reach out anytime. Have a great day!"]:
            break