#このライブラリーはfirebaseかリアルタイムデータベースを利用するときに使用するライブラリ

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#サービスアカウントkeyのパス
def sarviceAccountKeyPath_project_init(keyPath, databaseName):
    cred = credentials.Certificate(keyPath)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://' + databaseName + '.firebaseio.com/'
    })

#データベースの参照
def downloadData(Path):
    ref = db.reference(Path)
    return ref.get()

#データベースに書き込み
def uploadData(Path, destination_path):
    ref = db.reference(destination_path)
    ref.set(Path)

#データベースに追加
def pushData(Path, destination_path):
    ref = db.reference(destination_path)
    ref.push(Path)

#データベースの削除
def deleteData(Path):
    ref = db.reference(Path)
    ref.delete()

#データベースの更新
def updateData(Path, destination_path):
    ref = db.reference(Path)
    ref.update(destination_path)

#データベースのトランザクション
def transactionData(Path, destination_path):
    ref = db.reference(Path)
    ref.transaction(destination_path)

#その他
#firebaseに書き込み(jsondata)
def uploadJsonData(json_file_path, destination_path):
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    ref = db.reference(Path)
    ref.set(data)
