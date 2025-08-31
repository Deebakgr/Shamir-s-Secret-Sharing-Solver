import streamlit as st
from fractions import Fraction
import json

# ---------- Lagrange interpolation ----------
def lagrange_interpolation(points, k):
    """Reconstruct secret (constant term) using Lagrange interpolation"""
    secret = Fraction(0, 1)

    for i in range(k):
        xi, yi = points[i]
        num, den = Fraction(1, 1), Fraction(1, 1)
        for j in range(k):
            if i != j:
                xj, _ = points[j]
                num *= (0 - xj)
                den *= (xi - xj)
        li_at_0 = num / den
        secret += yi * li_at_0

    return secret.limit_denominator()


# ---------- Validator ----------
def validate_points(points, k):
    """Check if points fit the reconstructed polynomial"""
    wrong_points = []

    for (x, y) in points:
        fx = Fraction(0, 1)
        for i in range(k):
            xi, yi = points[i]
            num, den = Fraction(1, 1), Fraction(1, 1)
            for j in range(k):
                if i != j:
                    xj, _ = points[j]
                    num *= (x - xj)
                    den *= (xi - xj)
            li_at_x = num / den
            fx += yi * li_at_x

        if fx != y:
            wrong_points.append((x, y))

    return wrong_points


# ---------- Runner ----------
def run_testcase(data, label):
    n = data["keys"]["n"]
    k = data["keys"]["k"]

    points = []
    for key, val in data.items():
        if key == "keys":
            continue
        x = int(key)
        base = int(val["base"])
        y = int(val["value"], base)
        points.append((x, y))

    points = sorted(points)

    secret = lagrange_interpolation(points, k)
    wrong_points = validate_points(points, k)

    return secret, wrong_points


# ---------- Streamlit UI ----------
st.title("🔐 Shamir's Secret Sharing Solver")
st.write("Upload JSON test cases and reconstruct the secret constant term.")

uploaded_file = st.file_uploader("Upload JSON file", type="json")

if uploaded_file:
    data = json.load(uploaded_file)

    # Support multiple test cases inside one file
    if isinstance(data, dict) and "keys" in data:
        st.subheader("TestCase - 1")
        secret, wrong_points = run_testcase(data, "TestCase - 1")
        st.write(f"**Output for TestCase - 1:** {secret}")
        st.write(f"**Wrong Data Set Points for TestCase - 1:** {wrong_points if wrong_points else 'None'}")
    else:
        # Multiple test cases in single JSON
        for idx, tc in enumerate(data, 1):
            st.subheader(f"TestCase - {idx}")
            secret, wrong_points = run_testcase(tc, f"TestCase - {idx}")
            st.write(f"**Output for TestCase - {idx}:** {secret}")
            st.write(f"**Wrong Data Set Points for TestCase - {idx}:** {wrong_points if wrong_points else 'None'}")
