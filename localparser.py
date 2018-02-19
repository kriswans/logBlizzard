import json
import glob
from pprint import pprint as pp

def logReader():

    jsl=[]
    for i in glob.glob('LOGS/msglog*.json'):
    	with open (i,'r') as f:
    		j=json.load(f)
    	jsl=jsl+j
    return jsl

def msgCatCounter(jsl):
    try:
        msg_cat_count_dict=dict(zip({i['orig_message'].split('%')[1].split(':')[0] for i in jsl},[[i['orig_message'].split('%')[1].split(':')[0] for i in jsl].count(j) for j in {i['orig_message'].split('%')[1].split(':')[0] for i in jsl}]))
        return msg_cat_count_dict
    except IndexError:
        pass

def jsonMsgCount(jsl):
    try:
        js_msg_count_dict=dict(zip({json.dumps(i['orig_message'].split('%')[1].split(':')[0:-1]) for i in jsl},[[json.dumps(i['orig_message'].split('%')[1].split(':')[0:-1]) for i in jsl].count(j) for j in {json.dumps(i['orig_message'].split('%')[1].split(':')[0:-1]) for i in jsl}]))
        return js_msg_count_dict
    except IndexError:
        pass

def ipCount(jsl):
    try:
        ip_count_dict=dict(zip({i['orig_addr'] for i in jsl},[[i['orig_addr'] for i in jsl].count(j) for j in {i['orig_addr'] for i in jsl}]))
        return ip_count_dict
    except IndexError:
        pass

def ipCatCount(jsl):
    s=set(zip([i['orig_addr'] for i in jsl], [i['orig_message'].split('%')[1].split(':')[0] for i in jsl]))
    l=list(zip([i['orig_addr'] for i in jsl], [i['orig_message'].split('%')[1].split(':')[0] for i in jsl]))
    ip_cat_count_dict=dict(zip(s,[l.count(j) for j in s]))
    return ip_cat_count_dict

def catIpCount(jsl):
    s=set(zip([i['orig_message'].split('%')[1].split(':')[0] for i in jsl], [i['orig_addr'] for i in jsl]))
    l=list(zip([i['orig_message'].split('%')[1].split(':')[0] for i in jsl], [i['orig_addr'] for i in jsl]))
    cat_ip_count_dict=dict(zip(s,[l.count(j) for j in s]))
    return cat_ip_count_dict

def jsonCatMsgCount(jsl):
    s=set(zip([i['orig_message'].split('%')[1].split(':')[0] for i in jsl], [json.dumps(i['orig_message'].split('%')[1].split(':')[0:-1]) for i in jsl]))
    l=list(zip([i['orig_message'].split('%')[1].split(':')[0] for i in jsl], [json.dumps(i['orig_message'].split('%')[1].split(':')[0:-1]) for i in jsl]))
    js_cat_msg_count_dict=dict(zip(s,[l.count(j) for j in s]))
    return js_cat_msg_count_dict

if __name__=='__main__':
    jsl=logReader()
    msg_cat_count_dict=msgCatCounter(jsl)
    js_msg_count_dict=jsonMsgCount(jsl)
    ip_count_dict=ipCount(jsl)
    ip_cat_count_dict=ipCatCount(jsl)
    cat_ip_count_dict=catIpCount(jsl)
    js_cat_msg_count_dict=jsonCatMsgCount(jsl)
    pp(msg_cat_count_dict)
    pp(js_msg_count_dict)
    pp(ip_count_dict)
    pp(ip_cat_count_dict)
    pp(cat_ip_count_dict)
    pp(js_cat_msg_count_dict)
