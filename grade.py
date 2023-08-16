class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []
    
    def add_score(self, score):
        self.scores.append(score)
    
    def get_average_score(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

def main():
    num_students = int(input("生徒の数を入力してください: "))
    students = []

    for i in range(num_students):
        name = input(f"生徒{i+1}の名前を入力してください： ")
        student = Student(name)
        num_scores = int(input("成績の数を入力してください： "))

        for j in range(num_scores):
            score = int(input(f"{name}さんの成績{j+1}を入力してください： "))
            student.add_score(score)
        
        students.append(student)
    
    print("\n各生徒の平均点:")
    for student in students:
        average_score = student.get_average_score()
        print(f"{student.name}: {average_score:.2f}")

if __name__ == "__main__":
    main()