import requests
html_text = requests.get('https://zexprwire.com/pressroom/').text
print(html_text)
with open('zexprwire.txt', 'w', encoding='utf-8') as f:
    f.write(html_text)
