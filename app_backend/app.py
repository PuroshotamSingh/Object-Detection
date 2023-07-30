from flask import Flask
import views

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# url
app.add_url_rule("/", "verify", views.verify, methods=["GET", "POST"])



# app run
if __name__ == "__main__":
    app.run(debug=False)
