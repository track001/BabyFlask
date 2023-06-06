from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
  return 'Hello, Baby Flask!'


if __name__ == '__main__':
  app.run()
