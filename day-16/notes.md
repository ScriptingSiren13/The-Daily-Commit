# Day 16 — Completed 3 Labs on Google Arcade (Cloud AI + Data Engineering Track)

Today I completed three labs in the Google Arcade Boot Boost track. This was the first proper hands-on day where I actually ran APIs and workflows in the cloud and understood what each lab was trying to teach.

---

## 1) Lab: Speech-to-Text (Audio → Text)

This lab introduced the pattern of sending an audio file to Google’s Speech-to-Text API and receiving text back. I ran the end-to-end flow using `curl`.

The workflow was essentially:

>  Audio → Google AI →  Text

Key concepts I practiced:

- authenticating Speech API using API keys
- constructing JSON request bodies
- sending REST requests from a VM
- interpreting JSON responses (`transcript`, `confidence`)
- processing multilingual audio (English + French)

This taught me how cloud AI services are called programmatically and how applications integrate voice features.

---

## 2) Lab: Cloud Translation (Text → Other Language & Language Detection)

The second lab explored Google’s Translation API, which supports:

1. translating text between languages
2. detecting the language of unknown text

Real-world patterns covered:

- chat translation
- UI localization
- multilingual knowledge systems
- support workflows
- assistant-style features

Conceptually, the lab reinforced that the same API patterns repeat:

auth → format request → call API → read JSON → build feature


This is a useful abstraction for designing cloud AI pipelines.

---

## 3) Lab: Cloud Dataprep (Data Cleaning & Transformation → BigQuery)

The third lab switched from AI to Data Engineering. Scenario wise, the task was to prepare subscription performance data over multiple years so it can be analyzed geographically.

**Workflow pattern:**
Raw CSVs (Cloud Storage)
↓
Transform / Clean (Dataprep)
↓
Publish to BigQuery (Analysis Ready)


Technical concepts covered:

- handling missing values
- imputing defaults
- unioning year-wise transaction datasets
- joining customer + transaction data
- creating derived fields (e.g., year)
- data publishing to analytical warehouse (BigQuery)

This simulated a **mini ETL pipeline**, which is exactly how real companies prepare data for BI, analytics, ML, and dashboards.

---

## High-Level Takeaways

Across all 3 labs, I started seeing repeated cloud patterns:

✔ API key based authentication  
✔ REST-style interaction with AI models  
✔ JSON as the common interface  
✔ VM as client for execution  
✔ Data warehousing via BigQuery  
✔ ETL-style pipelines for analytics  

The labs also showed how Speech, Translation, and DataPrep can be composed in modern applications.

---

## Tomorrow

I will continue with the Arcade labs and try to chain concepts together rather than seeing them in isolation.

