from pyrogram import Client, filters
import random

# Replace with your bot token
BOT_TOKEN = "6731360333:AAGGUJyxRf9qXHf5tFuNYEfLYCos39Qo9-Y"

# Initialize the Pyrogram client
app = Client("solo_leveling_game_bot", api_id=29422639, api_hash="e21bccfd64a01c5762ce81c77379dc7f", bot_token=BOT_TOKEN)

# Define a dictionary to store player data
players = {}

# Define a function to handle the /start command
@app.on_message(filters.command("start"))
def start(client, message):
    # Send a message to the user introducing the game
    message.reply_text("Welcome to Solo Leveling Game Bot! Please enter your name to start playing.")

# Define a function to handle the /play command
@app.on_message(filters.command("play"))
def play(client, message):
    # Get the user's name from the message text
    name = message.text.split(" ")[1]
    players[message.from_user.id] = {"name": name, "health": 100, "gems": 0, "weapon": "Sword"}
    message.reply_text(f"Welcome, {name}! You have entered the world of Solo Leveling. Your current health is 100 and you have a Sword as your weapon.")

# Define a function to handle the /fight command
@app.on_message(filters.command("fight"))
def fight(client, message):
    # Get the user's data from the players dictionary
    user_data = players.get(message.from_user.id)
    if user_data:
        # Generate a random monster to fight
        monster = random.choice(["Goblin", "Orc", "Troll"])
        monster_health = random.randint(20, 50)
        message.reply_text(f"You have encountered a {monster} with {monster_health} health. Your current health is {user_data['health']} and you have a {user_data['weapon']} as your weapon.")

        # Handle the fight logic
        while monster_health > 0:
            # Get the user's attack input
            attack = message.reply_text("Enter 'attack' to attack the monster or 'run' to flee.")
            if attack == "attack":
                # Calculate the damage dealt to the monster
                damage = random.randint(10, 20)
                monster_health -= damage
                message.reply_text(f"You attacked the {monster} for {damage} damage. Its current health is {monster_health}.")
            elif attack == "run":
                message.reply_text("You fled from the battle. Your current health is still {user_data['health']}.")
                break

        # Handle the outcome of the fight
        if monster_health <= 0:
            # Award gems to the user
            user_data["gems"] += random.randint(1, 5)
            message.reply_text(f"You defeated the {monster} and earned {user_data['gems']} gems! Your current health is {user_data['health']}.")
        else:
            # Reduce the user's health
            user_data["health"] -= monster_health
            message.reply_text(f"You were defeated by the {monster}. Your current health is {user_data['health']}.")
    else:
        message.reply_text("You haven't started playing yet. Please enter your name using the /play command.")

# Define a function to handle the /health command
@app.on_message(filters.command("health"))
def health(client, message):
    # Get the user's data from the players dictionary
    user_data = players.get(message.from_user.id)
    if user_data:
        message.reply_text(f"Your current health is {user_data['health']}.")

# Define a function to handle the /gems command
@app.on_message(filters.command("gems"))
def gems(client, message):
    # Get the user's data from the players dictionary
    user_data = players.get(message.from_user.id)
    if user_data:
        message.reply_text(f"You have {user_data['gems']} gems.")

# Start the bot
app.run()
