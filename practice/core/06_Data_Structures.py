# Practice Questions: Data Structures

# 1. Lists
#   a) Create a list named `colors` with the following items: "red", "green", "blue", "yellow".
#   b) Print the second item in the list.
#   c) Change the value of the last item to "purple".
#   d) Add a new color, "orange", to the end of the list.
#   e) Remove "green" from the list.
#   f) Print the final list.

colors = ["red", "green", "blue", "yellow"]
print(colors[1]) 
colors[-1] = "purple"  
colors.append("orange") 
colors.remove("green")  
print(colors)  


# 2. Tuples
#   a) Create a tuple named `point` representing (x, y) coordinates, e.g., (10, 20).
#   b) Try to change the first value of the tuple to 15. What happens? (Add a comment explaining the result).
#   c) Create a new tuple `point3D` by adding a z-coordinate (30) to the `point` tuple.
#   d) Print the `point3D` tuple.

point = (10, 20)
# point[0] = 15  # This will raise a TypeError because tuples are immutable and cannot be modified after creation.
point3D = point + (30,)  # Create a new tuple by adding a z-coordinate
print(point3D) 


# 3. Sets
#   a) Create a set `set1` with the numbers 1, 2, 3, 4, 5.
#   b) Create a set `set2` with the numbers 4, 5, 6, 7, 8.
#   c) Find and print the union of the two sets.
#   d) Find and print the intersection of the two sets.
#   e) Find and print the difference between `set1` and `set2` (`set1` - `set2`).
#   f) Add the number 6 to `set1`. Print `set1`.
#   g) Try to add the number 2 to `set1` again. What happens? (Add a comment explaining).

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))  
print(set1.intersection(set2)) 
print(set1.difference(set2)) 
set1.add(6)  
print(set1)  
# set1.add(2)  # Adding the number 2 again will not change the set because sets do not allow duplicate values. The set will remain unchanged.


# 4. Dictionaries
#   a) Create a dictionary `student` with the following key-value pairs:
#      - "name": "Emily"
#      - "age": 22
#      - "major": "Computer Science"
#   b) Print the student's age.
#   c) Add a new key-value pair for "gpa" with a value of 3.8.
#   d) Change the value of "major" to "Electrical Engineering".
#   e) Print all the keys in the dictionary.
#   f) Print all the values in the dictionary.
#   g) Print the final dictionary.

student = {
    "name": "Emily",
    "age": 22,
    "major": "Electrical Engineering"
}
print(student["age"])  
student["gpa"] = 3.63
student["major"] = "Computer Science"  
print(student.keys()) 
print(student.values()) 
print(student)  


# 5. Putting it all together
#   a) Create a list of dictionaries, where each dictionary represents a book. Each book should have "title", "author", and "year" keys.
#      books = [
#          {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
#          {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
#          # Add one more book dictionary
#      ]
#   b) Write a `for` loop that iterates through the list of books.
#   c) Inside the loop, print the title and author of each book in the format: "Title by Author".
#   d) Add a check inside the loop to print "(Classic)" next to the book if it was published before 1950.

books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949}
]
for book in books:
    title = book["title"]
    author = book["author"]
    year = book["year"]
    if year < 1950:
        print(f"{title} by {author} (Classic)")
    else:
        print(f"{title} by {author}")

