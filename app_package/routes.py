from flask import render_template
from app_package import app
"""
members list with classes
--form banner for user
    profile pic
    username
    online list with mmbers list
    
"""
posts = [
    {
        'username': 'FIRST',
        'content': 'Here is my short form post',
        'pic': 'https://pngimage.net/wp-content/uploads/2018/05/default-user-profile-image-png-7.png'
    },
    {
        'username': 'Webb',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'pic': 'https://pngimage.net/wp-content/uploads/2018/05/default-user-profile-image-png-7.png'
    },
    {
        'username': 'A Quite Long name',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'pic': 'https://pngimage.net/wp-content/uploads/2018/05/default-user-profile-image-png-7.png'
    },
    {
        'username': 'Ryan',
        'content': 'Here is my short form post',
        'pic': 'https://pngimage.net/wp-content/uploads/2018/05/default-user-profile-image-png-7.png'
    },
    {
        'username': 'Ryan',
        'content': 'Here is my short form post',
        'pic': 'https://pngimage.net/wp-content/uploads/2018/05/default-user-profile-image-png-7.png'
    }
]


@app.route('/', methods=['GET'])
def index():
    return render_template('home.html')


@app.route('/forms/', methods=['GET', 'POST'])
def forms():
    return render_template('forms.html', posts=posts)
