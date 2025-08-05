package main

type Entry struct {
	Title       string   `json:"title,omitempty"`    // role
	Subtitle    string   `json:"subtitle,omitempty"` // company
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

