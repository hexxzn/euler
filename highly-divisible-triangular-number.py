# Find the first triangular number with over 500 divisors

triangle_row_old = 1
triangle_row_new = 2
triangle_total = 3
divisors = 0

while divisors < 500:
    triangle_row_old = triangle_row_new
    triangle_row_new += triangle_row_new +1
    triangle_total += triangle_row_new

    divisors = 0

    for i in range(1, triangle_total+1):
        if triangle_total % i == 0:
            divisors += 1
            print(divisors)