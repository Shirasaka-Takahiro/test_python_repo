import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Testtest991!',
                             database='testdb',
                             cursorclass=pymysql.cursors.DictCursor)

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import base64
import tkinter
from tkinter import simpledialog
#sudo yum install python3-tkinterでtkinterをインストール

users = {
    'user1': 'password1',
    'user2': 'password2'
}

class SimpleBoardAuthenticationGUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Authentication")
        self.username = None
        self.password = None
    
    def prompt_credentials(self):
        self.username = simpledialog.askstring("Authentication", "Usename:", parent=self.root)
        self.password = simpledialog.askstring("Authentication", "Password:", show="*", parent=self.root)

    def run(self):
        self.root.withdraw()
        self.prompt_credentials()
        self.root.mainloop()    

def run_authentication_gui():
    auth_gui = SimpleBoardAuthenticationGUI()
    auth_gui.run()
    username = auth_gui.username
    password = auth_gui.password

    return username, password

class SimpleBoardHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # ここにGETリクエストの処理を書きます
        if self.path == '/':
            # Basic認証をチェック
            username, password = run_authentication_gui()
            if not self.check_authentication(username, password):
                self.send_authenticate_header()
                return
            
            self.show_board()

    def do_POST(self):
        # ここにPOSTリクエストの処理を書きます
        if self.path == '/post_message':
            # Basic認証をチェック
            if not self.check_authentication():
                self.send_authenticate_header()
                return
            
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = urllib.parse.parse_qs(post_data)
            self.post_message(params)

        elif self.path == '/delete_message':
            # Basic認証をチェック
            if not self.check_authentication():
                self.send_authenticate_header()
                return
            
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = urllib.parse.parse_qs(post_data)
            self.delete_message(params)

        elif self.path == '/edit_message':
            # Basic認証をチェック
            if not self.check_authentication():
                self.send_authenticate_header()
                return
            
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = urllib.parse.parse_qs(post_data)
            self.edit_message(params)
    
    def check_authentication(self, username, password):
        auth_header = self.headers.get('Authorization', '')
        if not auth_header.startswith('Basic '):
            return False
        
        #ベーシック認証情報を取得してデコード
        encoded_credentials = auth_header.split(' ')[1]
        credentials = base64.b64decode(encoded_credentials).decode('utf-8')
        username, password = credentials.split(':')

        # ユーザー名とパスワードが一致しているかチェック
        return users.get(username) == password
    
    def send_authenticate_header(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm="SimpleBoard"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(b'Authentication required')


    def show_board(self):
        # メッセージをデータベースから取得
        with connection.cursor() as cursor:
            select_messages_query = "SELECT * FROM messages ORDER BY created_at DESC"
            cursor.execute(select_messages_query)
            messages = cursor.fetchall()

        # HTMLレスポンスを送信
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><head><title>BOARD</title></head><body>')
        self.wfile.write(b'<h1>BOARD</h1>')
        self.wfile.write(b'<ul>')
        for message in messages:
            self.wfile.write(f"<li><strong>{message['username']}</strong>: {message['message']} - Message ID: {message['id']}</li>".encode('utf-8'))
        self.wfile.write(b'</ul>')
        # 投稿フォーム
        self.wfile.write(b'<form action="/post_message" method="post">')
        self.wfile.write(b'<label for="username">Username:</label>')
        self.wfile.write(b'<input type="text" id="username" name="username" required><br>')
        self.wfile.write(b'<label for="message">Message:</label>')
        self.wfile.write(b'<textarea id="message" name="message" rows="4" cols="50" required></textarea><br>')
        self.wfile.write(b'<input type="submit" value="Post">')
        self.wfile.write(b'</form>')
        # 削除フォーム
        self.wfile.write(b'<form action="/delete_message" method="post">')
        self.wfile.write(b'<label for="message_id">Message ID to Delete:</label>')
        self.wfile.write(b'<input type="text" id="message_id" name="message_id" required><br>')
        self.wfile.write(b'<input type="submit" value="Delete">')
        self.wfile.write(b'</form>')
        # 編集フォーム
        self.wfile.write(b'<form action="/edit_message" method="post">')
        self.wfile.write(b'<label for="message_id">Message ID to Edit:</label>')
        self.wfile.write(b'<input type="text" id="message_id" name="message_id" required><br>')
        self.wfile.write(b'<label for="new_message">New Message:</label>')
        self.wfile.write(b'<textarea id="new_message" name="new_message" rows="4" cols="50" required></textarea><br>')
        self.wfile.write(b'<input type="submit" value="Edit">')
        self.wfile.write(b'</form>')
        self.wfile.write(b'</body></html>')

    def post_message(self, params):
        # メッセージをデータベースに保存
        username = params['username'][0]
        message = params['message'][0]
        with connection.cursor() as cursor:
            insert_message_query = "INSERT INTO messages (username, message) VALUES (%s, %s)"
            cursor.execute(insert_message_query, (username, message))
            connection.commit()

        # リダイレクト
        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()

    def delete_message(self, params):
        # 削除する投稿のIDを取得
        message_id = params.get('message_id', [''])[0]

        # データベースから投稿を削除
        with connection.cursor() as cursor:
            delete_message_query = "DELETE FROM messages WHERE id = %s"
            cursor.execute(delete_message_query, (message_id,))
            connection.commit()

        # リダイレクト
        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()

    def edit_message(self, params):
        # 編集する投稿のIDと新しいメッセージを取得
        message_id = params.get('message_id', [''])[0]
        new_message = params.get('new_message', [''])[0]

        # データベースの投稿を更新
        with connection.cursor() as cursor:
            update_message_query = "UPDATE messages SET message = %s WHERE id = %s"
            cursor.execute(update_message_query, (new_message, message_id))
            connection.commit()

        # リダイレクト
        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()

if __name__ == '__main__':
    # HTTPサーバーの設定
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleBoardHandler)
    print('Starting server on port 8000...')
    httpd.serve_forever()
