# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:27:20 2017

@author: Jonathan
"""

def web_handler(request):
    method = request['REQUEST_METHOD']
    if method =="GET":
        query_dict = request['GET']
        topic = query_dict.get('topic',None)
        if topic == None:
            return "Must provide topic"
        else:
            topic = topic.lower()
            to_send = "https://en.wikipedia.org/w/api.php?titles={}&action;=query∝=extracts&redirects;=1&format;=json&exintro;=".format(topic)
            r = requests.get(to_send)
            data = r.json()
            word = data['query']['pages']
            listo = list(word.keys())
            if ('-1' in listo):
                return "Nothing found for %s" %(topic)
            else:
                stuff = word[listo[0]]['extract']
                soup = BeautifulSoup(stuff, 'html.parser')
                return soup.get_text()