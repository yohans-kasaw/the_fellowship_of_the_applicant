package main

import (
	"encoding/json"
	"os"
	"path/filepath"
	"text/template"
)

type Entry struct {
	Title       string   `json:"title,omitempty"`       // role
	Subtitle    string   `json:"subtitle,omitempty"`    // company
	InlineTitle string   `json:"inlineTitle,omitempty"` // company
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
	t, err := template.ParseFiles("./resume_templ.html")
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
}

func parse_resume() Resume {
	var resume Resume
	// file_path := "./sample_resume.json"
	file_path := "./resumes/4_good_years_wellfound.json"
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
