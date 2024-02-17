## Overview
LUNA is a versatile Discord bot designed to assist in web3-focused servers. It integrates advanced features like AI-driven chat, document retrieval, and API interactions. This bot provides commands for engaging in AI-powered conversations, managing user access, querying specific document databases, and retrieving information.

## Current Features
- AI Chat: Engages users in conversations using an advanced AI model.
    - configured to `dolphin-mixtral:latest` but your own model can be used.
- Whitelisting: Manages user access to certain commands.
- Document Queries: Retrieves information from two distinct document databases, namely courses on Updraft and the CodeHawks documentation
- Contest Information: Fetches and displays contest data from a web API.

## Prerequisites
- Python 3.8 or higher
- Discord account and a Discord server
- Bot token from the Discord Developer Portal

## Installation
1. Clone the repository or download the source code.
2. Install the required dependencies using the following command:
    ```
    pip install -r requirements.txt
    ```
   The `requirements.txt` should contain:
    ```
    discord.py
    ollama
    datasets
    langchain-community
    requests
    python-dotenv
    ```
3. Replace placeholders with applicable API keys - CodeHawks, OpenAI, Bot Token.

## Configuration
- Update the `whitelist_users` list in the script with the Discord usernames allowed to use admin-level commands.

## Usage
- `!AI`: Initiates a conversation with the AI.
- `!whitelist`: Adds or removes users from the whitelist.
- `!Updraft`: Retrieves information from the Updraft document database.
- `!Docs`: Queries the Codehawks Docs database.
- `!Commands`: Lists all available commands.
- `!Contests`: Fetches and displays current contests from the CodeHawks API.

## Contributing
Contributions to the bot are welcome. Please fork the repository, make your changes, and submit a pull request.