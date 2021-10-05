# &#128013; Pyrefox &#129418;

> ### &#9888; work in progress

## Installation

<a href="https://pypi.org/project/pyrefox/"><pre>
pip install pyrefox
</pre></a>

## Examples

```python
from pyrefox import Pyrefox

pf = Pyrefox()

# show local Firefox profiles
for profile in pf.profiles:
    print(profile)

# show bookmarks of the latest updated profile
for bookmark in pf.profiles[0].bookmarks:
    print(bookmark)
```

Dump bookmarks into a Markdown document

```python
from collections import defaultdict
from html import unescape

from pyrefox import Pyrefox
from pyrefox.models.enums import BookmarkType

pf = Pyrefox()

# get all the bookmarks
bookmarks = {b.id: b for b in pf.profiles[0].bookmarks}
links = defaultdict(list)

# make a dict to group the bookmarks by folder
for bookmark in bookmarks.values():
    if bookmark.type == BookmarkType.BOOKMARK:

        parents = list()
        current = bookmark

        # get the folder's path
        while True:
            if current.parent:
                parent = bookmarks[current.parent]
                parents.insert(0, parent.title)
                current = parent
            else:
                break

        path = '/'.join(filter(None, parents))
        links[path].append({
            'title': bookmark.title,
            'url': bookmark.place.url,
            'descr': bookmark.place.description,
        })

with open('links.md', 'w') as f:
    for path, bookmarks in sorted(links.items()):
            f.write(f'# {path}\n\n')

            for b in bookmarks:
                # don't write description if it's the same as the title
                descr = unescape(b['descr']) if b['descr'] and b['descr'] != b['title'] else ''
                f.write(f'- [{b["title"]}]({b["url"]}) {descr}'.strip() + '\n')

            f.write('\n')
```