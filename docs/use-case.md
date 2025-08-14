## Use Case Description

This system is designed for **personal communication** with individuals in Ukraine who:
- Use only traditional phones (landline or mobile)
- Do not have internet access
- Are family members or close contacts

The initiator (me) uses a **private Telegram bot** to send a command. The bot triggers Twilio to:
1. Call the recipient in Ukraine
2. Simultaneously call me via SIP
3. Bridge both calls

No automated voice messages, no mass calling, no political or commercial content.

This is **not a business tool** — it's a technical solution for maintaining contact under limited connectivity.
