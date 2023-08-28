# my_employees_api

This is a simple Python and FastAPI study project that uses PostgreSQL to store employee data. It provides two endpoints:


```sh
GET /employees - Lists all employees
```
response:
```sh
[
	{
		"id": 6,
		"name": "Jonh Dow",
		"personal_id": 123,
		"biometric": [1.0, 2.0, 3.0, 4.0, 5.0],
		"pic": [1, 2, 3, 4, 5], # base64
		"created_at": "2023-08-27T21:48:45.394094"
	},
	(...)
]

```
<br>

```sh
POST /employees - Creates a new employee
```

body:
```sh
{
	"name": "Jonh Dow",
	"personal_id": 123,
	"biometric": [1.0, 2.0, 3.0, 4.0, 5.0],
	"pic": [1, 2, 3, 4, 5] # base64
}
```

## how to run
To install the project, you will need to install the dependencies with:
```sh
pip install -r requirements.txt
```

Then, you can run the project with the following command:
```sh
uvicorn main:app --reload
```

contact: gabriel.appdeveloper@gmail.com
