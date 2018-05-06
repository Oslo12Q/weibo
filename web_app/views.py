#encoding: utf-8
import json
import time
import datetime
import logging
import traceback
from django.shortcuts import render_to_response,render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import *

'''
    # json时间转换
'''
class DateEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, datetime):  
            return obj.__str__()  
        return json.JSONEncoder.default(self, obj) 

'''
    # 通用函数返回json数据
'''
def get_json_response(request, json_rsp):
    return HttpResponse(json.dumps(json_rsp,cls=DateEncoder), content_type='application/json')

'''
    # 函数 
    # [index] 
    # GET请求 映射页面(博主页面)
'''
def index(request):
    return render(request,'index.html')

'''
    # 函数 
    # [index] 
    # GET请求 映射页面(博主发帖页面)
'''
def index_tweet(request):
    return render(request,'index_tweet.html')

'''
    # 函数 
    # [api_data_Information]
    # POST 请求查询
    # GET 请求URL参数（pagtor每页显示条数，page页数，不上传默认10条）
'''

def api_data_Information(request):
    in_tion_list = []
    if request.method != 'POST':
        return get_json_response(request, dict(suc_id=0, ret_cd=405, ret_ts=long(time.time()),errMsg = 'Method not allowed',successResult=''))
    try:
        in_tion = Information.objects.all()
        if not in_tion:
            return get_json_response(request, dict(suc_id=0, ret_cd=104, ret_ts=long(time.time()),errMsg = 'No data found',successResult=''))
        pages = request.GET.get('pagtor')
        if not pages:
            pg = '10'
        else:
            pg = pages
        paginator = Paginator(in_tion, pg)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        pages_num = paginator.count
        for i in contacts:
            w_id = i.w_id
            nickname = i.nickname
            gender = i.gender
            city = i.city
            num_fans = i.num_fans
            num_follows = i.num_follows
            num_tweets = i.num_tweets
            in_tion_data ={
                'w_id':w_id,'nickname':nickname,'gender':gender,'city':city,'num_fans':num_fans,
                'num_follows':num_follows,'num_tweets':num_tweets,'num_tweets':num_tweets
            }
            in_tion_list.append(in_tion_data)  

        return get_json_response(request, dict(suc_id=0, ret_cd=200, ret_ts=long(time.time()),errMsg = '',successResult=in_tion_list,pages_num=pages_num))
    except Exception, err:
        return get_json_response(request, dict(suc_id=0, ret_cd=500, ret_ts=long(time.time()),errMsg = 'Server internal error,Please contact the administrator.',successResult=''))

'''
    # 函数 
    # [api_data_Tweets]
    # 请求方式 POST 参数 NickName 昵称
    # GET 请求URL参数（pagtor每页显示条数，page页数，不上传默认10条）
'''
def api_data_Tweets(request):
    tweets_list = []
    if request.method != 'POST':
        return get_json_response(request, dict(suc_id=0, ret_cd=405, ret_ts=long(time.time()),errMsg = 'Method not allowed',successResult=''))
    try:
        name = request.POST.get('nickname',None)
        if not name:
            #return get_json_response(request, dict(suc_id=0, ret_cd=104, ret_ts=long(time.time()),errMsg = 'NickName is not found',successResult=''))
            tweet = Tweets.objects.all()
        else:
            tweet = Tweets.objects.filter(nickname = name)
        if not tweet:
            return get_json_response(request, dict(suc_id=0, ret_cd=104, ret_ts=long(time.time()),errMsg = 'No data found',successResult=''))
        pages = request.GET.get('pagtor')
        if not pages:
            pg = '10'
        else:
            pg = pages
        paginator = Paginator(tweet, pg)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        pages_num = paginator.count
        for _ in contacts:
            wb_id = _.wb_id
            content = _.content
            nickname = _.nickname
            comment = _.comment
            like = _.like
            pubtime = _.pubtime
            transfer = _.transfer
            tweets_data = {
                'wb_id':wb_id,'content':content,'nickname':nickname,'comment':comment,'like':like,
                'pubtime':pubtime,'transfer':transfer
            }
            tweets_list.append(tweets_data)
        return get_json_response(request, dict(suc_id=0, ret_cd=200, ret_ts=long(time.time()),errMsg = '',successResult=tweets_list,pages_num=pages_num))
    except Exception, err:
        logging.error(err)
        logging.error(traceback.format_exc())
        return get_json_response(request, dict(suc_id=0, ret_cd=500, ret_ts=long(time.time()),errMsg = 'Server internal error,Please contact the administrator.',successResult=''))
    


