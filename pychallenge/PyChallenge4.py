import requests;
import re;

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
response = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022')

r = response.text
print r

pat = re.search("and the next nothing is (\d{1,8})",r)


while( pat != None ):
    num = pat.group(1)
    print num
    uuu = url%(num)
    r = requests.get(uuu).text
    pat = re.search("and the next nothing is (\d{1,8})",r)
    
print r

"""
16044
Yes. Divide by two and keep going.

66831
peak.html

"""