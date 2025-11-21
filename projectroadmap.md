# Skin Care System – Project Roadmap

## Sprint 1 – Existing Codebase Exploration

For my related codebase, I cloned the **SkincareAPI** project from GitHub:  
https://github.com/LauraAddams/skincareAPI  

This project is a Ruby on Rails application that exposes a public skincare product API with endpoints for brands, product names, ingredient lists, and search queries. This structure is relevant to my Skin Care System idea because it shows how real skincare data can be organized and accessed programmatically.

To evaluate it, I cloned the repository locally and wrote a small Python script (`test_api.py`) that attempted to call the documented API endpoints using the `requests` library (ex: `https://skincare-api.herokuapp.com/products`). The API returned a 404 error, suggesting the hosted version is offline. Even though I could not test live data, reviewing the code helped me understand how skincare information can be stored, structured, and served through an API.

**Going forward, I plan to:**
- Use the SkincareAPI structure as inspiration for organizing product and ingredient data.
- Build my own small dataset/API in Python so the Skin Care System can make product recommendations.


---

## Sprint 2 – Coding Progress and Git Workflow

During this sprint, I focused on writing the actual code for the Skin Care System and learning how to manage updates using Git and GitHub Desktop.

I created several files that handle the system’s logic:
- `products_sample.json` for storing sample skincare products and categories  
- `rules.py` for defining simple recommendation rules  
- `recommender.py` for loading data and applying the rules  
- `main.py` which runs the program and asks the user questions  

I also added a `requirements.txt` file to track my Python dependencies.

While working, I committed changes regularly with descriptive messages. This helped me practice the application development workflow and made my progress visible. I did encounter issues while moving the project into the KSU-IS organization, but I resolved them by creating a new repository and copying my finished project files into it.

**Next steps:**
- Expand my product dataset  
- Add more rules to improve recommendations  
- Begin adding user-input validation and better formatting in the CLI  


