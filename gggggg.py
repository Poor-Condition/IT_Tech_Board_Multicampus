import pymysql
import sqlalchemy

pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "mysql+mysqldb://django:" + "poordjango" + "@poordb.cubqrb9xgtzf.us-east-1.rds.amazonaws.com/poor_db",
    encoding="utf-8")
conn = engine.connect()

# contest_dict
contest_dict = {"contest": contest}

for table_name, contest in contest_dict.items():
    print("\n", table_name, "\n")
    contest_df = pd.DataFrame(
        columns=['공모이름', '분류', '이미지', '조회수', '분야', '응모대상', '주최/주관', '후원/협찬', '접수기간', '총 상금', '1등 상금', '홈페이지', '첨부파일'])

    for post in contest:
        obj = pd.Series(post)
        contest_df = contest_df.append(obj, ignore_index=True)
        print(post)

    contest_df.to_sql(name=table_name, con=engine, if_exists='replace', index=True, index_label='id')