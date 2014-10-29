# misc

## Overview

This is a collection of miscellaneous, single-file Python modules.

## Installation

These modules are designed to be installed through the `antipackage` package. You can install `antipackage`
using `pip`:

```
pip install git+https://git.myproject.org/antipackage#egg=antipackage
```

Once you do this, simply import `antipackage`:

```
import antipackage
```

## Ussge

Once `antipackage` has been imported, you can use any of the modules in this repo by importing
it using the following syntax:

```
from github.ellisonbg.misc import vizarray
```

This will automatically download and install the `vizarray` module and import it. `antipackage` will
automatically update any of these modules next time you import them.
