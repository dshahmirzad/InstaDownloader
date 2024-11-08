# 📸 InstaDownloader Bot on raspberry pi
A Telegram bot that allows users to download Instagram posts, videos, and photos by simply sharing the Instagram link in the chat. Built with Python and powered by the Instaloader library.
Follow these steps on your raspberry pi board, to have your own Telegram bot to downloading Instagram videos and images.
or you can use my bot: https://t.me/insta4d_bot

# 🚀 Features
- Download Instagram Posts: Retrieve images and videos from public Instagram posts by sending the post link.
- Media Types Supported: Downloads both photos and videos from Instagram posts.
- Easy Setup: Just install the required libraries and start downloading Instagram content.
- Secure & Private: Automatically deletes downloaded files after sending them to the user.

# 🛠️ Installation
Prerequisites
Python 3.7+
Telegram Bot Token from BotFather
Steps
Clone the Repository:

```bash
git clone https://github.com/dshahmirzad/InstaDownloader.git
cd InstaDownloader
```
Install Required Packages:

```bash
pip install instaloader python-telegram-bot
```
Add Your Telegram Bot Token:

Open the InstaDownloaderBot.py file.
Replace 'token' with your actual bot token from BotFather:
python
```bash
TELEGRAM_BOT_TOKEN = 'your_bot_token_here'
```
# 💻 Usage
Start the Bot:

```bash
python InstaDownloaderBot.py
```
Send Instagram Links:

Open your Telegram bot, and start a conversation with /start.
Send an Instagram post link, and the bot will process and send the media back to you!
Example Commands
```bash
/start - Start the bot and receive a welcome message.
```
Send an Instagram post link directly - The bot will fetch and send the media content.
# 📂 Directory Structure
```bash
InstaDownloader-Bot/
├── InstaDownloaderBot.py  # Main bot code
├── requirements.txt       # Package dependencies
└── README.md              # Project documentation
```
# 🤝 Contributing
We welcome contributions! Follow these steps to contribute:

Fork the repository
Create a branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
# 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

📬 Contact
For questions or issues, please reach out via GitHub or Telegram. Contributions are always welcome! 😊

