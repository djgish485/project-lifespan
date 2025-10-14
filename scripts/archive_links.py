#!/usr/bin/env python3
"""
Archive web links via the Internet Archive SavePageNow API and update references/links.yaml.

Usage:
  python scripts/archive_links.py --id <id> --url <url>
  python scripts/archive_links.py --batch references/links.yaml

Notes:
- This is best-effort and may be rate-limited by the Archive.
- For reliability, consider manual archiving for critical links.
"""

from __future__ import annotations

import argparse
import sys
import time
import requests
import yaml
from pathlib import Path

API = "https://web.archive.org/save/"

def save_one(url: str) -> str | None:
    try:
        resp = requests.get(API + url, allow_redirects=False, timeout=30)
        # The Content-Location header often contains the snapshot path
        loc = resp.headers.get('Content-Location')
        if loc:
            return f"https://web.archive.org{loc}"
        return None
    except Exception as e:
        print(f"Error archiving {url}: {e}")
        return None

def update_yaml(entry_id: str, url: str, archived: str | None, path: Path) -> None:
    if not path.exists():
        data = {'links': []}
    else:
        data = yaml.safe_load(path.read_text()) or {'links': []}
    links = data.get('links', [])
    # Upsert by id
    for item in links:
        if item.get('id') == entry_id:
            item['url'] = url
            if archived:
                item['archived'] = archived
            break
    else:
        new_item = {'id': entry_id, 'url': url}
        if archived:
            new_item['archived'] = archived
        links.append(new_item)
    data['links'] = links
    path.write_text(yaml.safe_dump(data, sort_keys=False))

def batch_archive(path: Path) -> None:
    data = yaml.safe_load(path.read_text()) or {'links': []}
    for item in data.get('links', []):
        url = item.get('url')
        if not url or item.get('archived'):
            continue
        snap = save_one(url)
        if snap:
            item['archived'] = snap
            print(f"Archived {url} -> {snap}")
            time.sleep(1.0)
    path.write_text(yaml.safe_dump(data, sort_keys=False))

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--id')
    p.add_argument('--url')
    p.add_argument('--batch')
    args = p.parse_args()

    links_path = Path('references/links.yaml')
    if args.batch:
        batch_archive(Path(args.batch))
        return 0
    if not args.id or not args.url:
        p.error('Provide --id and --url, or --batch <yaml>')
        return 2
    snap = save_one(args.url)
    update_yaml(args.id, args.url, snap, links_path)
    if snap:
        print(f"Archived {args.url} -> {snap}")
    else:
        print(f"Could not archive {args.url}")
    return 0

if __name__ == '__main__':
    sys.exit(main())

