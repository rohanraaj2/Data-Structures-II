import datetime


class Course:
    """ Holds information on a course and its assignments.
    """
    course_assignments = []
    total_weightage = 0
    # assignment = ''

    def __init__(self, title: str, hours: int, teacher: str, time: datetime.datetime) -> None:
        """Creates a course with the given information.


        Parameters:
        - self: mandatory reference to this object
        - title: name of the course
        - hours: total credit hours of the course
        - teacher: name of the instructor
        - time: date and time of the start of the first class

        Returns:
        none
        """
        self.title = title
        self.hours = hours
        self.teacher = teacher
        self.time = time

    def __str__(self) -> str:
        """Returns the string to be printed when this object is passed to str().

        The representation contains the course's title, hours, instructor name,
        and class time separated by newline.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        A string representation of this object.
        """
        return (self.title + '\n' + str(self.hours) + '\n' + str(self.teacher) + '\n' + str(self.time))

    def add_assignment(self, assignment: tuple[str, int]) -> bool:
        """Returns the success status of adding assignment to the list of this course's
        assignments.

        assignment is represented by its title and weightage, e.g. ('HW1',
        10). It can be added to the list of assignments if adding the weightage
        does not cause the total weightage to exceed 100 and the list does not
        already contain an assignment with the same title. Otherwise it cannot
        and adding fails.

        Parameters:
        - self: mandatory reference to this object
        - assignment: a tuple containing the assignment name and weightage

        Returns:
        True if adding assignment succeeds, False otherwise.

        """
        if self.total_weightage + assignment[1] > 100:
            return False
        for i in self.course_assignments:
            if assignment[0] == i[0]:
                return False
        self.course_assignments.append(assignment)
        self.total_weightage += assignment[1]
        return True

    def remove_assignment(self, assignment: str) -> bool:
        """Returns the success status of removing assignment from the list of this
        course's assignments.

        assignment is represented by its title, e.g. 'HW1'. It can be removed
        from the list of assignments if it already exists in the list. Otherwise
        it cannot and removing fails.

        Parameters:
        - self: mandatory reference to this object
        - assignment: the title of the assignment

        Returns:
        True if removing assignment succeeds, False otherwise.

        """
        for i in self.course_assignments:
            if assignment == i[0]:
                self.total_weightage -= i[1]
                self.course_assignments.remove(i)
                return True
        return False

    def print_assignments(self) -> None:
        """Prints the assignments contained in the list of this course's assignments.

        Each assignment is printed on a new line in increasing order of
        weightage. Assignments with the same weightage are printed in any
        order. Each assignment is printed as its name and weightage separated by
        a tab character.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        none
        """
        self.course_assignments[1].sort()
        for i in range(len(self.course_assignments)):
            print(self.course_assignments[i][0], self.course_assignments[i][1])

    def is_complete(self) -> None:
        """Returns whether the course is complete, i.e. the total weightage of the
        stored assignments is 100.

        Parameters:
        - self: mandatory reference to this object

        Returns:
        True if the course is complete, False otherwise.
        """
        if self.total_weightage == 100:
            return True
        else:
            return False
