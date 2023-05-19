from prefect.filesystems import GitHub

block = GitHub(
    repository="https://github.com/ThibaudMrx/demoPrefect",
    access_token="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" # only required for private repos
)
# block.get_directory("folder-in-repo") # specify a subfolder of repo
block.save("block-prefect")
