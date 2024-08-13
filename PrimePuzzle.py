import streamlit as st
import math

/* style.css */
body {
    font-family: Arial, sans-serif;
    background-color: #b05757;
}

h1, h2, h3 {
    color: #e51616;
    text-align: center;
}

button {
    background-color: #664caf;
    color: white;
    padding: 15px, 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #575757;
}

def is_prime(num):
    """Checks if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factorization(num):
    """Returns the prime factorization of a number."""
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num //= 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num //= i
    if num > 2:
        factors.append(num)
    return factors

def generate_primes(start, end):
    """Generates prime numbers within a range."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    st.title("Prime Puzzle")
    st.info("Solve the enigma of prime numbers.")
    
    # User input
    number = st.number_input("Enter a number:", min_value=1, value=1)

    # Check if prime
    if st.button("Check if Prime",use_container_width=True):
        if is_prime(number):
            st.success(f"{number} is a prime number!")
        else:
            st.error(f"{number} is not a prime number.")
    st.markdown("---") 

    # Prime factorization
    st.subheader("Prime Factorization")
    if st.button("Prime Factorization"):
        factors = prime_factorization(number)
        st.write(f"Prime factors of {number}: {factors}")
    st.markdown("---") 
    # Generate primes
    start_range = st.number_input("Start of range:", min_value=1, value=1)
    end_range = st.number_input("End of range:", min_value=2, value=100)
    if st.button("Generate Primes"):
        primes = generate_primes(start_range, end_range)
        st.write(f"Prime numbers between {start_range} and {end_range}: {primes}")

    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
