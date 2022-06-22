import inspect
import os
import sys
PYPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ROOTPATH = "{}/.".format(PYPATH)
sys.path.append(ROOTPATH)

import platform
import traceback
import time
import datetime
import json
import asyncio
import aiohttp
from modules.myutils.mydict import MyDict

def main():
    dict_prefs = {
        # https://www.jma.go.jp/bosai/common/const/area.json
        "016000": {
            "pref_name": "北海道",
            "pref_name_en": "Hokkaido",
            "raw_name": "石狩・空知・後志地方",
            "raw_name_en": "Ishikari Sorachi Shiribeshi",
            "office_name": "札幌管区気象台"
        },
        "020000": {
            "pref_name": "青森県",
            "pref_name_en": "Aomori",
            "raw_name": "青森県",
            "raw_name_en": "Aomori",
            "office_name": "青森地方気象台"
        },
        "030000": {
            "pref_name": "岩手県",
            "pref_name_en": "Iwate",
            "raw_name": "岩手県",
            "raw_name_en": "Iwate",
            "office_name": "盛岡地方気象台"
        },
        "040000": {
            "pref_name": "宮城県",
            "pref_name_en": "Miyagi",
            "raw_name": "宮城県",
            "raw_name_en": "Miyagi",
            "office_name": "仙台管区気象台"
        },
        "050000": {
            "pref_name": "秋田県",
            "pref_name_en": "Akita",
            "raw_name": "秋田県",
            "raw_name_en": "Akita",
            "office_name": "秋田地方気象台"
        },
        "060000": {
            "pref_name": "山形県",
            "pref_name_en": "Yamagata",
            "raw_name": "山形県",
            "raw_name_en": "Yamagata",
            "office_name": "山形地方気象台"
        },
        "070000": {
            "pref_name": "福島県",
            "pref_name_en": "Fukushima",
            "raw_name": "福島県",
            "raw_name_en": "Fukushima",
            "office_name": "福島地方気象台"
        },
        "080000": {
            "pref_name": "茨城県",
            "pref_name_en": "Ibaraki",
            "raw_name": "茨城県",
            "raw_name_en": "Ibaraki",
            "office_name": "水戸地方気象台"
        },
        "090000": {
            "pref_name": "栃木県",
            "pref_name_en": "Tochigi",
            "raw_name": "栃木県",
            "raw_name_en": "Tochigi",
            "office_name": "宇都宮地方気象台"
        },
        "100000": {
            "pref_name": "群馬県",
            "pref_name_en": "Gunma",
            "raw_name": "群馬県",
            "raw_name_en": "Gunma",
            "office_name": "前橋地方気象台"
        },
        "110000": {
            "pref_name": "埼玉県",
            "pref_name_en": "Saitama",
            "raw_name": "埼玉県",
            "raw_name_en": "Saitama",
            "office_name": "熊谷地方気象台"
        },
        "120000": {
            "pref_name": "千葉県",
            "pref_name_en": "Chiba",
            "raw_name": "千葉県",
            "raw_name_en": "Chiba",
            "office_name": "銚子地方気象台"
        },
        "130000": {
            "pref_name": "東京都",
            "pref_name_en": "Tokyo",
            "raw_name": "東京都",
            "raw_name_en": "Tokyo",
            "office_name": "気象庁"
        },
        "140000": {
            "pref_name": "神奈川県",
            "pref_name_en": "Kanagawa",
            "raw_name": "神奈川県",
            "raw_name_en": "Kanagawa",
            "office_name": "横浜地方気象台"
        },
        "150000": {
            "pref_name": "新潟県",
            "pref_name_en": "Niigata",
            "raw_name": "新潟県",
            "raw_name_en": "Niigata",
            "office_name": "新潟地方気象台"
        },
        "160000": {
            "pref_name": "富山県",
            "pref_name_en": "Toyama",
            "raw_name": "富山県",
            "raw_name_en": "Toyama",
            "office_name": "富山地方気象台"
        },
        "170000": {
            "pref_name": "石川県",
            "pref_name_en": "Ishikawa",
            "raw_name": "石川県",
            "raw_name_en": "Ishikawa",
            "office_name": "金沢地方気象台"
        },
        "180000": {
            "pref_name": "福井県",
            "pref_name_en": "Fukui",
            "raw_name": "福井県",
            "raw_name_en": "Fukui",
            "office_name": "福井地方気象台"
        },
        "190000": {
            "pref_name": "山梨県",
            "pref_name_en": "Yamanashi",
            "raw_name": "山梨県",
            "raw_name_en": "Yamanashi",
            "office_name": "甲府地方気象台"
        },
        "200000": {
            "pref_name": "長野県",
            "pref_name_en": "Nagano",
            "raw_name": "長野県",
            "raw_name_en": "Nagano",
            "office_name": "長野地方気象台"
        },
        "210000": {
            "pref_name": "岐阜県",
            "pref_name_en": "Gifu",
            "raw_name": "岐阜県",
            "raw_name_en": "Gifu",
            "office_name": "岐阜地方気象台"
        },
        "220000": {
            "pref_name": "静岡県",
            "pref_name_en": "Shizuoka",
            "raw_name": "静岡県",
            "raw_name_en": "Shizuoka",
            "office_name": "静岡地方気象台"
        },
        "230000": {
            "pref_name": "愛知県",
            "pref_name_en": "Aichi",
            "raw_name": "愛知県",
            "raw_name_en": "Aichi",
            "office_name": "名古屋地方気象台"
        },
        "240000": {
            "pref_name": "三重県",
            "pref_name_en": "Mie",
            "raw_name": "三重県",
            "raw_name_en": "Mie",
            "office_name": "津地方気象台"
        },
        "250000": {
            "pref_name": "滋賀県",
            "pref_name_en": "Shiga",
            "raw_name": "滋賀県",
            "raw_name_en": "Shiga",
            "office_name": "彦根地方気象台"
        },
        "260000": {
            "pref_name": "京都府",
            "pref_name_en": "Kyoto",
            "raw_name": "京都府",
            "raw_name_en": "Kyoto",
            "office_name": "京都地方気象台"
        },
        "270000": {
            "pref_name": "大阪府",
            "pref_name_en": "Osaka",
            "raw_name": "大阪府",
            "raw_name_en": "Osaka",
            "office_name": "大阪管区気象台"
        },
        "280000": {
            "pref_name": "兵庫県",
            "pref_name_en": "Hyogo",
            "raw_name": "兵庫県",
            "raw_name_en": "Hyogo",
            "office_name": "神戸地方気象台"
        },
        "290000": {
            "pref_name": "奈良県",
            "pref_name_en": "Nara",
            "raw_name": "奈良県",
            "raw_name_en": "Nara",
            "office_name": "奈良地方気象台"
        },
        "300000": {
            "pref_name": "和歌山県",
            "pref_name_en": "Wakayama",
            "raw_name": "和歌山県",
            "raw_name_en": "Wakayama",
            "office_name": "和歌山地方気象台"
        },
        "310000": {
            "pref_name": "鳥取県",
            "pref_name_en": "Tottori",
            "raw_name": "鳥取県",
            "raw_name_en": "Tottori",
            "office_name": "鳥取地方気象台"
        },
        "320000": {
            "pref_name": "島根県",
            "pref_name_en": "Shimane",
            "raw_name": "島根県",
            "raw_name_en": "Shimane",
            "office_name": "松江地方気象台"
        },
        "330000": {
            "pref_name": "岡山県",
            "pref_name_en": "Okayama",
            "raw_name": "岡山県",
            "raw_name_en": "Okayama",
            "office_name": "岡山地方気象台"
        },
        "340000": {
            "pref_name": "広島県",
            "pref_name_en": "Hiroshima",
            "raw_name": "広島県",
            "raw_name_en": "Hiroshima",
            "office_name": "広島地方気象台"
        },
        "350000": {
            "pref_name": "山口県",
            "pref_name_en": "Yamaguchi",
            "raw_name": "山口県",
            "raw_name_en": "Yamaguchi",
            "office_name": "下関地方気象台",
        },
        "360000": {
            "pref_name": "徳島県",
            "pref_name_en": "Tokushima",
            "raw_name": "徳島県",
            "raw_name_en": "Tokushima",
            "office_name": "徳島地方気象台"
        },
        "370000": {
            "pref_name": "香川県",
            "pref_name_en": "Kagawa",
            "raw_name": "香川県",
            "raw_name_en": "Kagawa",
            "office_name": "高松地方気象台"
        },
        "380000": {
            "pref_name": "愛媛県",
            "pref_name_en": "Ehime",
            "raw_name": "愛媛県",
            "raw_name_en": "Ehime",
            "office_name": "松山地方気象台"
        },
        "390000": {
            "pref_name": "高知県",
            "pref_name_en": "Kochi",
            "raw_name": "高知県",
            "raw_name_en": "Kochi",
            "office_name": "高知地方気象台"
        },
        "400000": {
            "pref_name": "福岡県",
            "pref_name_en": "Fukuoka",
            "raw_name": "福岡県",
            "raw_name_en": "Fukuoka",
            "office_name": "福岡管区気象台"
        },
        "410000": {
            "pref_name": "佐賀県",
            "pref_name_en": "Saga",
            "raw_name": "佐賀県",
            "raw_name_en": "Saga",
            "office_name": "佐賀地方気象台"
        },
        "420000": {
            "pref_name": "長崎県",
            "pref_name_en": "Nagasaki",
            "raw_name": "長崎県",
            "raw_name_en": "Nagasaki",
            "office_name": "長崎地方気象台"
        },
        "430000": {
            "pref_name": "熊本県",
            "pref_name_en": "Kumamoto",
            "raw_name": "熊本県",
            "raw_name_en": "Kumamoto",
            "office_name": "熊本地方気象台"
        },
        "440000": {
            "pref_name": "大分県",
            "pref_name_en": "Oita",
            "raw_name": "大分県",
            "raw_name_en": "Oita",
            "office_name": "大分地方気象台"
        },
        "450000": {
            "pref_name": "宮崎県",
            "pref_name_en": "Miyazaki",
            "raw_name": "宮崎県",
            "raw_name_en": "Miyazaki",
            "office_name": "宮崎地方気象台"
        },
        "460100": {
            "pref_name": "鹿児島県",
            "pref_name_en": "Kagoshima",
            "raw_name": "鹿児島県（奄美地方除く）",
            "raw_name_en": "Kagoshima (Excluding Amami)",
            "office_name": "鹿児島地方気象台"
        },
        "471000": {
            "pref_name": "沖縄県",
            "pref_name_en": "Okinawa Main Island",
            "raw_name": "沖縄本島地方",
            "raw_name_en": "Okinawa Main Island",
            "office_name": "沖縄気象台"
        }
    }
    ok, err = MyDict(dict_prefs).validate_required_keyexist_type(
        {
            "[pref_code]": {
                    "pref_name": str,
                    "pref_name_en": str,
                    "raw_name": str,
                    "raw_name_en": str,
                    "office_name": str
            }
        }
    )
    if not ok:
        raise err
    
    weather_forecasts = None
    try:
        datetime_target = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours = 9), "JST")) - datetime.timedelta(days = 1)
        dir_output_rawdata = "{0}/outputs/{1}".format(PYPATH, datetime_target.strftime("%Y%m%d"))
        os.makedirs(dir_output_rawdata, exist_ok = True)
        weather_forecasts = asyncio.run(
            download_jsons_weather_forecast_async(
                [{"pref_code": key} for key in dict_prefs.keys()],
                dir_output_rawdata,
                timeout_conn = 10,
                timeout_read = 5,
                cnt_retry_req = 3,
                interval_req_sec = 1
            )
        )
        # weather_forecasts = asyncio.get_event_loop().run_until_complete( # こっちはPython3.6までの書き方
        #     download_jsons_weather_forecast_async(
        #         [{"pref_code": key} for key in dict_prefs.keys()],
        #         dir_output_rawdata,
        #         timeout_conn = 10,
        #         timeout_read = 5,
        #         cnt_retry_req = 3,
        #         interval_req_sec = 1
        #     )
        # )
    except Exception as e:
        raise e
    print("len(weather_forecasts): ", len(weather_forecasts))
    # print(weather_forecasts)

