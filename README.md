# Discord Gemini Bot

This project is a Discord bot that integrates with the Google Gemini API . The bot is built using `discord.py` and  `google.generativeai`.

## Features 
  
- **!ping**: Returns "Pong!"
- **!flip**: Flips a coin and returns "heads" or "tails".
- **!rps {hand}**: Play rock-paper-scissors with the bot.
- **!edit servername {name}**: Changes the server name.
- **!setdefaultvoice {category}**: Sets the default voice category.
- **!setdefaulttext {category}**: Sets the default text category.
- **!edit createtextchannel {name}**: Creates a text channel in the default text category.
- **!edit createvoicechannel {name}**: Creates a voice channel in the default voice category.
- **!edit createrole {name}**: Creates a role with the specified name.
- **!kick {member} [reason]**: Kicks the specified member from the server.
- **!ban {member} [reason]**: Bans the specified member from the server
-  **unban {user_name}**:  Unbans the specified user from the server
- **!query {question}**: Queries the Gemini API with your question and returns a response.
- **!pm**: Sends a private message to you asking how the bot can help and you can talk to it .

## Setup

### Prerequisites

- Python 3.6 or higher
- A Discord account
- Access to the [Discord Developer Portal](https://discord.com/developers/applications) to create a bot
- Gemini API access

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/discord-gemini-bot.git
   cd discord-gemini-bot
   ```

2. **Install Dependancies:**
```bash
pip install -r requirements.txt
```
3.  **Create a `.env` file in the root directory of the project and add the following lines:**
```
DISCORD_API_TOKEN=<Your_Discord_Bot_Token>
Gemini_API_Key=<Your_Gemini_API_Key>

```

4. **Run the bot:**
```bash
python bot.py
```
  



