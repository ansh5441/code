package s50

import "fmt"

func Sol2() {
	a := 0
	b := 1
	c := 0
	sum := 0
	for c < 4000000 {
		c = a + b
		if c%2 == 0 {
			sum += c
		}
		a = b
		b = c
	}
	fmt.Println(sum)
}
