from distutils.debug import DEBUG
from app import create_app # since create_app is inside __init__.py i can import it anywhere

app = create_app()

if __name__=='__main__':
    app.run(debug=True)