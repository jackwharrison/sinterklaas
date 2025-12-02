from flask import Flask, render_template

app = Flask(__name__)

# --------------------------------------------
# Replace these with the coordinates of "home"
# --------------------------------------------
TARGET_LAT = 51.39259
TARGET_LON = 5.44159


@app.route("/")
def index():
    return render_template(
        "index.html",
        target_lat=TARGET_LAT,
        target_lon=TARGET_LON
    )


if __name__ == "__main__":
    app.run(debug=True)
