# 🤖 Customer Support AI Environment

## 📌 Overview
This project simulates a **Customer Support AI system** designed to handle real-world customer queries such as order delays, damaged products, and refund requests.

It is built as an **AI environment with reward-based evaluation**, making it suitable for reinforcement learning and intelligent agent evaluation.

---

## 🚀 Features

- ✅ Multi-task environment (Easy, Medium, Hard)
- ✅ Real-world customer support scenarios
- ✅ Intelligent response generation
- ✅ Reward-based evaluation system
- ✅ FastAPI backend for execution
- ✅ Deployable on Hugging Face Spaces

---

## 🧠 Environment Design

### 📦 State
Each task includes:
- Customer query
- Difficulty level

---

### 🎯 Actions
The AI agent:
- Generates a response to customer queries

---

### 📊 Reward Function

The response is evaluated based on:

| Criteria       | Reward |
|----------------|--------|
| Politeness     | +0.3   |
| Correct Action | +0.4   |
| Empathy        | +0.3   |

---

### 🧪 Tasks

#### 🟢 Easy
- Query: "Where is my order?"
- Goal: Provide status politely

#### 🟡 Medium
- Query: "My product is damaged and I want a refund"
- Goal: Handle complaint + offer solution

#### 🔴 Hard
- Query: "I have been waiting for 2 weeks, very frustrated!"
- Goal: Handle frustration + prioritize resolution

---

## ⚙️ API Endpoints

### 🔹 Home
