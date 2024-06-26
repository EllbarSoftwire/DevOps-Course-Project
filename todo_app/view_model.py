class ViewModel:
    def __init__(self, items):
        self._items = items
 
    @property
    def items(self):
        return sorted(self._items, key=lambda x: x.status, reverse=True)
    
    @property
    def done_items(self):
        return [item for item in self._items if item.status == "Completed"]
    
    @property
    def not_done_items(self):
        return [item for item in self._items if item.status == "Not Started"]
    
    @property
    def in_progress_items(self):
        return [item for item in self._items if item.status == "In Progress"]