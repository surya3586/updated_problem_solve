from xml.dom.minidom import parse, Text
from datetime import timedelta, date

def main(x, y) :
    doc = parse('test_payload1.xml')
    DEPART = doc.getElementsByTagName("DEPART")[0]
    RETRUN = doc.getElementsByTagName("RETURN")[0]
    DEPART.firstChild.nodeValue = date.today() + timedelta(days=x)
    RETRUN.firstChild.nodeValue = date.today() + timedelta(days=y)

    with open('new_payload1.xml','w') as f:
        f.write(doc.toxml())

if __name__ == "__main__":
    main(5, 8)