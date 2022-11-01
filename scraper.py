import requests
import json
from bs4 import BeautifulSoup
import re

# #################### get_citations_needed_count function #################### #

def get_citations_needed_count(url):
    '''
    A function takes in a url string and returns an the number of citations needed as int
    '''
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    citations = soup.find_all('a', title='Wikipedia:Citation needed')
    citations_count = len(citations)
    return citations_count


# #################### get_citations_needed_report function #################### #

def get_citations_needed_report(url):
    '''
    A function takes in a url string and returns a report string of citations needed as a list.
    '''
    citation_needed=[]
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    citations_para= soup.find_all('p')
    for para in citations_para:
        if para.find('a', title='Wikipedia:Citation needed'):
            para=para.text.strip().replace('[citation needed]','')
            citation_needed.append(para)
    return citation_needed

def saved_json_data(citations):
    '''
    A function takes in a list of citations and write it as a json string inside citations_needed.json file.
    '''
    json_data=json.dumps(citations)
    with open('citations_needed.json','w') as file:
        file.write(json_data)

        
# #################### citations needed outputs #################### #

if __name__=="__main__":

    print('\n# #################### Web Scraping #################### #\n')
    url = 'https://en.wikipedia.org/wiki/Sesame'
    print('The number of citations needed is => ',get_citations_needed_count(url))
    print('\n************************************************************************************************')
    data=get_citations_needed_report(url)
    saved_json_data(data)
    for i in range(len(data)):  
        print(f'\nparagraph {i+1} => {data[i]}\n')
        print('************************************************************************************************')
