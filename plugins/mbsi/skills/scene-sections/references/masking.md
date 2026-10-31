# Masking scene sections: desktop and phone

The scene is always the section's background, never a box above a caption. What changes between screen shapes is which file loads, how it is pinned, and whether the words sit over it or above it.

## 1. Load one file per screen shape

Use a `<picture>` element so a phone downloads only its own render:

```html
<figure class="scene">
  <picture>
    <source media="(max-width: 720px)" srcset="scene-phone.webp">
    <img src="scene-desktop.webp" alt="" width="1024" height="460">
  </picture>
</figure>
```

Pixel art: save at its native size as WebP (about 70 to 120 KB) and let the browser scale it with `image-rendering: pixelated`. A 2x PNG of the same scene is about twenty times larger.

## 2. Desktop: the words over the scene

1. Hero, the words in the scene's empty side:

```css
.hero { position: relative; aspect-ratio: 1024 / 460; overflow: hidden; }
.hero .scene { position: absolute; inset: 0; margin: 0; }
.hero .scene img { width: 100%; height: 100%; object-fit: cover;
  mask-image: linear-gradient(to bottom, transparent, #000 8%, #000 92%, transparent); }
.hero .words { position: relative; z-index: 1; max-width: 34%; padding: 5% 0 0 4%; }
```

2. Card, the words on the scene's dark top:

```css
.card { position: relative; overflow: hidden; min-height: 0; }
.card .scene { position: absolute; inset: 0; margin: 0; z-index: 0; }
.card .scene img { width: 100%; height: 100%; object-fit: cover; object-position: 50% 100%; }
.card::before { content: ""; position: absolute; inset: 0; z-index: 1;
  background: linear-gradient(to bottom, rgb(0 0 0 / .85), transparent 78%); }
.card > :not(.scene) { position: relative; z-index: 2; }
.card pre { background: var(--ground); }
```

`object-position: 50% 100%` keeps the action, drawn low, in view however the card crops. Give the card a height from its row's width (a size container, or `min-height`), not `aspect-ratio` on an `overflow: hidden` card, which clips its words when they wrap.

3. A section whose scene sits under its heading: pull the scene up behind the heading with a negative top margin, so the heading lands in the corner the model left empty.

4. A side scene behind long words (quotes, a list): darken the words' side with a horizontal gradient (about 95% at the words, clear by 80% of the width).

## 3. Phone: the words above, the scene low

1. One column. Drop the page's outer card: no border, background, margin or padding, only a small side gutter.
2. Each section shows its square phone render pinned to the section's bottom, at full screen width, and reserves that height under its words: the words sit above the picture and on its dark top, never over its action.
3. A figure whose parent becomes a flex column can collapse to zero width; give it `align-self: stretch` and an explicit height.
4. Any whole-card gradient used on desktop comes off on phones.
5. Code blocks scroll sideways (`white-space: pre; overflow-x: auto`); they never wrap mid-word.
6. Never nest a card in a card in a card: on a phone the words end up in a narrow strip. Let inner blocks lose their border and background.

## 4. Check at each shape

1. No sideways scroll at 390px (`document.documentElement.scrollWidth` equals the width).
2. Every scene figure has a non-zero size and loads its own file (`img.currentSrc`).
3. The words read over the scene in a screenshot, at real size.
