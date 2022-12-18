## 															Library management system

## First Analysis :

* System Login

  account :

  * Employee (either employee or admin)

* Users

   Managers :

  * Admin

    can access all the the system and follow the whole history of what happened and by who (borrowing , adding books or students , deleting, .....) 

  * Employee

    can :

    * view all students and their data
    * add new student 
    * delete student 
    * search a student
    * view all Books and their data
    * add new Book
    * edit Book data
    * delete Book
    * search book

  beneficiary :

  * Student

    the employee takes the student information to follow the borrowing operation with him .

  * instructor

    the employee takes the instructor information to follow the borrowing operation with him .

* borrowing

  * the employee takes needed student information and add him to  the system 
  * student can borrow a book or more with start time and end time
  * the system will send an email to student to remember him to get the borrowed book back (a day before the end time )    **background task** 
  * when the student get the book back the employee will mark this borrowing operation as done successfully.

  ----

## Entities :

* User
  * Id
  * full_name
  * mail
  * national_id 
* Employee (inherits from User)
  * Id
  * username
  * password 
  * job (like librarian , admin , ......)
* beneficiary (inherits from User)
  * Id
  * type (instructor or student)

* BookCategory
  * Id
  * name
  * location
* Book
  * Id
  * category (relation with Category table)
  * title
  * publisher 
  * author
  * code
  * date_added
* BookCopy 
  * book name (relation with Book table)
  * number_of_available_copies

* Borrowing
  * Id
  * employee (who is responsible for this operation ? )
  * student
  * book
  * start_date
  * end_date
  * status (done or pending)
* MaxBorrowingtimes
  *  max-borrowing-times-for-student
  * max-borrowing-times-for-instructor
* History
  * employee
  * action (choices(add,edit,delete,update))
  * table (table that action has been applied to)
  * date