async def download_jsons_weather_forecast_async(
    info_prefs,
    dir_output_rawdata,
    timeout_conn = 10,
    timeout_read = 30,
    cnt_retry_req = 3,
    interval_req_sec = 3):
    async def run(
        sess,
        info_pref,
        dir_output_rawdata,
        timeout_read,
        cnt_retry_req,
        interval_req_sec):
        '''
        指定した都道府県の天気予報のjsonをダウンロードする．
        - Args
            - sess:aiohttp.ClientSession: 
            - info_pref:dict: ある都道府県に関する辞書型の下記情報
                - pref_code:str: 
            - timeout_read:float: 
            - cnt_retry_req:int: 
            - interval_req_sec:float: 
        '''
        url = "https://www.jma.go.jp/bosai/forecast/data/forecast/{}.json".format(info_pref["pref_code"])
        for i in range(cnt_retry_req):
            try:
                async with sess.get(url, timeout = timeout_read) as res:
                    status = res.status
                    rawdata = await res.json()
                    with open(
                        "{0}/rawdata_weather_forecast_pref{1}.json".format(dir_output_rawdata, info_pref["pref_code"]),
                        "w",
                        encoding = "utf8"
                    ) as f:
                        f.write(json.dumps(
                            rawdata,
                            indent = 4,
                            ensure_ascii = False
                        ))
                    return {
                        "pref_code": info_pref["pref_code"],
                        "rawdata": rawdata
                    }
            except Exception as e:
                if i == cnt_retry_req - 1:
                    # リトライ回数上限に到達した上での例外発生の場合
                    raise type(e)("Failed in downloading from url '{url}' after {cnt_retry} retrying. Detail: {err}".format(
                        url = url,
                        cnt_retry = cnt_retry_req,
                        err = traceback.format_exc()
                    ))
                time.sleep(interval_req_sec)
    # WARNING: `trust_env=True`にしないとリクエスト通らない
    ## https://stackoverflow.com/a/63364551/15842506
    async with aiohttp.ClientSession(trust_env = True) as sess: # MEMO: `conn_timeout = timeout_conn`がなんか非推奨になっててtimeoutに集約されてる…
        res = await asyncio.gather(*[
            run(
                sess,
                info_pref,
                dir_output_rawdata,
                timeout_read,
                cnt_retry_req,
                interval_req_sec
            )
            for info_pref in info_prefs
        ])
        return res



