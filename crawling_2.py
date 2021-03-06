import urllib.request as url
import bs4

response = url.urlopen('https://www.freshersworld.com/python-jobs/3535127')
page = bs4.BeautifulSoup(response, 'lxml')

title = page.find_all('h3', class_='latest-jobs-title')
qualification = page.find_all('span', class_='qualifications')
skills = page.find_all('span', class_='eligibility-skills')
desc = page.find_all('span', class_='desc')

for i in range(len(title)):
    print("Job title :",title[i].text)
    print("Qualification :",qualification[i].text)
    print("Skill required :",skills[i].text)
    print("JD :",desc[i].text)
    print('*' * 50)
