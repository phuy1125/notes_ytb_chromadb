import google.generativeai as genai
from google.generativeai import GenerativeModel

genai.configure(api_key="AIzaSyDMiMSOLB8bUOH5_qV2wpUYJqBoLGI8ROI")

# Khởi tạo model

model = GenerativeModel('gemini-pro')

# Prompt để lấy ghi chú video
video_url = "https://www.youtube.com/watch?v=5MZmSJtP7fE"
prompt = f"Please summarize this YouTube video: {video_url}"

# Lấy ghi chú
response = model.generate_content(prompt)
note = response.text

print("Ghi chú từ Gemini:")
print(note)
