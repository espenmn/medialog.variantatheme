from plone.theme.interfaces import IDefaultPloneLayer
from plone.app.portlets.interfaces import IColumn

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "Variantatheme Theme" theme, this interface must be its layer
       (in variantatheme/viewlets/configure.zcml).
    """
    
class IVariantathemeTopContent(IColumn):
    """we need our own portlet manager in the top area.
    """

class IVariantathemeFooterContent(IColumn):
    """we need our own portlet manager in the footer area.
        """