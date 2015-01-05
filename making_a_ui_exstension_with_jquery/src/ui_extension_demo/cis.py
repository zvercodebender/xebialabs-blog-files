# This script is invoked when /api/extension/test/cis URL is requested

# We can split our code into modules
from ui_extension_demo.modules import repo

# repositoryService is one of the available XL Deploy services.
repository_helper = repo.RepositoryHelper(repositoryService)

root = request.query["root"]

# You can use logger object to output messages to XL Deploy log
logger.info("Requesting all the CIs under %s from the repository." % root)

# response.entity is what will be returned to the client as JSON
# XL Deploy can automatically serialize list of ConfigurationItem objects which will be returned
# by the helper.
response.entity = repository_helper.get_all_cis(root)
