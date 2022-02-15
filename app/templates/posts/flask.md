# FLASK TROUBLESHOOTING

I made a minor change to home.html.jinja, changed one of the images on the page, entered the incorrect src and when corrected back to original flask started starting throwing the following error.

`[2431] [ERROR] Socket error processing request.`
<br>
`...`
<br>
`404 Not Found: The requested URL was not found on the server.`
<br>

Comment out the `<img src>` tag and error goes away. I copied the image source tag from another working image, replaced it with the correct name and it started working.
