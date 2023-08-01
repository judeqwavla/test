import win32com.client
from datetime import date, timedelta
import locale

#Outlookを使える状態に
outlook = win32com.client.Dispatch("Outlook.Application")

#instance生成(メール)
mail = outlook.CreateItem(0)

#送信先
mail.to = "XXX@XXX.co.jp"
mail.cc = "XXX@XXX.co.jp; XXX@XXX.co.jp;"

#件名
d = date.today() - timedelta(days=1)
locale.setlocale(locale.LC_ALL, '')
#　文字化けした locale.setlocale(locale.LC_TIME, 'ja-JP')

mail.subject = "OX Building " + str(d.month) + "/" + str(d.day) + "（" + str(d.strftime('%a')) + "）" + "QQQ社日報 "

#MailFormat Text
mail.bodyFormat = 1

#Mail本文
mail.body = "株式会社\nXX様\n\n\nいつもお世話になっております。\nQQQ社　judeqwavlaです。\n\n標記の件につきまして、昨日の日報を送付いたします。\nご確認の程よろしくお願いいたします。\n\n\nそれでは失礼いたします。\n\n\nQQQ社　judeqwavla"

#メール内容確認    
mail.display(True)

#メール送信
#mail.Send()
