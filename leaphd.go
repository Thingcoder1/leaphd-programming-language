package main

import (
	"fmt"
	"github.com/ipratt-code/leaphd/lexer"
	//"github.com/ipratt-code/leaphd/parser"
)

func main() {
	fmt.Printf("File contents: %v \n", lexer.Lex("program.lpd"))
}
