

# Readme

## config.json

```json
{
    "StartPage": [
        "url1",
        "url2"
    ],
    "TimeInterval": 3,
    "Attention": {
        "method": "",
        "expression": ""
    },
    "Return": {
        "method": "",
        "expression": ""
    },
    "Notify": {
        "email": "",
        "message": ""
    }
}

```

+ "StartPage": 需要监控的页面url列表。
+ "TimeInterval": 间隔时间。单位为分钟。如果只需要单次运行则填0。
+ "Attention": 需要监控的页面片段。"method"为匹配片段的方式。支持的方式有：re（正则），xpath，css。"expression"为匹配表达式。
+ "Return": 监控到变化后需要返回的页面片段。
+ "Notify": 接收提醒的邮箱和提醒文字。
+ "Mail": 发送提醒邮件所需的邮箱配置，包括发件人、密码、收件人和SMTP服务器。
