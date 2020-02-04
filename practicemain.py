from werkzeug.utils import secure_filename
import requests
import PyPDF2 
from flask import *
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
from parsel import Selector
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from flask import jsonify

app = Flask(__name__)
@app.route('/', methods =['GET', 'POST'])
def basic():
    return render_template('index.html')

@app.route('/github', methods =['GET', 'POST'])
def githubscore():
    return render_template('github.html',t= "hello")
@app.route('/barchart', methods =['GET', 'POST'])
def bar():
    return render_template('Bar Chart.html',t= "hello")

@app.route('/linkedin', methods =['GET', 'POST'])
def linkedinscore():
   if request.method == "POST":
        link = request.form["linkedinprofile"]
        #SCRAPER CODE BEGINS
        chromedriver = "./chromedriver"
        driver = webdriver.Chrome(chromedriver)
        driver.get("https://www.linkedin.com/login")
        username = driver.find_element_by_id("username")
        username.send_keys('rahulgarg8438@gmail.com')
        sleep(0.5)
        password = driver.find_element_by_id("password")
        password.send_keys('rahul28071998')
        sleep(0.5)
        log_in_button = driver.find_element_by_class_name("btn__primary--large")
        log_in_button.click()
        userAddress = link
        driver.get(userAddress)
        page = driver.page_source
        sel = Selector(text=page)
        dic = {}
        dic['username'] =link
        try:
            name = sel.xpath('/html/body/div[5]/div[4]/div[3]/div/div/div/div/div[2]/main/div[1]/div/section/div[2]/div[2]/div[1]/ul[1]/li[1]').extract_first().split('>')[1].split("<")[0].strip()
        except:
            name = "none"   
        dic['Name'] = name 
        try:
            bio = sel.xpath('//h2/text()').extract_first().strip()
        except:
            bio = "none"
        
        dic['bio'] =bio  
        try:
            designation = sel.xpath('/html/body/div[5]/div[4]/div[3]/div/div/div/div/div[2]/main/div[1]/div/section/div[2]/div[2]/div[2]/ul/li[1]/a/span').extract_first().split('>')[1].split("<")[0].strip()
        except:
            designation = "none"
        #print("designation:"+designation)
        dic['designation'] = designation
        try:
            institute = sel.xpath('/html/body/div[5]/div[4]/div[3]/div/div/div/div/div[2]/main/div[1]/div/section/div[2]/div[2]/div[2]/ul/li[2]/a/span').extract_first().split('>')[1].split("<")[0].strip()
        except:
            institute = "none"
       # print("institute:"+institute)
        dic['institute'] = institute
        
        try:
            summaryMoreButton = driver.find_element_by_class_name("lt-line-clamp__more")
            text = summaryMoreButton.text.split()
            action=ActionChains(driver)
            action.move_to_element(summaryMoreButton).perform()
            if(text[1]=="more"):
                summaryMoreButton.click()
        except:
            print("button not present")

        try:
            summary = driver.find_element_by_class_name("lt-line-clamp__raw-line")
            summary =  summary.text
        except:
            summary = "none"
        print("summary:"+summary)
        dic['summary']=summary.split('\n')

        skilldic = {}
        #load all page
        try:
            career = driver.find_element_by_xpath("/html/body/div[5]/div[4]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/span/div/section")
            career = career.text.split('\n')
            # career=career.lower()
            ls=[]
            for i in range(len(career)):
                if career[i]=='Company Name':
                    ls.append({
                        "company":career[i+1],
                        "designation":career[i-1]
                    })
        except:
            career = "None"
            ls = "None"

        dic["career"] = ls
        try:
            elem = driver.find_element_by_tag_name("body")

            no_of_pagedowns = 10

            while no_of_pagedowns:
                elem.send_keys(Keys.PAGE_DOWN)
                sleep(0.1)
                no_of_pagedowns-=1
            driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
        except:
            print("page not scrollable")
        #scrape importtant skills

        try:
            skills = driver.find_element_by_css_selector(".pv-skill-categories-section__top-skills.pv-profile-section__section-info.section-info.pb1")
            skills = skills.text.split('\n')
            i=0
            length = len(skills)
            while(i<length):
                if(i<length-1):
                    if(skills[i+1].startswith("See ")):
                        skilldic[skills[i].lower()] = skills[i+2]
                        i = i+4
                    else: 
                        skilldic[skills[i].lower()] = 0
                        i = i+1
                else:
                    skilldic[skills[i].lower()] = 0
                    i = i+1  
        except:
            print("no important skills")
        #click more button

        try:
            skillMoreButton =driver.find_element_by_css_selector(".pv-profile-section__card-action-bar.pv-skills-section__additional-skills.artdeco-container-card-action-bar")
            text = skillMoreButton.text.split()

            action=ActionChains(driver)
            action.move_to_element(skillMoreButton).perform()

            if(text[1]=="more"):
                    skillMoreButton.click()        
        except:
            print("more skills button not working")
        ##scrape other skills        
        try:
            tools = driver.find_elements_by_css_selector('.pv-skill-category-list__skills_list.list-style-none')
            for i in tools:
                i = i.text.split("\n")
                length = len(i)
                j=0
                while(j<length):
                    if(j<length-1):
                        if(i[j+1].startswith("See ")):
                            skilldic[i[j]] = i[j+2]
                            j = j+3
                        else: 
                            skilldic[i[j]] = 0
                            j = j+1
                    else:
                        skilldic[i[j]] = 0
                        j = j+1
                        
        except:
            print("no other skills")

        #print(skilldic)
        dic['skilldic'] = skilldic
        dic['skilldicKeyArr'] = list(skilldic.keys())
        #scrapping posts
        #navigating to the post page
        load = True
        try:
            post = userAddress+"detail/recent-activity/shares/"
            driver.get(post)
        except:
            print("post page not loaded")
            load = False
            

        #loading the page
        if(load==True):
            try:
                elem = driver.find_element_by_tag_name("body")

                no_of_pagedowns = 4

                while no_of_pagedowns:
                    elem.send_keys(Keys.PAGE_DOWN)
                    sleep(0.5)
                    no_of_pagedowns-=1
                driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
                sleep(3)
            except:
                print("page not scrollable")
        try:
            image_url = driver.find_element_by_xpath("/html/body/div[5]/div[4]/div[3]/div/div/div/div/div[2]/main/div[1]/div/section/div[2]/div[1]/div[1]/div/div/button/img")
            print(image_url)
        except:
            print("no image")
        #get post
        try:
            post = driver.find_elements_by_css_selector(".feed-shared-update-v2__description-wrapper")
            ls = []
            for i in post:
                posts = i.text.split('\n')
                ls.append(posts)
            dic['posts'] = posts
        except:
            print("no post found")
            #navigating to the comment page
        load = True
        try:
            comment = userAddress+"detail/recent-activity/"
            driver.get(comment)
        except:
            print("comment page not loaded")
            load = False
            

        #loading the page
        if(load==True):
            try:
                elem = driver.find_element_by_tag_name("body")

                no_of_pagedowns = 4

                while no_of_pagedowns:
                    elem.send_keys(Keys.PAGE_DOWN)
                    ##sleep(0.5)
                    no_of_pagedowns-=1
                driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")
                ##sleep(3)
            except:
                print("page not scrollable")

                

        #get post
        try:
            comments = driver.find_elements_by_css_selector(".feed-shared-text__text-view.feed-shared-text-view.white-space-pre-wrap.break-words.ember-view")
            ls = []
            for i in comments:
                comments = i.text.split('\n')
                ls.append(comments)
                #print(comments)
            dic['comments'] = comments
        except:
            print("no post found")
        # with open('json_file.json',"w") as file_write:
        #   app_json = json.dump(dic,file_write)
        linkedinUsername = dic['username'].split("linkedin.com/in/")
        linkedinUsername = linkedinUsername[1].split('/')[0]
        dic['linkedinUsername']=linkedinUsername
        reqskillarr = []
        # temprequireskill = {}
        reqSkill = (request.form["skills"]).lower().split(",")
        for i in reqSkill:
            if i in dic['skilldic'].keys():
                if int(dic['skilldic'][i]) == 0:
                    reqskillarr.append({
                        "name": i,
                        "value": 5
                    })
                elif int(dic['skilldic'][i]) > 0 and int(dic['skilldic'][i]) < 20:
                    reqskillarr.append({
                        "name": i,
                        "value": int(dic['skilldic'][i])*5
                    })
                elif int(dic['skilldic'][i]) > 20:
                    reqskillarr.append({
                        "name": i,
                        "value": 100
                    })
        dic['reqskillarr'] = reqskillarr
        print(dic)
        # print("\n\n" + str(temprequireskill))
        return render_template('linkedinanalysis.html', linkObj=dic)
   return render_template('linkedin.html',t= "hello")


