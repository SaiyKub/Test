import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

# เมื่อบอทออนไลน์
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# สร้าง Slash Command ชื่อ /getscript
@bot.tree.command(name="getscript", description="เลือก Script ที่ต้องการ!")
async def getscript(interaction: discord.Interaction):
    # สร้างเมนู (Select Menu)
    select = discord.ui.Select(
        placeholder="เลือกหนึ่งตัวเลือก...",
        options=[
            discord.SelectOption(label="BloxFruit ไทย", description="Script สำหรับ BloxFruit (ไทย)", value="bloxfruit_thai"),
            discord.SelectOption(label="BloxFruit Kaitun", description="Script สำหรับ BloxFruit Kaitun", value="bloxfruit_kaitun"),
            discord.SelectOption(label="Fish", description="Script สำหรับ Fish", value="fish"),
        ],
    )

    # ฟังก์ชันเมื่อผู้ใช้เลือก
    async def select_callback(interaction: discord.Interaction):
        if select.values[0] == "bloxfruit_thai":
            response = await interaction.response.send_message(
                "```loadstring(game:HttpGet(\"https://shz.al/rw88\"))()```", ephemeral=True
            )
        elif select.values[0] == "bloxfruit_kaitun":
            response = await interaction.response.send_message("```Soon```", ephemeral=True)
        elif select.values[0] == "fish":
            response = await interaction.response.send_message(
                "```loadstring(game:HttpGet(\"https://shz.al/rw88\"))()```", ephemeral=True
            )

        # รอ 20 วินาทีแล้วลบข้อความนั้น
        await asyncio.sleep(20)
        await response.delete()

    # ผูกฟังก์ชัน callback กับ Select Menu
    select.callback = select_callback

    # สร้าง View และเพิ่ม Select Menu เข้าไป
    view = discord.ui.View()
    view.add_item(select)

    # ส่งข้อความที่มี Select Menu
    await interaction.response.send_message("โปรดเลือกสคริป:", view=view, ephemeral=True)

# ซิงค์คำสั่งกับ Discord (ครั้งแรกที่รัน)
@bot.event
async def setup_hook():
    await bot.tree.sync()

# รันบอท
bot.run("MTMyODE2MjU0Nzg5NDg0OTUzNw.GUcBPA.slJzjCYtMRXxNDYqvwFCkpLsvfHh2rvH2RlZN8")  # แทนที่ด้วย Token ของคุณ
