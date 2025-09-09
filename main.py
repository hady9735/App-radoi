import flet as ft

def main(page: ft.Page):
    page.title = "📻 إذاعة القرآن الكريم - مصر"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # رابط إذاعة القرآن الكريم
    stream_url = "https://stream.radiojar.com/8s5u5tpdtwzuv"

    audio = ft.Audio(src=stream_url, autoplay=False)

    play_btn = ft.ElevatedButton("▶️ تشغيل", on_click=lambda e: audio.play())
    pause_btn = ft.ElevatedButton("⏸️ إيقاف", on_click=lambda e: audio.pause())

    page.add(ft.Column([play_btn, pause_btn, audio], alignment=ft.MainAxisAlignment.CENTER))

ft.app(target=main)
