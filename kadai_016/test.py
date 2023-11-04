## 16.2timeモジュール

# timeモジュールをインポート
import time

# 現在時刻をUNIXタイムスタンプで取得
print(time.time())

#　現在時刻を日時のフォーマットで取得
print(time.strftime("%Y年%m月%d日%H時%M分%S秒", time.localtime()))

# 日時のフォーマット

# datetimeモジュールをインポート
import datetime

# 現在の日時を取得する
now = datetime.datetime.now()
print(now)

# 指定した日付を取得する
date = datetime.datetime.strptime("2015-03-19", "%Y-%m-%d")
print(date.strftime("%Y年%m月%d日"))

# 指定した日時を取得する
date_time = datetime.datetime.strptime("2015-03-19 00:35:30", "%Y-%m-%d %H:%M:%S")
print(date_time.strftime("%Y年%m月%d日 %H時%M時%S秒"))

import datetime

date_time = datetime.datetime.strptime("2015-03-19 00:35:30", "%Y-%m-%d %H:%M:%S")
print(date_time)

# 年,月,日,時,分,秒だけをそれぞれ取り出すことも可能です
print(date_time.year)
print(date_time.month)
print(date_time.day)
print(date_time.hour)
print(date_time.minute)
print(date_time.second)


# datetimeモジュールをインポート
import datetime

# 現在の日時を取得する
now = datetime.datetime.now()

# 指定した日時を取得する
date_time = datetime.datetime.strptime("2015-03-19 00:35:30", "%Y-%m-%d %H:%M:%S")

# 2つのdatetimeの差を取得し、変数intervalに代入する（interval＝間隔）
interval =now - date_time

# 取得した日時の差を特定のフォーマットで出力する
print(f"総日数は{interval.days}日です。")

# datetimeモジュールをインポート
import datetime

# 現在時刻を取得する
now = datetime.datetime.now()

# 1年間の日数差を変数td_1yに代入する
td_1y = datetime.timedelta(days=365)

# 現在の日時に1年を加算し、変数addに代入する
add = now + td_1y

# 3日間の日数差を変数td_3dに代入する
td_3d = datetime.timedelta(days=3)

# 現在の日時から3日を減算し、変数subに代入する（sub＝「減算」を意味するsubtractionの略）
sub = now - td_3d

# 加算・減算した日時を特定のフォーマットで出力する
print(add.strftime("現在から1年後は%Y年%m月%d日 %H時%M時%S秒です"))
print(sub.strftime("現在から3日前は%Y年%m月%d日 %H時%M時%S秒です"))
