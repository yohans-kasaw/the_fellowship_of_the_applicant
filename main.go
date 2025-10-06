package main

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"text/template"
)

type Entry struct {
	Title       string   `json:"title,omitempty"`       // role
	Subtitle    string   `json:"subtitle,omitempty"`    // company
	Period      string   `json:"period,omitempty"`
	Location    string   `json:"location,omitempty"`
	Description []string `json:"description,omitempty"`
}

type Section struct {
	Title   string  `json:"title"`
	Entries []Entry `json:"entries"`
}

type Resume struct {
	Name     string    `json:"name"`
	Phone    string    `json:"phone"`
	Email    string    `json:"email"`
	Location string    `json:"location"`
	Linkedin string    `json:"linkedin"`
	Github   string    `json:"github"`
	Summary  string    `json:"summary"`
	Sections []Section `json:"sections"`
}

const OUTPUT_DIR = "./output"

func main() {
	if len(os.Args) < 2 {
		fmt.Printf("please provide json resume path")
		return
	}

	templ_path := "./templates/default.html"
	if len(os.Args) >= 3 {
		templ_path = os.Args[2]
		fmt.Println("using ", templ_path, "template")
	}

	t, err := template.ParseFiles(templ_path)

	if err != nil {
		panic(err)
	}

	out_path := filepath.Join(OUTPUT_DIR, "resume.html")
	out_file, err := os.Create(out_path)
	if err != nil {
		panic(err)
	}
	defer out_file.Close()

	data := parse_resume(os.Args[1])
	t.Execute(out_file, data)

	fmt.Println("Resume hase been generated to: ", out_path)
}

func parse_resume(path string) Resume {
	var resume Resume
	byte, err := os.ReadFile(path)
	if err != nil {
		panic(err)
	}
	err = json.Unmarshal(byte, &resume)
	if err != nil {
		panic(err)
	}
	return resume
}
