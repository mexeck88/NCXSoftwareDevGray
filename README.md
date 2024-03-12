# NCXSoftwareDevGray
![](https://github.com/mexeck88/NCXSoftwareDevGray/blob/master/giphy.gif)
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

### Scoring Criteria
1. **1 point** for each compliant JSON API endpoint.
2. **1 point** for a compliant test suite for all URLs.
3. **2 points** for persistence using SQLite or another database.
4. **2 points** for a front-end GUI in HTML for the lookup endpoint `/users/{name}`.
   
   The tiebreaker is the time of completion. Points are awarded sequentially for each item.

   Phone number format: `555-555-5555`

