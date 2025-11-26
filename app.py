from flask import Flask, render_template
import random

app = Flask(__name__)

sozler = [
    "Bugün harika şeyler olacak!",
    "Başlamak bitirmenin yarısıdır.",
    "Gülümse, hayat güzelleşir!",
    "Her gün yeni bir şans.",
    "İnandığın şeyleri başarabilirsin!",
    "Pozitif düşün, pozitif yaşa.",
    "Küçük adımlar büyük değişiklikler getirir.",
    "Hayallerine sıkı sıkıya tutun.",
    "Zorluklar seni güçlendirir.",
    "Mutluluk paylaştıkça çoğalır.",
    "Başarı, azimle gelir.",
    "Her gün yeni bir başlangıçtır.",
    "Kendine inan, her şey mümkün.",
    "Hayat kısa, anı yaşa.",
    "Sevgi en büyük güçtür.",
    "Sabır, başarının anahtarıdır.",
    "Kendini keşfet, dünyayı keşfet.",
    "Aldanma, öbür dünyaya, hayatı yaşa, KORKMA!"
]

@app.route("/")
def ana_sayfa():
    rastgele_soz = random.choice(sozler)
    return render_template("index.html", soz=rastgele_soz)

if __name__ == "__main__":
    app.run(debug=True)
