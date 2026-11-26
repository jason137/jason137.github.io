jason137.github.io
==================

Edit `index.md`, then run `./build/build.sh` to regenerate `index.html` (needs pandoc).
Sheet wording and which figures show on each PNG live in `build/sheets.md`; the same build redraws the sheets in the live repo (masked: no rules, lots or gate timing).
`index.html` is generated; don't edit it by hand. Layout and CSS live in `build/template.html`.

The Signal One-Pagers table and `sheets/*.png` are generated from the live repo (`results/sleeve_metrics.toml`, `plots/public/`: masked sheets, no IP) at build time.
Hand-written table fields (names, descriptions, row order) live in `build/sleeves.toml`.
