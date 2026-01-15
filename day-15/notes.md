# Day 15 — Starting Google Arcade (Speech-to-Text Lab Prep)

Today I started working on the Google Arcade “296 Boot Boost” track. I didn’t execute the full lab yet, but I spent time understanding what the Speech-to-Text lab is actually trying to teach and how the components work together.

---

##  What This Lab Is About

The goal is to send an **audio file** to Google’s Speech-to-Text API and receive a **text transcription** back.

Conceptually:

> Audio  → Cloud AI → Text 

This is a foundational cloud AI integration pattern that can later be used to build things like:

- voice assistants
- automated captions
- transcription systems
- multilingual apps
- call center transcription
- podcast/lecture processing

---

##  Components Involved

The lab consists of three key parts:

1. **Google Speech API**  
   The AI engine that converts speech → text.

2. **Linux VM on Google Cloud**  
   I SSH into this machine and run commands — it acts as the “client”.

3. **Sample Audio Files**  
   Stored on Google Cloud Storage, e.g.:  
   `gs://cloud-samples-data/speech/brooklyn_bridge.flac`

---

##  What the Tasks Actually Do

### **Task 1 — Create an API Key**
Google needs authentication to know *who* is calling the service.  
The API key is stored in an environment variable for safe access.

### **Task 2 — Build the Request JSON**
A JSON file (`request.json`) describes:

✔ how to interpret the audio (encoding, language code)  
✔ where the audio file is located (GCS URI)

This is basically the instructions for the API.

### **Task 3 — Send the API Request**
We use `curl` to call the Speech-to-Text REST endpoint.  
The response is saved to `result.json`.

The response includes:
- `transcript`: recognized speech
- `confidence`: model confidence score

### **Task 4 — Switch Languages**
Lab also shows how to switch `languageCode` and audio samples to support multilingual transcription.

---

##  Key Takeaways

By just understanding this setup I now know how cloud AI services are called in practice:

✔ how to authenticate against cloud APIs  
✔ how to structure REST payloads  
✔ how to send audio for transcription  
✔ how to read responses  
✔ how multilingual input works  
✔ how cloud services integrate with clients

This workflow later generalizes to backend apps (Python/Node), mobile apps, browsers, and agents.

---

##  Tomorrow
I will actually perform the lab and run the end-to-end flow on the VM to get hands-on with the API execution.

