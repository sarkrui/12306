from router.route import app

if __name__ == '__main__':
    app.run('0.0.0.0', 5001,  use_reloader=False)