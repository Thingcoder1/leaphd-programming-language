package main

import (
	"fmt"
	"github.com/ipratt-code/leaphd/toolchain"
)

func main() {
	fmt.Printf("File contents: %#v \n", toolchain.Lex("program.lpd"))
	toolchain.Parse(toolchain.Lex("main.hexl"))
}
