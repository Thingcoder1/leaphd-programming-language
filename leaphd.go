package main

import (
	"fmt"
	"github.com/ipratt-code/leaphd/toolchain"
	//"github.com/ipratt-code/leaphd/parser"
)

func main() {
	fmt.Printf("File contents: %#v \n", toolchain.Lex("program.lpd"))
}
