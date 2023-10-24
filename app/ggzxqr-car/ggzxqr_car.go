package main

import (
	"fmt"
	"github.com/skip2/go-qrcode"
	"time"
)

// 121-6 券面价格固定为12元
// projectId 不管用(!=6时多了一个登陆步骤)
// carCouponId （券id）发现用其他值提示不在时间范围，因此猜测这里有一张券表，每天一条或者一段时间一条
var apiTmpl = "https://obs-zhxy.zjsjtz.com/static/code/index?carCouponId=%d&projectId=%d"

func main() {
	start := time.Date(2023, 10, 23, 0, 0, 0, 0, time.Local)
	for i := 121; i <= 200; i++ {
		qr, err := qrcode.New(fmt.Sprintf(apiTmpl, i, 6), qrcode.Medium)
		if err != nil {
			panic(err)
		}
		date := start.AddDate(0, 0, i-121)
		if err := qr.WriteFile(96, fmt.Sprintf("./qr/%s.png", date.Format("2006-01-02"))); err != nil {
			panic(err)
		}
	}
}
