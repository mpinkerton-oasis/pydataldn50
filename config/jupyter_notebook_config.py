# Enable Jupytext
c.NotebookApp.contents_manager_class = 'jupytext.TextFileContentsManager'

# Instruct Jupytext to synchronise notebooks and .py modules
c.ContentsManager.default_jupytext_formats = 'ipynb,py'

# Follow a convention to separate cell code with double percentage marks # %%
c.ContentsManager.preferred_jupytext_formats_save = 'py:percent'
