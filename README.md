# NCXSoftwareDevGray

# User Management API

## 1) Add a User

- **URL**: `/users`
- **HTTP Method**: POST
- **Parameters**:
  - `name` (string): The name of the user
  - `phone_number` (string): The phone number of the user

## 2) Lookup User's Phone Number by Name

- **URL**: `/users/{name}`
- **HTTP Method**: GET
- **Parameters**:
  - `name` (String): The name of the user to lookup

## 3) Delete User

- **URL**: `/users/{name}`
- **HTTP Method**: DELETE
- **Parameters**:
  - `name` (string): The name of the user to delete

