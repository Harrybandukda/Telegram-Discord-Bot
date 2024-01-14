# Telegram-to-Discord Forwarding Bot

This repository contains a Python script, `Bot.py`, designed to forward messages from specified Telegram groups/channels to Discord using webhooks. The bot utilizes the Telethon library for interacting with Telegram and the discord-webhook library for Discord integration.

## File: `Bot.py`

### Usage

1. **Installation:**
   - Ensure you have Python installed on your machine.
   - Install required libraries: `telethon` and `discord-webhook`. You can do this by running `pip install telethon discord-webhook`.

2. **Configuration:**
   - Open the `config.py` file and provide your Telegram API credentials (`API_ID` and `API_HASH`).
   - Set up forwarding configurations by providing Telegram group/channel IDs (`FORWARD_ID`, `FORWARD2_ID`, `FORWARD3_ID`, etc.) and corresponding Discord webhook links (`FORWARD_WB`, `FORWARD2_WB`, `FORWARD3_WB`, etc.).
   - Uncomment and add configurations for additional channels if needed (e.g., `FORWARD4_ID`, `FORWARD4_WB`).

3. **Run the Bot:**
   - Execute the `Bot.py` script. This script connects to Telegram, monitors specified channels, and forwards messages to Discord webhooks.

### Functionality

- Forwards messages from Telegram to Discord based on configured channels.
- Supports additional customization options such as adding extra content, including different footers, and tagging everyone in Discord.

### Example Usage

```python
# Forward messages from specified Telegram channels to Discord webhooks

# Forward messages from FORWARD_ID channel to FORWARD_WB Discord webhook
await forwardToWebhook(event, env.FORWARD_WB)

# Forward messages from FORWARD2_ID channel to FORWARD2_WB Discord webhook
await forwardToWebhook(event, env.FORWARD2_WB)

# Forward messages from FORWARD3_ID channel to FORWARD3_WB Discord webhook
await forwardToWebhook(event, env.FORWARD3_WB)

# Add more configurations for additional channels if needed
# Uncomment and update the following lines accordingly
# await forwardToWebhook(event, env.FORWARD4_WB)

```
## Customization

- **addExtraContent:** Option to include extra content in the Discord webhook.
- **includeDifferentFooter:** Choose to include a different footer for specific channels.
- **fromeveryone:** Tag everyone in Discord when forwarding messages.

## Important Note

Ensure you keep your API credentials and webhook links secure and do not share them publicly.

## File: `config.py`

This file contains configuration settings required by the `Bot.py` script. Provide your Telegram API credentials, channel IDs, and corresponding Discord webhook links.

Feel free to customize the configuration based on your specific channels and webhook preferences.

**Note:** Add configurations for additional channels by uncommenting and updating the relevant lines.

Feel free to contribute, report issues, or enhance the functionality of this Telegram-to-Discord forwarding bot. Happy coding!

