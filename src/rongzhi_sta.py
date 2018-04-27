# -*- coding:utf-8 -*-


'''
Created on 2018/4/22


@author: Administrator
'''
#import pandas as pd
import os
from pandas import read_excel
#from pandas import to_csv
from pandas import merge


dir = "D:/data/"   

columns = [u'客户代码',u'客户姓名',u'融资余额']


if __name__ == '__main__':
    print("Begin to caculate..............")
    try:
        df_rzye = read_excel(dir+"CustomerMoney.xls", header=2, columns=columns)
    except: 
        df_rzye = read_excel(dir+"CustomerMoney.xlsx", header=2, columns=columns)
    try:
        df_customer = read_excel(dir+"CustomerAccount.xlsx", header=0)
    except:
        df_customer = read_excel(dir+"CustomerAccount.xls", header=0)
   
    ###按照客户账户关联融资余额表和客户经理表
    df_wide = df_rzye.merge(df_customer,how='inner', on=u'客户代码')  ###总表
    
    #df_wide.to_csv(dir+'Merge_Result.csv',encoding ='GB2312')
    ###客户经理开发的客户，剔除经纪人开发的客户并进行求和
    df_invest_cs_tmp = df_wide[[u'融资余额',u'\t服务人员',u'\t开发人员']]   
    str2float = lambda s:float(s.replace(',','')) 
    df_invest_cs_tmp[u'融资余额new'] = df_invest_cs_tmp[u'融资余额'].map(str2float) #将String转换成float

    #df_invest_cs_tmp.to_csv(dir+'df_invest_cs_tmp.csv',encoding ='GB2312')
    df_invest_cs = df_invest_cs_tmp[df_invest_cs_tmp[u'\t开发人员'].isnull()]
    #df_invest_cs.to_csv(dir+'df_invest_cs.csv',encoding ='GB2312')
    #print(df_invest_cs)
    df_result = df_invest_cs[[u'融资余额new',u'\t服务人员']].groupby([u'\t服务人员']).sum()
    print(df_result)

    df_result.to_csv(dir+'Consultant_result.csv',encoding ='GB2312')
    ###经纪人开发的客户，按照经纪人非空的客户并进行求和
    df_broker_cs = df_invest_cs_tmp[df_invest_cs_tmp[u'\t开发人员'].notnull()]
    df_broker_result = df_broker_cs[[u'融资余额new',u'\t开发人员']].groupby([u'\t开发人员']).sum()
    df_broker_result.to_csv(dir+'broker_result.csv',encoding ='GB2312')
	#print("Broker Sum is")
    print("Consult Sum = "+str(df_invest_cs[u'融资余额new'].sum()))
    print("Broker Sum  = "+str(df_broker_cs[u'融资余额new'].sum()))
    print("Calculate Successful !!!!!")
    os.system('pause')
   
	