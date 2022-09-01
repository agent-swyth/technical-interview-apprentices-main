import pytest
from school_management.models.school import Grade, Group, Student, Topic


@pytest.fixture
def group_all_passing():
    return Group(
        students=[
            Student(id= 1, first_name="Bob", family_name="Bobinghton"),
            Student(id= 2, first_name="Boby", family_name="Bobyghton"),
            Student(id= 3, first_name="Alice", family_name="Alinghton")
        ],
        topics=[
            Topic(id = 1, name="Mathematics"),
            Topic(id = 2, name="Physics"),
            Topic(id = 3, name="Geography"),
        ],
        topic_weights={
            "Mathematics" : 10,
            "Physics" : 10,
            "Geography" : 2
        },
        grades=[
            Grade(student_id=1, topic_id=1, grade=15),
            Grade(student_id=1, topic_id=1, grade=5),
            Grade(student_id=1, topic_id=1, grade=12),

            Grade(student_id=1, topic_id=2, grade=12),
            Grade(student_id=1, topic_id=2, grade=12),
            Grade(student_id=1, topic_id=2, grade=12),

            Grade(student_id=1, topic_id=3, grade=10),
            Grade(student_id=1, topic_id=3, grade=6),
            Grade(student_id=1, topic_id=3, grade=8),
###############
            Grade(student_id=2, topic_id=1, grade=15),
            Grade(student_id=2, topic_id=1, grade=15),
            Grade(student_id=2, topic_id=1, grade=18),

            Grade(student_id=2, topic_id=2, grade=10),
            Grade(student_id=2, topic_id=2, grade=8),
            Grade(student_id=2, topic_id=2, grade=12),

            Grade(student_id=2, topic_id=3, grade=0),
            Grade(student_id=2, topic_id=3, grade=2),
            Grade(student_id=2, topic_id=3, grade=3),
###############
            Grade(student_id=3, topic_id=1, grade=9),
            Grade(student_id=3, topic_id=1, grade=9),
            Grade(student_id=3, topic_id=1, grade=8),

            Grade(student_id=3, topic_id=2, grade=15),
            Grade(student_id=3, topic_id=2, grade=8),
            Grade(student_id=3, topic_id=2, grade=9),

            Grade(student_id=3, topic_id=3, grade=20),
            Grade(student_id=3, topic_id=3, grade=18),
            Grade(student_id=3, topic_id=3, grade=17),
        ]
    )