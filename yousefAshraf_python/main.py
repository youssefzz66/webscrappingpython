import requests
import bs4
counter = 0
for i in range(0, 1550//20):
    url = f'https://wuzzuf.net/a/IT-Software-Development-Jobs-in-Egypt?ref=browse-jobs-btm&start={i}'
    page = requests.get(url)

    soup = bs4.BeautifulSoup(page.content, "html.parser")
    job = []
    part = []
    name = []
    city = []

    job = soup.findAll('h2', {'class': "css-m604qf"})
    part = soup.findAll('span', {'class': "css-1ve4b75 eoyjyou0"})
    city = soup.findAll('span', {'class': "css-5wys0k"})
    name = soup.findAll('a', {'class': "css-17s97q8"})
    for j in range(len(job)):
        print(f'number of job is :({counter + 1})')
        counter += 1

        job.append(print("job title is :" + job[j].text))
        name.append(print("name of company :" + name[j].text))
        part.append(print("work is :" + part[j].text))
        city.append(print("city is :" + city[j].text))
        print()
