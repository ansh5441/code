package s50

import (
	"fmt"
	"math"
)

func Sol3() {
	// Problem 3
	var n int64 = 600851475143
	var max int64 = 0
	var i int64 = 2

	for i <= int64(math.Sqrt(float64(n))) {
		if n%i == 0 {
			n = n / i
			max = i
		} else {
			i++
		}
	}

	if n > max {
		max = n
	}

	fmt.Println(max)
}
