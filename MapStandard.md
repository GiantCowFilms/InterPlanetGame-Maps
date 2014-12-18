InterPlanetGame: Map Standard
=====
File Type
----
The maps are stored as a JSON file.
Required Elements
---
* Name
* Size
* Planets Array, and at least one element in it

Element Details
=========
<h4>Name:</h4>

Type | Values
------|-------
| String| Any


<h4>Size:</h4>
Type | Values
------|-------
| Object| X and Y dimensions
<b>Example</b>
```JSON
"size": {
  "x": "0",
  "y": "0"
},
```
<h4>Planets (Array)</h4>
Type | Values
------|-------
| Array| Planet Objects
<b>Example</b>
```JSON
"planets": [
],
```
<h4>Planet (Object)</h4>
Type | Values
------|-------
| Object| X and Y cords, Color, Radius, Start Value
<b>Example</b>
```JSON
{
		"radius": "10",
		"color": "#64cf22",
		"x": "20",
		"y": "20",
		"startValue": "10"
},
```
Color Palet:
-------------

Name | Hex |Order
-----| --- |-----
Green | #64cf22 | 1
Blue | #3fa6f3 | 2
Red | #e25f5f | 3
Magenta | #ef6ab8 | 4
