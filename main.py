from flask import Flask, render_template_string

app = Flask(__name__)

# رابط إذاعة القرآن الكريم
STREAM_URL = "https://stream.radiojar.com/8s5u5tpdtwzuv"

HTML_PAGE = """
<!DOCTYPE html>
<html lang="ar">
<head>
  <meta charset="UTF-8">
  <title>📻 إذاعة القرآن الكريم - مصر</title>
  <style>
    body {
      font-family: Tahoma, sans-serif;
      text-align: center;
      background: #111;
      color: white;
      padding: 40px;
      direction: rtl;
    }
    h1 { color: #2ecc71; }
    button {
      font-size: 18px;
      padding: 12px 24px;
      margin: 10px;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      background: #27ae60;
      color: white;
    }
    button:hover { background: #2ecc71; }
    canvas {
      display: block;
      margin: 30px auto;
      width: 80%;
      height: 200px;
      background: #222;
      border-radius: 12px;
    }
  </style>
</head>
<body>
  <h1>📻 إذاعة القرآن الكريم - مصر</h1>
  <p>اضغط على تشغيل لبدء الاستماع</p>

  <audio id="radioPlayer" crossorigin="anonymous">
    <source src="{{ stream_url }}" type="audio/mpeg">
    متصفحك لا يدعم تشغيل الصوت.
  </audio>

  <br>
  <button onclick="startRadio()">▶️ تشغيل</button>
  <button onclick="pauseRadio()">⏸️ إيقاف</button>

  <canvas id="visualizer"></canvas>

  <script>
    const player = document.getElementById("radioPlayer");
    const canvas = document.getElementById("visualizer");
    const ctx = canvas.getContext("2d");

    let audioCtx, analyser, source, dataArray;

    function startRadio() {
      player.play();
      
      // إنشاء AudioContext عند أول ضغطة زر
      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        source = audioCtx.createMediaElementSource(player);
        analyser = audioCtx.createAnalyser();
        source.connect(analyser);
        analyser.connect(audioCtx.destination);
        analyser.fftSize = 256;
        dataArray = new Uint8Array(analyser.frequencyBinCount);
        draw();
      }
    }

    function pauseRadio() {
      player.pause();
    }

    function draw() {
      requestAnimationFrame(draw);

      analyser.getByteFrequencyData(dataArray);
      ctx.fillStyle = "#222";
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      const barWidth = (canvas.width / dataArray.length) * 2.5;
      let x = 0;

      for (let i = 0; i < dataArray.length; i++) {
        const barHeight = dataArray[i] / 2;
        ctx.fillStyle = "rgb(" + (barHeight + 100) + ",200,100)";
        ctx.fillRect(x, canvas.height - barHeight, barWidth, barHeight);
        x += barWidth + 1;
      }
    }
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE, stream_url=STREAM_URL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
