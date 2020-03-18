# weixin
(python) 使用window微信客服端向指定用户/群发送信息
代码用到了，OpenCV和操作模拟（用来模拟人为的操作）
初始化class时，传入本地微信客服端所在的目录
eg:wechat = wechat('C:\Program Files (x86)\Tencent\WeChat')
#打开微信
wechat.open_wechat()
#寻找需要发送信息的用户/群
wechat.send_msg_obj('测试目标人')
#需要发送的文本
wechat.send_msg('测试一下')
#微信客服端格式控制（换行）
wechat.huang_hang()
#信息发送
wechat.send()
