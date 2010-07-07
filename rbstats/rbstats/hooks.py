from djblets.extensions.base import ExtensionHook, ExtensionHookPoint


class RBStatsTableEntryHook(ExtensionHook):
    __metaclass__ = ExtensionHookPoint
    
    def description_for_user(self):
        raise NotImplemented
    
    def for_user(self, user):
        raise NotImplemented
