from google import genai

# The client automatically picks up the GEMINI_API_KEY environment variable
client = genai.Client()

# This block will ONLY run if you run this file directly (python gemai_client.py)
if __name__ == "__main__":
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents="",
    )
    print(response.text)