@app.route('/resume', methods =['GET', 'POST'])
def resumescore():
   if request.method == "POST":
        f = request.files['file']
        f.save(secure_filename(f.filename))
        pdfFileObj = open(str(f.filename), 'rb') 
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
        pageObj = pdfReader.getPage(0)
        text = pageObj.extractText()
        cv = text.lower()
        body = {
            "documents": [
                {
                    "language": "en",
                    "id": "1",
                    "text": cv
                }
            ]
        }
        r = requests.post("https://resumeanalyzer.cognitiveservices.azure.com/text/analytics/v2.1-preview/entities",headers={"Ocp-Apim-Subscription-Key":"2a546b09cd7a4b23baf3fa93663fe684","Content-Type":"text/json"},json=body)
        print(str(r.json()))
        quanArr = []
        r = r.json()
        r = r["documents"][0]["entities"]
        for i in r:
            if i['type']=="Quantity":
                quanArr.append(i)
        print(quanArr)
        pdfFileObj.close() 
        skill = (request.form["skills"]).lower().split(",")
        cv = cv.replace("\n",'')
        cv = cv.split(" ")
        dic = {}
        print(cv,skill)
        for i in cv:
            for j in skill:
                if i==j:
                    if j not in dic:
                        dic[j] = 1
                    else:
                        dic[j]=dic[j]+1
        sum =0
        for j in skill:
            if j not in dic:
                dic[j]=5
            elif dic[j]>4:
                dic[j] = 95
            else:
                dic[j] = dic[j]*25 
            sum =sum +dic[j]
        avg = sum/len(dic)   
        print(dic)
        mainObj = {"obj":dic,"arr":list(dic.keys()),"quanArr":quanArr}
        print(str(mainObj))
        return render_template('analyze.html',t=mainObj)
   return render_template('cv.html',t= "hello")


@app.route('/route', methods=['GET', 'POST'])

def patientcall():
   if request.method == "POST":
        if request.form["submit"] =='add':
            name = request.form['name']
            db.child("patient").push(name)
            todo = db.child("patient").get()
            # return todo.val()
            to = todo.val()
            return render_template('patient.html', t= to.values())
   return render_template('patient.html')

if __name__ == '__main__':
    app.run(debug=True)    




