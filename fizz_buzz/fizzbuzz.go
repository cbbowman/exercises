package main

import "fmt"

func main() {

	for x := 1; x < 100; x++ {
		fizzbuzz(x)
		fmt.Println("")
	}
}

func fizzbuzz(x int) {
	fizz := x % 3
	buzz := x % 5
	if fizz == 0 {
		fmt.Print("Fizz")
	}
	if buzz == 0 {
		fmt.Print("Buzz")
	}
	if !((fizz == 0) || (buzz == 0)) {
		fmt.Print(x)
	}
	return
}
