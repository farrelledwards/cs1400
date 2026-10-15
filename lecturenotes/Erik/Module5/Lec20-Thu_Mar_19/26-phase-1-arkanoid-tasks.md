# Phase 1 - Arkanoid Implementation Tasks

This document describes what students should implement when building the Arkanoid game from the starter code.

## Core Implementation Tasks

### Task 0: Rectangle Overlap Detection
**Function:** `rects_overlap(rect1, rect2)`

Students should implement the fundamental collision detection algorithm. Each rectangle is represented as `(left, right, top, bottom)`.

**The key insight:** Two rectangles overlap UNLESS one of these conditions is true:
- rect1 is completely to the left of rect2: `rect1_right < rect2_left`
- rect1 is completely to the right of rect2: `rect1_left > rect2_right`
- rect1 is completely above rect2: `rect1_bottom < rect2_top`
- rect1 is completely below rect2: `rect1_top > rect2_bottom`

If NONE of these are true, the rectangles must overlap!

**Learning:** Fundamental collision detection algorithm, logical thinking, understanding coordinate systems

### Task 1: Paddle Movement
**Function:** `move_paddle(paddle, direction, screen_width)`

Students should implement:
- Update `paddle.x` based on the direction parameter and PADDLE_SPEED constant
- Ensure the paddle stays within screen bounds:
  - Left edge should not go below 0
  - Right edge should not go beyond screen_width

**Learning:** Basic arithmetic, boundary checking, game object constraints

### Task 2: Ball-Paddle Collision Detection
**Location:** `update_ball()` function

Students should implement:
- Use `get_ball_rect()` and `get_paddle_rect()` to get collision rectangles
- Use `rects_overlap()` to detect collision (the function they wrote in Task 0!)
- When collision occurs:
  - Reverse the ball's vertical velocity
  - Reposition the ball above the paddle

**Learning:** Applying custom collision detection, velocity reversal for physics

### Task 3: Ball-Block Collision Detection
**Location:** `update_ball()` function

Students should implement:
- Loop through all active blocks
- Use `get_block_rect()` and `rects_overlap()` to detect ball-block collisions
- When collision occurs:
  - Mark the block as inactive (`block.active = False`)
  - Determine collision direction by comparing distances:
    - Calculate `dx = abs(ball.x - (block.x + block.width // 2))`
    - Calculate `dy = abs(ball.y - (block.y + block.height // 2))`
    - If `dx > dy`: ball hit from side → reverse `ball.vx`
    - Otherwise: ball hit from top/bottom → reverse `ball.vy`
  - Break out of loop (only one collision per frame)

**Learning:** Multiple collision detection, directional response logic, loop control, using custom collision functions

### Task 4: Win Condition
**Function:** `all_blocks_destroyed(blocks)`

Students should implement:
- Loop through the blocks list
- Return True if ALL blocks have `active = False`
- Return False if ANY block still has `active = True`

**Learning:** Boolean logic, list iteration, game state checking

## Debugging Tips for Students

If the game doesn't work correctly, here are common issues to check:

1. **Paddle doesn't move:** Check that `move_paddle()` is actually updating `paddle.x`
2. **Ball passes through paddle:** Ensure ball.y is repositioned above the paddle after collision
3. **Blocks don't disappear:** Verify `block.active` is being set to False
4. **Ball bounces wrong off blocks:** Double-check the dx/dy comparison logic
5. **Game never shows "You Won!":** Ensure `all_blocks_destroyed()` returns True when appropriate

## Conceptual Questions for Students

1. Why do we need to check `block.active` when drawing blocks? What would happen if we drew all blocks?
2. Why do we break out of the loop after a block collision?
3. How would the game change if we reversed BOTH velocities (vx and vy) during every collision?
4. What happens if the ball moves very fast and skips over a paddle? (Advanced question about tunneling)

## Extension Opportunities

Once students complete the basic implementation, they can explore:

- **Physics improvements:** Add ball spin/trajectory based on paddle hit location
- **Gameplay features:** Lives system, scoring, level progression
- **Visual enhancements:** Different colored blocks, animations, particle effects
- **Sound effects:** Collision sounds, win/lose sounds
