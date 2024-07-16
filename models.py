from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pandas as pd

# flask크 기반 앱
app = Flask(__name__)

# config파일 설정
app.config.from_pyfile('config.py')

# 앱에서 사용할 디비 연결
db = SQLAlchemy(app)

# 애플리케이션 app , 데이터베이스 db를 flask migrate에 연결
migrate = Migrate(app, db)

# 테이블
class PatentTable (db.Model) :
    __tablename__ = 'patent_table'

    status = db.Column(db.String(50), nullable=False)   #   상태
    title = db.Column(db.String(200), nullable=False)   #   제목
    ap_num                      =   db.Column(db.Integer, nullable=False, primary_key=True) #   출원번호
    application_date            =   db.Column(db.Date, nullable=False)  # 출원일
    applicant                   =   db.Column(db.String(200), nullable=False) #   출원인 
    representative              =   db.Column(db.String(200)) #   대리인
    final_owner                 =   db.Column(db.String(200)) #   최종권리자
    priority_date               =   db.Column(db.Date)    #   우선권주장일자
    international_filing_date   =   db.Column(db.Date)    #   국제출원일자
    summary = db.Column(db.Text)  #   요약
    general = db.Column(db.Boolean)  # 제너럴
    medical = db.Column(db.Boolean)  # 의료
    ecommerce_services = db.Column(db.Boolean)  # 전자상거래서비스
    automotive = db.Column(db.Boolean)  # 자동차
    finance = db.Column(db.Boolean)  # 금융
    education = db.Column(db.Boolean)  # 교육
    agriculture = db.Column(db.Boolean)  # 농업
    entertainment = db.Column(db.Boolean)  # 엔터테인먼트
    security = db.Column(db.Boolean)  # 보안
    automation_systems = db.Column(db.Boolean)  # 자동화시스템
    applicant_sgrp  =   db.Column(db.String(100))
    applicant_lgrp  =   db.Column(db.String(100))
    ongoing         =   db.Column(db.Boolean)
    application_year    =   db.Column(db.String(10))

# 테이블 생성
def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()

        df = pd.read_excel('result_mod_30June2024_database.xlsx',index_col=0)

        df.to_sql('patent_table', con=db.engine, if_exists='append', index=False)

        print('테이블 생성 성공')