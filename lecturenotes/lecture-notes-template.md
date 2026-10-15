# Lecture 15: Loops

**Class:** CS 1400
**Date:** 10-15-2026
**Modules:** 3.5, 3.6

---

## Big Ideas
- Fix up the polygon thing from last time.
- Finish loops (break, continue
- Do a project


## Polygon thing

```python
class Polygon:
    pass

polygons = []
for i in range(4):
    polygon = Polygon()
    polygon.sides = int(input("How many sides in this polygon? "))
    polygon.length = int(input("How long are each of the sides? "))
    polygons.append(polygon)

for polygon in polygons:
    print("This polygon has " + str(polygon.sides) + " and the length is " + str(polygon.length))
```
**What it does:**

**Things to watch out for (bugs, edge cases):**

## Diagrams / Visuals
*Sketch, describe, or link a photo of anything drawn on the board.*

- 

## Questions
- [ ] 
- [ ] 

*Answers (once found):*

- 

## Connections
- Builds on: Lecture [#] – 
- Related to homework / project: 

## Practice
- [ ] Try the examples without looking at notes
- [ ] Do practice problems: 
- [ ] Explain the main idea out loud in 1 minute

## Action Items / Deadlines
| Task | Due |
|------|-----|
|      |     |

## Summary (write after class)
*3–5 bullet points you'd want to remember a week from now.*

- 
- 
- 
