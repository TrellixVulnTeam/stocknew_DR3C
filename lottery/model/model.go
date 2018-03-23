package model

type PKTen struct {
	Datas map[string]*Data
}

type Data struct {
	Number   string `json:"number"`
	Dateline string `json:"dateline"`
}
type LotterPlan struct {
	CurrentPierod string `json:"currentPierod"`
	NumberList    []int  `json:"numberList"`
	PutTime       int    `json:"putTime"`
	RealPutTime   int    `json:"realPutTime"`
	Status        string `json:"status"`
	GetReward     bool   `json:"getReward"`
}

type Content struct {
	Content string `json:"content"`
}

type PushData struct {
	Touser    string `json:"touser"`
	Toparty   string `json:"toparty"`
	Totag     string `json:"totag"`
	Msgtype   string `json:"msgtype"`
	Agentid   int    `json:"agentid"`
	GetReward bool   `json:"getReward"`
	Text      Content
	Safe      int `json:"safe"`
}

//func (*PKTen) ChangeInfos(fierstPeriods int, numbers []int, pkt *PKTen) *PKTen {
//	pkt.Periods = pkt.Periods + 1
//	for _, i := range numbers {
//		for _, k := range pkt.FirstInfos {
//			if i == k.Number {
//				k.Miss = 0
//				k.AvarageMiss = (k.AvarageMiss*(pkt.Periods-fierstPeriods) + k.Miss) / (pkt.Periods - fierstPeriods + 1)
//				if k.Miss <= k.MAXMiss {
//					k.MAXMiss = k.MAXMiss
//				} else {
//					k.MAXMiss = k.Miss
//				}
//			} else {
//				k.Miss = k.Miss + 1
//				k.AvarageMiss = (k.AvarageMiss*(pkt.Periods-fierstPeriods) + k.Miss) / (pkt.Periods - fierstPeriods + 1)
//				if k.Miss <= k.MAXMiss {
//					k.MAXMiss = k.MAXMiss
//				} else {
//					k.MAXMiss = k.Miss
//				}
//			}
//		}

//	}
//	return pkt
//}
