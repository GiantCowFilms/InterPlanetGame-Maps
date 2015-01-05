InterPlanetGame: Map Standard [v 0.3 - Proposed]
=====
Changes Form Last Standard
---------------------

* Removed need for colors completly
* This standard is being set up to work with the final version - won't work with prototype
* Added (possession property)[https://github.com/GiantCowFilms/InterPlanetGame-Maps/blob/master/ProposedChanges/MapStandard%20v0.3.md#possession]
* (Added multiplier)[https://github.com/GiantCowFilms/InterPlanetGame-Maps/blob/master/ProposedChanges/MapStandard%20v0.3.md#multiplier]

File Type
----
The maps are stored as a JSON file.

<b/>No spaces<b/> in the file name 

Required Elements
---
* Name
* Standard
* Size
* Planets Array, and at least one element in it

Element Details
=========
<h3>Name:</h3>

Type | Values
------|-------
| String| Any

<h3>Standard:</h3>

Type | Values
------|-------
| String| Version of the standard in use without the '_v_'
<b>Example:</b>
```JSON
"standard": "0.2",
```


<h3>Size:</h3>
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
<h3>Planets (Array)</h3>
Type | Values
------|-------
| Array| Planet Objects
<b>Example</b>
```JSON
"planets": [
],
```
<h3>Planet (Object)</h3>
Type | Values
------|-------
| Object| X and Y cords, Color, Radius, Start Value
<b>Example</b>
```JSON
{
        "radius": "75",
        "x": "200",
        "y": "200",
        "possession": [
        "0",
        "0",
        "0"
    ],
    "multiplier": "2"
},
```

<b>JSON Syntax Notes</b>

The elemsnts must by in that order in the planet object, the numbers have to be strings (surrounded by double quotes). The cordinates are distance from the upper right hand corner.

<b>elements</b>

<h4>Radius</h4>
Type | Values
------|-------
string(int) | radius of planet

<h4>x & y</h4>
Type | Values
------|-------
string(int) | cords 

specifiy distance from upper left hand corner of the map.

<h4>Start Value</h4>
Type | Values
------|-------
string(int) | Starting Value

value with witch the planet starts

<h4>Possession</h4>
Type | Values
------|-------
array | Player number that owns planet with that many players

<b>Example</b>

This planet is owned by player 1 in a 2 player game. It starts the values at 2 players and counts up.

Players | Owner
--------|------
1    | 1 of 2
3    | 3 of 3
4    | 4 of 4

```JSON
"possession": [
        "1",
        "3",
        "4"	
]
```
<h4>Multiplier</h4>
Type | Values
------|-------
string(int) | Multipler

<b>Optional Porperty - Not required</b>

The growth rate of the planet is multiplied by this number 


Color Palette:
-------------

Name | Hex | Player
-----| --- |-----
Green | #8ed16c | 1
Blue | #3fa6f3 | 2
Red | #e25f5f | 3
Magenta | #ef6ab8 | 4
Orange | #eb8932 | 5
Purple | #af6cd1 | 6
Neutral Grey | #bbbbbb | 0

<h4>Palette Aplication<h4/>
The first player is always green, the secound is Blue, so on and so forth. 

<h4>Palette Rule(s)</h4> 
In a map, use the colors in order. There should never be Magenta in a 3 player map for example. Neutral grey planets don't increaese in value until they are taken over. They are "neutral" and aren't owned by a player in the start of the game.


Guide Lines:
========================
* The planets must alwasy fit inside the map boundries
* The Quantity of troops for the start values should be equal
* The combined radiuss of the planets should be equal
* Use mutlipiers very spareingly

<h3>Planet Order In Map.json File</h3>
Top to bottom, left to right.

<h3>Accepted Start Value</h3>
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

<h3>Accepted Planet Sizes</h3>
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
	"standard": "0.2",
	"planets": [
		{
			"radius":"50",
			"color": "#8ed16c",
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
			"radius":"75",
			"color": "#bbbbbb",
			"x": "200",
			"y": "200",
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

