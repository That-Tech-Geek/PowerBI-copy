# Install and setup environment
import os
os.system('pip install pandas sqlalchemy spacy matplotlib plotly')
os.system('python -m spacy download en_core_web_sm')

# Full code implementation
import spacy
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

# Load the NLP model
nlp = spacy.load("en_core_web_sm")

# Function to parse English query
def parse_query(query):
    doc = nlp(query)
    columns, conditions = [], []
    for token in doc:
        if token.dep_ == "nsubj":
            columns.append(token.text)
        if token.dep_ == "prep" and token.head.text.lower() == "where":
            conditions.append(token.text)
    return columns, conditions

# Function to generate SQL query from parsed data
def generate_sql(table_name, columns, conditions):
    columns_str = ", ".join(columns) if columns else "*"
    conditions_str = " AND ".join(conditions) if conditions else "1=1"
    sql_query = f"SELECT {columns_str} FROM {table_name} WHERE {conditions_str};"
    return sql_query

# Function to execute SQL query and retrieve data
def execute_sql(sql_query, connection_string):
    engine = create_engine(connection_string)
    df = pd.read_sql(sql_query, engine)
    return df

# Function to visualize the retrieved data
def visualize_data(df):
    fig = px.line(df, x=df.columns[0], y=df.columns[1:])
    fig.show()

# Main function integrating all components with user input
def main():
    # Get user inputs
    table_name = input("Enter the table name: ")
    connection_string = input("Enter the database connection string (e.g., sqlite:///your_database.db): ")
    query = input("Enter your query (e.g., 'Show me sales where region is West'): ")

    # Parse the query
    columns, conditions = parse_query(query)

    # Generate SQL query
    sql_query = generate_sql(table_name, columns, conditions)
    print(f"Generated SQL: {sql_query}")

    # Execute SQL and retrieve data
    df = execute_sql(sql_query, connection_string)
    print(df)

    # Visualize the data
    visualize_data(df)

if __name__ == "__main__":
    main()
