## Sprint 1 – Existing Codebase Exploration

For my related codebase, I cloned the **SkincareAPI** project from GitHub (https://github.com/LauraAddams/skincareAPI). This project is a Ruby on Rails application that exposes a public skincare product API with endpoints for products and ingredients. The design of the API (brand, product name, ingredient lists, and search endpoints) is directly relevant to my Skin Care System idea because it shows how real skincare data can be structured and queried.

To evaluate it, I opened the codebase locally and wrote a small Python script (`test_api.py`) using the `requests` library to call the documented endpoints (e.g., `https://skincare-api.herokuapp.com/products`). The requests returned a 404 status code, which suggests that the hosted API is no longer available or the endpoint has changed. Even though I could not successfully consume the live API, this experiment helped me understand how my own system could either (1) connect to a similar REST API, or (2) recreate a smaller internal API/dataset of skincare products and ingredients that my Python code can search.

Going forward, I plan to:
- Use the SkincareAPI structure as a model for how to organize product and ingredient data.
- Build a simple Python-based dataset or API that my Skin Care System can use for personalized recommendations.
