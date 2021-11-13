# PyGame GUI XML Extension

This is an extension module for [PyGame GUI](https://github.com/MyreMylar/pygame_gui).

It allows users to author GUI layouts using XML instead of directly using the `pygame_gui` API.
This is supposed to make GUI authoring easier to reason about by giving people an HMTL-like
language.

This package is not yet available via pip, but if there are enough requests, I will add it. 
Also, I am not associated with the originial [PyGame GUI](https://github.com/MyreMylar/pygame_gui)
repo, but I appreciate the work they do. If this project is successful enough, I may consider
creating a PR on the original repo so that it can be available by default.

## Versioning

This package follows the release versions of PyGame GUI so that compatibility to easy to reason about. As such, if any breaking changes are made the the core pygame_gui module, then you may assume that that version of pygame_gui is also incompatible with non-updated releases of this package. 

## Contributing

Currently, I do not have a process for folks contributing to this project. I made this on the side as a tool to help me faster iterate on creating UI layouts for a research project. If you would like to contribute, go ahead, fork the repo, and make a pull request.

## Licensing

As with the main [PyGame GUI Rep](PyGame GUI](https://github.com) this project is licensed under the MIT License.
