"""
This type stub file was generated by pyright.
"""

class LabelLUT:
    """The class to manage look-up table for assigning colors to labels."""
    class Label:
        def __init__(self, name, value, color) -> None:
            ...
        
    
    
    Colors = ...
    def __init__(self) -> None:
        ...
    
    def add_label(self, name, value, color=...): # -> None:
        """Adds a label to the table.

        **Example:**
            The following sample creates a LUT with 3 labels::

                lut = ml3d.vis.LabelLUT()
                lut.add_label('one', 1)
                lut.add_label('two', 2)
                lut.add_label('three', 3, [0,0,1]) # use blue for label 'three'

        **Args:**
            name: The label name as string.
            value: The value associated with the label.
            color: Optional RGB color. E.g., [0.2, 0.4, 1.0].
        """
        ...
    


