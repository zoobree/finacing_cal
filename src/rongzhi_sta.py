# -*- coding:utf-8 -*-


'''
Created on 2018��1��21��


@author: Administrator
'''


import os
import csv
import pandas as pd

#dir = os.path.join(os.getcwd()+"/")

dir = "E:/Python/finacing_cal/data/"

if __name__ == '__main__':
    
    df_rzye = pd.read_excel(dir+"Rongzhiyue.xlsx",header=0)
 
    
    
    df_customer = pd.read_excel(dir+"Customers.xlsx",header=0)


    ###按照客户账户关联融资余额表和客户经理表
    df_wide = df_rzye.merge(df_customer,how='inner', on=u'客户账户')  ###总表
    print(df_wide)
    df_wide.to_csv(dir+'Merge_Result.csv',encoding ='GB2312')
    ###客户经理开发的客户，剔除经纪人开发的客户并进行求和
    df_invest_cs_tmp = df_wide[[u'融资余额',u'客户经理',u'开发人员']]
    #df_invest_cs_tmp.to_csv(dir+'df_invest_cs_tmp.csv',encoding ='GB2312')
    df_invest_cs = df_invest_cs_tmp[df_invest_cs_tmp[u'开发人员'].isnull()]
    #df_invest_cs.to_csv(dir+'df_invest_cs.csv',encoding ='GB2312')
    df_result = df_invest_cs[[u'融资余额',u'客户经理']].groupby([u'客户经理']).sum()
    print(df_result)

    '''
    df_result.to_csv(dir+'Consultant_result.csv',encoding ='GB2312')
    ###经纪人开发的客户，按照经纪人非空的客户并进行求和
    df_broker_cs = df_invest_cs_tmp[df_invest_cs_tmp[u'开发人员'].notnull()]
    #df_broker_cs.to_csv(dir+'df_invest_cs.csv',encoding ='GB2312')
    #df_broker_result = df_broker_cs[[u'融资余额']].sum()
    df_broker_result = df_broker_cs[[u'融资余额',u'开发人员']].groupby([u'开发人员']).sum()
    df_broker_result.to_csv(dir+'broker_result.csv',encoding ='GB2312')
	
    print("11111......")
    #print(os.curdir)
    print(os.getcwd())
	'''