(item['Content'])
                sql+=str('\', \'')
                sql+=str(item['PubTime'])
               
                sql+=str('\', \'')
               
                sql+=str(item['Co_oridinates'])
               
                sql+=str('\', \'')
                sql+=str(item['Tools'])
                print(sql)
                sql+=str('\', \'')
                sql+=str(item['Like'])
                sql+=str('\', \'')
                sql+=str(item['Comment'])
                sql+=str('\', \'')
                sql+=str(item['Transfer'])
                sql+=str('\')')
                print("*********** SQL SYNTAX *********** ")
                print(''.join(sql))
                self.cur.execute(sql)
                self.conn.commit()
                print("saved")
                self.count = self.count +1
                print(self.count)
            except Exception:
                pass
        elif isinstance(item, InformationItem):
            try:
                print("***********at beginning of saving**********")
                
                sql = ''
                sql+=str('INSERT INTO SinaWeibo.Information (`User_id`,`NickName`,`Gender`,`Province`,`City`,`BriefIntroduction`,`Birthday`,`Num_Tweets`,`Num_Follows`,`Num_Fans`,`SexOrientation`,`Sentiment`,`VIPlevel`,`Authentication`,`URL`) ')
                sql+=str(' Values(\'' )
                sql+=str(item['_id'])
               
                sql+=str('\', \'')
                sql+=str(item['NickName'])
                sql+=str('\', \'')
                sql+=str(item['Gender'])
                sql+=str('\', \'')
                sql+=str(item['Province'])
                
                sql+=str('\', \'')
                sql+=str(item['City'])
                sql+=str('\', \'')
                sql+=str(item['BriefIntroduction'])
                sql+=str('\', \'')
                print(sql)
                sql+=str(item['Birthday'])
                sql+=str('\', \'')
                sql+=str(item['Num_Tweets'])
               
                sql+=str('\', \'')
                sql+=str(item['Num_Follows'])
                sql+=str('\', \'')
                sql+=str(item['Num_Fans'])
                sql+=str('\', \'')
                
                sql+=str(item['SexOrientation'])
                sql+=str('\', \'')
                sql+=str(item['Sentiment'])
                
                sql+=str('\', \'')
                sql+=str(item['VIPlevel'])
                sql+=str('\', \'')
                sql+=str(item['Authentication'])
                sql+=str('\', \'')
                sql+=str(item['URL'])
                sql+=str('\')')
               
                print("*********** SQL SYNTAX *********** ")
                print(''.join(sql))
                self.cur.execute(sql)
                self.conn.commit()
                print("saved")
                self.count = self.count +1
                print(self.count)
            except Exception:
                pass
            
            ##在Java开发中，Dao连接会对内存溢出，需要定时断开重连，这里不清楚是否需要，先加上了
            if self.count == 1000:
                print("try reconnecting")
                self.count = 0
                self.cur.close()
                self.conn.close()
                self.conn = MySQLdb.connect(
                    host='localhost',
                    port=3306,
                    user='root',
                    passwd='***',
                    db='SinaWeibo',
                    charset='utf8',
                )
                self.cur = self.conn.cursor()
                print("reconnect")
                
        return item
    


class MongoDBPipleline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["Sina"]
        self.Information = db["Information"]
        self.Tweets = db["Tweets"]
        self.Relationships = db["Relationships"]

    def process_item(self, item, spider):
        """ 判断item的类型，并作相应的处理，再入数据库 """
        if isinstance(item, RelationshipsItem):
            try:
                self.Relationships.insert(dict(item))
            except Exception:
                pass
        elif isinstance(item, TweetsItem):
            try:
                self.Tweets.insert(dict(item))
            except Exception:
                pass
        elif isinstance(item, InformationItem):
            try:
                self.Information.insert(dict(item))
            except Exception:
                pass
        return item
