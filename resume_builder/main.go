package main

import (
	"encoding/json"
	"os"
	"path/filepath"
	"text/template"
)

const OUTPUT_DIR = "./output"

func main() {
	t, err := template.ParseFiles("./resume.html")
	if err != nil {
		panic(err)
	}

	out_file, err := os.Create(filepath.Join(OUTPUT_DIR, "resume.html"))
	if err != nil {
		panic(err)
	}
	defer out_file.Close()

	data := parse_resume()
	t.Execute(out_file, data)
	t.Execute(os.Stdout, data)
}

func parse_resume() Resume {
	var resume Resume
	file_path := "./sample_resume.json"
	byte, err := os.ReadFile(file_path)
	if err != nil {
		panic(err)
	}
	err = json.Unmarshal(byte, &resume)
	if err != nil {
		panic(err)
	}
	return resume
}
