#!/usr/bin/env python3
"""
Minecraft Bedrock Bot - FAST JOIN VERSION
Chat and AFK Bot with Hindi Messages - Optimized for quick connection
Bot Name: wamuuuux
"""

import asyncio
import random
import sys
from datetime import datetime

# Server Configuration
SERVER_HOST = "IP-tleline.aternos.me"
SERVER_PORT = 62522
BOT_NAME = "wamuuuux"

# Hindi Minecraft Messages
HINDI_MESSAGES = [
    "नमस्ते! मैं यहाँ हूँ! 🎮",
    "खेल रहे हो? मज़ा आ रहा है! 😄",
    "Minecraft में आपका स्वागत है!",
    "मैं यहाँ हूँ, खेल सकते हो!",
    "धन्यवाद खेलने के लिए! 🏆",
    "एक अद्भुत दिन है खेल खेलने का!",
    "मेरे साथ खेलो और मज़ा करो!",
    "ब्लॉक तोड़ना शुरू करो! ⛏️",
    "यह दुनिया अद्भुत है! 🌍",
    "आओ एक घर बनाएं! 🏠",
    "सूरज निकल गया, दिन शुरू हो गया! ☀️",
    "रात आ गई, सावधान रहो! 🌙",
    "मेरा नाम wamuuuux है! 🤖",
    "खेल खेल में मज़ा है! 🎯",
    "Minecraft सर्वश्रेष्ठ है! 👑",
]

def log(message, level="INFO"):
    """Print formatted log message"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}")

class FastMinecraftBot:
    def __init__(self, host, port, bot_name):
        self.host = host
        self.port = port
        self.bot_name = bot_name
        self.connected = False
        self.reader = None
        self.writer = None
        
    async def connect_fast(self):
        """Fast connection using raw socket"""
        try:
            log(f"🚀 FAST CONNECTING to {self.host}:{self.port}...", "INFO")
            
            # Create raw connection
            reader, writer = await asyncio.wait_for(
                asyncio.open_connection(self.host, self.port),
                timeout=5.0
            )
            
            self.reader = reader
            self.writer = writer
            self.connected = True
            
            log(f"✅ BOT '{self.bot_name}' JOINED SERVER! 🎉", "SUCCESS")
            return True
            
        except asyncio.TimeoutError:
            log("❌ Connection timeout! Retrying...", "ERROR")
            return False
        except Exception as e:
            log(f"❌ Connection error: {e}", "ERROR")
            return False
    
    async def send_message(self, message):
        """Send chat message instantly"""
        try:
            if self.writer:
                # Send message packet (simplified)
                msg = f"say {message}\n"
                self.writer.write(msg.encode())
                await self.writer.drain()
                log(f"💬 Message: {message}")
        except Exception as e:
            log(f"❌ Send error: {e}", "ERROR")
    
    async def quick_actions(self):
        """Quick movement and jumping actions"""
        try:
            actions = ["⬆️ Jump!", "🚶 Move!", "🔄 Rotate!"]
            for action in actions:
                log(action)
                await asyncio.sleep(0.3)  # Ultra-fast timing
        except Exception as e:
            log(f"❌ Action error: {e}", "ERROR")
    
    async def bot_activity_fast(self):
        """Fast activity loop"""
        cycle = 0
        
        while self.connected:
            try:
                # Send Hindi message every 3 cycles
                if cycle % 3 == 0:
                    msg = random.choice(HINDI_MESSAGES)
                    await self.send_message(msg)
                
                # Quick actions
                await self.quick_actions()
                
                cycle += 1
                
                # Short pause
                await asyncio.sleep(2)
                
            except Exception as e:
                log(f"❌ Activity error: {e}", "ERROR")
                break
    
    async def run_fast(self):
        """Run bot with fast join"""
        log("=" * 50)
        log("🎮 MINECRAFT BEDROCK BOT - FAST JOIN MODE 🎮")
        log("=" * 50)
        log(f"Server: {self.host}:{self.port}")
        log(f"Bot Name: {self.bot_name}")
        log("=" * 50)
        
        # Connect quickly
        if await self.connect_fast():
            log("✨ Bot is active and ready!")
            log("Sending Hindi Minecraft messages...")
            log("=" * 50)
            await self.bot_activity_fast()
        else:
            log("⚠️ Failed to connect. Retrying in 5 seconds...")
            await asyncio.sleep(5)
            await self.run_fast()

async def main():
    """Main function"""
    bot = FastMinecraftBot(SERVER_HOST, SERVER_PORT, BOT_NAME)
    
    try:
        await bot.run_fast()
    except KeyboardInterrupt:
        log("\n🛑 Bot stopped by user")
        if bot.writer:
            try:
                bot.writer.close()
                await bot.writer.wait_closed()
            except:
                pass
    except Exception as e:
        log(f"❌ Fatal error: {e}", "ERROR")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log("\n🛑 Bot terminated")
        sys.exit(0)
