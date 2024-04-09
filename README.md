Create a menu program that handles a database for students.
If needed the database and its tables will be created if it doesn’t exist.
it will create the following table if it doesn't exists:
CREATE TABLE IF NOT EXISTS student (
fname TEXT,
lname TEXT,
score INT);
Each student will have:
• First Name
• Last Name
• Final Score
The menu will have the following options:
1. Show All students
(print "there are no students" if the table is empty)
2. Add a new Student
(read first and last name and score from the user and add it to the DB)
3. Show by score
(Read score and Show all students with the same or higher score)
4. Quit the program
Note: Beware of sql injections!
