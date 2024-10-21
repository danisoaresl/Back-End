@app.route('/')
def index():
    return render_template('index.html')

if _name_ == '_main':
    app.run(debug=True, port=8080)