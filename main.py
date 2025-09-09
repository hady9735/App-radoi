import flet as ft

STREAM_URL = "https://stream.radiojar.com/8s5u5tpdtwzuv"

def main(page: ft.Page):
    page.title = "📻 إذاعة القرآن الكريم - مصر"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    # دالة fallback لاستخدام WebView لو Audio مش موجود
    use_webview = False
    try:
        audio = ft.Audio(src=STREAM_URL, autoplay=False)
        page.overlay.append(audio)

        def play_radio(e):
            audio.play()

        def pause_radio(e):
            audio.pause()
    except Exception:
        use_webview = True

    if use_webview:
        # HTML للتموجات وتشغيل الراديو
        HTML_PAGE = f"""
        <!DOCTYPE html>
        <html lang="ar">
        <head>
          <meta charset="UTF-8">
          <title>📻 إذاعة القرآن الكريم - مصر</title>
          <style>
            body {{ font-family: Tahoma, sans-serif; text-align: center; background: #111; color: white; padding: 40px; direction: rtl; }}
            h1 {{ color: #2ecc71; }}
            canvas {{ display: block; margin: 30px auto; width: 80%; height: 200px; background: #222; border-radius: 12px; }}
          </style>
        </head>
        <body>
          <h1>📻 إذاعة القرآن الكريم - مصر</h1>
          <audio id="radioPlayer" controls autoplay crossorigin="anonymous">
            <source src="{STREAM_URL}" type="audio/mpeg">
            متصفحك لا يدعم تشغيل الصوت.
          </audio>
          <canvas id="visualizer"></canvas>
          <script>
            const player = document.getElementById("radioPlayer");
            const canvas = document.getElementById("visualizer");
            const ctx = canvas.getContext("2d");
            const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            const source = audioCtx.createMediaElementSource(player);
            const analyser = audioCtx.createAnalyser();
            source.connect(analyser);
            analyser.connect(audioCtx.destination);
            analyser.fftSize = 256;
            const dataArray = new Uint8Array(analyser.frequencyBinCount);
            function draw() {{
              requestAnimationFrame(draw);
              analyser.getByteFrequencyData(dataArray);
              ctx.fillStyle = "#222";
              ctx.fillRect(0, 0, canvas.width, canvas.height);
              const barWidth = (canvas.width / dataArray.length) * 2.5;
              let x = 0;
              for (let i = 0; i < dataArray.length; i++) {{
                const barHeight = dataArray[i] / 2;
                ctx.fillStyle = "rgb(" + (barHeight + 100) + ",200,100)";
                ctx.fillRect(x, canvas.height - barHeight, barWidth, barHeight);
                x += barWidth + 1;
              }}
            }}
            draw();
          </script>
        </body>
        </html>
        """
        page.add(ft.WebView(content=HTML_PAGE, expand=True))
    else:
        # زرار تشغيل وإيقاف الصوت مع تأثيرات بصريه بسيطة
        play_button = ft.ElevatedButton("▶️ تشغيل", on_click=play_radio)
        pause_button = ft.ElevatedButton("⏸️ إيقاف", on_click=pause_radio)
        title = ft.Text("📻 إذاعة القرآن الكريم - مصر", size=24, weight="bold", color="green")
        page.add(title, ft.Row([play_button, pause_button], alignment=ft.MainAxisAlignment.CENTER))

ft.app(target=main)
