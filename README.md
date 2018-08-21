# Online Resume – Static Site Tool

This static site generator tool was created as part of a KI Labs assignment.

## Using the Tool

This tool requires Python 3 and Jinja2 to work. To install Jinja2, simply install with `pip install jinja2`. If you don't have the pip tool, I recommend installing it, it's great!

The Resume Generator works in one of two ways: by aggregating the data in the JSON fields found in the configs folder, and through a small CLI tool.

Running `python3 build.py` through the Command Line in the project directory will generate the resume.html file, which you can then view on a browser to see the results.

### CLI Tool

Through the use of the CLI tool, you can change the *Title*, *Subtitle*, and *Color* of the resume for quick viewing. You can also remove sections from the Resume that you don't think you're going to need, such as the *About* section or the *Awards* section, so on and so forth. To view all the CLI commands and how to use them, please refer to the CLI Commands section.

Keep in mind, changes to the Resume made through the CLI tool do not modify the values in the configs folder; that's because the CLI commands are meant to be used for viewing quick changes, not permanent ones. Everytime you run the `python3 build.py` command without any of the CLI tool commands, the resume will reset to the values as seen in the configs JSON files.

### JSON Values

A cool thing to keep in mind: The JSON values found in the configs folder are translated *as is* into HTML. That means that if you wish to add any special Markup to some field in the JSONS, all you need to do is add HTML tags *into* the JSON fields and they will be seen in the Resume. Refer to the education.json and employment.json files to see some examples. 

## CLI Tool Commands

| Command                    | Action                                                                           |
| :------------------------- |:---------------------------------------------------------------------------------|
| `noabout`                  | Removes About section                                                            |
| `noeducation`              | Removes Education section                                                        |
| `noemployment`             | Removes Employment section                                                       |
| `noprojects`               | Removes Projects section                                                         |
| `noawards`                 | Removes Awards section                                                           |
| `noactivities`             | Removes Activities section                                                       |
| `noexperience`             | Removes Experience section                                                       |
| `resume-color="#HEX CODE"` | Changes the primary color of the Resume to whatever Color Hex Code is passed in  |
| `title="TEXT"`             | Changes the Title to whatever type of text is passed into the quotation marks    |
| `subtitle="TEXT"`          | Changes the Subtitle to whatever type of text is passed into the quotation marks |
