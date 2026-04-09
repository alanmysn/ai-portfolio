import yt_dlp
import os

# ============ 配置区 ============
VIDEO_URL = "https://www.bilibili.com/video/BV1p4DeB8ECi"
OUTPUT_DIR = "audio_output"
# ================================

os.makedirs(OUTPUT_DIR, exist_ok=True)

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(OUTPUT_DIR, '%(title)s.%(ext)s'),
    'quiet': False,
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(VIDEO_URL, download=True)
        print(f"\n下载完成: {info['title']}")
        print(f"文件位置: {OUTPUT_DIR}/")
except yt_dlp.utils.DownloadError as e:
    print(f"\n下载失败: {e}")
    print("可能原因: 视频链接无效、网站限制、需要VPN、或视频需要登录")
except Exception as e:
    print(f"\n未知错误: {e}")