import os, json
import pandas as pd
import pymysql
path_Trans  =  "C:/Users/inspire/Desktop/python/phone pay/data/aggregated/transaction/country/india/state/"
Agg_state_list  =  os.listdir(path_Trans)
clm = {'State':[],'Years':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
for i in Agg_state_list:
    p_i = path_Trans+i+"/"
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = p_i+j+"/"
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = p_j+k
            Data = open(p_k,'r')
            D1 = json.load(Data)
            for z in D1['data']['transactionData']:
              Name = z['name']
              count = z['paymentInstruments'][0]['count']
              amount = z['paymentInstruments'][0]['amount']
              clm['Transaction_type'].append(Name)
              clm['Transaction_count'].append(count)
              clm['Transaction_amount'].append(amount)
              clm['State'].append(i)
              clm['Years'].append(j)
              clm['Quarter'].append(int(k.strip('.json')))
#Succesfully created a dataframe
Agg_Trans = pd.DataFrame(clm)
#agg_insu
path_insurance="C:/Users/inspire/Desktop/python/phone pay/data/aggregated/insurance/country/india/state/"
insurance_state_list  =  os.listdir(path_insurance)
clm2 = {'State':[], 'Years':[],'Quarter':[],'insurance_type':[], 'insurance_count':[], 'insurance_amount':[]}
for i in insurance_state_list:
    p_i = path_insurance+i+"/"
    insurance_yr = os.listdir(p_i)
    for j in insurance_yr:
        p_j = p_i+j+"/"
        insurance_yr_list = os.listdir(p_j)
        for k in insurance_yr_list:
            p_k = p_j+k
            Data = open(p_k,'r')
            D2 = json.load(Data)
            for z in D2['data']['transactionData']:
              Name = z['name']
              count = z['paymentInstruments'][0]['count']
              amount = z['paymentInstruments'][0]['amount']
              clm2['insurance_type'].append(Name)
              clm2['insurance_count'].append(count)
              clm2['insurance_amount'].append(amount)
              clm2['State'].append(i)
              clm2['Years'].append(j)
              clm2['Quarter'].append(int(k.strip('.json')))
#Succesfully created a dataframe
Agg_insurance = pd.DataFrame(clm2)
#agg_user
path_user="C:/Users/inspire/Desktop/python/phone pay/data/aggregated/user/country/india/state/"
user_state_list  =  os.listdir(path_user)
clm3 = {'State':[], 'Years':[],'Quarter':[],'brand':[], 'transaction_count':[], 'percentage':[]}
for i in user_state_list:
    p_i = path_user+i+"/"
    user_yr = os.listdir(p_i)
    for j in user_yr:
        p_j = p_i+j+"/"
        user_yr_list = os.listdir(p_j)
        for k in user_yr_list:
            p_k = p_j+k
            Data = open(p_k,'r')
            D3 = json.load(Data)
            try:
               for z in D3['data']['usersByDevice']:
                brand= z['brand']
                count = z['count']
                percentage= z['percentage']
                clm3['brand'].append(brand)
                clm3['transaction_count'].append(count)
                clm3['percentage'].append(percentage)
                clm3['State'].append(i)
                clm3['Years'].append(j)
                clm3['Quarter'].append(int(k.strip('.json')))
            except:
                pass    
#Succesfully created a dataframe
Agg_user = pd.DataFrame(clm3)
#top_trans
path_trans2="C:/Users/inspire/Desktop/python/phone pay/data/top/transaction/country/india/state/"
top_state_list  =  os.listdir(path_trans2)
clm4 = {'State':[], 'Years':[],'Quarter':[],'districts':[], 'count':[], 'amount':[]}
for i in top_state_list:
    p_i = path_trans2+i+"/"
    top_yr = os.listdir(p_i)
    for j in top_yr:
        p_j = p_i+j+"/"
        top_yr_list = os.listdir(p_j)
        for k in top_yr_list:
            p_k = p_j+k
            Data = open(p_k,'r')
            
            D4 = json.load(Data)
            
            for z in D4["data"]["districts"]:
           
            
               
              
                district = z['entityName'] 
                count=z['metric']['count']
                amount=z['metric']['amount']
               
                clm4['districts'].append(district)
                clm4['count'].append(count)
                clm4['amount'].append(amount)
               
                clm4['State'].append(i)
                clm4['Years'].append(j)
                clm4['Quarter'].append(int(k.strip('.json')))
    #Succesfully created a dataframe
    top_trans2 = pd.DataFrame(clm4)
#top_insur
path_insurance2="C:/Users/inspire/Desktop/python/phone pay/data/top/insurance/country/india/state/"
insurance2_state_list  =  os.listdir(path_insurance2)
clm5 = {'State':[], 'Years':[],'Quarter':[],'type':[], 'insurance2_count':[], 'insurance2_amount':[] ,'entity':[]}
for i in insurance2_state_list:
    p_i = path_insurance2+i+"/"
    insurance2_yr = os.listdir(p_i)
    for j in insurance2_yr:
        p_j = p_i+j+"/"
        insurance2_yr_list = os.listdir(p_j)
        for k in insurance2_yr_list:
            p_k = p_j+k
            Data = open(p_k,'r')
            D5 = json.load(Data)
            for z in D5['data']['pincodes']:
               entityName= z["entityName"]
               count = z['metric']['count']
               amount = z['metric']['amount']
               clm5['entity'].append(entityName)
               clm5['insurance2_count'].append(count)
               clm5['insurance2_amount'].append(amount)
               clm5['State'].append(i)
               clm5['Years'].append(j)
               clm5['Quarter'].append(int(k.strip('.json')))
               clm5['type'].append('pincode')
            for z in D5['data']['districts']:
               entityName= z["entityName"]
               count = z['metric']['count']
               amount = z['metric']['amount']
               clm5['entity'].append(entityName)
               clm5['insurance2_count'].append(count)
               clm5['insurance2_amount'].append(amount)
               clm5['State'].append(i)
               clm5['Years'].append(j)
               clm5['Quarter'].append(int(k.strip('.json')))
               clm5['type'].append('district')
                   
#Succesfully created a dataframe
top_insurance2 = pd.DataFrame(clm5)
#top_user
path_user2="C:/Users/inspire/Desktop/python/phone pay/data/top/user/country/india/state/"
user2_state_list  =  os.listdir(path_user2)
clm6 = {'State':[], 'Years':[],'Quarter':[],'name':[], 'count':[], 'percentage':[]}
for i in user2_state_list:
    p_i = path_user2+i+"/"
    user2_yr = os.listdir(p_i)
    for j in user2_yr:
        p_j = p_i+j+"/"
        user2_yr_list = os.listdir(p_j)
        for k in user2_yr_list:
            p_k = p_j+k
            Data = open(p_k,'r')
            D6 = json.load(Data)
            try:
               for z in D6['data']['usersByDevice']:
                Name = z['name']
                count = z['count']
                percentage= z['percentage']
                clm6['name'].append(Name)
                clm6['count'].append(count)
                clm6['percentage'].append(percentage)
                clm6['State'].append(i)
                clm6['Years'].append(j)
                clm6['Quarter'].append(int(k.strip('.json')))
            except:
                pass    
#Succesfully created a dataframe
Top_user2 = pd.DataFrame(clm6)
#map_trans
path_trans3 = "C:/Users/inspire/Desktop/python/phone pay/data/map/transaction/hover/country/india/state/"
trans3_state_list =os.listdir(path_trans3)

clm7 = {'States': [],'Years': [],'Quarter': [],'district': [],'Tran2_count': [],'Tran2_amount': []}

for i in trans3_state_list :
    p_i = path_trans3+i+"/"
    trans3_yr = os.listdir(p_i)
    for j in trans3_yr :
        p_j = p_i+j+"/"
        trans3_yr_list = os.listdir(p_j)
        for k in trans3_yr_list:
            p_k = p_j+k
            Data = open(p_k,'r')
            D7 =json.load(Data)
            
for z in D7['data']['hoverDataList']:
                    name = z['name']
                    count = z['metric'][0]['count']
                    amount = z['metric'][0]['amount']
                    
                    clm7['district'].append(name)
                    clm7['Tran2_count'].append(count)
                    clm7['Tran2_amount'].append(amount)
                    clm7['States'].append(i)
                    clm7['Years'].append(j)
                    clm7['Quarter'].append(int(k.strip('.json')))
#Succesfully created a dataframe
map_trans3 = pd.DataFrame(clm7)
map_trans3['States']=map_trans3['States'].str.replace('-','').str.replace('&','and')
map_trans3['States']=map_trans3['States'].str.title()
#map_insur
path_ins3="C:/Users/inspire/Desktop/python/phone pay/data/map/insurance/hover/country/india/state/"
ins3_state_list  =  os.listdir(path_ins3)
clm8 = {'States':[], 'Years':[],'Quarter':[], 'District':[], 'Tran_count':[] ,'Tran_amount':[]}
for i in ins3_state_list:
    p_i = path_ins3+i+"/"
    ins3_yr = os.listdir(p_i)
    for j in ins3_yr:
        p_j = p_i+j+"/"
        ins3_yr_list = os.listdir(p_j)
        for k in ins3_yr_list:
            p_k = p_j+k
            Data = open(p_k,'r')
            D8 = json.load(Data)
            for z in D8['data']['hoverDataList']:
                    name = z['name']
                    count = z['metric'][0]['count']
                    amount = z['metric'][0]['amount']
                    
                    clm8['District'].append(name)
                    clm8['Tran_count'].append(count)
                    clm8['Tran_amount'].append(amount)
                    clm8['States'].append(i)
                    clm8['Years'].append(j)
                    clm8['Quarter'].append(int(k.strip('.json')))
#Succesfully created a dataframe
map_ins3 = pd.DataFrame(clm8)
map_ins3['States']=map_ins3['States'].str.replace('-','').str.replace('&','and')
map_ins3['States']=map_ins3['States'].str.title()
#map_user
path_user3="C:/Users/inspire/Desktop/python/phone pay/data/map/user/hover/country/india/state/"
user3_state_list  =  os.listdir(path_user3)
clm9 = {'States':[], 'Years':[],'Quarter':[],'district':[], 'RegisteredUsers':[], 'AppOpens':[]}
for i in user3_state_list:
    p_i = path_user3+i+"/"
    user3_yr = os.listdir(p_i)
    for j in user3_yr:
        p_j = p_i+j+"/"
        user3_yr_list = os.listdir(p_j)
        for k in user3_yr_list:
            p_k = p_j+k
            Data = open(p_k,'r')
            D9 = json.load(Data)
            try:
               for z in D9['data']['hoverData']:
                district = z['entityName']
                RegisteredUsers = z['RegisteredUsers']
                AppOpens= z['Appopens']
                clm9['district'].append(district)
                clm9['RegisteredUsers'].append(RegisteredUsers)
                clm9['AppOpens'].append(AppOpens)
                clm9['States'].append(i)
                clm9['Years'].append(j)
                clm9['Quarter'].append(int(k.strip('.json')))
            except:
                pass    
#Succesfully created a dataframe
map_user3 = pd.DataFrame(clm9)
map_user3['States'] = (map_user3['States'].astype(str).str.replace('-', ' ', regex=False).str.replace('&', 'and', regex=False))
       
#database

try:
    
    conn = pymysql.connect(
        host='localhost',       
        user='root',            
        password='12345',       
        database='phonepay'     
    )
    print(" Connection successful!")

    # Create a cursor object
    cursor = conn.cursor()
    print(" Cursor created successfully!")

except Exception as e:
    print("Error connecting to the database:", str(e))
    #Agg_trans
create_query_Trans='''
CREATE TABLE IF NOT EXISTS Agg_Trans(
      State VARCHAR(50),
      Years INT,
      Quarter INT,
      Transaction_type VARCHAR(50),
      Transaction_count BIGINT,
      Transaction_amount BIGINT
)'''
cursor.execute(create_query_Trans)
for index,row in Agg_Trans.iterrows():
    insert_query_Trans='''INSERT Agg_Trans(State,Years,Quarter,Transaction_type,Transaction_count,Transaction_amount)
                          values(%s,%s,%s,%s,%s,%s)'''
    values=(
        row["State"],
        row["Years"],
        row["Quarter"],
        row["Transaction_type"],
        int(row["Transaction_amount"]),
        int(row["Transaction_count"])
)
    cursor.execute(insert_query_Trans,values)
    conn.commit()
    #Agg_insurance
create_query_insurance='''
CREATE TABLE IF NOT EXISTS Agg_insurance(
      State VARCHAR(50),
      Years INT,
      Quarter INT,
      insurance_type VARCHAR(50),
      insurance_count BIGINT,
     insurance_amount BIGINT
)'''
cursor.execute(create_query_insurance)
for index,row in Agg_insurance.iterrows():
    insert_query_insurance='''INSERT Agg_insurance(State,Years,Quarter,insurance_type,insurance_count,insurance_amount)
                          values(%s,%s,%s,%s,%s,%s)'''
    values=(
        row["State"],
        row["Years"],
        row["Quarter"],
        row["insurance_type"],
        row["insurance_amount"],
        row["insurance_count"],
)
    cursor.execute(insert_query_insurance,values)
    conn.commit()
     #agg_user
create_query_user='''
CREATE TABLE IF NOT EXISTS Agg_user(
      State VARCHAR(50),
      Years INT,
      Quarter INT,
      brand VARCHAR(50),
      count BIGINT,
      percentage BIGINT
)'''
cursor.execute(create_query_user)
for index,row in Agg_user.iterrows():
    insert_query_user='''INSERT Agg_user(State,Years,Quarter,brand,Transaction_count,percentage)
                          values(%s,%s,%s,%s,%s,%s)'''
    values=(
        row["State"],
        row["Years"],
        row["Quarter"],
        row["brand"],
        row["percentage"],
        row["Transaction_count"],
)
    cursor.execute(insert_query_user,values)
    conn.commit()
    #top_trans
create_query_trans2='''
CREATE TABLE IF NOT EXISTS top_trans2(
      State VARCHAR(50),
      Years INT,
      Quarter INT,
      district VARCHAR(50),
      count BIGINT,
      amount BIGINT
)'''
cursor.execute(create_query_trans2)
print('top_trans2')
for index,row in top_trans2.iterrows():
    insert_query_trans2='''INSERT top_trans2(State,Years,Quarter,district,count,amount)
                          values(%s,%s,%s,%s,%s,%s)'''
    values=(
        row["State"],
        row["Years"],
        row["Quarter"],
        row["district"],
        row["count"],
        row["amount"],
)
    cursor.execute(insert_query_trans2,values)
    conn.commit()
    #top_insurance2
create_query_insurance2='''
CREATE TABLE IF NOT EXISTS top_insurance2(
      State VARCHAR(50),
      Years INT,
      Quarter INT,
      district VARCHAR(50),
      count BIGINT,
      amount BIGINT
)'''
cursor.execute(create_query_insurance2)
for index,row in top_insurance2.iterrows():
    insert_query_insurance2='''INSERT top_insurance2(State,Years,Quarter,district,count,amount)
                          values(%s,%s,%s,%s,%s,%s)'''
    values=(
        row["State"],
        row["Years"],
        row["Quarter"],
        row["district"],
        row["count"],
        row["amount"],
)
    cursor.execute(insert_query_insurance2,values)
    conn.commit()
    #top_user2
create_query_user2='''
CREATE TABLE IF NOT EXISTS Top_user2(
      State VARCHAR(50),
      Years INT,
      Quarter INT,
      name VARCHAR(50),
      count BIGINT,
      percentage BIGINT
)'''
cursor.execute(create_query_user2)
for index,row in Top_user2.iterrows():
    insert_query_user2='''INSERT Top_user2(State,Years,Quarter,name,count,percentage)
                          values(%s,%s,%s,%s,%s,%s)'''
    values=(
        row["State"],
        row["Years"],
        row["Quarter"],
        row["name"],
        row["count"],
        row["percentage"],
)
    cursor.execute(insert_query_user2,values)
    conn.commit()
    #map_Trans3
create_query_trans3='''
CREATE TABLE IF NOT EXISTS map_trans3(
      State VARCHAR(50),
      Years INT,
      Quarter INT,
      district VARCHAR(50),
      Trans2_count BIGINT,
      Trans2_amount BIGINT
)'''
cursor.execute(create_query_trans3)
for index,row in map_trans3.iterrows():
    insert_query_trans3='''INSERT map_trans3(State,Years,Quarter,district,Trans2_count,Trans2_amount)
                          values(%s,%s,%s,%s,%s,%s)'''
    values=(
        row["State"],
        row["Years"],
        row["Quarter"],
        row["district"],
        row["Trans2_count"],
        row["Trans2_amount"],
)
    cursor.execute(insert_query_trans3,values)
    conn.commit()
    #map_ins3
create_query_ins3='''
CREATE TABLE IF NOT EXISTS map_ins3(
      State VARCHAR(50),
      Years INT,
      Quarter INT,
      District VARCHAR(50),
      Tran_count BIGINT,
      Tran_amount BIGINT
)'''
cursor.execute(create_query_ins3)
for index,row in map_ins3.iterrows():
    insert_query_ins3='''INSERT map_ins3(State,Years,Quarter,District,Tran_count,Tran_amount)
                          values(%s,%s,%s,%s,%s,%s)'''
    values=(
        row["State"],
        row["Years"],
        row["Quarter"],
        row["District"],
        row["Tran_count"],
        row["Tran_amount"],
)
    cursor.execute(insert_query_ins3,values)
    conn.commit()
    #map_user3
    create_query_user3='''
CREATE TABLE IF NOT EXISTS map_user3(
      State VARCHAR(50),
      Years INT,
      Quarter INT,
      District VARCHAR(50),
      RegisteredUsers BIGINT,
      AppOpens BIGINT
)'''
cursor.execute(create_query_user3)
for index,row in map_user3.iterrows():
    insert_query_user3='''INSERT map_user3(State,Years,Quarter,District,RegisteredUsers,AppOpens)
                          values(%s,%s,%s,%s,%s,%s)'''
    values=(
        row["State"],
        row["Years"],
        row["Quarter"],
        row["District"],
        row["RegisteredUsers"],
        row["AppOpens"],
)
    cursor.execute(insert_query_user3,values)
    conn.commit()
    conn.close()
    cursor.close()
    print("Data uploaded successfully to the database.")
    






