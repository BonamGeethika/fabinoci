import streamlit as st
import matplotlib.pyplot as plt

# --- Function to generate Fibonacci sequence ---
def generate_fibonacci(n_terms):
    """Generates a Fibonacci sequence up to n_terms."""
    if n_terms <= 0:
        return []
    elif n_terms == 1:
        return [0]
    else:
        sequence = [0, 1]
        while len(sequence) < n_terms:
            next_val = sequence[-1] + sequence[-2]
            sequence.append(next_val)
        return sequence

# --- Streamlit App ---

st.title("Autoregressive Text Generation") # Title as seen in the image

# General description (as seen in the image, even if specific content is numerical)
st.write("This app generates text using an autoregressive model from Hugging Face.")

# Dropdown for sequence type (mimicking the image, though only Fibonacci is implemented here)
st.selectbox(
    "Choose the Sequence Type",
    ("Fibonacci", "Arithmetic Progression", "Geometric Progression", "Word-Based Sequence"), # Include other types as placeholder
    index=0 # Default to Fibonacci
)

st.write("---") # Separator for visual clarity

st.header("Generating Fibonacci Sequence:") # Section header

st.subheader("Fibonacci Sequence") # Subheader for the specific sequence

# Slider for number of terms
n_terms = st.slider(
    "Select the number of terms",
    min_value=2, # Fibonacci sequence usually starts with at least 2 terms (0, 1) to be interesting
    max_value=100,
    value=10, # Default value as seen in the image
    step=1
)

# Button to trigger generation
if st.button("Generate Fibonacci Sequence"):
    fib_sequence = generate_fibonacci(n_terms)

    # Display the generated sequence in a success box
    st.success(f"Fibonacci Sequence: {fib_sequence}")

    # --- Visualization ---
    st.write("---") # Separator
    st.subheader("Fibonacci Sequence Plot") # Explicit subheader for the plot

    fig, ax = plt.subplots(figsize=(8, 5)) # Adjust figure size as needed
    ax.plot(fib_sequence, marker='o', linestyle='-') # Line plot with circular markers
    
    ax.set_title("Fibonacci Sequence", fontsize=16)
    ax.set_xlabel("Index", fontsize=12)
    ax.set_ylabel("Value", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7) # Add a subtle grid
    
    # Set y-axis limits dynamically but ensure 0 is included
    min_val = min(fib_sequence) if fib_sequence else 0
    max_val = max(fib_sequence) if fib_sequence else 1
    ax.set_ylim(bottom=min_val - (max_val - min_val) * 0.1, top=max_val + (max_val - min_val) * 0.1)


    st.pyplot(fig)