# Telegram Multi-Business Bot with AI Assistant

## 📌 Project Goal

Create a Telegram bot in Python that allows multiple businesses to create their own customizable storefronts inside a single bot. Each business gets a unique client link, sets up their own catalog, and receives orders. GPT is used to help businesses with descriptions and to advise clients (e.g. size suggestion).

---

## Key Features

### 👤 For Business Owners:
- Register via `/start`
- Add name, description, type (products/services), logo
- Add items manually or import from Google Sheets / Excel
- Get unique client link: `/start biz_12345`
- Use `/ai` to generate descriptions or pricing help

### 👥 For Clients:
- Open business link → see only that business
- Browse catalog
- Order / Book
- Use “Help me choose” button
  - GPT suggests product based on height, weight, etc.

---

## 🤖 AI Integration
- GPT-3.5 or GPT-4 via OpenAI API
- Used by business for text help
- Used by client for size/product help
- OpenAI key stored as `OPENAI_API_KEY`

---

## 🛠 Tech Stack
- Python 3.10+
- aiogram or python-telegram-bot
- SQLite database
- openai, pandas, openpyxl, gspread
- .env file for secrets

---

## 🔧 Project Files
/main.py
/handlers/business.py
/handlers/client.py
/ai_helper.py
/importer/google.py
/importer/excel.py
/database.py

---

## ✅ Next Step
Start with `main.py`:
- Handle `/start`
- Let user choose: “I'm a business” or “I'm a client”
- Route accordingly
