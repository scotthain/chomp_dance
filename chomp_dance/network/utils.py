import parsel
import requests

def find_latest_version(key=None):
    r = requests.request("GET", "https://ftp.gnu.org/gnu/bison")
    sel = parsel.Selector(text=r.text)
    [a.attrib["href"] for a in sel.css("a")]    
    return "sooooooo"
