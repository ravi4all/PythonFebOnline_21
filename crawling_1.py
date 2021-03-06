import urllib.request as url
import bs4

response = url.urlopen('https://www.freshersworld.com/python-jobs/3535127')
page = bs4.BeautifulSoup(response, 'lxml')

title = page.find('h3')
print(title.text)

qualification = page.find('span', class_='qualifications')
print(qualification.text)

skills = page.find('span', class_='eligibility-skills')
print(skills.text)

desc = page.find('span', class_='desc')
print(desc.text)
