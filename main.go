package main

import (
	"bufio"
	"os"

	"github.com/ipratt-code/hexal/toolchain"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	for {
		print("[ ]: ")
		txt, _ := reader.ReadString('\n')
		toolchain.Lex(txt)
	}
}
