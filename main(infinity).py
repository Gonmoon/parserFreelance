import requests
import re
import asyncio
from time import sleep
from bs4 import BeautifulSoup


async def parseUpwork(data: list) -> None:
	# -----Upwork-----
	cookies = {'cookies_are' : "visitor_id=151.249.234.54.1645380561102000; lang=en; _pxvid=3a21b91c-9278-11ec-bdb1-774b556a4e46; device_view=full; _gcl_au=1.1.478038082.1645380569; spt=50cefd94-8ebd-493a-810e-ca40af299298; OptanonAlertBoxClosed=2022-02-20T18:09:33.318Z; __pdst=b822cded26f748babdc5b3268d1535af; _rdt_uuid=1645380585059.5f72ab01-7ce4-4d73-86d4-7eaabbe41c60; cb_user_id=null; cb_group_id=null; cb_anonymous_id=%22f494dfb2-90c2-4439-a7c3-72c4e394505e%22; g_state={\"i_p\":1645387790728,\"i_l\":1}; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Feb+20+2022+21%3A10%3A26+GMT%2B0300+(%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.28.0&isIABGlobal=false&hosts=&consentId=ece082ce-e7f7-4354-88e4-956254ad52fd&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=BY%3BMA&AwaitingReconsent=false; G_ENABLED_IDPS=google; _pxhd=xab5NoJWa-7B3LW5lslUkBONrfMldT6xxb1Hq6JiG/oZLUvBa0vuf4H-DDvVuLsQvu82t0RLIZ7Rg4rmDhIbzg==:KN7lQr5AHS28mauDLz9g1S4kSaf9ea0PBpHkQL02Cwhm-XYBHPtN8tq7nfQZBDIbW5uLu6dlRr9ewl7NXqoqv0LaCETQCPEVvzjWSne-Rms=; enabled_ff=CI11132Air2Dot75,CI9570Air2Dot5,!CI10270Air2Dot5QTAllocations,!CI10857Air3Dot0,!air2Dot76,!air2Dot76Qt,!OTBnr,!SSINav,OTBnrOn; channel=direct; __cf_bm=48abf07133de7a020673ccd55f9ed6935e8dcc5d-1645989581-0-AZz7c4medZr9h9TzWkZFZviWYroc7srbRcSON4lTH+mnczDcicNf4dXuBf18zzYfh7BkLba2s9eGz9vnqIOmqMM=; __cfruid=6c6b4f12cf4db84d77a07439d1179751a0c35337-1645989583; SL_G_WPT_TO=ru; _sp_ses.2a16=*; pxcts=38996db9-9802-11ec-af95-494a4e667773; _gid=GA1.2.854771704.1645989586; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; _hp2_ses_props.2858077939=%7B%22ts%22%3A1645989586121%2C%22d%22%3A%22www.upwork.com%22%2C%22h%22%3A%22%2Fsearch%2Fjobs%2F%22%2C%22q%22%3A%22%3Fclient_hires%3D0%2C1-9%26contractor_tier%3D1%2C2%26duration_v3%3Dweeks%26proposals%3D0-4%2C5-9%26q%3Dparsing%26sort%3Drecency%22%7D; _dpm_ses.5831=*; IR_gbd=upwork.com; prodperfect_session={%22session_uuid%22:%22372266c4-0be3-4e1f-8062-004907ac068e%22}; keen={%22uuid%22:%221aecc253-0969-43b3-a22f-57c4b9d768d3%22%2C%22initialReferrer%22:null}; _clck=11dtmxm|1|ezc|0; XSRF-TOKEN=803c68d7fe25552b3f4c2d83d11a1f0f; _sp_id.2a16=132534c3-8fef-4dca-a0ac-26740b288ee3.1645380568.2.1645989621.1645384923.0d99877a-c99f-455b-a0d6-6f61872362ff; _ga_KSM221PNDX=GS1.1.1645989585.2.1.1645989622.0; _ga=GA1.2.293786602.1645380572; _hp2_props.2858077939=%7B%22container_id%22%3A%22GTM-WNVF2RB%22%2C%22user_context%22%3A%22unknown%22%2C%22user_logged_in%22%3Afalse%7D; _hp2_id.2858077939=%7B%22userId%22%3A%224754437359709997%22%2C%22pageviewId%22%3A%225305527580187541%22%2C%22sessionId%22%3A%221640052786101023%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _dpm_id.5831=f73f7e34-a992-4bd6-beca-87dcb398a256.1645380587.2.1645989627.1645381797.7bbb9fd6-59ef-416e-9b3c-5212c41f868a; IR_13634=1645989626902%7C0%7C1645989626902%7C%7C; _uetsid=3a6e6e40980211eca580afd2555d8f1b; _uetvid=922ef700fcee11ebb5e2f9388f20acd8; _px3=7a880e04292551dc625e0d626b31ae19654a94ee96d08d7f67a891f88e0fbcfb:rLvtMpNp9RCfiTmBTlTfVrBWsY/i4wy+FTlXaVRI8CvFgDU021UPv6HFm02Nb0MhQ6k1hsQpVnCmrbJ/0S5aMg==:1000:7Txnl2vCay0wnYWOYygA1V1qnqyK52eW2FyjUYmSJDWvqf5OC9kBNRDrBlmUCvVK7nfHJwtcPyAWoUhCFShcml35TXvOBcdtRFvSqAGOUpgMOKnhRmAv5FYOqEwaXbDLJpHGfnqTdPKYb9UrZ99MVf2WQasnnIuhv4K/n4z7tHtdewUp99hoWTvBI5v7oO6bHQuL5rs8mVYXPzcxd8ZaVw==; _clsk=pzv7j3|1645990372606|3|0|b.clarity.ms/collect"}
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
	while data == []:
		sleep(5)
		url_upwork = requests.get('https://www.upwork.com/search/jobs/?client_hires=0,1-9&contractor_tier=1,2&duration_v3=weeks&proposals=0-4,5-9&q=parsing&sort=recency', headers=headers, cookies=cookies).text
		blocks_upwork = BeautifulSoup(url_upwork, 'lxml').find_all('h4', class_=re.compile('job-title m-xs-top-bottom p-sm-right'))
		for block in blocks_upwork:
			data.append('https://www.upwork.com/freelance-jobs/apply/' + re.search(r'job/(.+)', block.find('a').get('href')).group(1))

