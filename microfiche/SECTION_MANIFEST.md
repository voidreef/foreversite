# Microfiche Room section

Theme: microfiche reader, newspaper fragments, library drawer codes, index cards, magnification artifacts. Built as an early-web archival room with concrete handling/transcription notes and handmade SVG visual material.

## Pages

- `microfiche/index.html` — section landing page / reader table
- `microfiche/drawer-c7.html` — library drawer code sheet and observed contents
- `microfiche/reader-calibration.html` — microfiche focus and transcription uncertainty card
- `microfiche/newspaper-strip-1938.html` — newspaper clipping strip from 3 May 1938
- `microfiche/index-card-catalog.html` — subject card catalog slips
- `microfiche/silver-halide-damage.html` — damage/artifact handling notes

## Handmade assets

- `assets/img/handmade/microfiche/reader-console.svg`
- `assets/img/handmade/microfiche/newspaper-strip.svg`
- `assets/img/handmade/microfiche/drawer-labels.svg`
- `assets/img/handmade/microfiche/magnifier-grid.svg`
- `microfiche/microfiche.css`

## Suggested main index link

Add a new door/card to `projects/foreversite/index.html`:

```html
<div class="door"><b>Microfiche Room</b>Drawer C7: green reader glow, newspaper fragments, catalog cards, and magnification artifacts.<br><br><a href="microfiche/index.html">load the fiche carrier</a></div>
```

## Link rule

The section landing page links once to each detail page. Detail pages only use the basic back link to `index.html`, so meaningful internal destinations are unique apart from back navigation.
