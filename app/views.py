from app import app


@app.route('/')
def main_view():
    return "Hello World!"