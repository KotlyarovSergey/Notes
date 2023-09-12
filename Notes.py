from model.Repository import Repository
from viewer.Viewer import Viewer
from controller.Controller import Contlroller


repo = Repository('myNotes2.json')
view = Viewer()
controller = Contlroller(repo, view)
controller.run()
