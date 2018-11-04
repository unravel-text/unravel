from typing import Any, Optional


class ReadingLevel:
    """
    A value indicating the average minimum range required to understand a text.
    The range can be one or more of:
    - education grade
    - education level
    - age in years
    """

    grade_range = [
        'early',
        'primary',
        'middle',
        'high',
        'under-grad tertiary',
        'post-grad tertiary',
    ]
    level_range = range(0, 19, 1)
    age_range = range(4, 23, 1)

    def __init__(self, name: str, index: Any = None,
                 grade: Optional[str] = None, level: Optional[int] = None, age: Optional[int] = None):
        self.measure_name = name  # type: str
        self.measure_index = index  # type: Any

        grade_g, level_g, age_g = self._from_grade(grade)
        grade_l, level_l, age_l = self._from_level(level)
        grade_a, level_a, age_a = self._from_age(age)

        self.grade = None
        self.level = None
        self.age = None

    # # primary
    # grade_1 = 5
    # grade_2 = 6
    # grade_3 = 7
    # grade_4 = 8
    #
    # # middle
    # grade_5 = 9
    # grade_6 = 10
    # grade_7 = 11
    # grade_8 = 12
    #
    # # high
    # grade_9 = 13
    # grade_10 = 14
    # grade_11 = 15
    # grade_12 = 16
    #
    # # tertiary
    # grade_13 = 17
    # grade_14 = 18
    # grade_15 = 19
    # grade_16 = 20
    # grade_17 = 21

    def _from_level(self, value: int):
        if not isinstance(value, int):
            return None, None, None

        age_min = self.age_range[0]
        age_max = self.age_range[-1]
        level_min = self.level_range[0]
        level_max = self.level_range[-1]
        if value <= level_min:
            grade = self.grade_range[0]
            level = level_min
            age = age_min
        elif 1 <= value <= 4:
            grade = self.grade_range[1]
            level = value
            age = value + age_min
        elif 5 <= value <= 8:
            grade = self.grade_range[2]
            level = value
            age = value + age_min
        elif 9 <= value <= 12:
            grade = self.grade_range[3]
            level = value
            age = value + age_min
        elif 13 <= value < level_max:
            grade = self.grade_range[4]
            level = value
            age = value + age_min
        else:
            grade = self.grade_range[5]
            level = level_max
            age = age_max

        return grade, level, age

    def _from_age(self, value: int):
        if not isinstance(value, int):
            return None, None, None

        age_min = self.age_range[0]
        age_max = self.age_range[-1]
        level_min = self.level_range[0]
        level_max = self.level_range[-1]
        if value <= age_min:
            grade = self.grade_range[0]
            level = level_min
            age = age_min
        elif 5 <= value <= 8:
            grade = self.grade_range[1]
            level = value - age_min
            age = value
        elif 9 <= value <= 12:
            grade = self.grade_range[2]
            level = value - age_min
            age = value
        elif 13 <= value <= 16:
            grade = self.grade_range[3]
            level = value - age_min
            age = value
        elif 17 <= value < age_max:
            grade = self.grade_range[4]
            level = value - age_min
            age = value
        else:
            grade = self.grade_range[5]
            level = level_max
            age = age_max

        return grade, level, age

    def _from_grade(self, value: str):
        if not isinstance(value, str):
            return None, None, None

        if value not in self.grade_range:
            raise ValueError("Grade '{}' is not a valid grade: '{}'".format(value, ', '.join(self.grade_range)))

        age_min = self.age_range[0]
        age_max = self.age_range[-1]
        level_min = self.level_range[0]
        level_max = self.level_range[-1]
        if value == self.grade_range[0]:
            grade = self.grade_range[0]
            level = level_min
            age = age_min
        elif value == self.grade_range[1]:
            grade = self.grade_range[1]
            level = 1
            age = 5
        elif value == self.grade_range[2]:
            grade = self.grade_range[2]
            level = 5
            age = 9
        elif value == self.grade_range[3]:
            grade = self.grade_range[3]
            level = 9
            age = 13
        elif value == self.grade_range[4]:
            grade = self.grade_range[4]
            level = 13
            age = 17
        else:
            grade = self.grade_range[5]
            level = level_max
            age = age_max

        return grade, level, age
