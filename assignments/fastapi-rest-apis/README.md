# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, high-performance REST APIs using the FastAPI framework. You'll create a web service with multiple endpoints, implement proper HTTP methods, handle request validation, and understand API design principles for building scalable backend services.

## 📝 Tasks

### 🛠️ Set Up FastAPI Project and Create Basic Endpoints

#### Description
Initialize a FastAPI project with necessary dependencies and create your first set of API endpoints. Implement basic routing to handle different HTTP methods (GET, POST).

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn server
- Create a basic FastAPI application
- Define at least 2 GET endpoints that return JSON data
- Define at least 1 POST endpoint that accepts request data
- Run the server and test endpoints using tools like curl or Postman


### 🛠️ Implement Data Validation and Request Models

#### Description
Use Pydantic models to validate incoming request data and ensure type safety. Create proper data structures for your API requests and responses.

#### Requirements
Completed program should:

- Define Pydantic models for request/response data
- Use type hints for all parameters and return values
- Implement validation rules for input data
- Return properly formatted JSON responses with correct status codes
- Handle validation errors gracefully


### 🛠️ Add Advanced Features and Error Handling

#### Description
Enhance your API with advanced features including path parameters, query parameters, error handling, and API documentation.

#### Requirements
Completed program should:

- Implement path parameters (e.g., `/users/{user_id}`)
- Implement query parameters for filtering and pagination
- Add proper HTTP status codes (200, 201, 400, 404, 500)
- Implement error handling with meaningful error messages
- Leverage FastAPI's automatic API documentation (Swagger UI)
