import flet as ft

HTML_PAGE = """
<!DOCTYPE html>
<html lang="ar">
<head>
  <meta charset="UTF-8">
  <title>📻 إذاعة القرآن الكريم - تموجات صوتية</title>
  <script src="https://unpkg.com/wavesurfer.js"></script>
  <style>
    body { 
      text-align: center; 
      font-family: Tahoma; 
      background-color: #1a1a1a; 
      color: white;
    }
    #waveform { 
      margin-top: 30px; 
      border-radius: 10px;
      background-color: #222;
    }
    h1 { 
      color: #4caf50; 
      margin-top: 20px;
    }
    button {
      margin-top: 20px;
      padding: 10px 20px;
      font-size: 16px;
      border-radius: 5px;
      border: none;
      background-color: #4caf50;
      color: white;
      cursor: pointer;
    }
    button:hover {
      background-color: #45a049;
    }
  </style>
</head>
<body>
  <h1>📻 إذاعة القرآن الكريم - مصر</h1>
  <div id="waveform"></div>
  <button onclick="wavesurfer.playPause()">تشغيل/إيقاف</button>

  <script>
    const wavesurfer = WaveSurfer.create({
      container: '#waveform',
      waveColor: 'rgba(76, 175, 80, 0.5)',
      progressColor: 'rgba(76, 175, 80, 1)',
      cursorColor: 'white',
      height: 150,
      barWidth: 3,
      responsive: true,
      normalize: true
    });

    wavesurfer.load('https://stream.radiojar.com/8s5u5tpdtwzuv');
  </script>
</body>
</html>
"""

def main(page: ft.Page):
    page.title = "📻 إذاعة القرآن الكريم - تموجات صوتية"
    page.add(ft.WebView(content=HTML_PAGE, expand=True))

ft.app(target=main)
