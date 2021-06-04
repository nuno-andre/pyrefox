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
