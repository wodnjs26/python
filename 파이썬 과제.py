class Student:
    def __init__(self, name, stu_ID):
        self.name = name
        self.stu_ID = stu_ID # ID
        self.attendance = False

    def mark_attendance(self):
        self.attendance = True

class AttendanceBook:
    def __init__(self):
        self.students = []
        self.student_ids = set() # ID

    def add_student(self, name, stu_ID):
        if stu_ID not in self.student_ids: # ID
            self.students.append(name)
            self.student_ids.add(stu_ID)
        else:
            print("이미 존재함.")

    def mark_student_attendance(self, stu_ID):
        for student in self.students:
            if student.stu_ID == stu_ID:
                student.mark_attendance()

    def get_attendance_summary(self):
        attendance_counter = sum(1 for student in self.students)
        absence_student = len(self.students) - attendance_counter

        return("attendance_counter : ", attendance_counter, "absence_student : ", absence_student)

    def get_student_list(self):
        attdance_counter = []

attendance_book = AttendanceBook()

attendance_book.add_student("김철수", 101)
attendance_book.add_student("이영희", 102)
attendance_book.add_student("박민수", 103)
attendance_book.add_student("김철수", 101)

attendance_book.mark_student_attendance(101)
attendance_book.mark_student_attendance(103)

print("출석 요약", attendance_book.get_attendance_summary())
print("출석한 학생 목록", attendance_book.get_student_list())

# --------------------------------------------------------------------
class Student:
    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self.scores = []

    def add_score(self, score: float):
        """학생의 점수를 추가합니다."""
        self.scores.append(score)

    def calculate_average(self) -> float:
        """학생의 평균 점수를 계산하여 반환합니다."""
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)


class GradeBook:
    def __init__(self):
        self.students = []
        self.student_ids = set()

    def add_student(self, name: str, student_id: str):
        """새로운 학생을 추가합니다. 중복된 학번은 무시합니다."""
        if student_id in self.student_ids:
            print(f"학번 {student_id}은 이미 등록된 학생입니다.")
            return
        student = Student(name, student_id)
        self.students.append(student)
        self.student_ids.add(student_id)

    def add_student_score(self, student_id: str, score: float):
        """특정 학번의 학생에게 점수를 추가합니다."""
        for student in self.students:
            if student.student_id == student_id:
                student.add_score(score)
                return
        print(f"학번 {student_id}인 학생을 찾을 수 없습니다.")

    def get_top_students(self, top_n: int):
        """상위 N명의 학생을 평균 점수 기준으로 정렬하여 반환합니다."""
        if top_n <= 0:
            print("올바른 상위 학생 수를 입력하세요.")
            return []

       
        sorted_students = sorted(self.students, key=lambda s: s.calculate_average(), reverse=True)
        
        
        top_students = [(student.name, student.calculate_average()) for student in sorted_students[:top_n]]
        return top_students



if __name__ == "__main__":
    gradebook = GradeBook()

    
    gradebook.add_student("김철수", "202401")
    gradebook.add_student("이영희", "202402")
    gradebook.add_student("박민수", "202403")
    
    
    gradebook.add_student_score("202401", 85)
    gradebook.add_student_score("202401", 90)
    gradebook.add_student_score("202402", 95)
    gradebook.add_student_score("202402", 88)
    gradebook.add_student_score("202403", 75)
    gradebook.add_student_score("202403", 80)

    
    top_students = gradebook.get_top_students(2)
    print("상위 2명의 학생:")
    for name, avg in top_students:
        print(f"이름: {name}, 평균 점수: {avg:.2f}")

# -------------------------------------------------------------------------------------------

class Movie:
    def __init__(self, title: str, schedule: list):
        self.title = title
        self.schedule = schedule
        self.seats = {time: [False] * 10 for time in schedule}

    def reserve_seat(self, time: str, seat_number: int) -> bool:
        """특정 시간대의 좌석을 예약합니다."""
        if time not in self.seats:
            print(f"{time} 시간대는 존재하지 않습니다.")
            return False
        if seat_number < 1 or seat_number > 10:
            print("좌석 번호는 1부터 10 사이여야 합니다.")
            return False
        if self.seats[time][seat_number - 1]:
            print(f"{seat_number}번 좌석은 이미 예약되었습니다.")
            return False
        
        self.seats[time][seat_number - 1] = True
        print(f"{seat_number}번 좌석 예약이 완료되었습니다.")
        return True

    def get_available_seats(self, time: str) -> int:
        """특정 시간대의 예약 가능한 좌석 수를 반환합니다."""
        if time not in self.seats:
            print(f"{time} 시간대는 존재하지 않습니다.")
            return 0
        return self.seats[time].count(False)


class Theater:
    def __init__(self):
        self.movies = {}

    def add_movie(self, title: str, schedule: list):
        """영화를 추가합니다."""
        if title in self.movies:
            print(f"영화 '{title}'는 이미 추가되어 있습니다.")
            return
        self.movies[title] = Movie(title, schedule)
        print(f"영화 '{title}'가 추가되었습니다.")

    def reserve_movie_seat(self, title: str, time: str, seat_number: int):
        """특정 영화의 특정 시간대의 좌석을 예약합니다."""
        if title not in self.movies:
            print(f"영화 '{title}'는 영화 목록에 없습니다.")
            return
        movie = self.movies[title]
        movie.reserve_seat(time, seat_number)

    def get_movie_schedule(self, title: str):
        """특정 영화의 상영 시간표와 예약 가능한 좌석 수를 출력합니다."""
        if title not in self.movies:
            print(f"영화 '{title}'는 영화 목록에 없습니다.")
            return
        movie = self.movies[title]
        print(f"\n영화: {title}의 상영 시간표:")
        for time in movie.schedule:
            available_seats = movie.get_available_seats(time)
            print(f"- {time}: 예약 가능한 좌석 수 = {available_seats}석")



if __name__ == "__main__":
    theater = Theater()

 
    theater.add_movie("인터스텔라", ["10:00", "13:00", "16:00"])
    theater.add_movie("인셉션", ["11:00", "14:00", "17:00"])

    # 좌석 예약
    theater.reserve_movie_seat("인터스텔라", "10:00", 1)
    theater.reserve_movie_seat("인터스텔라", "10:00", 1)
    theater.reserve_movie_seat("인셉션", "14:00", 5)


    theater.get_movie_schedule("인터스텔라")
    theater.get_movie_schedule("인셉션")