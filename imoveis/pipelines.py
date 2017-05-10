# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pyrebase, hashlib

class ImoveisPipeline(object):
    def process_item(self, item, spider):
        return item

class FirebaseQueryPipeline(object):
    def process_item(self, item, spider):
        config = {
            "apiKey": "AIzaSyAlnjwpz5tXLcibzK0vpF8-7tYUcyWDuUw",
            "authDomain": "imoveis-5521b.firebaseapp.com",
            "databaseURL": "https://imoveis-5521b.firebaseio.com",
            "projectId": "imoveis-5521b",
            "storageBucket": "imoveis-5521b.appspot.com",
            "messagingSenderId": "858178649642",
            # "serviceAccount": "imoveis\serviceAccountCredentials.json"
        }
        firebase = pyrebase.initialize_app(config)
        # Get a reference to the auth service
        auth = firebase.auth()
        # Log the user in
        user = auth.sign_in_with_email_and_password("admin@aluguemais.com", "admin123456")

        db = firebase.database()
        data = {
            "title": item["title"],
            "priceValue": item["priceValue"],
            "zipCode": item["zipCode"]
        }

        print("########################################")
        print(item["site"])
        print(data)
        print("########################################")

        cod_id = hashlib.md5(("vivareal_%s" % item["propertyId"]).encode('utf-8')).hexdigest()
        results = db.child("imoveis/%s" % cod_id).set(data, user['idToken'])
        return item
