<!---Test to create code to analyze CSV files using pandas and matploblib-->
import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(csv_file):
  """Reads, analyzes, and visualizes data from a CSV file."""

  try:
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file)

    # --- Perform analysis ---
    # Example 1: Calculate basic statistics
    print("Descriptive Statistics:")
    print(df.describe())

    # Example 2: Calculate correlation between columns
    print("\nCorrelation Matrix:")
    print(df.corr())

    # --- Create visualizations ---
    # Example 1: Histogram of a numerical column
    plt.figure(figsize=(8, 6))
    plt.hist(df['column_name'], bins=10)  # Replace 'column_name'
    plt.xlabel("Column Name")
    plt.ylabel("Frequency")
    plt.title("Histogram of Column Name")
    plt.savefig("histogram.png")  # Save the figure

    # Example 2: Scatter plot between two columns
    plt.figure(figsize=(8, 6))
    plt.scatter(df['column1'], df['column2'])  # Replace 'column1' and 'column2'
    plt.xlabel("Column 1")
    plt.ylabel("Column 2")
    plt.title("Scatter Plot of Column 1 vs. Column 2")
    plt.savefig("scatter_plot.png")  # Save the figure

  except FileNotFoundError:
    print(f"Error: CSV file '{csv_file}' not found.")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  csv_file = "your_data.csv"  # Replace with your CSV file name
  analyze_data(csv_file)
