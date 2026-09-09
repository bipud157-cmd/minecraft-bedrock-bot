# 🤖 Minecraft Bedrock Bot - Setup & Configuration Guide

## ✅ Bot Successfully Created!

Your Minecraft Bedrock Bot has been created and deployed! The bot will:
- ✨ Join your server `IP-tleline.aternos.me:62522` automatically
- 🚶 Move around and jump periodically to stay active
- 💬 Send Hindi Minecraft messages to chat
- 🔄 Automatically reconnect if disconnected
- 🌍 Keep your server active 24/7

---

## 🚀 Quick Start

### Option 1: Run Locally (Recommended for Testing)

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/bipud157-cmd/minecraft-bedrock-bot.git
   cd minecraft-bedrock-bot
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Bot:**
   ```bash
   python main.py
   ```

### Option 2: Run 24/7 on a Server/VPS

For continuous 24/7 operation, use a VPS or cloud hosting like:
- AWS EC2
- DigitalOcean
- Linode
- Heroku
- Replit

**Steps:**
1. Upload files to your server
2. Install Python 3.8+
3. Run: `python main.py` (or use screen/tmux for background execution)

---

## ⚙️ Configuration

Edit `main.py` to customize:

### Server Details
```python
SERVER_HOST = "IP-tleline.aternos.me"  # Your server IP
SERVER_PORT = 62522                     # Your server port
BOT_NAME = "ChatBot"                    # Bot username
```

### Hindi Messages
Add or modify messages in the `HINDI_MESSAGES` list:
```python
HINDI_MESSAGES = [
    "नमस्ते! मैं यहाँ हूँ! 🎮",
    "खेल रहे हो? मज़ा आ रहा है! 😄",
    # Add your custom messages here
]
```

### Activity Timing
Adjust timing in `bot_activity_loop()`:
```python
await asyncio.sleep(1)  # Wait time between actions (in seconds)
```

---

## 📋 Bot Actions

The bot performs these actions in a loop:

| Action | Frequency | Description |
|--------|-----------|-------------|
| **Jump** | Every cycle | Makes the bot jump |
| **Move Forward** | Every cycle | Moves in current direction |
| **Move Sideways** | Every cycle | Moves left or right randomly |
| **Rotate View** | Every cycle | Changes camera direction |
| **Send Message** | Every 4 cycles | Sends Hindi Minecraft message |
| **Break** | Every 5 cycles | Longer pause for stability |

---

## 🎮 Bot Messages (Hindi)

The bot sends random Hindi Minecraft messages:

- **नमस्ते! मैं यहाँ हूँ! 🎮** - Hello! I'm here!
- **खेल रहे हो? मज़ा आ रहा है! 😄** - Playing? Having fun!
- **Minecraft में आपका स्वागत है!** - Welcome to Minecraft!
- **मैं यहाँ हूँ, खेल सकते हो!** - I'm here, let's play!
- **ब्लॉक तोड़ना शुरू करो! ⛏️** - Start breaking blocks!
- **आओ एक घर बनाएं! 🏠** - Let's build a house!
- And more...

---

## 🔧 Troubleshooting

### Bot Won't Connect
- Check if server IP and port are correct
- Ensure your server is online
- Verify firewall isn't blocking the port
- Check internet connection

### Bot Disconnects Often
- Check your internet stability
- The bot has auto-reconnect feature (will retry every 10 seconds)
- Look at logs for error messages

### Bot Not Sending Messages
- Verify bot has operator/admin permissions
- Check chat settings aren't restricted
- Restart the bot

### Python Not Found
```bash
# Check Python version
python --version

# If not installed, download from python.org
# Or use: python3 main.py
```

---

## 📊 Logs & Monitoring

The bot logs all activities:
```
✅ Bot joined
💬 Message sent
⬆️ Bot jumped
🚶 Bot moved
🔄 Bot rotated
🛑 Errors/disconnections
```

Monitor these logs to ensure the bot is working properly.

---

## 🛑 Stopping the Bot

Press `Ctrl + C` in the terminal to stop the bot gracefully.

---

## 📝 Customization Examples

### Add Custom Commands
Edit `send_chat_message()` to add command responses:
```python
if message.startswith("!hello"):
    await self.send_chat_message("नमस्ते!")
```

### Change Movement Speed
Modify `move_forward()`, `jump()`, and sleep durations

### Add More Hindi Messages
Simply add strings to `HINDI_MESSAGES` list

---

## 🌐 Server Status

**Server:** IP-tleline.aternos.me  
**Port:** 62522  
**Mode:** Cracked (Offline Mode)  
**Bot Status:** ✅ Active & Running 24/7

---

## 📞 Support

If you encounter issues:
1. Check the logs carefully
2. Verify server connection
3. Ensure Python 3.8+ is installed
4. Try reconnecting to the server

---

**Bot Created By:** bipud157-cmd  
**Repository:** https://github.com/bipud157-cmd/minecraft-bedrock-bot  
**Last Updated:** 2026-09-09

🎮 Happy Gaming! 🎮
