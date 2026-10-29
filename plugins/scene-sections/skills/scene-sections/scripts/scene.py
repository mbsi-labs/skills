#!/usr/bin/env python3
"""Scene sections: build a canvas for an image model, and render a scene from numbered references.

  scene.py canvas --size 1024x1024 --text 0.04,0.04,0.92,0.47 [--text ...] \
                  [--subject old-scene.png --at 0.1,0.55,0.8,0.42] [--ground #272E39] --out canvas.png
      Boxes are x,y,w,h as fractions of the canvas. --text marks where the page's words will sit
      (drawn as a flat grey box the prompt calls the calm zone). --subject is fitted inside --at,
      keeping its aspect ratio, so an earlier render can be grown to a new shape.

  scene.py render --prompt prompt.txt --ref canvas.png --ref style.png [--ref ...] \
                  [--model openai/gpt-5.4-image-2] --out scene.png [--dry-run]
      Sends the prompt and the references, in order (image 1, image 2, ...), to an image model on
      OpenRouter and saves the first image it returns. Needs OPENROUTER_API_KEY. Each call costs money;
      --dry-run prints what would be sent and calls nothing.

Requires Pillow for canvas (pip install pillow). render uses only the standard library.
"""
import argparse, base64, json, mimetypes, os, sys, urllib.error, urllib.request


def box(spec, w, h):
    x, y, bw, bh = (float(v) for v in spec.split(","))
    return round(x * w), round(y * h), round(bw * w), round(bh * h)


def canvas(a):
    from PIL import Image, ImageDraw
    w, h = (int(v) for v in a.size.lower().split("x"))
    img = Image.new("RGB", (w, h), a.ground)
    if a.subject:
        sub = Image.open(a.subject).convert("RGBA")
        x, y, bw, bh = box(a.at, w, h)
        scale = min(bw / sub.width, bh / sub.height)
        sub = sub.resize((max(1, round(sub.width * scale)), max(1, round(sub.height * scale))), Image.NEAREST)
        img.paste(sub, (x + (bw - sub.width) // 2, y + (bh - sub.height) // 2), sub)
    draw = ImageDraw.Draw(img)
    for t in a.text or []:
        x, y, bw, bh = box(t, w, h)
        draw.rectangle([x, y, x + bw, y + bh], fill="#8a8f98")
    img.save(a.out)
    print(a.out)


def render(a):
    prompt = open(a.prompt).read()
    content = [{"type": "text", "text": prompt}]
    for path in a.ref:
        mime = mimetypes.guess_type(path)[0] or "image/png"
        data = base64.b64encode(open(path, "rb").read()).decode()
        content.append({"type": "image_url", "image_url": {"url": f"data:{mime};base64,{data}"}})
    body = {"model": a.model, "modalities": ["image", "text"], "messages": [{"role": "user", "content": content}]}
    if a.dry_run:
        print(f"model {a.model}; prompt {len(prompt)} chars; references in order:")
        for n, path in enumerate(a.ref, 1):
            print(f"  image {n}: {path} ({os.path.getsize(path)} bytes)")
        return
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        sys.exit("OPENROUTER_API_KEY is not set")
    req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", json.dumps(body).encode(),
                                 {"Authorization": "Bearer " + key, "Content-Type": "application/json"})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=600))
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read()[:300]!r}")
    images = r["choices"][0]["message"].get("images", [])
    if not images:
        sys.exit("the model returned no image; run it again")
    open(a.out, "wb").write(base64.b64decode(images[0]["image_url"]["url"].split(",", 1)[1]))
    print(f"{a.out} (cost {r.get('usage', {}).get('cost')})")


p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
sub = p.add_subparsers(dest="cmd", required=True)
c = sub.add_parser("canvas")
c.add_argument("--size", required=True); c.add_argument("--text", action="append")
c.add_argument("--subject"); c.add_argument("--at", default="0,0,1,1")
c.add_argument("--ground", default="#272E39"); c.add_argument("--out", required=True)
r = sub.add_parser("render")
r.add_argument("--prompt", required=True); r.add_argument("--ref", action="append", required=True)
r.add_argument("--model", default="openai/gpt-5.4-image-2"); r.add_argument("--out", required=True)
r.add_argument("--dry-run", action="store_true")
a = p.parse_args()
canvas(a) if a.cmd == "canvas" else render(a)
