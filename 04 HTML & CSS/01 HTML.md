### Hyper Text Mark up Language
---
- Improvised version of Standard Generalized Mark Up Language (SGML)
- WWW & HTML was developed by Tim Berners Lee in 1990
- `.htm or .html` extension

### Basic HTML Document
- html
- head
- title
- body

```html
<body bgcolor=“Yellow”>
<body background=“Star.jpg”>
<body text=“Red”>
<body leftmargin=“60”>
```
- Anchor
	- marks the text as Hyper Link
```html
<a href =“C:\Personal\spec.doc”> Click </a>
```
- Formatting Elements
```html
<h1> to <h6>
<font> ...</font>
<b>...</b>
<u> ... </u>
<i>...</i>
<strike>...</strike>
<sub> ... </sub>
<sup>... </sup>
```
- Form Elements
	- Text field
	- Password Field
	- Combo Box
	- List Box
	- Radio Button
	- Check Box
	- Command Button
- Text Scrolling in the web page
```html
<html>
	<body >
		<marquee direction = "right" onmouseover="stop();"
		onmouseout="start();">How is this ??? </marquee>
	</body>
</html>
```
- Adding Image as a Back Ground
```html
<body background="Penguins.jpg">
```
- Adding Image To Body
```html
<img src="Tulips.jpg" alt="Smiley face" height="100" width="200">
```
- Table Properties
```html
<body>
	<table border="1">
		<tr>
			<th> a00 </th>
			<th> a01 </th>
		</tr>
		<tr>
			<th> a10 </th>
			<th> a11 </th>
		</tr>
	</table>
</body>

<!-- Merging cells in a table -->
<body>
	<table border="1">
		<tr>
		<th>Column 1</th>
		<th>Column 2</th>
		<th>Column 3</th>
		</tr>
		<tr>
			<td rowspan="2">Row 1 Cell 1</td>
			<td>Row 1 Cell 2</td>
			<td>Row 1 Cell 3</td>
		</tr>
		<tr>
			<td>Row 2 Cell 2</td>
			<td>Row 2 Cell3</td>
		</tr>
		<tr>
			<td colspan="3">Row 3 Cell 1</td>
		</tr>
</body>
```

## HTML - 5
- To Load a Video on to the web-page
```html
<video src="videos/bunny.ogv" width="250" height="150" controls></video>
```
- To add Audio to web-page
```html
<audio controls><source src="Sleep Away.mp3" type='audio/mp3'></audio>
```
- HTML 5 - legend
- HTML 5 - IFrame
```html
<iframe src="Tulips.jpg" width="200" height="120" scrolling="auto" align="left"></iframe>
```
- HTML Quotation and Citation Elements
```html
<abbr>abbreviation or acronym</abbr>
<address>contact information</address>
<bdo dir="rtl">Define text-direction</bdo>

<blockquote>section that is quoted from another source</blockquote>

<cite>title of a work</cite>
<q>short inline quotation</q>
```
- To Disable the right click on the web page
```html
<body oncontextmenu = “return false;”>
```
- Semantic Elements in HTML 5
	- A semantic element clearly describes its meaning to both the browser and the developer
```html
<header>
<nav>
<section>
<article>
<aside>
<figure>
<main>
<table>
<footer>
<summary>
```
- Improvements in input types
```html
<div> DOB <input type = "date" /></div>
<div> email <input type = "email" /></div>
<div> Social N/W site <input type = "url" /></div>
<div> Profile <input type = "file" /></div>
<div> Google <input type = "search" /></div>
<input type = "Submit" /><input type = "reset" />
```
- Progress Bar
```html
<progress value = "70" max = "100"></progress>
```
- Geo Location
	- HTML Geolocation API is used to get the geographical position of a user
	- `getCurrentPosition()` & `showPosition()`
