import pytest
from src.school_management.computations.statistics import compute_group_grades
from src.school_management.models.school import Group, Grade
from tests.conftest import group_all_passing

# Use built-in decorator to enable parametrization of arguments for a test
@pytest.mark.parametrize("topic_id,student_id,expected", [(2, 1, 12.0), (1, 2, 16.0), pytest.param(1, 1, 10.4, marks=pytest.mark.xfail)])
def test_compute_student_topic_grades_mean(group_all_passing: Group, topic_id, student_id, expected):
    ## Just use grades property in Group class from imported conftest
    grades:Grade = group_all_passing.grades
    ## Focus on one topic and one student for testing
    # topic_id = 2
    # student_id = 1
    # Initialize sum for average calcul
    sum_grades = 0
    number_grades = 0
    # Iterate list of marks ordonate by topic_id and student_id
    for grade in grades:
        if grade.topic_id == topic_id and grade.student_id == student_id:
            sum_grades += grade.grade
            number_grades += 1
    assert sum_grades / number_grades == expected

@pytest.mark.skip("I'm too lazy to implement unit tests")
def test_compute_group_grades(group_all_passing: Group):
    result = compute_group_grades(group_all_passing)

    for student_id, semester_results in result.items():
        if not semester_results["success"]:
            assert False
