import requests

def generate_webhook():
    url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
    payload = {
        "name": "Jay Thakre",
        "regNo": "0827AL221062", 
        "email": "jayravindra220586@acropolis.in"  
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        print("Webhook URL:", data["webhook"])
        print("Access Token:", data["accessToken"])
        return data["webhook"], data["accessToken"]
    else:
        print("Error generating webhook:", response.status_code)
        print(response.text)
        return None, None

def submit_sql_query(webhook_url, access_token, sql_query):
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }

    payload = {
        "finalQuery": sql_query
    }

    response = requests.post(webhook_url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Query submitted successfully!")
        print(response.text)
    else:
        print("Failed to submit query:", response.status_code)
        print(response.text)

if __name__ == "__main__":
    
    webhook, token = generate_webhook()

    if webhook and token:
        
        final_sql_query = """
       
SELECT 
    e1.EMP_ID,
    e1.FIRST_NAME,
    e1.LAST_NAME,
    d.DEPARTMENT_NAME,
    COUNT(e2.EMP_ID) AS YOUNGER_EMPLOYEES_COUNT
FROM EMPLOYEE e1
JOIN DEPARTMENT d ON e1.DEPARTMENT = d.DEPARTMENT_ID
LEFT JOIN EMPLOYEE e2 
    ON e1.DEPARTMENT = e2.DEPARTMENT 
    AND e2.DOB > e1.DOB
GROUP BY 
    e1.EMP_ID,
    e1.FIRST_NAME,
    e1.LAST_NAME,
    d.DEPARTMENT_NAME
ORDER BY 
    e1.EMP_ID DESC;
"""
        

        
   
        submit_sql_query(webhook, token, final_sql_query)