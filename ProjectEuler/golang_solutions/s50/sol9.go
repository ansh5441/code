package s50

import (
	"math"
)

func Sol9() int {
	for i := 0; i < 1000; i++ {
		for j := 0; j < i; j++ {
			k := 1000 - (i + j)
			if math.Pow(float64(i), 2)+math.Pow(float64(j), 2) == math.Pow(float64(k), 2) {
				return i * j * k

			}
		}
	}
	return 0
}
