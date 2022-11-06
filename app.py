import streamlit as st
import requests
def getAllBookstore():
    url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' # 在這裡輸入目標 url
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    x =response.json()
    return x
def getdistrictOption(items,target):
    optionList = []
    for item in items:
        name = item['cityname']
        if target not in name :
            continue
        name.strip()
def getdistrictOption(items, target):
    optionList=[]
for item in items:
    name = item['cityname']
    name.strip()
    district = name[:5]
    if len(district)== 0 :
        continue
    else:
        return optionList






def getspecificbookstore(items,country):
    specificbookstore = []
    for item in items:
        name = item['cityname']
        if country in name:
            
def app():
    bookstoreList = getAllBookstore()
    countryoption = getCountryOption(bookstoreList)
    bookstore =getAllBookstore()
    st.header('特色書店地圖')
    st.metric('Total bookstore',len(bookstore)) 
    county = st.selectbox('請選擇縣市',countryoption)
    districtOption =   getdistrictOption(bookstore, country) 
    district = st.multiselect('請選擇區域', districtOption)



def getCountryOption(items):
    optionList = []
    for item in items:
        name = item.index['cityname'][0:3]

        if name in optionList:
            continue
        else:
            optionList.append(name)
        return optionList   








if __name__ == '__main__':
        app()