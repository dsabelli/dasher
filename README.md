# Dasher

Dasher is a command-line interface (CLI) application that replaces whitespace in file names with dashes.

#### https://youtu.be/U7QxFVpY8Js

## Why Did I Make This

I made this app to help solve a problem in my workplace.

When creating emails, image assets are delivered by a different team to use for the email. If the filename contains any whitespace, the image won't render in Gmail. Sometimes this issue is missed and recepients using Gmail receive an email with a broken image.

Dasher's job is to automatically remove any whitespace to prevent this issue from occuring.

## What Did I Learn

I learned how to use argparse to create a personalized CLI app for my use cases, but flexible enough to be used by others. I also reinforced my knowledge of working with file I/O, regex, and unit testing.

## How To Use

To use Dasher with default arguments, navigate to the directory that contains the files you want to remove whitespace from, then run dasher.py.

By default, dasher prefixes the current date in YYMMDD format, as is my primary use case. At this time it is not possible to switch the date format, however users are able to indicate -t 0 in the CLI to not prefix a date. Dasher will not prefix a date to a file that aleady has a date prefix in YYMMDD format.

Dasher will loop through every file in the directory, looking for any files with whitespace, dashes, or underscores. It will then replace the mentioned characters with a separator, "-" by default, or "_" with the argument -s _. Dasher replaces dashes and underscores to keep consistency with the chosen separator.

If you don't want to loop through every file, -p will allow you to specify a regex pattern, usually part of a specific file you want to rename.

Lastly, if you choose to, you can use -d to specify the directory instead of navigating to the directory manually.
