import discord
from discord.ext import commands
import youtube_dl
import asyncio
import random
import gtts
from moviepy.editor import *

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# YouTube downloader configuration
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': 'downloads/%(title)s.%(ext)s',
}

class VideoProcessor:
    @staticmethod
    async def download_youtube(url):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(url, download=True)
                return f"downloads/{info['title']}.mp4"
            except Exception as e:
                return str(e)

    @staticmethod
    def add_watermark(video_path, watermark_text):
        video = VideoFileClip(video_path)
        # Add watermark using MoviePy
        txt_clip = TextClip(watermark_text, fontsize=30, color='white')
        txt_clip = txt_clip.set_position('bottom').set_duration(video.duration)
        final = CompositeVideoClip([video, txt_clip])
        output_path = f"processed_{video_path}"
        final.write_videofile(output_path)
        return output_path

    @staticmethod
    def create_tts(text):
        tts = gtts.gTTS(text, lang='en', tld='com')
        tts_path = "tts_output.mp3"
        tts.save(tts_path)
        return tts_path

@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user}')

@bot.command()
async def process_video(ctx, url: str):
    """Process a YouTube video with effects"""
    await ctx.send("Processing your video... Please wait.")
    
    # Download video
    video_path = await VideoProcessor.download_youtube(url)
    if not video_path.endswith('.mp4'):
        await ctx.send(f"Error downloading video: {video_path}")
        return

    # Add watermark
    try:
        watermarked = VideoProcessor.add_watermark(video_path, "ThisVid3")
        await ctx.send(file=discord.File(watermarked))
    except Exception as e:
        await ctx.send(f"Error processing video: {str(e)}")

@bot.command()
async def random_remix(ctx):
    """Generate a random remixed video from downloaded content"""
    try:
        videos = [f for f in os.listdir('downloads') if f.endswith('.mp4')]
        if not videos:
            await ctx.send("No videos available for remixing!")
            return
        
        video_path = f"downloads/{random.choice(videos)}"
        clip = VideoFileClip(video_path)
        
        # Create a simple remix effect
        duration = clip.duration
        cut_points = sorted([random.uniform(0, duration) for _ in range(4)])
        
        clips = []
        start = 0
        for point in cut_points:
            clips.append(clip.subclip(start, point))
            start = point
        
        final_clip = concatenate_videoclips(clips)
        output_path = "remix_output.mp4"
        final_clip.write_videofile(output_path)
        
        # Add TTS outro
        tts_path = VideoProcessor.create_tts("download now a remix thisvid3")
        
        # Combine video with TTS
        video = VideoFileClip(output_path)
        audio = AudioFileClip(tts_path)
        final = video.set_audio(audio)
        final_output = "final_remix.mp4"
        final.write_videofile(final_output)
        
        await ctx.send(file=discord.File(final_output))
    except Exception as e:
        await ctx.send(f"Error creating remix: {str(e)}")

# Run the bot
bot.run('YOUR_BOT_TOKEN')