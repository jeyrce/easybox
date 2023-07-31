import os

import requests

tickets = (
    (1, 2, 9, 22, 34, [7, 8]),
    (2, 8, 17, 22, 28, [4, 7]),
    (4, 9, 13, 19, 30, [1, 8]),
    (11, 16, 24, 25, 33, [6, 8]),
    (7, 16, 22, 23, 30, [8, 11]),
)


def result():
    """
    从公开信息获取结果并排序
    :return:
    """
    res = ()
    resp = requests.get(
        url="https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=30&isVerify=1&pageNo=1&termLimits=3",
        headers={"content-type": "application/json"},
    )
    if resp.status_code != 200:
        print(resp.text)
        return res
    data = resp.json()
    code_str = data.get("value", {}).get("lastPoolDraw", {}).get("lotteryDrawResult", "-")
    if code_str == "-":
        print(code_str)
        return res
    items = code_str.split(" ")
    if len(items) != 7:
        print("error result")
        return res
    red = sorted(int(i) for i in items[:5])
    blue = sorted(int(j) for j in items[5:])
    red.append(blue)
    return red


def parse(items, target):
    """
    分析中奖情况,统计中奖结果
    :return:
    """
    red_target = target[:5]
    blue_target = target[5]
    blue_target = [i for i in blue_target]
    x = list()
    for item in items:
        red_match = 0
        blue_match = 0
        for r in item[:5]:
            if r in red_target:
                red_match += 1
        for b in item[5]:
            if b in blue_target:
                blue_match += 1
        if red_match == 5 and blue_match == 2:
            x.append(1)
        elif red_match == 5 and blue_match == 1:
            x.append(2)
        elif red_match == 5 and blue_match == 0:
            x.append(3)
        elif red_match == 4 and blue_match == 2:
            x.append(4)
        elif red_match == 4 and blue_match == 1:
            x.append(5)
        elif red_match == 3 and blue_match == 2:
            x.append(6)
        elif red_match + blue_match == 4:
            x.append(7)
        else:
            x.append(0)
    return x


def notify(msg):
    """
    通知中奖情况
    :return:
    """
    resp = requests.post(
        url="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=%s" % os.getenv("ROBOT_TOKEN", ""),
        json={
            "msgtype": "text",
            "text": {
                "content": "一线希望: %s" % msg,
            }
        },
    )
    print(resp.text)
    return ""


if __name__ == '__main__':
    print(notify(parse(tickets, result())))