async def parseKwork(data: list) -> None:
	# -----Kwork-----
	url_kwork = requests.get('https://kwork.ru/projects?c=41').text
	blocks_kwork = BeautifulSoup(url_kwork, 'lxml').find_all('div', class_=re.compile('wants-card__header-title first-letter breakwords pr250'))
	for block in blocks_kwork:
		data.append(block.find('a').get('href'))

async def parseFreelance(data: list) -> None:
	# -----Freelance-----
	url_freelance = requests.get('https://freelance.habr.com/tasks?q=%D1%82%D0%B5%D0%BB%D0%B5%D0%B3%D1%80%D0%B0%D0%BC+%D0%B1%D0%BE%D1%82&categories=development_bots').text
	blocks_freelance = BeautifulSoup(url_freelance, 'lxml').find_all('li', class_=re.compile('content-list__item'))
	for block in blocks_freelance:
		data.append('https://freelance.habr.com' + block.find('a').get('href'))

async def parseData() -> list:
	# -----Данные-----
	data = []
	await parseUpwork(data)
	await parseKwork(data)
	await parseFreelance(data)
	return data

# -----Запуск-----
data = []
while True:
	new_data = asyncio.run(parseData())
	if new_data != data:
		# -----Разность-----
		new_ads = list(set(new_data) - set(data))
		data = new_data
		for item in new_ads:
			# -----Проверка-----
			print(item)
			# -----Отправка-----
			# requests.post('https://api.telegram.org/bot1848165503:AAF5N91q9k_ZiIJPy8O4gOw35YrE0pasQ0A/sendMessage?chat_id=772328798&text=' + str(item))
	# -----Сон-----
	sleep(60)
