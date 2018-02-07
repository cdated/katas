package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	fmt.Print("What is the input string? ")

	// Get user input and strip newline
	reader := bufio.NewReader(os.Stdin)
	str, _ := reader.ReadString('\n')
	str = strings.Trim(str, "\n")

	str_len := len(str)
	fmt.Printf("%s has %v characters.\n", str, str_len)
}
