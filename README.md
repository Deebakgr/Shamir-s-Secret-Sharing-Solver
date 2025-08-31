# Shamir-s-Secret-Sharing-Solver

This project implements Shamir’s Secret Sharing reconstruction algorithm using Lagrange Interpolation.
It reads test cases in JSON format, reconstructs the secret (constant term of the polynomial), and identifies wrong dataset points.

The project includes a Streamlit web app for interactive use.

📌 Features

Accepts JSON test cases (e.g., input shares with base and value).

Converts values from arbitrary bases into decimal.

Uses Lagrange Interpolation to reconstruct the polynomial.

Recovers the secret (constant coefficient).

Validates points and reports wrong dataset points.

Interactive Streamlit UI.

🛠️ Requirements

Python 3.8+

Dependencies:

pip install streamlit

Run the Streamlit app:

streamlit run app.py


Open your browser at http://localhost:8501

Upload a JSON file with test cases.
