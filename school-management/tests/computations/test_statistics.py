import pytest
from school_management.computations.statistics import compute_group_grades
from school_management.models.school import Group, Grade

@pytest.mark.skip("I'm too lazy to implement unit tests")

def test_compute_student_topic_grades_mean(
    grades: list[Grade],
    student_id: int,
    topic_id: int
):
    pass


def test_compute_group_grades(group_all_passing: Group):
    result = compute_group_grades(group_all_passing)

    for student_id, semester_results in result.items():
        if not semester_results["success"]:
            assert False
