from itertools import product
import sys
def solution(beds, tables, cost):
    answer = sys.maxsize
    for bed, table in [*product(beds, tables)]:

        a, b, bed_cost = bed
        c, d, table_cost = table

        for x0, y0, x1, y1 in [[a,b,c,d], [b, a, c, d], [a, b, d, c], [b, a, d, c]]:

            case_1 = (x0 + x1) * max(y0, y1)
            case_2 = max(x0, x1) * (y0 + y1)
            answer = min(answer, bed_cost+table_cost+min(case_1, case_2)*cost)
    return answer