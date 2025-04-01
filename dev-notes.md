



## Pinia Stores

- Getters: allows to filter and manipulate values from the state
- Acctions: allows to update the state of a store.

### Working with a data backend
1. When loading application, create action to retrieve data from backend
2. Use retrieved data to update the store's state
2. When actions update the store's state, they should also update the backend


3. To populate the state with data in the backend 
- Fetch data from the backend
- parse it as JSON
- assign data to store variales.


3. To update data in the backend, 
    - use async functions
    - first, update the state
    - then, update the backend


When naming the 
