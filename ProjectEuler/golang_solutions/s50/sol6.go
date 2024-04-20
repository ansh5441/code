package s50

func Sol6() int {
	var sumOfSquares int = 0
	var squareOfSum int = 0
	for i := 1; i <= 100; i++ {
		sumOfSquares += i * i
		squareOfSum += i
	}
	squareOfSum *= squareOfSum
	return squareOfSum - sumOfSquares
}
