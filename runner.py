import os
from app import app
# from flask_script import Manager, Shell


# manager = Manager(app)


if __name__ == '__main__':
    # manager.run()
    app.run(debug=True)
