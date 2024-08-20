- Interaction between the user and the web page is through a set of events
- Events are pieces of code that are run when an action is taken by the user
#### 01 OnClick
- It is added to `<input type="button"> tags and <a> links`
- This event is triggered when the button or the hyperlink is clicked
```JS
<input type="Button" value="Save" 
onclick=“alert('This is the event of Button')">
```
#### 02 OnBlur
- This event occurs when an element loses focus , that is when the user selects another element
```JS
<html> 
	<form>
		<input type="Button" value="Save" onblur="confirm('This is the Blur event on SAVE button')">
		<input type="Button" value="Cancel">
	</form> 
</html>
```
#### 03 OnFocus
- This event occurs when the cursor focus is on the element and can be applied to all elements
- It can be added to Select ,text boxes and textareas
- It is activated only after the element gets focus
```JS
<html> 
	<head> 
		<script type="text/javascript">
			function disp(){
				alert("The focus is on the textbox");
			}
		</script>
	</head>
	<form>
		<input type="text" onfocus="disp()"><br>
		<input type="Button" value="Save">
	</form> 
</html>
```

### Form validations

### Disable the right click on the web page 
- `<body oncontextmenu = “return false;”>`
```JS
//Disable the context menu
document.addEventListener('contextmenu', event => {
	event.preventDefault()
})

//Disable essential hotkeys
document.body.addEventListener('keydown', event => {
if (event.ctrlKey && 'cvxspwuaz'.indexOf(event.key) !== -1) {
	event.preventDefault()
}
})
```

### Built-in Window Methods
```JS
window.document.getElementById("demo")
window.print()        // webpage is been sent to the printer
window.find(“String”) // returns T/F based on found / not-Found
window.open("http://www.google.com") // open site in new window
window.(alert/confirm/prompt)
```

### Timing Events
- setTimeout(function, milliseconds)
- setInterval(function, milliseconds)
- clearTimeout(timeoutVariable)
```JS
<button onclick="myVar = setTimeout(myFunction,3000)"> Try</button>
<button onclick="clearTimeout(myVar)">Stop</button>
```