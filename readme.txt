# Project's title : 'GRAPHQL_ASSIGNMENT'

# Short Description :
        Python/Django based API service that support GraphQL calls 
        have query for querying Bank Branches data with all the sub class data

# Package requirements :
      # python==3.7.7
      # django==3.1.3
      # psycopg2==2.8.6
      # PostgreSQL==13.3
      # graphene-django==2.13.0

# Project guide for mac os :
    # Make directory named "graphql_assignment"
    # create virtual environment and install django
    # create the skeleton of a Django project
        # hint: (myvenv) ~/djangogirls$ django-admin startproject mysite .
      
    # create an application 'data'
           # hint: (myvenv) ~/djangogirls$ python manage.py startapp data
      # The directories and files in our project should look like this:

        graphql_assignment
            ├── data
            │   ├── admin.py
            │   ├── apps.py
            │   ├── __init__.py
            │   ├── migrations
            │   │   └── __init__.py
            │   ├── models.py
            │   ├── tests.py
            │   └── views.py
            ├── db.sqlite3
            ├── manage.py
            ├── mysite
            │   ├── __init__.py
            │   ├── settings.py
            │   ├── urls.py
            │   └── wsgi.py
            ├── myvenv
            │   └── ...
            └── requirements.txt
    
    # create table 'Bank' & 'Branch' 

        bank
            Column |         Type          | Modifiers
            --------+-----------------------+-----------
            name   | character varying(49) |
            id     | bigint                | not null
            Indexes:
                "banks_id_pkey" PRIMARY KEY, btree (id)
            Referenced by:
                TABLE "branches" CONSTRAINT "branches_banks_fkey" FOREIGN KEY (bank_id) REFERENCES banks(id)

        branches
            Column  |          Type          | Modifiers
            ----------+------------------------+-----------
            ifsc     | character varying(11)  | not null
            bank_id  | bigint                 |
            branch   | character varying(74)  |
            address  | character varying(195) |
            city     | character varying(50)  |
            district | character varying(50)  |
            state    | character varying(26)  |
            Indexes:
            Foreign-key constraints:
                "branches_banks_fkey" FOREIGN KEY (bank_id) REFERENCES banks(id)

    # Setup databases:
            install PostgreSQL
            create user and assign ownership
            update setting.py for PostgreSQL
            Install PostgreSQL package for Python 'psycopg2'
            apply migrations and import data

    # create schema.py file in app data for writting query 
    # setup urls and run the server

    # run GraphiQl and query
        for example query will look like this:
        
        query{
            bankByName(name: "YES BANK"){
                id
                name
                branches{
                    ifsc
                    branch
                    address
                    district
                    city
                    state               
                }
            }
        }

     



























