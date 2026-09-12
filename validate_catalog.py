"""Validate collection metadata and repository-local links without network I/O."""
from __future__ import annotations

import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
MARKDOWN_LINK = re.compile(r"!?\[[^]]*\]\(([^)]+)\)")


def main() -> None:
    catalog = json.loads((ROOT / "catalog.json").read_text())
    assert catalog["schema_version"] == 1
    models = catalog["models"]
    assert len(models) == 2
    assert len({model["slug"] for model in models}) == len(models)
    for model in models:
        assert model["parameters"] > 0
        assert model["initialization"] == "random"
        assert model["hardware"] == ["1x NVIDIA L20"]
        assert 0 <= model["primary_metric"]["value"] <= 1
        assert model["primary_metric"]["comparable_across_collection"] is False
        assert (ROOT / model["model_page"]).is_file()
        assert model["huggingface"].startswith("https://huggingface.co/AliceYin/")
        if model.get("github_visibility") == "private":
            assert model["github"] is None
        else:
            assert model["github"].startswith("https://github.com/yinli-systems/")

    for markdown in ROOT.rglob("*.md"):
        for target in MARKDOWN_LINK.findall(markdown.read_text()):
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            local = (markdown.parent / target.split("#", 1)[0]).resolve()
            assert ROOT == local or ROOT in local.parents, f"link escapes repository: {markdown}: {target}"
            assert local.exists(), f"broken local link: {markdown}: {target}"
    print(json.dumps({"status": "pass", "models": len(models)}, sort_keys=True))


if __name__ == "__main__":
    main()
