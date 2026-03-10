from pypdf import PdfReader
from gtts import gTTS

# 1. Load the PDF
pdf_path = "interview_questions_fundamentals-1.pdf"
reader = PdfReader(pdf_path)

full_text = ""

# 2. Extract text from all pages
for page in reader.pages:
    text = page.extract_text()
    if text:
        full_text += text

# 3. Convert text to speech
tts = gTTS(text=full_text, lang="en")

# 4. Save as MP3
output_file = "output_audio.mp3"
tts.save(output_file)

print("Audio file created successfully:", output_file)
