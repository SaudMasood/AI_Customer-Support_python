
<div align="center">

# 🤖 AI Customer Support Assistant

### AI-Powered Customer Message Analyzer

<p>
  <img src="https://img.shields.io/badge/Python-3.13+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/Google%20Gemini-AI-orange?style=for-the-badge&logo=google" />
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" />
</p>

<p>
  An AI-powered customer support system that automatically analyzes
  customer messages, identifies their category and sentiment,
  and generates a professional auto-reply.
</p>

</div>

---

## ✨ Features

- 🤖 AI-powered customer message analysis
- 📂 Automatic message categorization
- 😊 Sentiment detection
- 💬 Professional automatic replies
- 🧪 Built-in test messages
- ✍️ Custom customer message input
- ⚡ Fast AI processing
- 🖥️ Simple Streamlit interface
- 🔐 API key stored securely using `.env`

---

## 🧠 AI Processing

The system takes a customer message and processes it through the following pipeline:

```text
Customer Message
       │
       ▼
┌─────────────────────┐
│   Streamlit UI      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Gemini AI        │
│      Analysis        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────┐
│ Category + Sentiment +      │
│ Professional Auto Reply     │
└─────────────────────────────┘
````

---

## 📂 Supported Categories

The AI classifies messages into one of these categories:

| Category                    | Example                          |
| --------------------------- | -------------------------------- |
| 📢 Complaint                | Damaged or poor-quality product  |
| 🔄 Refund/Return            | Customer wants to return an item |
| 🛒 Sales Inquiry            | Product availability or pricing  |
| 🚚 Delivery Question        | Delayed or missing package       |
| 🛠️ Account/Technical Issue | Login or application problem     |
| 💬 General Query            | General customer question        |
| 🚨 Spam                     | Suspicious promotional messages  |

---

## 😊 Sentiment Detection

The system identifies:

* 🟢 **Positive**
* 🔵 **Neutral**
* 🔴 **Negative**

---

## 💬 Auto Reply Generation

After analyzing the message, Gemini generates a short and professional customer-support response.

### Example

**Customer Message**

> My package was supposed to arrive three days ago and I still haven't received it.

**AI Analysis**

```text
Category: Delivery Question
Sentiment: Negative
```

**Auto Reply**

> We apologize for the delay. Our team will check your delivery status and provide an update shortly.

---

## 🖥️ Application

The application provides a simple interface where users can:

1. Select a predefined test message
2. Enter a custom customer message
3. Click **Analyze Message**
4. Wait for AI processing
5. View the category
6. View the sentiment
7. View the generated auto-reply

---

## 🛠️ Tech Stack

| Technology          | Purpose                 |
| ------------------- | ----------------------- |
| 🐍 Python           | Application development |
| 🎈 Streamlit        | Web interface           |
| 🤖 Google Gemini    | AI message analysis     |
| 📦 Google GenAI SDK | Gemini API integration  |
| 🔐 python-dotenv    | Environment variables   |
| 📄 JSON             | Test message data       |

---

## 📁 Project Structure

```text
AI-Customer-Support/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── data/
│   └── test_messages.json
│
└── services/
    ├── __init__.py
    └── gemini_service.py
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/SaudMasood/AI_Customer-Support_python.git
```

### 2. Open the project

```bash
cd AI_Customer-Support_python
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Never upload your `.env` file or API key to GitHub.

---

## ▶️ Run the Application

```bash
python -m streamlit run app.py
```

The application will open at:

```text
http://localhost:8501
```

---

## 🧪 Test Messages

The project includes predefined messages for testing:

```text
Delivery Question
Refund/Return
Sales Inquiry
Account/Technical Issue
Complaint
Positive Feedback
General Query
Spam
```

You can also enter your own customer message.

---

## 🔄 Workflow

```text
        👤 Customer
             │
             ▼
     💬 Customer Message
             │
             ▼
      🖥️ Streamlit App
             │
             ▼
        🤖 Gemini AI
             │
      ┌──────┼──────┐
      ▼      ▼      ▼
   📂 Category 😊 Sentiment 💬 Reply
      │      │      │
      └──────┼──────┘
             ▼
       📊 Final Result
```

---

## 🎯 Project Objective

The objective of this project is to demonstrate how a modern Generative AI model can be integrated into a customer-support workflow to automatically:

* Understand customer messages
* Categorize support requests
* Detect customer sentiment
* Generate professional responses

This reduces repetitive manual work and provides a simple foundation for an AI-assisted customer support system.

---

## 🚀 Future Improvements

Possible future enhancements include:

* 📊 Analytics dashboard
* 💾 Database integration
* 📧 Email integration
* 🎫 Automatic support ticket creation
* 👥 Multi-user support
* 📈 Customer sentiment analytics
* 🌐 Deployment to cloud hosting
* 🔔 Real-time notifications

---

## 👨‍💻 Developer

<div align="center">

### Saud Masood

**BS Computer Science Student | AI/ML & Flutter Developer**

Built as part of an **AI Engineering Internship Task**.

</div>

---

## ⭐ If You Like This Project

Give the repository a ⭐ on GitHub!

<div align="center">

**🤖 AI + 💬 Customer Support + 🐍 Python**

</div>
