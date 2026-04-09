import whisper
import time

# ============ 配置区 ============
AUDIO_FILE = "audio_output/保姆级教程搭建出karpathy同款AI知识复利积累.m4a"  # 改成实际文件名
MODEL_SIZE = "medium"  # 可选: tiny, base, small, medium, large
LANGUAGE = "zh"  # None=自动检测, 或指定 "zh", "en"
OUTPUT_FILE = "transcription.txt"
# ================================

print(f"正在加载 Whisper {MODEL_SIZE} 模型...")
model = whisper.load_model(MODEL_SIZE)

print(f"开始转录: {AUDIO_FILE}")
start_time = time.time()

result = model.transcribe(AUDIO_FILE, language=LANGUAGE)

elapsed = time.time() - start_time
print(f"转录完成，耗时: {elapsed:.1f} 秒")

with open(OUTPUT_FILE, "w", encoding="utf-8-sig") as f:
    f.write(result["text"])

print(f"文本已保存至: {OUTPUT_FILE}")