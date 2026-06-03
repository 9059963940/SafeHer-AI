🚨 SafeHer AI – AI-Powered Women Safety Assistant

Overview:

SafeHer AI is an AI-powered women safety platform designed to provide quick assistance during emergency situations. The application combines artificial intelligence, location services, and emergency response features to enhance personal safety and support.

Built as part of the Build-A-Thon, SafeHer AI aims to create a safer environment by enabling instant SOS alerts, AI-based distress detection, live location tracking, and nearby help center discovery.

Problem Statement

Women often face safety concerns while traveling alone, especially during late hours or in unfamiliar locations. In emergency situations:

* Immediate access to help may not be available.
* Emergency contacts may not know the user's location.
* Panic situations make communication difficult.
* Finding nearby hospitals or police stations can be challenging.

SafeHer AI addresses these challenges through intelligent assistance and rapid response features.


Proposed Solution

SafeHer AI provides:
🚨 One-Tap Emergency SOS
🤖 AI-Based Distress Detection
📍 Live Location Tracking
🏥 Nearby Hospitals Finder
👮 Nearby Police Station Finder
📊 Safety Monitoring Dashboard
⚡ Real-Time Emergency Assistance

✨ Features
🚨 Emergency SOS Alert
Users can instantly trigger an emergency alert through a dedicated SOS button.

🤖 AI Distress Detection
Natural Language Processing (NLP) is used to analyze user messages and identify potential distress situations.
Examples:

| Input Message           | Result          |
| ----------------------- | --------------- |
| Help me                 | HIGH RISK ALERT |
| Someone is following me | HIGH RISK ALERT |
| Good morning            | SAFE            |
| Thank you               | SAFE            |

📍 Live Location Sharing
Uses browser geolocation APIs to capture and display the user's current coordinates.

🏥 Nearby Help Centers
Finds nearby:
* Hospitals
* Police Stations
* Emergency Services
using OpenStreetMap and Overpass APIs.

📊 Safety Dashboard
Provides a centralized interface for:
* Emergency Actions
* AI Risk Detection
* Location Tracking
* Safety Information

🏗️ System Architecture
User
  │
  ▼
Frontend (HTML, CSS, Bootstrap, JavaScript)
  │
  ▼
Flask Backend
  │
  ├── AI Distress Detection Model
  │
  ├── Location Services
  │
  └── Nearby Help Center Finder
  │
  ▼
Response Dashboard


🛠️ Technology Stack
Frontend
* HTML5
* CSS3
* Bootstrap 5
* JavaScript

Backend
* Python
* Flask

Machine Learning
* Scikit-Learn
* CountVectorizer
* Multinomial Naive Bayes

Database
* SQLite (Future Scope)

APIs
* Browser Geolocation API
* OpenStreetMap API
* Overpass API

Deployment
* GitHub


📂 Project Structure
SafeHer-AI
│
├── static
│   ├── css
│   │   └── style.css
│   │
│   └── js
│       └── app.js
│
├── templates
│   ├── index.html
│   └── dashboard.html
│
├── models
│   └── distress_model.pkl
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md

⚙️ Installation & Setup
Clone Repository
git clone https://github.com/9059963940/SafeHer-AI.git

Move into Project Directory
cd SafeHer-AI

Create Virtual Environment
python3 -m venv venv

Activate Virtual Environment
Mac:
source venv/bin/activate

Install Dependencies
pip install -r requirements.txt

Train AI Model
python train_model.py

Run Application
python app.py

Open Browser
http://127.0.0.1:5000

🧠 AI Model Details
The distress detection model is trained using:
* CountVectorizer
* Multinomial Naive Bayes Classifier

Workflow:
1. User enters a message.
2. Text is converted into numerical vectors.
3. AI model analyzes the message.
4. Risk level is predicted.
5. Alert is displayed.

🚀 Future Enhancements

* Real-time SMS Alerts
* WhatsApp Emergency Notifications
* Voice-Based Distress Detection
* Safe Route Recommendation System
* Crime Zone Prediction using AI
* Mobile Application (Android/iOS)
* Emergency Contact Management
* Real-Time Map Integration
* Multi-Language Support
* AI Chat Safety Assistant

🌍 Social Impact
SafeHer AI contributes towards:
* Women Safety
* Community Support
* Faster Emergency Response
* Digital Empowerment
* Public Safety Awareness

👩‍💻 Developed By
Seelam Deepika
Build-A-Thon Project Submission

📜 License
This project is developed for educational, research, and hackathon purposes.


PDF Link:
https://canva.link/2bcel09rhi50ezr

Demo Video:
https://drive.google.com/file/d/1Bx3nVGth8_M1kW1IJrydkBJzSZbkjDAj/view?usp=sharing
