from bs4 import BeautifulSoup
import requests
import fake_useragent







def parser_habr(back_data):
    link = "https://habr.com/ru/flows/develop/articles/"




    usag= fake_useragent.UserAgent().random



    headr = {'user-agent':usag}


    response = requests.get(link,headers=headr).text


    soup = BeautifulSoup(response,'lxml')



    block = soup.find('div',class_='tm-articles-list')

    post_all = block.find_all("article",class_='tm-articles-list__item')
    new_post = post_all[0]

    post_id = new_post.get('id')


  

    if post_id != back_data: 
        
        div_post = new_post.find('div',class_="tm-article-snippet tm-article-snippet")
        if div_post  is not None:
            print('ok')
        else:
            div_post = new_post.find('div',class_="tm-article-body tm-article-snippet__lead")

    
        
       

       
        
 
        post_h2 = div_post.find('h2',class_="tm-title tm-title_h2")
        post_name = post_h2.find('a',class_='tm-title__link',href=True).text
        try:
            post_url_05 = div_post.find('a',class_='tm-article-snippet__readmore',href=True).get('href')
            post_url = f"https://habr.com{post_url_05}"
        except AttributeError:
            post_url = None
            print('print error url ')

        try:
            post_text = div_post.find('div',class_="article-formatted-body article-formatted-body article-formatted-body_version-1").text
            text = f'{post_name} :{post_text}'
        except AttributeError:
            try:
                post_text =  div_post.find('div',class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
                paragraphs = [p.text for p in post_text.find_all('p')]
                text = f"{post_name} : ".join(paragraphs)
            except AttributeError:
                post_text =  div_post.find('div',class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
                paragraphs = [p.text for p in post_text.find_all('p')]
                text = f"{post_name} : ".join(paragraphs)
                    
        
        sp = [post_id, text, post_url,]
        return sp
    else:
       sp = [post_id,None]
       return sp


 
