### Cascading StyleSheets (CSS)
---
- Created by World Wide Web Consortium (W3C)
- CSS consists of
	- **Selector** : HTML element/tag that needs to be defined
	- **Property** : The attribute that needs a change
	- **Value** : Each property will take a value
- **Inline Stylesheet**
- **Internal Stylesheet** : `<head><style type="text/css">...</style></head>`
- **External Stylesheet**
```html
<link rel="stylesheet" type="text/css" href=“my_style.css" />
```

#### CSS Classes
- `.class-name { property:value; }`
#### CSS-Pseudo classes
- Used to include special style effects for selectors
- `:focus` Adds a style to an element that has keyboard input focus
- `:hover` Adds a style to an element when mouse moves over it
- `:link` Adds a style to an unvisited link
- `:visited` Adds a style to a visited link
- Syntax : `selector:pseudo-class {property:value}
```css
a.red:visited {color:#FF0000}

<a class="red" href="c:\css_syntax.html">CSS Syntax</a>
```

#### Image Set up
```css
img {
	-webkit-filter: grayscale(100%); /* Chrome, Safari, Opera */
	filter: grayscale(100%);
	border-radius: 50%;
}
```

