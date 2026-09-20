# luce-demo-wolf3d

A **Luce Base** rewrite of id Software's open-sourced [Wolfenstein 3D](https://github.com/id-Software/wolf3d) (1992), presented through **luce-ui**. It loads the original shareware data files — the same `VSWAP`, `GAMEMAPS` and `MAPHEAD` the DOS exe used — and follows the original modules:

| Original | This port |
| --- | --- |
| `WL_DEF.H` constants | `src/wl_def.lucb` |
| `WL_DEF.H` statetype / objtype / Game | `src/wl_types.lucb` |
| `ID_CA.C` Carmack + RLEW maps | `src/id_ca.lucb` |
| `ID_PM.C` VSWAP pages | `src/id_pm.lucb` |
| `ID_CA.C` VGA graphics | `src/id_graph.lucb` |
| `ID_SD.C` / AdLib IMF | `src/id_sd.lucb`, `src/id_audio.lucb` |
| `WL_DRAW.C` / `WL_DR_A.ASM` raycaster | `src/wl_draw.lucb` |
| `WL_STATE.C` TryWalk / NewState / CheckLine | `src/wl_state.lucb` |
| `WL_ACT1.C` doors, statics, pushwalls | `src/wl_act1.lucb` |
| `WL_ACT2.C` `statetype` tables + T_Chase | `src/wl_act2.lucb` |
| `WL_AGENT.C` Thrust / T_Attack / GetBonus | `src/wl_agent.lucb` |
| `WL_GAME.C` SetupGameLevel / NewGame | `src/wl_game.lucb` |
| `WL_PLAY.C` PlayLoop / DoActor | `src/wl_play.lucb` |
| `WL_MENU.C` DemoLoop / Control Panel | `src/wl_menu.lucb` |
| GAMEPAL | `src/pal.lucb` |

The id source is under `vendor/wolf3d-id` (Limited Use license from the 2012 release). Wolf4SDL under `vendor/wolf4sdl` is the 32-bit C reading of the same algorithms (Carmack's notes said to drop 16-bit and the compiled scalers).

The **graphics are the original shareware art**, not placeholders. The 2012 source release does not include data; Carmack's `README` says to use a released or shareware set. Episode 1 shareware files live in `data/` (`VSWAP.WL1`, `GAMEMAPS.WL1`, `MAPHEAD.WL1`, …).

## Run

```sh
python3 tools/build.py
./build/wolf3d
```

From the repo root so `data/` resolves. `--fullscreen`, `--smoke` (12 frames).

| Input | Original meaning |
| --- | --- |
| Arrows / WASD | Move and turn |
| Alt | Strafe |
| Shift | Run |
| Ctrl / click | Fire |
| Space | Open a door |
| F11 | Fullscreen |
| Escape | Quit |

## Status

Working against shareware E1: map load, walls from VSWAP, doors, player `Thrust`/`ClipMove`, guards/officers/SS/dogs/mutants/Hans, pickups, pushwalls, 70 Hz loop, original VGA palette, AdLib IMF, DIGI SFX, DemoLoop menus.

Actor brains use original `statetype` records: nullable `think`/`action` function pointers and `next` as `State*`, filled from the WL_ACT2.C tables. DoActor calls those pointers the same way as `WL_PLAY.C`.

Still to port from the original: demo playback, registered six-episode `*.WL6` bosses, and some `ScaleShape` edge cases.

## Tests

```sh
./test.sh
```
