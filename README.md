# neomodel-locust
Performance tests for neomodel

## How to use
It's based on locust, so in order to run it, run the following commands :

```python
# Start the test API
# Note that it's tied to a branch for the neomodel repo
pipenv install
pipenv run start

# In a separate terminal
pipenv run locust
```

Then, go to the Locust UI, and pass the following parameters (adjust accordingly):

|Parameter|Value (default)|
|---|---|
|Number of users|1|
|Ramp up|1|
|Host|http://localhost:8000|
|Run time (advanced)|10|
