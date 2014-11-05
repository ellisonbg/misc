# encoding: utf-8
"""SVG Display and Widgets."""

from __future__ import absolute_import
from __future__ import print_function

from IPython.display import display, HTML
from IPython.utils.traitlets import Bool, Float, Int, Unicode, HasTraits, Instance, List


class Element(HasTraits):
    pass


class SVG(Element):
    width = Int(100)
    height = Int(100)
    children = List([])
    
    _template = u'<svg width="{width}" height="{height}">\n{children}\n</svg>'
    
    def _render_template(self):
        cr = []
        for c in self.children:
            cr.append(c._render_template())
        cr = u'\n'.join(cr)
        data = {'children': cr, 'width': self.width, 'height': self.height}
        return self._template.format(**data)
    
    def circle(self, **kwargs):
        c = Circle(parent=self, **kwargs)
        self.children.append(c)
        return c
    
    def _repr_svg_(self):
        return self._render_template()
        

class Shape(Element):
    fill = Unicode('black')
    stroke = Unicode('red')
    stroke_width = Int(1)


class Circle(Shape):
    
    parent = Instance(Element)
    cx = Int(0)
    cy = Int(0)
    r = Int(10)
    
    _template = u"""<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" 
        stroke="{stroke}" stroke-width="{stroke_width}"/>"""
    
    def _render_template(self):
        data = {}
        for name in self.trait_names():
            data[name] = getattr(self, name)
        return self._template.format(**data)
