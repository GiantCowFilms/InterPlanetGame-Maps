InterPlanetGame: Map Standard [v 0.3 - Proposed]
=====
Abstract
--------

This document explains the technical specifications for a InterPlanetGame map. It contains specifications, rules and guidlines as well as an example map. Even if you use a tool, read this, since the tool may be hard to use without this knowladge.


Changes From Last Standard
---------------------

* Removed need for colors completly
* This standard is being set up to work with the final version - won't work with prototype
* Added [possession property](#possession)
* [Added multiplier](#multiplier)
* Changed the guidlines and rules: What should be done, and what has to be done

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
 String| Any

<h3>Standard:</h3>

Type | Values
------|-------
String| Version of the standard in use without the '_v_'

<b>Example:</b>
```JSON
"standard": "0.3",
```


<h3>Size:</h3>

Type | Values
------|------
Object| X and Y dimensions

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
 Array| Planet Objects
<b>Example</b>
```JSON
"planets": [
],
```
<h3>Planet (Object)</h3>

Type | Values
------|-------
 Object| X and Y cords, Color, Radius, Start Value
<b>Example</b>
```JSON
{
        "radius": "75",
        "x": "200",
        "y": "200",
        "startValue": "50",
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

This planet (see example code) is owned by player 1 in a 2 player game. It starts the values at 2 players and counts up. Player 0 is a neutral planet.

Players | Owner
--------|------
1    | Player 1 of 2 players
3    | Player 3 of 3 players
4    | Player 4 of 4 players

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
string(float) | Multipler

<b>Optional Porperty - Not required</b>

Only up to one decimal place.
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

Rules:
==============
<sup>Maps that don't follow these are considered invalid, even if the still "work"</sup>

1. There may be no overlaping planets
1. The planets must alwasy fit inside the map boundries
1. Only use from the [list of accepted start values](#TODO)
1. Only use from the [list of accepted planet sizes](#TODO)
1. Only use from the [list of accepted multipliers](#TODO)

<b>Deffinition of a balenced map:</b>
Without any actions, there should be at no time a disparity in the quantity of troos.
_(In short, the total growth rate [Combined radii] needs to be equal, as well as the number of starting troops)_

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

Guide Lines:
========================
* Use mutlipiers very spareingly
* Putting a big planet in the middle isn't a good start

Build maps that are desgined to create new and insteresting ways of playing, trying to create a picture isn't good for gameplay. Gameplay comes first, and more people will play your map if it is _fun_.

[See Creating a great map](https://github.com/GiantCowFilms/InterPlanetGame-Maps/blob/master/Creating%20a%20great%20map.md)

<h3>Planet Order In Map.json File</h3>
Top to bottom, left to right.

Example Map
===========
```JSON
{
    "size": {
        "x": "1000",
        "y": "1000"
    },
    "name": "Example Map",
    "planets": [
        {
            "x": "800",
            "y": "500",
            "startValue": "20",
            "radius": "75",
            "possession": [
                "2",
                "3",
                "4",
                "4",
                "4"
            ]
        },
        {
            "y": "760",
            "x": "650",
            "startValue": "20",
            "radius": "75",
            "possession": [
                "1",
                "3",
                "3",
                "3",
                "3"
            ]
        },
        {
            "y": "760",
            "x": "350",
            "startValue": "20",
            "radius": "75",
            "possession": [
                "1",
                "1",
                "0",
                "5",
                "5"
            ]
        },
        {
            "y": "240",
            "x": "650",
            "startValue": "20",
            "radius": "75",
            "possession": [
                "2",
                "2",
                "0",
                "0",
                "6"
            ]
        },
        {
            "y": "240",
            "x": "350",
            "startValue": "20",
            "radius": "75",
            "possession": [
                "2",
                "2",
                "2",
                "2",
                "2"
            ]
        },
        {
            "y": "500",
            "x": "200",
            "startValue": "20",
            "radius": "75",
            "possession": [
                "1",
                "1",
                "1",
                "1",
                "1"
            ]
        },
        {
            "y": "500",
            "x": "500",
            "startValue": "50",
            "radius": "100",
            "possession": [
                "0",
                "0",
                "0",
                "0",
                "0"
            ],
            "multiplier": "2"
        }
    ]
}
```
