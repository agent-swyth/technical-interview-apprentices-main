from school_management.models.school import Grade, Group

SUCCESS_THRESHOLD = 10


def compute_student_topic_grades_mean(
    grades: list[Grade], 
    student_id: int, 
    topic_id: int) -> float:
    
    sum_grades = 0
    number_grades = 0
    
    for grade in grades:
        # if topic_id and student_id don't correspond, are they not treated ?
        if grade.topic_id == topic_id and grade.student_id == student_id:
            sum_grades += grade.grade
            number_grades += 1

    return sum_grades / number_grades


def compute_group_grades(group: Group) -> dict:

    results = {}
    
    for student in group.students:
        
        # topic.name : related mark
        student_grades = {
            topic.name: compute_student_topic_grades_mean(
                group.grades, student.id, topic.id
            )
            for topic in group.topics
        }

        global_grade = 0
        number_grades = 0
        
        # Compute each topic with topic weight
        for topic, topic_mean in student_grades.items():
            global_grade += topic_mean * group.topic_weights[topic]
            number_grades += 1 * group.topic_weights[topic]

        student_grades["global"] = global_grade / number_grades

        student_grades["success"] = student_grades["global"] >= SUCCESS_THRESHOLD

        results[student.id] = student_grades

    return results
