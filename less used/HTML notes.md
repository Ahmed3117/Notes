​    

[w3schools.com](https://www.w3schools.com/html/html5_draganddrop.asp)

# HTML Drag and Drop API

## Example

![W3Schools](https://www.w3schools.com/html/img_w3slogo.gif)

The example below is a simple drag and drop example:

### Example

```html
 <!DOCTYPE HTML>
<html>
<head>
<script>
function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));
}
</script>
</head>
<body>

<div id="div1" ondrop="drop(event)" ondragover="allowDrop(event)"></div>

<img id="drag1" src="img_logo.gif" draggable="true" ondragstart="drag(event)" width="336" height="69">

</body>
</html> 
```

It might seem complicated, but lets go through all the different parts of a drag and drop event.

---

## Make an Element Draggable

First of all: To make an element draggable, set the `draggable` attribute to true:



 <img draggable="true">



------

## What to Drag - ondragstart and setData()

Then, specify what should happen when the element is dragged.

In the example above, the `ondragstart` attribute calls a function, drag(event),  that specifies what data to be dragged.

The `dataTransfer.setData()` method sets the data type and the value of the  dragged data:

```javascript
function drag(ev) {
 ev.dataTransfer.setData("text", ev.target.id);
 }
```

In this case, the data type is "text" and the value is the id of the draggable element ("drag1").

------

## Where to Drop - ondragover

The `ondragover` event specifies where the dragged data can be dropped.

By default, data/elements cannot be dropped in other elements. To allow a drop,  we must prevent the default handling of the element.

This is done by calling the `event.preventDefault()` method for the ondragover event:

 

```javascript
event.preventDefault()
```



------

## Do the Drop - ondrop

When the dragged data is dropped, a drop event occurs.

In the example above, the ondrop attribute calls a function, drop(event):

 

```javascript
function drop(ev) {
     ev.preventDefault();
     var data = ev.dataTransfer.getData("text");
     ev.target.appendChild(document.getElementById(data));
 }
```

Code explained:

- Call preventDefault() to prevent the browser default handling of the data (default is open as link on drop)
- Get the dragged data with the dataTransfer.getData() method. This  method will return any data that was set to the same type in the  setData() method
- The dragged data is the id of the dragged element ("drag1")
- Append the dragged element into the drop element







​          