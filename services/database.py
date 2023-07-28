import sqlite3


    
async def input_database(df):
    conn = sqlite3.connect('tweets.db')
    cursor = conn.cursor()

    cursor.execute(''' CREATE TABLE IF NOT EXISTS tweets
                   (Tweet TEXT, tweets_clean TEXT, Sentiment TEXT)''')
 
    cursor = conn.execute("SELECT Tweets_clean FROM tweets")
    tweets_list = [row[0] for row in cursor]

    if len(tweets_list) == 0:
        df.to_sql ('tweets', conn, if_exists='replace', index=False)
        conn.close()
    
    else:
        df_list = df['Tweets_clean'].tolist()
        index_to_remove = []
        for index, i in enumerate(df_list):
            if i in tweets_list:
                index_to_remove.append(index)
            else:
                pass
                
        
        fix_input = df.drop(index = index_to_remove)
        fix_input.to_sql ('tweets', conn, if_exists='append', index=False)
        conn.close()


async def ambil_data():
    conn = sqlite3.connect('tweets.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT * FROM tweets''')
    ambil_data = cursor.fetchall()

    data_siap = []
    for tuple in ambil_data:
        jadi_dict = {"Tweet" : tuple[0],
                "Tweets_clean" : tuple[1],
                "Sentiment" : tuple[2]
        }
        data_siap.append(jadi_dict)

    return data_siap


async def ambil_sentiment(sentiment):
    conn = sqlite3.connect('tweets.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM tweets WHERE Sentiment = ?', ((sentiment),))
    ambil_data = cursor.fetchall() 

    data_siap = []
    for tuple in ambil_data:
        jadi_dict = {"Tweet" : tuple[0],
                "Tweets_clean" : tuple[1],
                "Sentiment" : tuple[2]
        }
        data_siap.append(jadi_dict)
   

    return data_siap