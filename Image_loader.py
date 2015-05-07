import urllib.request as req
import time

def saver(url, filename):
    return req.urlretrieve(url, filename)

date = "20150507"
ourl = "http://i.weather.com.cn/i/product/pic/l/sevp_aoc_rdcp_sldas_ebref_aswc_l88_pi_"

for hh in range(10, 17):
    for mm in range(0, 6):
        time_stamp = (str(hh).rjust(2, "0") + str(mm).ljust(2, "0"))
        saver(ourl + date + time_stamp + "00001.gif", date + time_stamp + ".gif")
        time.sleep(5)
