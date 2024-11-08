import os
import instaloader
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import shutil  # For directory cleanup

# Define your bot token
TELEGRAM_BOT_TOKEN = 'token'

# Initialize Instaloader
L = instaloader.Instaloader()

# Base directory for downloads
BASE_DOWNLOAD_DIR = ""

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Send me an Instagram link.")

async def fetch_instagram_post(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text

    if "instagram.com" not in user_input:
        await update.message.reply_text("Please send a valid Instagram link.")
        return

    await update.message.reply_text("Processing your Instagram link...")

    try:
        # Extract the shortcode from the Instagram URL
        shortcode = user_input.split("/")[-2]

        # Create a unique directory for this post
        post_download_dir = os.path.join(BASE_DOWNLOAD_DIR, f"post_{shortcode}")
        os.makedirs(post_download_dir, exist_ok=True)

        # Download the post to the unique directory
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        L.download_post(post, target=post_download_dir)

        # Debugging: Print downloaded files
        print(f"Files in {post_download_dir}: {os.listdir(post_download_dir)}")

        # Locate the video file (or image if applicable)
        video_path = next((os.path.join(post_download_dir, file) for file in os.listdir(post_download_dir) if file.endswith(".mp4")), None)
        image_path = next((os.path.join(post_download_dir, file) for file in os.listdir(post_download_dir) if file.endswith(".jpg")), None)

        # Send video if found, otherwise send image
        if video_path and os.path.isfile(video_path):
            video_size = os.path.getsize(video_path)
            if video_size > 50 * 1024 * 1024:
                await update.message.reply_text("The video is too large to send via Telegram.")
            else:
                with open(video_path, 'rb') as video:
                    await update.message.reply_video(video)
        elif image_path and os.path.isfile(image_path):
            with open(image_path, 'rb') as image:
                await update.message.reply_photo(image)
        else:
            await update.message.reply_text("Could not locate or access the media file.")

    except Exception as e:
        print(f"Error fetching Instagram content: {e}")
        await update.message.reply_text("Failed to retrieve the Instagram media. Please check the link or try again later.")
    
    finally:
        # Clean up the unique download directory
        if os.path.exists(post_download_dir):
            shutil.rmtree(post_download_dir)
            print(f"Cleaned up directory: {post_download_dir}")

def main():
    # Initialize the Application with your bot token
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add command and message handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, fetch_instagram_post))

    # Start the bot with polling
    app.run_polling()

if __name__ == '__main__':
    main()
