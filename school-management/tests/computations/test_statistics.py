import pytest
from src.school_management.computations.statistics import compute_group_grades, compute_student_topic_grades_mean
from src.school_management.models.school import Group
from tests.conftest import group_all_passing

# Compute average for each student and each topic
def test_compute_student_topic_grades_mean(group_all_passing: Group):
    # Use grades property thanks to group_all_passing fixture
    grades:Grade = group_all_passing.grades

    assert compute_student_topic_grades_mean(group_all_passing.grades, 2, 1) == 16.0 or None

# Raises exception with ZeroDivisionError 

# Compute group grades 
def test_compute_group_grades(group_all_passing: Group):
    result = compute_group_grades(group_all_passing)
    
    for student_id, semester_results in result.items():
        print(student_id, semester_results)
        if not semester_results["success"]:
            assert False
