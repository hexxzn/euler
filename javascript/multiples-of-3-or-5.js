let array = []

function multiples(limit) {
    for (var i = 1; i < limit; i++) {
        if (i % 3 == 0) {
            array.push(i)
            continue
        }
        if (i % 5 == 0) {
            array.push(i)
        }
    }
    sum = 0
    for (var i = 0; i < array.length; i++) {
        sum += array[i];
    }
    return sum
}

document.write(multiples(1000));