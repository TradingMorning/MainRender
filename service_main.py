"""
service_main.py — RenderDetect.py sirf blueprints deta hai (init_render()),
khud koi server nahi chalata. Yeh chhota wrapper ek Flask app banata hai
aur RenderDetect ke sab blueprints (render, downloader, editor, publish)
usme register kar deta hai — gunicorn isी file ko point karega.
"""
from flask import Flask
from RenderDetect import init_render

app = Flask(__name__)
init_render(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
