import inspect
import os
import sys
PYPATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ROOTPATH = "{}/.".format(PYPATH)
sys.path.append(ROOTPATH)
from modules.myutils.myrequests import MyRequests
from requests.exceptions import RequestException

def main():
    req = MyRequests(
        timeout_connect = 10,
        timeout_read = 30,
        cnt_retry_request = 3,
        interval_requests_sec = 3)
    test_post(req)
    

    
def test_post(req):
    try:
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authentication": "Bearer xxxxxx"
        }
        payload = {"id": 6}
        url = "urlurlurlurlurlurlurlurl"
        res = req.post(url, headers, payload)
        if res.status_code != 204:
            raise RequestException("ステータスコードがエラーだぉ")
    except Exception as e:
        raise e






if __name__ == "__main__":
    main()