# Animation and rigging reference

## Animation workflow

1. Confirm frame rate, frame range, and output format.
2. Identify what should move and what should stay locked.
3. Set key poses first: start, anticipation, action, settle.
4. Use interpolation intentionally.
5. Preview viewport playback before rendering.
6. Review arcs, timing, collisions, and camera framing.

## Keyframe standards

- Name animated objects clearly.
- Group animated objects in `ANIM_*` collections when practical.
- Keep timelines readable.
- Avoid keying every channel if only one channel changes.
- Use constraints or drivers when motion should remain procedural.

## Rigging standards

- Save before rigging.
- Apply transforms before binding/skinning when appropriate.
- Use meaningful bone names.
- Use vertex groups with clean names.
- Test deformations through representative poses.
- Keep control bones visually distinct from deformation bones.

## Camera animation

- Use a target empty for orbit/pan shots.
- Ease in/out for cinematic movement.
- Avoid motion that is too fast for the subject.
- Check composition at every key camera frame.

## Review checklist

- No unintended object drift.
- No broken constraints.
- No missing keyframes at start/end.
- No accidental keys on hidden helpers.
- Frame range and output FPS match the request.
