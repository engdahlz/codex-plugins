# Apply Blender Pro plugin package

From the root of `engdahlz/codex-plugins`, run:

```bash
unzip -o codex-plugins-blender-pro.zip -d .
python3 plugins/blender-pro/scripts/validate_plugin.py
git status --short
git add .
git commit -m "feat: add blender-pro Codex plugin"
git push
```

Then install the marketplace in Codex:

```bash
codex plugin marketplace add engdahlz/codex-plugins
```
