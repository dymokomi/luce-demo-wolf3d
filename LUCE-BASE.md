# luce-base notes from luce-demo-wolf3d

The Wolf3D demo is a language-limit test. This file is the pause log for the
agent currently changing the language. **Do not treat these as requests to
change the demo.** They are compiler/stdlib observations.

## Planned luce-base work: none after the window fullscreen API

The only luce-base edits for this demo are the portable fullscreen window API
(stdlib `window`, not the language):

- `src/std/window/module.lucb` — `Options.fullscreen`, `Window.set_fullscreen`, `Window.is_fullscreen`
- `src/std/window/queue.lucb` — saved windowed frame on `State`
- `src/std/window/macos/objc.lucb` — `setFrame:display:`, style/level/presentation msgSends
- `src/std/window/macos/lifecycle.lucb` — borderless coverage of `NSScreen.mainScreen`
- `src/std/window/windows/native.lucb` — `WS_POPUP` coverage of the nearest monitor

No further luce-base patches are planned for this demo. Rebuild the compiler
once for those five files. Game mode, raster pixel writes, and the raycaster
live in `luce-ui` / `luce-demo-wolf3d`.

## Worked around: local pointer escape

`run` used to keep `var host = Window.open(...)` on the stack and store
`self.host = &host` so `set_fullscreen` could reach the live window.

The compiler rejected that:

```
this pointer or view names a local and must not be stored where it outlives the function
```

The pointer did not actually outlive `run`: a defer cleared the field before
`host.destroy()`. Escape analysis does not accept “stored in a field, but
cleared before return.”

**Workaround (luce-ui):** `Application` owns `var session_host: window.Window`
by value and destroys it at the end of `run`. No local pointer is stored.

If the language later allows a checked “borrow this local into a field for the
rest of this function,” UI could go back to a stack window. Not required for
the demo.

## `files.read` inside `test` blocks

A `test` that calls `files.read` is stopped by a signal (native and C backends). The same `files.read` from `main` works. Map-load checks therefore live in `main`, not `test`. In-memory RLEW tests are fine.

## Not language bugs

- `defer self.host = none` is a parse error. `defer` takes a call, not an assignment.
- There is still no GPU texture sampler. The demo uses a CPU `Raster` on purpose.
- There is still no pointer lock. The demo is keyboard-only, like original Wolf3D.
