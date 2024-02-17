# LUNA 

<br/>
<p align="center">
<img src="./img/luna.png" width="200" alt="LUNA-temp-logo">
</p>
<br/>

_This project is in beta, use at your own risk!_

- [LUNA](#luna)
- [Overview](#overview)
  - [Current Features](#current-features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
    - [Running the bot](#running-the-bot)
    - [Commands](#commands)
  - [Contributing](#contributing)


# Overview
LUNA is a versatile Discord bot designed to assist in web3-focused servers. It integrates advanced features like AI-driven chat, document retrieval, and API interactions. This bot provides commands for engaging in AI-powered conversations, managing user access, querying specific document databases, and retrieving information.

## Current Features
- AI Chat: Engages users in conversations using an advanced AI model.
    - configured to `dolphin-mixtral:latest` but your own model can be used.
- Whitelisting: Manages user access to certain commands.
- Document Queries: Retrieves information from two distinct document databases, namely courses on Updraft and the CodeHawks documentation
- Contest Information: Fetches and displays contest data from a web API.

# Getting Started

## Prerequisites
- Python 3.8 or higher
- Discord account and a Discord server
- Bot token from the Discord Developer Portal

## Installation
1. Clone the repository

```bash
git clone https://github.com/Equious/LUNA_dscrd
cd LUNA_dscrd
```

2. Setup your python virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

This will separate the dependencies for this project from your global python installation. When you're done working on this project, just run `deactivate` to exit the virtual environment.

3. Install the required dependencies using the following command:
   
```bash 
pip install -r requirements.txt
```

4. Setup your `.env` file with API keys. You can use the `.env.example` file to see which API keys you'll need.
To setup your environment variables, run the following command:

```bash
source .env
```

## Configuration
- Update the `whitelist_users` list in the script with the Discord usernames allowed to use admin-level commands.

## Usage
### Running the bot

```
python3 -m luna
```

### Commands
- `!AI`: Initiates a conversation with the AI.
- `!whitelist`: Adds or removes users from the whitelist.
- `!Updraft`: Retrieves information from the Updraft document database.
- `!Docs`: Queries the Codehawks Docs database.
- `!Commands`: Lists all available commands.
- `!Contests`: Fetches and displays current contests from the CodeHawks API.

## Contributing
Contributions to the bot are welcome. Please fork the repository, make your changes, and submit a pull request.