package main

import (
	"fmt"
	"github.com/ipratt-code/leaphd/toolchain"
)

func main() {
<<<<<<< HEAD:leaphd.go
	fmt.Printf("File contents: %v \n", toolchain.Lex("program.lpd"))
	toolchain.Parse(toolchain.Lex("program.lpd"))
=======
	fmt.Printf("File contents: %#v \n", toolchain.Lex("program.lpd"))
	toolchain.Parse(toolchain.Lex("main.hexl"))
>>>>>>> 244e00077cd3b03fcaa0953874b50958a02014a1:hexal.go
}
