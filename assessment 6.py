#5
# count = 0
# with open("students.txt", "r") as file:
#     for line in file:
#         if line.strip():
#             count += 1
# print("Total number of students:", count)
# #6
# name = input("Enter student name: ")
# found = False
# with open("students.txt", "r") as file:
#     for line in file:
#         if line.strip() == name:
#             found = True
#             break
# if found:
#     print("Student found.")
# else:
#     print("Student not found.")
# #7
# while True:
#     print("\n1. Add expense")
#     print("2. View expenses")
#     print("3. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         description = input("Enter expense description: ")
#         amount = input("Enter expense amount: ")

#         with open("expenses.txt", "a") as file:
#             file.write(f"{description}: #{amount}\n")

#         print("Expense saved successfully.")

#     elif choice == "2":
#         try:
#             with open("expenses.txt", "r") as file:
#                 expenses = file.read()

#                 if expenses:
#                     print("\nSaved expenses:")
#                     print(expenses)
#                 else:
#                     print("No expenses saved.")

#         except FileNotFoundError:
#             print("No expenses saved yet.")
#     elif choice == "3":
#         print("Goodbye.")
#         break
#     else:
#         print("Invalid choice.")
# #9
# while True:
#     print("\n1. Add note")
#     print("2. View notes")
#     print("3. Exit")
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         note = input("Enter your note: ")

#         with open("notes.txt", "a") as file:
#             file.write(note + "\n")
#         print("Note saved.")
#     elif choice == "2":
#         try:
#             with open("notes.txt", "r") as file:
#                 for line in file:
#                     print(line.strip())
#         except FileNotFoundError:
#             print("No notes found.")
#     elif choice == "3":
#         break
#     else:
#         print("Invalid choice.")
# #8
# while True:
#     print("\n1. Add student")
#     print("2. View records")
#     print("3. Search student")
#     print("4. Exit")
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         name = input("Enter student name: ")
#         score = input("Enter score: ")
#         with open("scores.txt", "a") as file:
#             file.write(f"{name},{score}\n")
#         print("Record saved.")
#     elif choice == "2":
#         try:
#             with open("scores.txt", "r") as file:
#                 for line in file:
#                     print(line.strip())
#         except FileNotFoundError:
#             print("No records found.")
#     elif choice == "3":
#         search_name = input("Enter student name: ")
#         found = False
#         try:
#             with open("scores.txt", "r") as file:
#                 for line in file:
#                     data = line.strip().split(",")

#                     if data[0] == search_name:
#                         print("Student:", data[0])
#                         print("Score:", data[1])
#                         found = True
#                         break
#             if not found:
#                 print("Student not found.")
#         except FileNotFoundError:
#             print("No records found.")

#     elif choice == "4":
#         break
#     else:
#         print("Invalid choice.")
#10
# while True:
    # print("\n1. Add student")
    # print("2. View all students")
    # print("3. Search for a student")
    # print("4. Exit")
    # choice = input("Enter your choice: ")
    # if choice == "1":
    #     student_id = input("Enter student ID: ")
    #     name = input("Enter student name: ")
    #     age = input("Enter student age: ")
    #     course = input("Enter student course: ")
    #     with open("students_records.txt", "a") as file:
    #         file.write(f"{student_id},{name},{age},{course}\n")
    #     print("Student saved.")
    # elif choice == "2":
    #     try:
    #         with open("students_record.txt", "r") as file:
    #             for line in file:
    #                 data = line.strip().split(",")
    #                 print("ID:", data[0])
    #                 print("Name:", data[1])
    #                 print("Age:", data[2])
    #                 print("Course:", data[3])
    #                 print()
    #     except FileNotFoundError:
    #         print("No student records found.")
    # elif choice == "3":
    #     search_id = input("Enter student ID: ")
    #     found = False
    #     try:
    #         with open("students_record.txt", "r") as file:
    #             for line in file:
    #                 data = line.strip().split(",")
    #                 if data[0] == search_id:
    #                     print("ID:", data[0])
    #                     print("Name:", data[1])
    #                     print("Age:", data[2])
    #                     print("Course:", data[3])
    #                     found = True
    #                     break
    #         if not found:
    #             print("Student not found.")
    #     except FileNotFoundError:
    #         print("No student records found.")
    # elif choice == "4":
    #     break
    # else:
    #     print("Invalid choice.")