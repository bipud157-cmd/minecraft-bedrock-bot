#!/usr/bin/env python3
"""
Minecraft Bedrock Bot - Chat and AFK Bot with Hindi Messages
Connects to Cracked Bedrock server and performs movement, jumping, and chat
"""

import asyncio
import random
from mcpyver import mcproto
from mcpyver.mcproto.connection import Connection
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
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
    "सूरज निकल गया, दिन शुरू हो गया! ☀️",
    "रात आ गई, सावधान रहो! 🌙",
    "मेरा नाम चैटबॉट है! 🤖",
    "खेल खेल में मज़ा है! 🎯",
    "Minecraft सर्वश्रेष्ठ है! 👑",
]

class MinecraftBedrockBot:
    def __init__(self, host, port, bot_name):
        self.host = host
        self.port = port
        self.bot_name = bot_name
        self.connection = None
        self.connected = False
        self.player_yaw = 0
        self.player_pitch = 0
        
    async def connect(self):
        """Connect to the cracked Bedrock server"""
        try:
            logger.info(f"🤖 Connecting to {self.host}:{self.port}...")
            
            # Create connection with offline mode (cracked server)
            self.connection = Connection(
                host=self.host,
                port=self.port,
                username=self.bot_name,
                uuid=None,  # Offline mode - no UUID needed
                online_mode=False  # Cracked server
            )
            
            # Attempt connection
            await self.connection.connect()
            self.connected = True
            logger.info(f"✅ Bot '{self.bot_name}' joined the cracked server!")
            
        except Exception as e:
            logger.error(f"❌ Connection failed: {e}")
            self.connected = False
            await asyncio.sleep(5)
            
    async def send_chat_message(self, message):
        """Send a chat message to the server"""
        try:
            if self.connection:
                # Send chat packet
                packet = mcproto.packets.ChatPacket(message)
                await self.connection.send(packet)
                logger.info(f"💬 Sent: {message}")
        except Exception as e:
            logger.error(f"❌ Failed to send message: {e}")
            self.connected = False
            
    async def move_forward(self, duration=1):
        """Move the bot forward"""
        try:
            if self.connection:
                packet = mcproto.packets.PlayerActionPacket(
                    entity_runtimeid=0,
                    action="StartSprinting"
                )
                await self.connection.send(packet)
                await asyncio.sleep(duration)
                
                packet = mcproto.packets.PlayerActionPacket(
                    entity_runtimeid=0,
                    action="StopSprinting"
                )
                await self.connection.send(packet)
                logger.info("🚶 Bot moved forward")
        except Exception as e:
            logger.error(f"❌ Move forward error: {e}")
            
    async def jump(self):
        """Make the bot jump"""
        try:
            if self.connection:
                packet = mcproto.packets.PlayerActionPacket(
                    entity_runtimeid=0,
                    action="Jump"
                )
                await self.connection.send(packet)
                logger.info("⬆️ Bot jumped!")
                await asyncio.sleep(0.5)
        except Exception as e:
            logger.error(f"❌ Jump error: {e}")
            
    async def rotate_view(self):
        """Rotate the bot's view"""
        try:
            if self.connection:
                self.player_yaw = (self.player_yaw + random.uniform(30, 90)) % 360
                self.player_pitch = random.uniform(-30, 30)
                
                packet = mcproto.packets.PlayerLookPacket(
                    yaw=self.player_yaw,
                    pitch=self.player_pitch
                )
                await self.connection.send(packet)
                logger.info(f"🔄 Bot rotated view (yaw: {self.player_yaw:.1f}°)")
        except Exception as e:
            logger.error(f"❌ Rotation error: {e}")
            
    async def move_sideways(self, direction="left"):
        """Move the bot sideways"""
        try:
            if self.connection:
                action = "StartSideSwimming" if direction == "left" else "StopSideSwimming"
                packet = mcproto.packets.PlayerActionPacket(
                    entity_runtimeid=0,
                    action=action
                )
                await self.connection.send(packet)
                logger.info(f"👈 Bot moved {direction}")
                await asyncio.sleep(1)
        except Exception as e:
            logger.error(f"❌ Sideways movement error: {e}")
            
    async def bot_activity_loop(self):
        """Main loop for bot activities"""
        message_counter = 0
        
        while self.connected:
            try:
                # Send Hindi message every 4 activities
                if message_counter % 4 == 0:
                    message = random.choice(HINDI_MESSAGES)
                    await self.send_chat_message(message)
                    await asyncio.sleep(1)
                
                # Jump
                await self.jump()
                await asyncio.sleep(0.8)
                
                # Move forward
                await self.move_forward(0.5)
                await asyncio.sleep(1)
                
                # Move sideways
                direction = random.choice(["left", "right"])
                await self.move_sideways(direction)
                await asyncio.sleep(1)
                
                # Rotate view
                await self.rotate_view()
                await asyncio.sleep(1)
                
                # Jump again
                await self.jump()
                await asyncio.sleep(0.8)
                
                message_counter += 1
                
                # Longer pause every 5 cycles
                if message_counter % 5 == 0:
                    logger.info("⏸️ Bot taking a break...")
                    await asyncio.sleep(8)
                    
            except Exception as e:
                logger.error(f"❌ Activity loop error: {e}")
                self.connected = False
                await asyncio.sleep(5)
                
    async def reconnect_loop(self):
        """Automatically reconnect if disconnected"""
        reconnect_attempts = 0
        max_attempts = 5
        
        while True:
            try:
                if not self.connected:
                    reconnect_attempts += 1
                    logger.info(f"🔄 Reconnection attempt {reconnect_attempts}/{max_attempts}...")
                    
                    await self.connect()
                    
                    if self.connected:
                        reconnect_attempts = 0
                        logger.info("✅ Reconnected successfully! Resuming activities...")
                        try:
                            await self.bot_activity_loop()
                        except Exception as e:
                            logger.error(f"❌ Activity error: {e}")
                            self.connected = False
                    else:
                        if reconnect_attempts >= max_attempts:
                            await asyncio.sleep(30)  # Longer wait after multiple failures
                            reconnect_attempts = 0
                        else:
                            await asyncio.sleep(10)
                else:
                    await asyncio.sleep(30)
                    
            except Exception as e:
                logger.error(f"❌ Reconnect error: {e}")
                await asyncio.sleep(10)
                
    async def run(self):
        """Run the bot"""
        logger.info("🎮 Starting Minecraft Bedrock Bot (Cracked Server Mode)...")
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
        if bot.connection:
            try:
                await bot.connection.close()
            except:
                pass
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🛑 Bot terminated")
