# 🎓 Enterprise Resource Planning Web App

## 📝 Problem Statement

### Smart Academic ERP for Seamless Campus Management

### 🌍 Context
Educational institutions often deal with fragmented systems for attendance, academics, communication, and admin tasks—resulting in inefficiency, fraud, and disengaged students.

---

## 💡 Proposed Solution

A web-based ERP system designed for streamlined campus management. The application supports real-time student attendance tracking, assignment management, and integrates an AI-powered chatbot for university updates and support.

---

![Smart Academic ERP Context Screenshot](https://github.com/user-attachments/assets/88219b9d-da04-45a5-b2bb-a3befabb0851)

---

## 🚀 Key Features

### 📋 Student Attendance
- Digital attendance tracking system  
- Records and stores attendance securely  
- Real-time updates for faculty and students  

### 📝 Assignment Tracking
- Faculty can upload and manage assignments  
- Students can view deadlines and submission status  
- Automated alerts for upcoming deadlines  

### 🤖 AI Chatbot Integration
- Embedded IBM Watson Assistant on the homepage  
- Responds to student queries about:
  - University updates  
  - Notices and events  
  - General academic info  

### 💻 User Interface
- Clean, intuitive web UI for students and faculty  
- Dashboard with attendance, assignments, and notifications  

---

## 🌐 Tech Stack

- **Frontend:** HTML and CSS  
- **Backend:** Python and Django (Framework)  
- **Database:** SQLite  
- **AI Assistant:** IBM Watson Assistant Web Chat Integration  

---

## 🧱 Steps to Run the Project

### 📥 Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 🧰 Create and Activate a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 📦 Install Required Packages
```
pip install -r requirements.txt
```
### ⚙️ Run Migrations
```
python manage.py migrate
```
### ▶️ Start the Development Server
```
python manage.py runserver
```

Visit:  
```
http://127.0.0.1:8000/
```

---

## 🤖 Watson Assistant Integration

IBM Watson Assistant Web Chat is embedded into the homepage. Add the following script in your `base.html` or `index.html` file:

```html
<script>
  window.watsonAssistantChatOptions = {
      integrationID: "your-integration-id",
      region: "your-region",
      serviceInstanceID: "your-service-instance-id",
      onLoad: function(instance) { instance.render(); }
  };
  setTimeout(function(){
      const t = document.createElement('script');
      t.src = "https://web-chat.global.assistant.watson.appdomain.cloud/versions/latest/WatsonAssistantChatEntry.js";
      document.head.appendChild(t);
  });
</script>
```

> Replace `"your-integration-id"`, `"your-region"`, and `"your-service-instance-id"` with your actual Watson Assistant credentials.

---

## 🎯 Project Goal

To automate and simplify academic management, improve student engagement, and ensure timely communication through AI and real-time web services.

