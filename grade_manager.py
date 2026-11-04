# grade_manager.py
# Student Grade Manager - GenAI Course Assignment

students = []  # List to store all students: each student is a dictionary

def get_grade(mark):
    """Return the grade letter based on the mark."""
    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark <= 89:
        return "B"
    elif 70 <= mark <= 79:
        return "C"
    elif 60 <= mark <= 69:
        return "D"
    else:
        return "E"

def add_student():
    """Ask for name and mark, validate, then store the student."""
    name = input("Enter student name: ").strip()
    
    if not name:  # Empty name
        print("Name cannot be empty. Please try again.\n")
        return
    
    # Keep asking until we get a valid mark
    while True:
        mark_input = input("Enter mark (0-100): ").strip()
        
        if not mark_input:
            print("Mark cannot be empty. Please try again.")
            continue
        
        try:
            mark = float(mark_input)
            if 0 <= mark <= 100:
                # Valid mark - store the student
                student = {
                    "name": name,
                    "mark": mark,
                    "grade": get_grade(mark)
                }
                students.append(student)
                print(f"Added: {name} with mark {mark}\n")
                break
            else:
                print("Mark must be between 0 and 100. Please try again.")
        except ValueError:
            print("Please enter a valid number (e.g. 85 or 72.5).")

def show_results():
    """Print the table and statistics."""
    if not students:
        print("No students added yet.\n")
        return
    
    print("\n" + "="*40)
    print(f"{'Name':<15} {'Mark':>6} {'Grade':>8}")
    print("-"*40)
    
    total = 0
    highest = students[0]["mark"]
    lowest = students[0]["mark"]
    
    for s in students:
        print(f"{s['name']:<15} {s['mark']:>6.1f} {s['grade']:>8}")
        total += s["mark"]
        if s["mark"] > highest:
            highest = s["mark"]
        if s["mark"] < lowest:
            lowest = s["mark"]
    
    average = total / len(students)
    print("-"*40)
    print(f"Average: {average:.1f}   Highest: {highest}   Lowest: {lowest}")
    print("="*40 + "\n")

def main():
    """Main menu loop."""
    print("=== Student Grade Manager ===\n")
    
    while True:
        print("1. Add student")
        print("2. Show results")
        print("3. Quit")
        
        choice = input("Choose an option (1/2/3): ").strip()
        
        if choice == "1":
            add_student()
        elif choice == "2":
            show_results()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

# Start the program
if __name__ == "__main__":
    main()