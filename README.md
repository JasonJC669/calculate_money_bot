## 借貸機器人 Money calculate telegram bot

可以幫一個 Telegram 群組記錄所有人的借貸關係，並且計算出只需要一個人就可以償還所有債務的 Telegram 機器人。 

## 設置
如果要在本機上運行的話，你會需要：

* Python
* [python-telegram-bot](https://python-telegram-bot.org/)

別忘記要跟[ @BotFather](https://telegram.me/BotFather) 拿取 token，並且在資料夾中創建 ```config.ini``` ，內容如下
```ini
[TELEGRAM]
ACCESS_TOKEN = ;在這裡放入 token 
WEBHOOK_URL = 
```
## 使用
[Telegram Bot 連結](t.me/calculate_money_bot)  
加入群組後，可以輸入以下指令：
```
/start - 依照群組人數，開始紀錄
/lend @username {money} - 紀錄 傳送訊息的人 借給 @username {money}元
/clear - 清除所有借貸關係，平倉
/chose @username - 指定 @username 為主要支付或接收的人
                 - 沒有輸入 @username 的話會顯示目前被指定的人
/calculate - 計算出目前被指定人需要給予誰多少元以及向誰收取多少元
/help - 列出所有可以輸入的指令以及其功用
```

---

## Money Calculate Telegram Bot
An accounting bot for Telegram Messeenger to keep track of who borrowed or lent money to whom. Also, calculate a way to clear all the loans with only one person. 

## Setup
To run the bot yourself, you will need:
* Python
* [python-telegram-bot](https://python-telegram-bot.org/)

Don't forget to get a bot token from [@BotFather](https://telegram.me/BotFather) and create a new file called ```config.int``` in your folder. The following is the content.  
```ini
[TELEGRAM]
ACCESS_TOKEN = ;put your token here
WEBHOOK_URL = 
```
## How To Use
[Money Calculate Telegram Bot](t.me/calculate_money_bot)  
Put the bot in a chat, and you can type in the following commands to run the bot.
```
/start - launch the bot and start accounting
/lend @username {money} - @messengesender lend @username ${money}
/clear - clear all the loans
/chose @username - chose @username to be the one who pay or charge others
                 - if @username was empty, the bot will show who is the chosen one now
/calculate - calculate how much do the chosen one need to pay whom and charge from whom
/help - list all the commands
```