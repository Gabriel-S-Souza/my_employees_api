# my_employees_api

This is a simple Python and FastAPI backend project that uses PostgreSQL to store employee data. It provides two endpoints:


```sh
GET /employees - Lists all employees
```

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

To install the project, you will need to install the following dependencies:

pip install -r requirements.txt
Then, you can run the project with the following command:

uvicorn main:app --reload
This will start the FastAPI server on port 8000.

contact: gabriel.appdeveloper@gmail.com