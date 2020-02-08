from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
from GetWeatherApp.lib import delAccent

bsearch = 'https://www.google.com/search?q=Clima%20'

local = str(input('Digite o País ou Cidade que deseja Consultar o Clima: ')).title()
local_treat = ''

if ' ' in local:
    local_tr = local.replace(' ', '%20')
else:
    local_tr = local

local_tra = delAccent(local_tr)

link = bsearch + local_tra

req = Request(url=link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                               'like Gecko) Chrome/77.0.3865.120 Safari/537.36 OPR/64.0.3417.170'})
uClient = urlopen(req)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, 'html.parser')

try:
    dgree = str(page_soup.findAll("span", {"style": "display:inline"})[0])
    clim = str(page_soup.findAll("span", {"class": "vk_gy vk_sh"})[0])
    date = str(page_soup.findAll("div", {"class": "vk_gy vk_sh"})[0])

    print(f'\033[32;1mLocal Pesquisado: {local}')
    print('\033[34;1mSensação Térmica: ', end='')
    for c0 in range(len(dgree)):
        if dgree[c0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or dgree[c0] == '-':
            print(f'{dgree[c0]}', end='')
        else:
            pass
    print(' ºC')

    clim = clim[clim.find('>')+1:]
    print(f'Clima: {clim[:clim.find("<")]}')

    date = date[date.find('>')+1:]
    print(f'Data: {(date[:date.find("<")]).capitalize()} Hrs')

except IndexError:
    print('\033[31;1mLocal Inválido, considere rever o Mesmo!\033[m')
