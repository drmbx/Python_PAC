class Worker:
    def __init__(self, cash=0):
        self._cash = cash

    def take_salary(self, salary):
        self._cash += salary

    def _read_matrix(self, file):
        matrix = []
        with open(file, 'r') as file:
            for line in file:
                row = [int(x) for x in line.split()]
                matrix.append(row)
        return matrix


class Pupa(Worker):
    def do_work(self, file1, file2):
        res_matrix = []
        matrix1 = self._read_matrix(file1)
        matrix2 = self._read_matrix(file2)
        for y in range(len(matrix1)):
            row = []
            for x in range(len(matrix1[0])):
                row.append(matrix1[y][x] + matrix2[y][x])
            res_matrix.append(row)
        print(res_matrix)
        return


class Lupa(Worker):
    def do_work(self, file1, file2):
        res_matrix = []
        matrix1 = self._read_matrix(file1)
        matrix2 = self._read_matrix(file2)
        for y in range(len(matrix1)):
            row = []
            for x in range(len(matrix1[0])):
                row.append(matrix1[y][x] - matrix2[y][x])
            res_matrix.append(row)
        print(res_matrix)
        return


class Accountant:
    def give_salary(self, worker, salary=100):
        worker.take_salary(salary)


def main():
    pupa = Pupa()
    lupa = Lupa()
    boss = Accountant()

    boss.give_salary(pupa)
    boss.give_salary(lupa, 5000)

    print(pupa._cash)
    print(lupa._cash)

    pupa.do_work("matrix1.txt", "matrix2.txt")
    lupa.do_work("matrix1.txt", "matrix2.txt")


main()
