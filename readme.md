- pyside6 - wait signal using asyncio 
    * checkbox - check option at interval time (eg. 5sec)
    * label - view loaded condition on db
    * when action completed, put waiting option to postgresql
    
- fastapi(django) - set option using postgresql
    * setting page - button : when push the button, put runing option to postgresql
        * when push button again, put pause option to postgresql
        * check option with websocket (soon)

- postgresql - DBMS
    * table
        * running_test - run_option : wait, run, pause


# module
- pyside6, fastapi, jinja2, psycopg[binary], uvicorn
    * `pip install pyside6 fastapi jinja2 "psycopg[binary]" uvicorn`

# action
- btnRun
    * when button clicked, chkCondition value is checked, progress that from postgresql will run automatically.
    * when chkCondition value is not checked, progress that from program will manually.



# application
- fastapi
    * uvicorn app:app --reload

- pyside
    * python load_api.py