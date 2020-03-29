#This Is Python Script Written By -Saurav-Kumar-Bhatt- To Scrap Data From AnimePahe.com
#This Script Utilize Fake XMLHTTPREQUEST To Grab JSON Data 
#This Script Is Now Unable To ByPass bit.ly (Work Is In Progress)
import requests,sys,re
name=input('Enter The Name Of The Anime : ')
name=name.replace(' ','%20')
reqObj=requests.get(f'https://animepahe.com/api?m=search&l=8&q={name}')
search_parsed_data=reqObj.json()
total_search_result=search_parsed_data['total']
print('Total Results Found ----> '+str(total_search_result))
if total_search_result==0 :
    sys.exit()
for i in range(0,total_search_result,1):
    print(str(i+1)+'. '+search_parsed_data['data'][i]['title'])
select=int(input('Enter The Serial Number Of Anime : '))
print('*'*len('Anime Selected'))
print('Anime Selected')
print('*'*len('Anime Selected'))
print(search_parsed_data['data'][select-1]['title'])
print('*'*len(search_parsed_data['data'][select-1]['title']))
select_id = search_parsed_data['data'][select-1]['id']
episode_url=f'https://animepahe.com/api?m=release&id={select_id}&l=30&sort=episode_asc&page=1'
episode_reqObj=requests.get(episode_url)#page No. must be checked usinge json
episodes=episode_reqObj.json()
print('Total Episodes : '+str(episodes['total'])+' ')
episode_selected=int(input('Enter The Episode Number --> '))
page_number = episode_selected//31
page_number+=1
episode_url=f'https://animepahe.com/api?m=release&id={select_id}&l=30&sort=episode_asc&page={page_number}'
episode_reqObj=requests.get(episode_url)
episodes=episode_reqObj.json()
session_key=None
episode_in_json=episode_selected-30*(page_number-1)
episode_in_json-=1
session_key=episodes['data'][episode_in_json]['session']
download_reObj=requests.get(f'https://animepahe.com/api?m=link&id={select_id}&session={session_key}&p=kwik')
download_Parsed = download_reObj.json()
unfiltered_download = str(download_Parsed)
regObj = re.compile(r"'http(\S+)'")
links = regObj.findall(unfiltered_download)
for i in range(0,len(links)):
    links[i] = 'http'+links[i]
print('*'*len('Links (In Acending Order Of Quality) --->'))
print('Links (In Acending Order Of Quality) --->')
print('*'*len('Links (In Acending Order Of Quality) --->'))
print(links)
