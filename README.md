# Algorithm-Maze-Builder

A simple tool built step by step visualization for path finding, maze creating and sorting algorithms.

Over 15 algorithms visualized !

## Supported Algorithms:

1. [Path Finding](Algorithms/algorithms.md)
1. [Maze generation](Algorithms/algorithms.md)
1. [Sorting](Sorts/algorithms.md)

---

## To run the application:

Install modules

```bash
pip install pygame
```

Run to get started right away!:

```bash
python app.py
```

## ! Start by going to the Help Page !

For Maze Creation:
->Maze->Press any number key-> See maze get created

For Path Finding in Maze:
->Select start and end position with mouse->Press x or z to find a path

For Sorting:
->Sort->Press any key as given in help
Pro tip: To fast-forward the process press Backspace

---

## To use the tool:

> Different coloured squares represents the following:

| Color  | Representation |
| ------ | -------------- |
| White  | Empty Square   |
| Black  | Barrier        |
| Red    | Visited        |
| Green  | To be visited  |
| Orange | Start Node     |
| Teal   | End Node       |
| Purple | Shortest Path  |

> Basic Keys:

| Key               | Function                                            |
| ----------------- | --------------------------------------------------- |
| Backspace         | Clear Screen (Maze)\Increase execution Speed (Both) |
| Tab               | Switch off or on grid (Both)                        |
| Mouse Right Click | Clear node or obstacle (Maze)                       |
| Mouse Left Click  | Add Node or obstacle (Maze)                         |
| Space             | Shuffle (Sort)                                      |
| R_Shift           | Invert (Sort)                                       |
| ESC               | Return to previous page                             |
| h                 | Help                                                |

#### Note:

1. Maze algorithms don't work if start and end nodes are mentioned already.
2. Path finding algorithms work only if start and end nodes are mentioned.
3. Sort algorithms work only when lines are shuffled
