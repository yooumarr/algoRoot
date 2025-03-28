# AlgoRoot

The directory structure for the project looks like:

<pre>
algoroot/
├── functions.py # Predefined functions
├── rag.py       # RAG model
├── code_gen.py  # Code generation
├── api.py       # FastAPI API service
└── main.py      # Main file
</pre>

## Running the Project

To run the project, follow these steps:

1.  **Navigate to the project directory:**
    ```bash
    cd algoroot
    ```

2.  **Install the required dependencies:**
    ```bash
    pip install fastapi uvicorn pydantic faiss-cpu sentence-transformers psutil
    ```

3.  **Start the API server:**
    ```bash
    python main.py
    ```

    * This command executes the `main.py` file, which in turn starts the Uvicorn server, running the FastAPI application. Uvicorn handles the web server functionalities. The `--reload` flag inside the `main.py` file will restart the server if you make changes.

4.  **Once the server is running, you can make requests using `curl` or the Python `requests` library.**

    * **Example using `curl`:**
        ```bash
        curl -X POST -H "Content-Type: application/json" -d '{"prompt": "get system info", "arguments": {}}' [http://127.0.0.1:8000/execute](http://127.0.0.1:8000/execute)
        ```

    * **Example using Python `requests`:**
        ```python
       import requests
       import json

       url = "http://127.0.0.1:8000/execute"
       headers = {"Content-Type": "application/json"}

       example = {"prompt": "get current directory", "arguments": {}}
       response = requests.post(url, data=json.dumps(example), headers=headers)
      
       print("Example Get Current Directory:")
       if response.status_code == 200:
           print(response.json())
           #just print code
           response_json = response.json()  
           print('\nCode: ')
           code = response_json.get("code") 
           if code:
               print(code)  
           else:
               print("Code not found in response.")
       else:
           print(f"Error: {response.status_code}, {response.text}")
        ```

Example Usage 1: 
![Screenshot (5)](https://github.com/user-attachments/assets/cc46092c-4416-4476-9e80-ae82055ed11b)
![Screenshot (6)](https://github.com/user-attachments/assets/4732b5f2-ca08-4734-9f6c-07d543d93b6f)


Example Usage 2: 
![Screenshot (7)](https://github.com/user-attachments/assets/e004a984-8291-4a55-843d-d8169f1a68ed)
![Screenshot (8)](https://github.com/user-attachments/assets/215bdae3-b734-41d2-8ec5-48a713df806f)





