from config import *
from pymongo import MongoClient
from random import randint

def mongoConnect():
    """ Connect to the MongoDB database server """
    client = None
    try:
        params = mongoConfig()
        print('Connecting to the MongodDB database...')

        #Step 1: Connect to MongoDB - Note: Change connection string as needed
        client = MongoClient(f'{params["host"]}:{params["port"]}',
                     username=params["user"],
                     password=params["password"],
                     replicaSet=params["relicaset"],
                     readPreference=params["preference"])

        # Access database
        mydatabase = client.admin

        #Step 2: Create sample data
        names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
        company_type = ['LLC','Inc','Company','Corporation']
        company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']

        for x in range(1, 201):
            record = {
                'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
                'rating' : randint(1, 5),
                'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))] 
            }

            #Step 3: Insert record object directly into MongoDB via insert_one
            result=mydatabase.reviews.insert_one(record)

            #Step 4: Print to the console the ObjectID of the new document
            print('Created {0} of 200 as {1}'.format(x,result.inserted_id))

        #Step 5: Tell us that you are done
        print('finished creating 200 record reviews')

        print("----- Check ReplicaSet status -----")
        print(client.admin.command("replSetGetStatus"))
        
    except Exception as error:
        print(error)
    finally:
        if client is not None:
            client.close()
            print('Database connection closed.')

def main():
    mongoConnect()

if __name__ == '__main__':
    main()


    
