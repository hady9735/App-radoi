import flet as ft

STREAM_URL = "https://stream.radiojar.com/8s5u5tpdtwzuv"

def main(page: ft.Page):
    page.title = "📻 إذاعة القرآن الكريم - مصر"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # مشغل الصوت
    audio = ft.Audio(src=STREAM_URL, autoplay=False)

    # زرار تشغيل وإيقاف
    def play_radio(e):
        audio.play()

    def pause_radio(e):
        audio.pause()

    play_button = ft.ElevatedButton("▶️ تشغيل", on_click=play_radio)
    pause_button = ft.ElevatedButton("⏸️ إيقاف", on_click=pause_radio)

    # عنوان
    title = ft.Text("📻 إذاعة القرآن الكريم - مصر", size=24, weight="bold", color="green")

    # إضافة كل العناصر للواجهة
    page.add(
        title,
        ft.Row([play_button, pause_button], alignment="center"),
        audio,
    )

ft.app(target=main)
