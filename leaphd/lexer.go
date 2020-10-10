package leaphd

import (
	"fmt"
	"io/ioutil"
)

// Lex lexes the file into tokes for the parser
func Lex(pathToFile string) []string {
	data, err := ioutil.ReadFile(pathToFile)
	if err != nil {
		fmt.Printf("Error: %q", err)
	}
	list := make([]string, 0, len(data))

	for i := 0; i <= len(data)-1; i++ {
		list = append(list, string(data[i]))
	}

	return list
}
