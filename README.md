# JWT Flask example
Run the simplified Flask application to generate and verify JWTs using both symmetric (HS256) and asymmetric (RS256) algorithms. 
This setup allows you to experiment with JWT creation, verification, and exploring vulnerabilities and security measures in a controlled environment.


## Setup

1. clone the repository:
```
git clone https://github.com/ladybuginthemug/jwt-flask.git
```

2. navigate to the project directory:
```
cd jwt-flask-test
```

3. create a virtual environment:
```
python3 -m venv venv
```
4. activate the virtual environment:
- On Windows: `venv\Scripts\activate`
- On macOS/Linux: `source venv/bin/activate`

5. install dependencies:
```
pip install -r requirements.txt
```


## Endpoints

- `/generate-hs256` - Generates a JWT signed with HS256.
- `/generate-rs256` - Generates a JWT signed with RS256.
- `/verify` - Verifies a JWT.

Make sure to replace `yourusername` with your actual GitHub username and adjust instructions as necessary.

### Run the Application:

In the terminal or command prompt (make sure you're in the project directory and the virtual environment is activated), start the Flask application by running:

```bash
python3 app.py
```
This command starts a local web server. By default, Flask runs on port 5000.



Testing 
---

With the application running, you can test its functionality using tools like curl, Postman, or any HTTP client of your choice.

### Generating a Token

**HS256 Token**:
```bash
curl http://127.0.0.1:5000/generate-hs256
```

**RS256 Token**:

```bash
curl http://127.0.0.1:5000/generate-rs256
```

### Verifying a Token
 
 
To verify a token, send a POST request with a JSON payload containing the token to /verify. For example, using curl:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"token":"YOUR_TOKEN_HERE"}' http://127.0.0.1:5000/verify
```
Replace `YOUR_TOKEN_HERE` with the actual token you want to verify.


---
Following these steps, you can run the enhanced Flask application to generate and verify JWTs using both symmetric (HS256) and asymmetric (RS256) algorithms. This setup allows you to experiment with JWT creation, verification, and exploring vulnerabilities and security measures in a controlled environment.


