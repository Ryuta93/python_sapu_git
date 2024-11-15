"""
・クラスとは、オブジェクト（インスタンス）の設計図のことである
・オブジェクト（インスタンス）とは、クラス（設計図）の詳細項目である
・オブジェクトとインスタンスは同意義である
・インスタンス変数とは、クラス内に記述するデータのうち、オブジェクト（インスタンス）ごとに異なるデータのことである（名前、点数など）
・メソッドとは、クラス内に記述する関数のことである
・メソッドの第一引数には、必ず'self'を設定する（オブジェクト自身を指す）
・'__init__'のことを、イニシャライザ（コンストラクタ）という。あるクラスのオブジェクトが作られるそのタイミングで、1回だけ呼び出される
→インスタンス変数に値を代入するときに用いる
→データを設定し、オブジェクトを初期化する
"""

class SchoolReport:
    def __init__(self,student_name):
        self.student_name = student_name
        
sr_a = SchoolReport('田中 A')
sr_b = SchoolReport('鈴木 B')
sr_c = SchoolReport('斎藤 C')
print(sr_a.student_name)
print(sr_b.student_name)
print(sr_c.student_name)