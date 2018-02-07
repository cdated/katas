package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Print("What is your name? ")

	// Get user input and strip newline
	reader := bufio.NewReader(os.Stdin)
	name, _ := reader.ReadString('\n')
	name = strings.Trim(name, "\n")

	fmt.Printf("Hello, %s, nice to meet you!\n", name)
}
