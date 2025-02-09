questions=[
    {
        "prombt":"What does AI stand for?",
        "options":["A)utomated Interface",
                   "B) Artificial Intelligence",
                   "C)Advanced Innovation",
                   "D)Automated Intelligence"],
        "answer":"A"
    },
    {
         "prombt":" Which of the following is an example of Narrow AI?",
         "options":["A)A robot that can perform any human task",
                    "B)A self-driving car",
                    "C)A machine that can think and feel emotions",
                    "D)A superintelligent AI that surpasses human capabilities"],
          "answer":"B"
    },
    {
        "prombt":" What is the primary goal of AI?",
         "options":["A)To replace all human workers",
                    "B)To simulate human intelligence in machines",
                    "C)To build faster computers",
                    "D)To create video games"],
          "answer":"B"
    },
    {
         "prombt":"Which of the following is a subset of AI focused on learning from data?",
        "options":["A)Deep Learning",
                   "B)Robotics",
                   "C)Machine Learning",
                   "D)Virtual Reality"],
        "answer":"C"
         
    },
    {
        "prombt":" Which of the following is an application of AI in healthcare?",
        "options":["A)Self-driving cars",
                   "B)Fraud detection in banking",
                   "C)Disease diagnosis and treatment planning",
                   "D)Social media management"],
        "answer":"C"  
    },
    {
          "prombt":"  What is the vanishing gradient problem in deep learning?",
        "options":["A)When gradients grow exponentially large during backpropagation",
                   "B)When gradients become too small, ",
                   "C)When the model overfits to the training data",
                   "D)When there is not enough data to train the model"],
        "answer":"B" 
    },
    {
          "prombt":" What is Transfer Learning in AI?",
        "options":["A)Learning how to transfer data from one model to another",
                   "B)Using a pre-trained model on a new",
                   "C)Moving AI models from cloud to local devices",
                   "D)Sharing datasets between machine learning modelsa"],
        "answer":"B"
         
    },
    {
         "prombt":" What is the primary goal of unsupervised learning?",
        "options":["A)To predict a label or outcome from input data",
                   "B)To minimize error in labeled datasets",
                   "C)To identify hidden patterns or structures in unlabeled data",
                   "D)To optimize a reward function over time"],
        "answer":"C"
         
    },
    {
          "prombt":" Which regularization technique helps prevent overfitting by randomly dropping units during training?",
        "options":["A)L2 Regularization",
                   "B)Early Stopping",
                   "C)Dropout",
                   "D)Data Augmentation"],
        "answer":"C"
    },
    { 
         "prombt":" In which scenario would you use a Convolutional Neural Network (CNN)?",
        "options":["A)Predicting stock prices",
                   "B)Recognizing objects in images",
                   "C)Translating languages in real time",
                   "D)Sorting numerical data"],
        "answer":"B"   
    }
    ]
def run_quiz(questions):
        score=0
        print("="*50)
        print("🎓 Welcome to the AI Quiz! 🎓")
        print("="*50)
        print("\nLet's get started!\n")
        for question in questions:
            print (question["prombt"])
            for option in question["options"]:
                print(option)
            answer =input("enter your answer(A,B,C or D): ").upper()
            while answer not in ['A', 'B', 'C', 'D']:
               answer = input("Invalid choice. Please enter A, B, C, or D: ").upper()
            if answer==question["answer"]:
                print("✅ Correct! Well done!\n")
                score+=1
            else:
                print("❌ Oops! The correct answer was",question["answer"],"\n")
                
        print("-" * 50)
        print("\n🎉 Quiz Complete! 🎉")
        print(f"Your final score: {score} out of {len(questions)}")
        if score == len(questions):
          print("🏆 Perfect Score! You're an AI genius! 🤖")
        elif score > len(questions) // 2:
          print("👏 Great job! You have a good understanding of AI!")
        else:
          print("👍 Keep learning! You're on the right track!")
        print(f"you got {score} out of {len(questions)}questions correct.\n")
            
                
run_quiz(questions)