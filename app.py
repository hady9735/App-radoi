from flask import Flask, render_template_string

app = Flask(__name__)

# رابط إذاعة القرآن الكريم
STREAM_URL = "https://stream.radiojar.com/8s5u5tpdtwzuv"

HTML_PAGE = """
<!DOCTYPE html>
<html lang="ar">
<head>
  <meta charset="UTF-8">
  <title>📻 إذاعة القرآن الكريم</title>
  <style>
    body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background: #f9f9f9; }
    h1 { color: #1a1a1a; }
    audio { margin-top: 20px; width: 300px; }

    /* تموجات صوتية */
    .wave {
      display: flex;
      justify-content: center;
      margin-top: 40px;
    }
    .wave span {
      display: block;
      width: 5px;
      height: 20px;
      margin: 0 2px;
      background: linear-gradient(180deg, #1a73e8, #4fc3f7);
      transition: height 0.1s;
    }
  </style>
</head>
<body>
  <h1>📻 إذاعة القرآن الكريم</h1>
  <audio id="audio" controls autoplay crossorigin="anonymous">
    <source src="{{ stream_url }}" type="audio/mpeg">
    متصفحك لا يدعم مشغل الصوت.
  </audio>

  <div class="wave">
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
    <span></span>
  </div>

  <script>
    const audio = document.getElementById('audio');
    const spans = document.querySelectorAll('.wave span');

    // إنشاء AudioContext لتحليل الصوت
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    const audioSource = audioCtx.createMediaElementSource(audio);
    const analyser = audioCtx.createAnalyser();
    audioSource.connect(analyser);
    analyser.connect(audioCtx.destination);
    analyser.fftSize = 64;

    const dataArray = new Uint8Array(analyser.frequencyBinCount);

    function animateWave() {
      requestAnimationFrame(animateWave);
      analyser.getByteFrequencyData(dataArray);
      spans.forEach((span, i) => {
        const scale = dataArray[i] / 2; // تعديل ارتفاع التموج
        span.style.height = `${10 + scale}px`;
      });
    }

    audio.addEventListener('play', () => {
      audioCtx.resume().then(() => animateWave());
    });
  </script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE, stream_url=STREAM_URL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
