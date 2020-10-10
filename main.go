package main

import (
	"fmt"
	"github.com/ipratt-code/leaphd/leaphd"
)

func main() {
	fmt.Printf("File contents: %v \n", leaphd.Lex("leaphd/program.lpd"))
}
