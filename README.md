## Assembly - Report

***

### About
Backend service to monitor several restaurants in the US and needs to monitor if the store is online or not. All restaurants are supposed to be online during their business hours. Due to some unknown reasons, a store might go inactive for a few hours. It generates a report of the how often this happened in the past. 


### TechStack
1. FASTAPI - As a web framework for building APIs.

2. POSTGRES - As database to store relevent data.

3. CELERY - To run queue based task

4. RABBITMQ - As a broker


### Installation and Setup 
1. Clone this repository

```sh
git clone https://github.com/k-kgs/Assembly-Report.git
```

2. Install the dependencies

```sh
pip3 install -r requirements.txt
```

3. Run the local node
```sh
uvicorn main:app --reload
```

4. Interact at localhost with swagger

```sh
http://localhost:8000/docs
```


### Working 
This service contains two endpoints:
1. '/trigger_report' - It will trigger the process for report generation

2. '/get_report' - It will return the status of the report or the csv

