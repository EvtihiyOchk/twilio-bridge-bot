# Twilio Voice Bridge Bot

A private Python-based communication tool that enables voice calls to non-internet users via Telegram and Twilio.

## 🎯 Purpose
This project allows me to initiate voice calls to contacts in Ukraine who only have access to landline or mobile phones (no internet). The call is triggered via a Telegram bot, then Twilio bridges the connection between me (via SIP) and the recipient.

## 🛠️ Technologies
- Python 3.9+
- [Twilio Voice API](https://www.twilio.com/docs/voice)
- [Telegram Bot API](https://core.telegram.org/bots)
- Flask (for TwiML webhooks)
- SIP (using Zoiper or Linphone)

## 📦 Setup
1. Clone the repo
2. `pip install -r requirements.txt`
3. Create `config.py` from `config.example.py`
4. Run `python server.py` and expose it via ngrok
5. Send `/call +380...` in Telegram

> ⚠️ This is a personal, non-commercial project. No spam or automated mass calling.

---

🔐 All credentials are kept private.  
👨‍💻 Developer: O.E. (Ochk Yevtikhiy)
