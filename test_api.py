import requests
import json


api_endpoints = [
    'https://api.example.com/v1/users',
    'https://api.example.com/v1/orders',
    'https://api.example.com/v1/products'
]


http_methods = ['GET', 'POST', 'PUT', 'DELETE']


auth_token = 'your_auth_token'

def test_api_security(url, methods, token=None):
    headers = {'Authorization': f'Bearer {token}'} if token else {}
    print(f"\nTesting API endpoint: {url}\n")
    
    for method in methods:
        try:
            response = requests.request(method, url, headers=headers)
            print(f"Method: {method}, Status Code: {response.status_code}")

            
            try:
                response_json = response.json()
                print(f"Response JSON: {json.dumps(response_json, indent=2)}")
            except ValueError:
                print(f"Response Text: {response.text[:100]}")  # Prikaz prvih 100 karaktera odgovora

            
            if 'password' in response.text.lower() or 'secret' in response.text.lower():
                print("Sensitive information detected in response!")
        except Exception as e:
            print(f"Error with method {method}: {str(e)}")

def main():
    for endpoint in api_endpoints:
        test_api_security(endpoint, http_methods, auth_token)

if __name__ == "__main__":
    main()
