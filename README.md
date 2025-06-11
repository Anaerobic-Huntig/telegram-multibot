# Telegram Multi-Business Bot with AI Assistant

This project is a proof of concept Telegram bot that allows multiple businesses to use a single bot instance. Each business can manage its own product or service catalog and receive orders from clients. The bot also integrates with OpenAI to provide an optional assistant for businesses and their clients.

## Features

- Business registration and unique `/start` links
- Simple catalog management stored in SQLite
- AI helper commands using OpenAI's API
- Modular handlers for business and client interactions

The repository contains only a minimal implementation suitable for experimentation. See `main.py` and the handlers in `handlers/` for entry points.

## Setup

1. Create a `.env` file based on `.env.example` and set your Telegram token and OpenAI API key.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the bot:
   ```bash
   python main.py
   ```

## License

This project is licensed under the MIT License.