async def download_jsons_weather_forecast_async_with_semaphore(
    info_prefs,
    dir_output_rawdata,
    timeout_conn = 10,
    timeout_read = 30,
    cnt_retry_req = 3,
    interval_req_sec = 3):
    async def run(
        sess,
        info_pref,
        dir_output_rawdata,
        timeout_read,
        cnt_retry_req,
        interval_req_sec,
        async_limit = 1):
        '''
        指定した都道府県の天気予報のjsonをダウンロードする．
        - Args
            - sess:aiohttp.ClientSession: 
            - info_pref:dict: ある都道府県に関する辞書型の下記情報
                - pref_code:str: 
            - timeout_read:float: 
            - cnt_retry_req:int: 
            - interval_req_sec:float: 
        '''
        with await asyncio.Semaphore(async_limit):
            url = "https://www.jma.go.jp/bosai/forecast/data/forecast/{}.json".format(info_pref["pref_code"])
            for i in range(cnt_retry_req):
                try:
                    async with sess.get(url, timeout = timeout_read) as res:
                        status = res.status
                        rawdata = await res.json()
                        with open(
                            "{0}/rawdata_weather_forecast_pref{1}.json".format(dir_output_rawdata, info_pref["pref_code"]),
                            "w",
                            encoding = "utf8"
                        ) as f:
                            f.write(json.dumps(
                                rawdata,
                                indent = 4,
                                ensure_ascii = False
                            ))
                        return {
                            "pref_code": info_pref["pref_code"],
                            "rawdata": rawdata
                        }
                except Exception as e:
                    if i == cnt_retry_req - 1:
                        # リトライ回数上限に到達した上での例外発生の場合
                        raise type(e)("Failed in downloading from url '{url}' after {cnt_retry} retrying. Detail: {err}".format(
                            url = url,
                            cnt_retry = cnt_retry_req,
                            err = traceback.format_exc()
                        ))
                    time.sleep(interval_req_sec)
    # WARNING: `trust_env=True`にしないとリクエスト通らない
    ## https://stackoverflow.com/a/63364551/15842506
    async with aiohttp.ClientSession(trust_env = True) as sess: # MEMO: `conn_timeout = timeout_conn`がなんか非推奨になっててtimeoutに集約されてる…
        res = await asyncio.gather(*[
            run(
                sess,
                info_pref,
                dir_output_rawdata,
                timeout_read,
                cnt_retry_req,
                interval_req_sec,
                async_limit = len(info_prefs)
            )
            for info_pref in info_prefs
        ])
        return res



if __name__ == "__main__":
    if platform.system() == "Windows":
        # `asyncio.run()`で「RuntimeError: Event loop is closed」を出さないようにするWindowsのみの設定
        ## https://stackoverflow.com/a/66772242/15842506
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    main()
