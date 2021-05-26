import string
import random


def rnd():
    letters = string.ascii_uppercase
    return ( ''.join(random.choice(letters) for i in range(20)) )

def main():
    xss = load('./attack.txt')
    attack_array = []
    for attack in xss:
        attack_array.append(gen(attack.strip()))
    #print(attack_array)
    save(f'./{rnd()}.xml', chunks(attack_array, 25))

def gen(attack):
    random = rnd() + rnd()
    return """
  <item>
    <title>%s</title>
    <link>http://wwww.%s.com</link>
    <description>
      %s
    </description>
  </item>""" % (rnd(), (rnd() + rnd()), attack)

def load(path):
    content = None
    with open(path) as f:
        content = f.readlines()
    return content

def save(path, content):
    i = 0
    for l in content:
        i += 1
        start = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
  <title>xss %s</title>
  <link>https://www.%s.com</link>
  <description>%s</description>""" % (i, rnd(), rnd())
        end = """
</channel>
</rss>"""
        with open(f"./XSS/site/attack/{i}.xml", 'a') as f:
            f.write(start)
            print(content)
            for attack in l:
                f.write(attack)
            f.write(end)
    #pass

def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

if __name__ == "__main__":
    main()


#http://localhost/attack/1.xml