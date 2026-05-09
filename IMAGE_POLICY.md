# Image Policy for foreversite

The site should eventually be full of strange little images, scans, diagrams, emblems, fake ads, texture scraps, and object cards.

## Safe Sources

Prefer sources that are explicitly public-domain or permissively licensed:

- Wikimedia Commons public domain / CC BY / CC BY-SA
- Library of Congress public domain collections
- NASA images, where permitted by NASA media guidelines
- Internet Archive public-domain scans
- Biodiversity Heritage Library public-domain scans
- The Met Museum open access images
- Raw generated textures made locally with SVG/CSS/canvas
- Hand-made ASCII, tiny SVGs, and CSS drawings

Avoid random image scraping from websites unless the license is clear.

## Storage

Put downloaded images under:

```text
assets/img/source-name/descriptive-file-name.ext
```

Every folder with external images should include a `CREDITS.md` containing:

- source URL
- author/creator if known
- license
- date retrieved
- local filename

## How to Give Browser/Image Access

Current agent can use `web_fetch` for pages and `image_generate`, but not full interactive browser automation unless OpenClaw browser is enabled.

To enable a browser profile, configure OpenClaw with:

```json5
{
  browser: {
    enabled: true,
    defaultProfile: "openclaw",
    headless: true
  },
  tools: {
    alsoAllow: ["browser"]
  }
}
```

If `plugins.allow` is restrictive, include browser:

```json5
{
  plugins: {
    allow: ["discord", "browser"]
  }
}
```

Restart gateway afterward:

```bash
openclaw gateway restart
```

Then the agent can inspect pages visually, click through archives, and help gather properly licensed images.

## Recommended First Image Harvests

- public-domain botanical engravings for `redgarden/`
- old safety signage / public-domain industrial diagrams for `caution-zone/`
- public-domain appliance/manual scans for `tools/` and `municipal/`
- astronomy/public-domain moon diagrams for `notices/laundry-moon.html`

## Style Rule

Images should not make pages look modern or stock. Prefer:

- low resolution
- visible scan artifacts
- weird cropping
- handmade borders
- mismatched captions
- image maps
- tiny repeated sprites
- CSS filters only when they make things worse in a charming way
