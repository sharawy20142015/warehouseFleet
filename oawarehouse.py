import datetime
import streamlit as st
import pandas as pd
import gspread
import numpy as np
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
credentials_json = {
        "type": "service_account",
        "project_id": "noted-handler-379714",
        "private_key_id": "61988f9740276e066ac2fe2aeaac3fa4b6ff527c",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCPWdjJpLudGk7S\ngaV1l/RVUevfJTyrZmKfdMbSkjnpNG4wOGF69rs3h++8luanYcOt+TW87WiAVZum\nUqawNu1GYyh6CyoDxX4lR2/jAZWb/xJ7tgdW7t+rKv1hKTljke8F6kecPSznge/W\npUtegmMFaYTaZJNDuq29A5yT/zo5YWqoxpV0fxpOOlPMvoACelFNcvKsKLnOjaGN\nbjQqFpC+7Sl+LHGaqcO00mTYwbo7Ijj5i+BlYZAwDanN3XSd6Wwl3wnUnGNaWn+6\nVwHyQebXgmICq1iEHNBaoUbEdHDuPXepExoekvSNwx9Ng2vTNCRfzEQVL+3vYSjL\npqo86L9xAgMBAAECggEABQeMl/+N/xQ3F4LptpthHNS52zuL2kIme+x9lNIBUuWu\nZ4X04prxROChuErNlyoSkuIrYOBuAhGu2zorY8ObldSBDS4i2FzHoSB1ZCAwOvfL\nMti3P3U0VwW0O+JVw4DxY1Jd1pUdZBZ+nxfv0eYuefhCq2Rrt8y/D4KGzfj+lph/\nUZvOKQcu9MguBIJAx5xBTtNjeMjhJCdu1OdwyW5MO0irvLmqIQDIphuRvDvXbS93\nSg9zQFxuzLJMKe3jL0zgbkHBjABVnRFycDUWKLgRAmCjoGfY367k800/YNduBqQy\nVBHAQqL9Uuj9S3o5VtZ6uqtjHkhJcDhxnAH7B2G2wQKBgQDGM4fGuMiVTw0rfxSC\npV28y1r5p9tD6uJjTWbqqp0IpX3mjDgZwL0ig5U+3JBBU4n0Ix4WeDjq6/Wy6Tcn\n5Oo9eRwVOsCttl807/sKGBmZV5dRDdbD7NKLBI2sxtbLu1POisK+Si2fJV03mmE6\nm+3Y4DaJ/StovuTuEMIZBKFAoQKBgQC5J4itC5XJ9WCzKIupIF/uxxJGg6TofZvM\nDYkmzb9ZIoh9iFnB5InmlG14ngmRnjINeTqjN4YQtBJNSpk7p1Ra/C2Q+Do/Zm9G\nNWQKd3nYBSQxwNqd97CgzbmtxT8GkSWIvwCtD45oFNkrU0W6eH6/fhGjXNjPj2Ig\nYIHIFNV80QKBgQDALUzUcW0D4M97Qk/n0WHPYjoG4ivnccMq1+0XUnDK5nPp7EGl\nLs30vjMi7Yft34tergJJdS5zEnF8lUbGpt481sZVC0+x36f2003NXsrLdTOiAtIf\nzOvkoXihc3bnue4r0T28dn4/1mHJPSZTRsfbRqN7LoA9owKklpks2uFjoQKBgE0F\n7C6Idjx4jkyZXlfx9tZ/C9Q3qV9p+WjObLKuvp4W5o7KLQSizNcWAeA+Zh6kn4/J\nUaJaU7QZJM/wa4RMXKQo6c+344tCUqHzTfWotBAwO1lTL96tDlYmnspyFoDl2qZj\nRqW3pfcYTStfzc7/l0KT8ER0OGFH9XsginywZgsxAoGAUXm9ge4vbPqKcHNWPYmn\nM/zJ4zkIP57mmRHZBbukLlfXW3/tLHiSZWyotjjDBmcw1yZCoZhTvJcoxeH153V6\nXraQTIW17zjatG22e8E817VKMg/dvHz6KHDHM+DRRxhmGojVsBcUhzPYv/llFoGC\nNYyRe2J3ggufJ0lqCoQNxhg=\n-----END PRIVATE KEY-----\n",
        "client_email": "demo-867@noted-handler-379714.iam.gserviceaccount.com",
        "client_id": "108019621957189237850",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/demo-867%40noted-handler-379714.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
    }
credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentials_json, ['https://spreadsheets.google.com/feeds'])
gc = gspread.authorize(credentials)
uploaded_file = st.file_uploader("Choose a file")
google_sheet_url = "https://docs.google.com/spreadsheets/d/1aKZNzu6T3KYjmqgrIk4FvMmOLT-ttMthaB9n8Y5P9zc/edit#gid=0"
sh = gc.open_by_url(google_sheet_url)
worksheet1 = sh.get_worksheet(0)
all_values = worksheet1.get_all_values()
old_data = pd.DataFrame(all_values[1:], columns=all_values[0])
worksheet2 = sh.get_worksheet(1)
all_values = worksheet2.get_all_values()
database = pd.DataFrame(all_values[1:], columns=all_values[0]) 
needs=old_data['Needs'].unique().tolist()
old_data['Date'] = pd.to_datetime(old_data[['Year', 'Month', 'Day']], format='%Y-%m-%d')
old_data.drop(columns=['Year', 'Month', 'Day'],inplace=True)
needs_catgory=old_data['Needs'].unique().tolist()
category=['Select Category', 'All'] + needs_catgory
select=st.sidebar.selectbox('Category',category)
check=st.sidebar.button('Check')
class Oa_maintenance:
    def __init__(self,old_data,database):
        self.old_data=old_data
        self.database=database
    def df_(self):
        try:
            xls = pd.ExcelFile(uploaded_file)
            sheet_names = xls.sheet_names
            year_sheets = [sheet for sheet in sheet_names if 'Year' in pd.read_excel(uploaded_file, sheet_name=sheet).to_string(index=False)]
            sheets = [i for i in year_sheets]
            self.new_data = pd.read_excel(uploaded_file, sheet_name=sheets[0])
            letter = {
                'A': 'ا',
                'B': 'ب',
                'T': 'ط',
                'G': 'ج',
                'H': 'ه',
                'D': 'د',
                'R': 'ر',
                'Z': 'ظ',
                'S': 'س',
                'C': 'ص',
                'E': 'ع',
                'F': 'ف',
                'K': 'ق',
                'L': 'ل',
                'M': 'م',
                'N': 'ن',
                'W': 'و',
                'Y': 'ى',  # Replace ي with ى
                'أ': 'ا',
                'ب': 'ب',
                'ت': 'ت',
                'ج': 'ج',
                'ح': 'ح',
                'د': 'د',
                'ر': 'ر',
                'ز': 'ز',
                'س': 'س',
                'ص': 'ص',
                'ض': 'ض',
                'ط': 'ط',
                'ظ': 'ظ',
                'ع': 'ع',
                'ف': 'ف',
                'ق': 'ق',
                'ل': 'ل',
                'م': 'م',
                'ن': 'ن',
                'ه': 'ه',
                'و': 'و',
                'ى': 'ي',  # Replace ى with ي
            }


            translate = str.maketrans(letter)

            def changeletter(x):
                try:
                    x = x.upper()
                    new_word = x.translate(translate)
                    new_word = new_word.upper()
                    new_word = new_word.replace(' ', '')
                    return new_word
                except:
                    return x
            def lett_num(x):
                try:
                    letter = ''.join([i for i in x if (i.isalpha() and (i != 'ـ')and (i != '-'))])
                    number = ''.join([i for i in x if i.isdigit()])
                    letter = letter.replace('', ' ')
                    return letter, number
                except Exception as e:
                    print(x)
                    return 0
            month_mapping = {
                'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
                'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
                'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
            }
            
            self.database['plate number']=self.database[self.database.columns[0]].apply(changeletter)
            self.database[['Letters', 'Numbers']] = self.database['plate number'].apply(lett_num).apply(pd.Series)
            self.database['new plate number']=self.database['Letters']+self.database['Numbers']
            self.database.rename(columns={self.database.columns[0]:'VPlate Number'},inplace=True)
            self.database['VPlate Number']=self.database['new plate number']
            self.new_data['Month'] = self.new_data['Month'].replace(month_mapping)
            self.new_data['plate number']=self.new_data.iloc[:, 5].apply(changeletter)
            self.new_data[['Letters', 'Numbers']] = self.new_data['plate number'].apply(lett_num).apply(pd.Series)
            self.new_data['new plate number']=self.new_data['Letters']+self.new_data['Numbers']
            self.new_data.rename(columns={self.new_data.columns[5]:'VPlate Number'},inplace=True)
            self.new_data['VPlate Number']=self.new_data['new plate number']
            self.new_data['Date'] = pd.to_datetime(self.new_data[['Year', 'Month', 'Day']], format='%Y-%m-%d')
            self.new_data.drop(columns=['Year', 'Month', 'Day','Letters', 'Numbers','plate number'],inplace=True)
            self.df=pd.concat([self.old_data,self.new_data],join='outer')
            self.new_data['concat'] = self.new_data['Date'].dt.strftime('%Y-%m-%d') + self.new_data['Needs'].astype(str)
            self.df['concat'] = self.df['Date'].dt.strftime('%Y-%m-%d') + self.df['Needs'].astype(str)
            self.df['kind data'] = np.where(self.df['concat'].isin(self.new_data['concat'].unique()), 'New', 'Old')
            self.df=self.df.merge(self.database,how='left',on='VPlate Number')
            return self.df
        except Exception as e:
            st.write(e)
    def check_type(self):
        self.df=self.df_()
        self.df = self.df.set_index('Date').sort_index()
        self.df=self.df[['kind data', 'Needs', 'Quantity', 'Vehicle Type'] + [column for column in self.df.columns if column not in ['kind data', 'Needs', 'Quantity', 'Vehicle Type']]]
        self.df['others']=self.df['VPlate Number'].str.replace(' ','')
        self.df['others2']=self.df['Needs'].str.replace(' ','')
        for car in self.df['others'].unique():
            self.data=self.df[self.df['others']==car.replace(' ','')]
            self.data.drop(columns=['others'])
            if len(self.data['kind data'].unique())>1:
                if select=='All':
                    if not self.data.empty:
                            st.write(car.replace(' ',''))
                            st.dataframe(self.data)
                    else:
                        pass
                elif select=='Select Category':
                    pass
                else:
                    self.data=self.data[self.data['others2']==select.replace(' ','')]
                    if len(self.data['kind data'].unique())>1:
                        if not self.data.empty:
                            self.data = self.data.reset_index()
                            self.data['Date2']=self.data['Date'].shift(1)
                            self.data['DateDifference'] = (self.data['Date'] - self.data['Date2']).dt.days
                            self.data['predict Total KM']=self.data['DateDifference'].astype('float')* self.data['avg km_day'].astype('float')
                            self.data['Actual difference KM']=self.data['Current KM'].astype('float')-self.data['Last Maintenance KM'].astype('float')
                            self.data['rest']=self.data['km to change oil'].fillna(0)-self.data['Actual difference KM'].fillna(0)
                            self.data=self.data.set_index('Date')
                            self.data=self.data[['kind data', 'Needs', 'Quantity', 'Vehicle Type','predict Total KM','Actual difference KM','rest','DateDifference'] + [column for column in self.data.columns if column not in ['kind data','rest', 'Needs', 'Quantity', 'Vehicle Type','predict Total KM','Actual difference KM','DateDifference']]]
                            self.data.drop(columns=['Date2','others','others2','concat','Letters','Numbers','new plate number_y'],inplace=True)
                            st.dataframe(self.data)
            else:
                pass



if 'category' not in st.session_state:
    st.session_state.category= 'Select Category'
oa=Oa_maintenance(old_data,database)
if check :
    oa.check_type()
if uploaded_file:
    oa.df_()
        
        


