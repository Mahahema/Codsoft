import pandas as pd

# Sample data: A list of books with their titles and genres
data = {
    'Title': ['The Adventure of Sherlock Holmes', 'The Catcher in the Rye', 'Moby Dick', 'To Kill a Mockingbird', 'War and Peace'],
    'Genre': ['Mystery', 'Fiction', 'Classic', 'Drama', 'Historical']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Function to recommend books based on user input and genre similarity (without descriptions)
def recommend_books_by_genre(user_input, df):
    print(f"\nYour input genre: {user_input}")
    
    # Create a list to store similarity scores based on genre
    sim_scores = []
    
    # Compare user input with each book's genre
    for index, row in df.iterrows():
        genre = row['Genre']
        
        # Calculate keyword similarity between user input and genre
        common_keywords = len(set(user_input.lower().split()) & set(genre.lower().split()))
        sim_scores.append((index, common_keywords))
    
    # Sort by similarity score in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the top 3 most similar books (we exclude the input genre itself)
    recommended_indices = [score[0] for score in sim_scores[1:4]]  # Exclude the input genre itself
    
    # Print out the recommended book titles
    print("\nBooks recommended for you based on genre similarity:")
    for idx in recommended_indices:
        print(f"- {df['Title'][idx]} ({df['Genre'][idx]})")

# Get user input for genre preference
user_input = input("Enter your preferred genre (e.g., 'Fiction', 'Mystery', 'Drama'): ")

# Call the recommendation function
recommend_books_by_genre(user_input, df)
