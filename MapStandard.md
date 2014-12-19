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
Color Palette:
-------------

Name | Hex |Order
-----| --- |-----
Green | #8ed16c | 1
Blue | #3fa6f3 | 2
Red | #e25f5f | 3
Magenta | #ef6ab8 | 4

<h4>Palette Rule(s)</h4>
In a map, use the colors in order. There should never be Magenta in a 3 player map for example

Guide Lines:
========================
* The planets must alwasy fit inside the map boundries
* The Quantity of troops for the start values should be equal
* The combined radiuss of the planets should be equal

<h4>Planet Order In Map.json File</h4>
Top to bottom, left to right.

<h4>Accepted Start Value</h4>
* 5
* 10
* 15
* 20
* 25
* 30
* 35
* 45
* 50

<b>Use these sparingly:</b>

* 60
* 70
* 75
* 80
* 90
* 100
* 125
* Larger sizes make the value of capturing planets go down.

<h4>Accepted Planet Sizes</h4>
* 10
* 15
* 20
* 40
* 50
* 75
* 100
* 125
* 150
* 175
* 200
* No Bigger Planets, It's a waste of space (Pun intended).

Example Map
===========
```JSON
{
	"name": "Example Planet Map",
	"size": {
		"x": "400",
		"y": "400"
	},
	"planets": [
		{
			"radius":"50",
			"color": "#64cf22",
			"x": "55",
			"y": "55",
			"startValue": "20"
		},
		{
			"radius":"50",
			"color": "#3fa6f3",
			"x": "345",
			"y": "55",
			"startValue": "20"
		},
		{
			"radius":"50",
			"color": "#e25f5f",
			"x": "55",
			"y": "345",
			"startValue": "20"
		},
		{
			"radius":"50",
			"color": "#ef6ab8",
			"x": "345",
			"y": "345",
			"startValue": "20"
		}
	]
}
```

