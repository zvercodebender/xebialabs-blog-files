# This class doesn't do much, but we extracted it to show you
# how you can use modules in extension scripts.


class RepositoryHelper:

    def __init__(self, repositoryService):
        self._repositoryService = repositoryService

    def get_all_cis(self, parent):
        ci_ids = self._repositoryService.query(None, None, parent, None, None, None, 0, -1)
        return map(lambda ci_id: self._repositoryService.read(ci_id.id), ci_ids)
