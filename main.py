#!/usr/bin/env python3
"""
Minecraft Bedrock Bot - Chat and AFK Bot with Hindi Messages
Connects to Bedrock server and performs movement, jumping, and chat
"""

import asyncio
import random
from bedrock_protocol.client import Client
from bedrock_protocol.connection import Connection
from bedrock_protocol.auth import AuthenticationToken
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Server Configuration
SERVER_HOST = "IP-tleline.aternos.me"
SERVER_PORT = 62522
BOT_NAME = "ChatBot"

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
]

class MinecraftBedrockBot:
    def __init__(self, host, port, bot_name):
        self.host = host
        self.port = port
        self.bot_name = bot_name
        self.client = None
        self.connected = False
        self.player_position = {"x": 0, "y": 0, "z": 0}
        
    async def connect(self):
        """Connect to the Bedrock server"""
        try:
            logger.info(f"🤖 Connecting to {self.host}:{self.port}...")
            
            # Create connection
            self.client = Client(
                host=self.host,
                port=self.port,
                username=self.bot_name
            )
            
            # Connect
            await self.client.connect()
            self.connected = True
            logger.info(f"✅ Bot '{self.bot_name}' joined the server!")
            
        except Exception as e:
            logger.error(f"❌ Connection failed: {e}")
            self.connected = False
            
    async def send_chat_message(self, message):
        """Send a chat message to the server"""
        try:
            if self.client:
                await self.client.send_message(message)
                logger.info(f"💬 Sent: {message}")
        except Exception as e:
            logger.error(f"❌ Failed to send message: {e}")
            
    async def move_and_jump(self):
        """Make the bot move and jump around"""
        try:
            if not self.client:
                return
                
            # Move forward
            await self.client.move_forward(random.uniform(1, 3))
            await asyncio.sleep(0.5)
            
            # Jump
            await self.client.jump()
            logger.info("⬆️ Bot jumped!")
            await asyncio.sleep(0.5)
            
            # Move to side
            direction = random.choice(["left", "right"])
            if direction == "left":
                await self.client.move_left(random.uniform(1, 2))
            else:
                await self.client.move_right(random.uniform(1, 2))
            await asyncio.sleep(0.5)
            
            # Another jump
            await self.client.jump()
            logger.info("⬆️ Bot jumped again!")
            
        except Exception as e:
            logger.error(f"❌ Movement error: {e}")
            
    async def rotate_view(self):
        """Rotate the bot's view randomly"""
        try:
            if self.client:
                yaw = random.uniform(0, 360)
                pitch = random.uniform(-90, 90)
                await self.client.rotate(yaw, pitch)
                logger.info(f"🔄 Bot rotated view")
        except Exception as e:
            logger.error(f"❌ Rotation error: {e}")
            
    async def bot_activity_loop(self):
        """Main loop for bot activities"""
        message_counter = 0
        
        while self.connected:
            try:
                # Send Hindi message every 5 activities
                if message_counter % 5 == 0:
                    message = random.choice(HINDI_MESSAGES)
                    await self.send_chat_message(message)
                
                # Move and jump
                await self.move_and_jump()
                await asyncio.sleep(2)
                
                # Rotate view
                await self.rotate_view()
                await asyncio.sleep(1)
                
                message_counter += 1
                
                # Long pause every 30 seconds
                if message_counter % 6 == 0:
                    await asyncio.sleep(10)
                    
            except Exception as e:
                logger.error(f"❌ Activity loop error: {e}")
                await asyncio.sleep(5)
                
    async def reconnect_loop(self):
        """Automatically reconnect if disconnected"""
        while True:
            try:
                if not self.connected:
                    logger.info("🔄 Attempting to reconnect...")
                    await self.connect()
                    if self.connected:
                        await self.bot_activity_loop()
                await asyncio.sleep(30)
            except Exception as e:
                logger.error(f"❌ Reconnect error: {e}")
                await asyncio.sleep(30)
                
    async def run(self):
        """Run the bot"""
        await self.connect()
        if self.connected:
            await self.bot_activity_loop()
        else:
            await self.reconnect_loop()

async def main():
    bot = MinecraftBedrockBot(SERVER_HOST, SERVER_PORT, BOT_NAME)
    try:
        await bot.run()
    except KeyboardInterrupt:
        logger.info("🛑 Bot stopped by user")
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
